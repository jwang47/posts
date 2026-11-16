#!/usr/bin/env python3
"""Scale arithmetic for the carbon removal report (carbon-removal.md).

Reads analysis.json and one raw IGCC file, plus the cited parameters in
PARAMS below, and writes removal.json. Standard library only.

    python3 removal.py

A number in the report with the label [D] comes from analysis.json or a
raw file. A number with the label [C] is computed here from cited
parameters; it is only as good as those parameters, and each one has
its own label and source in PARAMS.
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUDGET = (
    HERE / "data/igcc/carbon_budget"
    / "budget_normal_magicc_True_fair_False_esf_7.1pm26.7_likeli_0.6827_"
      "nonCO2pc50.0_GtCO2_permaf_False_zecsd_0.0_asym_False_hdT_1.24"
      "NonlinNonCO2_all_None_recEm213.csv"
)

# name: (value, label, source)
PARAMS = {
    "tcre_c_per_1000gt": (0.45, "S", "IPCC AR6 WG1 figure SPM.10; likely range 0.27-0.63"),
    "tcre_low": (0.27, "S", "same"),
    "tcre_high": (0.63, "S", "same"),
    "removal_now_gt": (2.2, "S", "State of CDR 3rd edition, June 2026"),
    "novel_share_of_removal": (0.001, "S", "State of CDR 3rd edition: about 0.1%"),
    "removal_need_2050_gt": (8.75, "S", "State of CDR 3rd edition via Carbon Brief; 2nd edition gave 7-9"),
    "novel_now_2024_mt": (1.3, "S", "State of CDR 2nd edition, June 2024"),
    "novel_need_2050_gt": (1.0, "S", "State of CDR 3rd edition: novel methods pass 1 Gt/yr by 2050"),
    "ocean_sink_gtc": (3.4, "S", "Global Carbon Budget 2025, year 2024"),
    "land_sink_gtc": (1.9, "S", "Global Carbon Budget 2025, year 2024"),
    "gtc_to_gtco2": (3.664, "S", "Global Carbon Budget conversion"),
    "tropical_regrowth_tco2_ha": (11.2, "S", "Poorter et al. 2016: 3.05 MgC/ha/yr in the first 20 years"),
    "temperate_regrowth_tco2_ha": (5.0, "M", "middle of a 3-7 range from memory"),
    "boreal_regrowth_tco2_ha": (2.0, "M", "middle of a 1-3 range from memory"),
    "cook_patton_gt": (8.9, "S", "Cook-Patton et al. 2020, natural regrowth to 2050"),
    "cook_patton_mha": (678.0, "S", "same"),
    "afolu_removal_2050_gt": (2.98, "S", "IPCC AR6 WG3 chapter 12, median of 2 C or lower scenarios"),
    "mo_potential_gtc": (226.0, "S", "Mo et al. 2023, range 151-363"),
    "mo_new_forest_gtc": (87.0, "S", "Mo et al. 2023, land where forest was removed"),
    "india_mha": (329.0, "M", "area of India"),
    "cropland_mha": (1500.0, "M", "world cropland"),
    "dac_min_mwh_t": (0.123, "S", "thermodynamic minimum, 19.5 kJ/mol at 400 ppm"),
    "dac_low_mwh_t": (1.5, "S", "low end of company and analyst figures"),
    "dac_mid_mwh_t": (2.0, "S", "companies estimate 2-3 MWh/t with compression"),
    "dac_high_mwh_t": (2.5, "S", "Keith et al. 2018: 8.81 GJ of gas per tonne"),
    "belfer_low_twh_gt": (1400.0, "S", "Belfer Center, low-carbon energy for 1 Gt of DACCS"),
    "belfer_high_twh_gt": (4200.0, "S", "same"),
    "coal_power_t_per_mwh": (0.95, "M", "CO2 from coal power"),
    "mammoth_nameplate_t": (36000.0, "S", "Climeworks Mammoth design"),
    "mammoth_net_h1_2026_t": (675.0, "S", "net removal, first half of 2026"),
    "stratos_nameplate_t": (500000.0, "S", "1PointFive Stratos design"),
    "durable_sold_mt": (49.46, "S", "CDR.fyi via carboncredits.com, all years"),
    "durable_delivered_mt": (1.67, "S", "same"),
    "world_gdp_trillion": (117.0, "S", "IMF WEO 2025 via secondary sites"),
    "cost_low": (100.0, "S", "US DOE Carbon Negative Shot target"),
    "cost_mid": (340.0, "S", "Sievert et al. 2024, DAC at 1 Gt/yr, range 226-835"),
    "cost_high": (600.0, "S", "near the 2026 supplier break-even for DACCS, $670"),
    "prudent_storage_gt": (1460.0, "S", "Gidden et al. 2025"),
}


def p(name):
    return PARAMS[name][0]


def budget_gt_per_tenth():
    """Slope of the remaining carbon budget, 50% column, 1.5 to 1.7 C."""
    rows = {}
    with open(BUDGET, newline="") as f:
        for row in csv.DictReader(f):
            rows[round(float(row["dT_targets"]), 1)] = float(row["0.5"])
    return {
        "source": str(BUDGET.relative_to(HERE)),
        "budget_gt_50pct": {str(t): round(rows[t], 1) for t in (1.5, 1.6, 1.7, 2.0)},
        "gt_per_0.1c": round((rows[1.7] - rows[1.5]) / 2, 1),
    }


def main():
    a = json.loads((HERE / "analysis.json").read_text())
    fossil = a["co2_fossil"]["world_gt"]["2025"]
    land_use = a["co2_fossil"]["world_land_use_gt"]
    co2 = fossil + land_use
    el = a["electricity_world"]["twh"]
    gen = el["2025"]["generation"]
    solar = el["2025"]["solar"]
    grid = a["electricity_world"]["carbon_intensity_g_per_kwh"]["2025"] / 1000

    out = {"inputs_from_analysis_json": {
        "co2_fossil_2025_gt": fossil, "co2_land_use_gt": land_use,
        "co2_total_gt": round(co2, 2), "generation_2025_twh": gen,
        "solar_2025_twh": solar, "grid_t_per_mwh": grid}}

    # 1. Removal and temperature
    b = budget_gt_per_tenth()
    tcre = 100 / p("tcre_c_per_1000gt")
    out["temperature"] = {
        "igcc_budget": b,
        "tcre_gt_per_0.1c": round(tcre),
        "tcre_gt_per_0.1c_range": [round(100 / p("tcre_high")), round(100 / p("tcre_low"))],
        "years_of_co2_per_0.1c": [round(b["gt_per_0.1c"] / co2, 1), round(tcre / co2, 1)],
        "gt_per_year_for_0.1c_in_50_years": [round(b["gt_per_0.1c"] / 50, 1), round(tcre / 50, 1)],
        "cooling_from_8.75_gt_for_50_years_c": round(p("removal_need_2050_gt") * 50 * p("tcre_c_per_1000gt") / 1000, 2),
        "warming_per_year_of_co2_c": round(co2 * p("tcre_c_per_1000gt") / 1000, 3),
        "prudent_storage_c": round(p("prudent_storage_gt") * p("tcre_c_per_1000gt") / 1000, 2),
    }

    # 2. Sinks and the size of the job
    ocean = p("ocean_sink_gtc") * p("gtc_to_gtco2")
    land = p("land_sink_gtc") * p("gtc_to_gtco2")
    novel_now = p("removal_now_gt") * p("novel_share_of_removal")
    years = 2050 - 2026
    out["scale"] = {
        "ocean_sink_gtco2": round(ocean, 1), "land_sink_gtco2": round(land, 1),
        "natural_sinks_gtco2": round(ocean + land, 1),
        "natural_sinks_share_of_co2_percent": round(100 * (ocean + land) / co2),
        "removal_now_share_of_co2_percent": round(100 * p("removal_now_gt") / co2, 1),
        "novel_now_mt": round(novel_now * 1000, 1),
        "novel_growth_factor_to_2050": round(p("novel_need_2050_gt") / novel_now),
        "novel_growth_percent_per_year": round(100 * ((p("novel_need_2050_gt") / novel_now) ** (1 / years) - 1), 1),
        "novel_growth_factor_to_2050_from_2024_count": round(p("novel_need_2050_gt") / (p("novel_now_2024_mt") / 1000)),
        "novel_growth_percent_per_year_from_2024_count": round(100 * ((p("novel_need_2050_gt") / (p("novel_now_2024_mt") / 1000)) ** (1 / years) - 1), 1),
        "solar_growth_percent_per_year_2015_2025": round(100 * ((solar / el["2015"]["solar"]) ** 0.1 - 1), 1),
        "total_removal_growth_factor": round(p("removal_need_2050_gt") / p("removal_now_gt"), 1),
    }

    # 3. Trees
    rates = {"tropical": p("tropical_regrowth_tco2_ha"),
             "temperate": p("temperate_regrowth_tco2_ha"),
             "boreal": p("boreal_regrowth_tco2_ha")}
    mha_per_gt = {k: round(1000 / v) for k, v in rates.items()}
    afolu = p("afolu_removal_2050_gt")
    out["trees"] = {
        "mha_per_gt_per_year": mha_per_gt,
        "cook_patton_tco2_per_ha": round(1000 * p("cook_patton_gt") / p("cook_patton_mha"), 1),
        "cook_patton_area_vs_india": round(p("cook_patton_mha") / p("india_mha"), 1),
        "cook_patton_area_share_of_cropland_percent": round(100 * p("cook_patton_mha") / p("cropland_mha")),
        "mha_for_afolu_median_tropical": round(afolu * mha_per_gt["tropical"]),
        "mha_for_afolu_median_temperate": round(afolu * mha_per_gt["temperate"]),
        "mo_potential_gtco2": round(p("mo_potential_gtc") * p("gtc_to_gtco2")),
        "mo_potential_years_of_co2": round(p("mo_potential_gtc") * p("gtc_to_gtco2") / co2, 1),
        "mo_potential_max_cooling_c": round(p("mo_potential_gtc") * p("gtc_to_gtco2") * p("tcre_c_per_1000gt") / 1000, 2),
        "mo_new_forest_gtco2": round(p("mo_new_forest_gtc") * p("gtc_to_gtco2")),
        "mo_new_forest_max_cooling_c": round(p("mo_new_forest_gtc") * p("gtc_to_gtco2") * p("tcre_c_per_1000gt") / 1000, 2),
    }

    # 4. Direct air capture
    def twh(mwh_per_t, gt=1.0):
        return mwh_per_t * gt * 1000

    need = p("removal_need_2050_gt")
    net_year = 2 * p("mammoth_net_h1_2026_t")
    t_per_second = co2 * 1e9 / (365.25 * 86400)
    out["dac"] = {
        "twh_per_gt": {k: round(twh(p(f"dac_{k}_mwh_t"))) for k in ("min", "low", "mid", "high")},
        "share_of_world_generation_percent_per_gt": {
            "low": round(100 * twh(p("dac_low_mwh_t")) / gen, 1),
            "mid": round(100 * twh(p("dac_mid_mwh_t")) / gen, 1),
            "high": round(100 * twh(p("dac_high_mwh_t")) / gen, 1),
            "belfer": [round(100 * p("belfer_low_twh_gt") / gen, 1), round(100 * p("belfer_high_twh_gt") / gen, 1)]},
        "mid_twh_per_gt_share_of_solar_percent": round(100 * twh(p("dac_mid_mwh_t")) / solar),
        "all_need_by_dac_twh": round(twh(p("dac_mid_mwh_t"), need)),
        "all_need_by_dac_share_of_generation_percent": round(100 * twh(p("dac_mid_mwh_t"), need) / gen),
        "second_law_efficiency_percent": [round(100 * p("dac_min_mwh_t") / p("dac_high_mwh_t"), 1),
                                          round(100 * p("dac_min_mwh_t") / p("dac_low_mwh_t"), 1)],
        "per_mid_mwh": {
            "removed_by_dac_t": 1.0,
            "avoided_if_it_replaces_average_grid_t": round(p("dac_mid_mwh_t") * grid, 2),
            "avoided_if_it_replaces_coal_t": round(p("dac_mid_mwh_t") * p("coal_power_t_per_mwh"), 2)},
        "mammoth_net_per_year_t": net_year,
        "mammoth_share_of_nameplate_percent": round(100 * net_year / p("mammoth_nameplate_t"), 1),
        "mammoth_plants_per_gt_at_nameplate": round(1e9 / p("mammoth_nameplate_t")),
        "stratos_plants_per_gt_at_nameplate": round(1e9 / p("stratos_nameplate_t")),
        "world_co2_t_per_second": round(t_per_second),
        "mammoth_h1_2026_in_seconds_of_world_co2": round(p("mammoth_net_h1_2026_t") / t_per_second, 2),
    }

    # 5. Market and cost
    gdp = p("world_gdp_trillion") * 1e12
    costs = {k: p(f"cost_{k}") for k in ("low", "mid", "high")}
    per_tenth = [b["gt_per_0.1c"], tcre]
    out["market"] = {
        "delivered_share_of_sold_percent": round(100 * p("durable_delivered_mt") / p("durable_sold_mt"), 1),
        "all_durable_deliveries_in_minutes_of_world_co2": round(p("durable_delivered_mt") * 1e6 / t_per_second / 60),
    }
    out["cost"] = {
        "usd_billion_per_year": {
            f"{gt}_gt": {k: round(gt * c) for k, c in costs.items()} for gt in (1.0, need)},
        "percent_of_gdp": {
            f"{gt}_gt": {k: round(100 * gt * 1e9 * c / gdp, 2) for k, c in costs.items()} for gt in (1.0, need)},
        "usd_trillion_per_0.1c": {
            k: [round(g * c / 1000, 1) for g in per_tenth] for k, c in costs.items()},
    }

    out["params"] = {k: {"value": v[0], "label": v[1], "source": v[2]} for k, v in PARAMS.items()}
    (HERE / "removal.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "params"}, indent=1))


if __name__ == "__main__":
    main()
