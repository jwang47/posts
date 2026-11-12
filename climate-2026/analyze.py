#!/usr/bin/env python3
"""Compute the derived numbers in README.md from the files in data/.

    python -X utf8 analyze.py      # writes analysis.json

Standard library only. Every number in the report marked [D] comes from
analysis.json, so a reader can check it against the raw files.
"""
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "data")


def rows(rel):
    with open(os.path.join(D, rel), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def slope(xs, ys):
    """Least-squares slope."""
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def r(x, n=2):
    return None if x is None else round(x, n)


out = {}

# --- Global mean surface temperature (IGCC four-dataset mean, vs 1850-1900)
g = [(int(float(x["timebound_lower"])), float(x["GMST"]))
     for x in rows("igcc/global_mean_temperatures/annual_averages.csv")]
gd = dict(g)
last = g[-1][0]
out["gmst"] = {
    "source": "data/igcc/global_mean_temperatures/annual_averages.csv",
    "baseline": "1850-1900",
    "latest_year": last,
    "latest": gd[last],
    "by_year": {y: gd[y] for y in range(2015, last + 1)},
    "warmest_five": sorted(g, key=lambda t: -t[1])[:5],
    "mean_last_10y": r(sum(gd[y] for y in range(last - 9, last + 1)) / 10, 3),
    "mean_last_20y": r(sum(gd[y] for y in range(last - 19, last + 1)) / 20, 3),
    "trend_c_per_decade": {
        "1970-%d" % last: r(10 * slope(*zip(*[t for t in g if t[0] >= 1970])), 3),
        "1970-2010": r(10 * slope(*zip(*[t for t in g if 1970 <= t[0] <= 2010])), 3),
        "%d-%d" % (last - 14, last): r(10 * slope(*zip(*[t for t in g if t[0] >= last - 14])), 3),
        "%d-%d" % (last - 29, last): r(10 * slope(*zip(*[t for t in g if t[0] >= last - 29])), 3),
    },
}

# --- Berkeley Earth, re-based to 1850-1900 (file is vs 1951-1980)
be = {}
with open(os.path.join(D, "primary/berkeley-earth-land-ocean-annual.txt"), encoding="utf-8") as f:
    for line in f:
        p = line.split()
        if p and p[0].isdigit():
            be[int(p[0])] = float(p[1])
base = sum(be[y] for y in range(1850, 1901)) / 51
out["berkeley_earth"] = {
    "source": "data/primary/berkeley-earth-land-ocean-annual.txt (air temperature over sea ice)",
    "latest_year": max(be),
    "vs_1850_1900": {y: r(be[y] - base, 3) for y in sorted(be) if y >= 2015},
}

# --- Human-induced warming (IGCC assessment)
hw = rows("igcc/anthropogenic_warming/Assessment-Update-2025_GMST_headlines.csv")
out["human_induced_warming"] = [
    {k: x[k] for k in ("timebound_lower", "timebound_upper", "anthropogenic_p05",
                       "anthropogenic_p50", "anthropogenic_p95", "ghg_p50",
                       "other_human_forcing_p50", "natural_p50", "notes")}
    for x in hw]
out["human_induced_warming_extrapolation"] = rows(
    "igcc/anthropogenic_warming/Assessment-Extrapolation-2026_GMST_headlines.csv")

# --- Greenhouse gas concentrations
c = rows("igcc/greenhouse_gas_concentrations/ghg_concentrations.csv")
first, lastc = c[0], c[-1]
out["concentrations"] = {
    "source": "data/igcc/greenhouse_gas_concentrations/ghg_concentrations.csv",
    "first_year": first["timebound_lower"], "latest_year": lastc["timebound_lower"],
}
for gas in ("CO2", "CH4", "N2O"):
    a, b = float(first[gas]), float(lastc[gas])
    by = {x["timebound_lower"]: float(x[gas]) for x in c}
    out["concentrations"][gas] = {
        "first": r(a, 1), "latest": r(b, 1), "rise_percent": r(100 * (b / a - 1), 0),
        "rise_last_10y_per_year": r((b - by[str(int(lastc["timebound_lower"]) - 10)]) / 10, 2),
        "rise_last_year": r(b - float(c[-2][gas]), 2),
    }

# --- Effective radiative forcing, latest year
e = rows("igcc/effective_radiative_forcing/ERF_best_aggregates.csv")[-1]
out["forcing_w_m2"] = {k: r(float(v), 2) for k, v in e.items()
                       if k in ("timebound_lower", "CO2", "CH4", "N2O", "aerosol", "halogen",
                                "O3", "anthro", "natural", "total", "wmghg")}

# --- Warming by emitted compound
out["warming_by_emitted_compound_c"] = {
    x["Compound emitted"]: num(x["Total_p50"])
    for x in rows("igcc/anthropogenic_warming_by_species/temperature_relative_to_1750.csv")}

# --- Earth's energy imbalance: mean heating rate over a period, W/m2
ee = rows("igcc/earth_energy_imbalance/earth_energy_imbalance.csv")
tot = {int(float(x["timebound_lower"])): float(x["total"]) for x in ee if num(x["total"]) is not None}
AREA, YEAR = 5.101e14, 365.25 * 86400


def eei(a, b):  # heat content is in ZJ at mid-year
    return r((tot[b] - tot[a]) * 1e21 / (AREA * YEAR * (b - a)), 2)


ly = max(tot)
# The total stops earlier than the ocean series; the ocean holds about 90%.
oc = {int(float(x["timebound_lower"])): float(x["ocean_full-depth"]) for x in ee
      if x["timebound_lower"] and num(x["ocean_full-depth"]) is not None}
lo = max(oc)
ocean = lambda a, b: r((oc[b] - oc[a]) * 1e21 / (AREA * YEAR * (b - a)), 2)
out["energy_imbalance_w_m2"] = {
    "source": "data/igcc/earth_energy_imbalance/earth_energy_imbalance.csv (total heat gain, ZJ)",
    "1971-2006": eei(1971, 2006), "2006-%d" % ly: eei(2006, ly),
    "%d-%d" % (ly - 12, ly): eei(ly - 12, ly),
    "heat_gain_zj_1971_to_%d" % ly: r(tot[ly] - tot[1971], 0),
    "ocean_only": {"1971-2006": ocean(1971, 2006), "2006-%d" % lo: ocean(2006, lo),
                   "%d-%d" % (lo - 10, lo): ocean(lo - 10, lo)},
    "ocean_share_of_heat_gain_1971_%d_percent" % ly: r(100 * (oc[ly] - oc[1971]) / (tot[ly] - tot[1971]), 0),
}

# --- Greenhouse gas emissions (IGCC, GtCO2e, GWP100 AR6)
ge = [x for x in rows("igcc/greenhouse_gas_emissions/greehouse_gas_emissions_co2eq.csv")
      if num(x["CH4"]) is not None]
gl = ge[-1]
parts = {k: float(gl[k]) for k in ("CO2-FFI", "CO2-LULUCF", "CH4", "N2O", "F-gases")}
out["ghg_emissions_gtco2e"] = {
    "year": gl["timebound_lower"], "total": r(sum(parts.values()), 1),
    "parts": {k: r(v, 1) for k, v in parts.items()},
    "share_percent": {k: r(100 * v / sum(parts.values()), 0) for k, v in parts.items()},
}

# --- Sea level
s = rows("igcc/sea_level_rise/IGCC_GMSL_ensemble.csv")
sl = {int(float(x["timebound_lower"])): float(x["mean"]) for x in s}
ls = max(sl)
out["sea_level_mm"] = {
    "rise_1901_to_%d" % ls: r(sl[ls] - sl[1901], 0),
    "rate_mm_per_year": {
        "1901-1971": r((sl[1971] - sl[1901]) / 70, 2),
        "1993-%d" % ls: r(slope(*zip(*[(y, v) for y, v in sl.items() if y >= 1993])), 2),
        "%d-%d" % (ls - 10, ls): r(slope(*zip(*[(y, v) for y, v in sl.items() if y >= ls - 10])), 2),
    },
}

# --- Emissions by country (Our World in Data, from the Global Carbon Budget)
co = rows("owid/co2-extract.csv")
by = {}
for x in co:
    by.setdefault(x["country"], {})[int(x["year"])] = x
yr = max(y for y, x in by["World"].items() if num(x["co2"]) is not None)
yc = max(y for y, x in by["China"].items() if num(x["co2"]) is not None)
w = by["World"]
out["co2_fossil"] = {
    "source": "data/owid/co2-extract.csv",
    "world_latest_year": yr, "country_latest_year": yc,
    "world_gt": {y: r(float(w[y]["co2"]) / 1000, 2) for y in range(yr - 12, yr + 1)},
    "world_growth_percent_per_year": {
        "2000-2010": r(100 * ((float(w[2010]["co2"]) / float(w[2000]["co2"])) ** 0.1 - 1), 2),
        "2010-2019": r(100 * ((float(w[2019]["co2"]) / float(w[2010]["co2"])) ** (1 / 9) - 1), 2),
        "2019-%d" % yr: r(100 * ((float(w[yr]["co2"]) / float(w[2019]["co2"])) ** (1 / (yr - 2019)) - 1), 2),
    },
    "world_land_use_gt": r(num(w[yc]["land_use_change_co2"]) / 1000, 2) if num(w[yc]["land_use_change_co2"]) else None,
    "by_country": {},
}
for name in ("China", "United States", "European Union (27)", "India", "Japan", "Russia",
             "High-income countries", "Low-income countries", "Africa",
             "International aviation", "International shipping"):
    x = by[name][yc]
    peak = max((num(v["co2"]) or 0, y) for y, v in by[name].items())
    out["co2_fossil"]["by_country"][name] = {
        "gt": r(float(x["co2"]) / 1000, 2),
        "share_percent": r(num(x["share_global_co2"]), 1),
        "per_capita_t": r(num(x["co2_per_capita"]), 1),
        "consumption_per_capita_t": r(num(by[name].get(yc - 1, x)["consumption_co2_per_capita"]), 1),
        "cumulative_share_percent": r(num(x["share_global_cumulative_co2"]), 1),
        "peak_year": peak[1],
        "change_since_peak_percent": r(100 * (float(x["co2"]) / peak[0] - 1), 0),
    }
out["co2_fossil"]["world_per_capita_t"] = r(num(w[yc]["co2_per_capita"]), 1)

# --- Electricity (Our World in Data, from Ember and the Energy Institute)
en = rows("owid/energy-extract.csv")
eb = {}
for x in en:
    eb.setdefault(x["country"], {})[int(x["year"])] = x
ew = eb["World"]
ey = max(y for y, x in ew.items() if num(x["solar_electricity"]) is not None)
cols = ("coal", "gas", "fossil", "nuclear", "hydro", "solar", "wind", "renewables", "low_carbon")
out["electricity_world"] = {
    "source": "data/owid/energy-extract.csv", "latest_year": ey,
    "share_percent": {y: {k: r(num(ew[y][k + "_share_elec"]), 1) for k in cols}
                      for y in (2000, 2010, 2015, 2020, ey - 1, ey)},
    "twh": {y: {k: r(num(ew[y][k + "_electricity"]), 0) for k in cols + ("oil",)}
            | {"generation": r(num(ew[y]["electricity_generation"]), 0)}
            for y in (2015, 2020, ey - 1, ey)},
    "solar_doubling_check_twh": {y: r(num(ew[y]["solar_electricity"]), 0) for y in range(ey - 9, ey + 1)},
    "carbon_intensity_g_per_kwh": {y: r(num(ew[y]["carbon_intensity_elec"]), 0) for y in (2000, 2010, 2020, ey)},
}
g1, g0 = ew[ey], ew[ey - 1]
out["electricity_world"]["change_twh_last_year"] = {
    k: r(num(g1[k]) - num(g0[k]), 0) for k in
    ("electricity_generation", "solar_electricity", "wind_electricity",
     "low_carbon_electricity", "fossil_electricity", "coal_electricity")}
out["electricity_by_country_%d" % ey] = {
    n: {k: r(num(eb[n][ey][k + "_share_elec"]), 1) for k in ("coal", "fossil", "solar", "wind", "low_carbon")}
    for n in eb if n != "World" and num(eb[n][ey]["solar_share_elec"]) is not None}

# --- Cross-checks from the agency files in data/primary/ (present after a
# --- run of fetch.py on a machine that can reach the agencies)
def lines(rel, enc="utf-8"):
    with open(os.path.join(D, rel), encoding=enc) as f:
        return [l.rstrip("\n") for l in f if l.strip() and not l.startswith("#")]


def table(rel, enc="utf-8"):
    return [[c.strip() for c in l.split(",")] for l in lines(rel, enc)]


if os.path.exists(os.path.join(D, "primary/hadcrut5-global-annual.csv")):
    x = {}
    t = {int(a[0]): float(a[1]) for a in table("primary/hadcrut5-global-annual.csv")[1:]}
    b = sum(t[y] for y in range(1850, 1901)) / 51
    x["hadcrut5_vs_1850_1900"] = {y: r(t[y] - b, 2) for y in (2023, 2024, 2025)}
    t = {int(a[0]): float(a[1]) for a in table("primary/noaa-globaltemp-annual.csv")[1:]
         if a[0].isdigit()}
    b = sum(t[y] for y in range(1850, 1901)) / 51
    x["noaa_globaltemp_vs_1850_1900"] = {y: r(t[y] - b, 2) for y in (2023, 2024, 2025)}
    # GISTEMP starts in 1880, so it stays on its own 1951-1980 baseline.
    gis = {a[0]: a for a in table("primary/nasa-gistemp-global-monthly.csv") if a[0].isdigit()}
    mon = lambda y: [float(v) for v in gis[str(y)][1:13] if v != "***"]
    n = len(mon(last + 1))
    x["nasa_gistemp_vs_1951_1980"] = {
        "annual": {y: float(gis[str(y)][13]) for y in (2023, 2024, 2025)},
        "first_%d_months" % n: {y: r(sum(mon(y)[:n]) / n, 2) for y in (2024, 2025, last + 1)},
    }
    # ERA5: anomalies are against 1991-2020. Copernicus adds 0.88 C for 1850-1900.
    OFF = 0.88
    era = [(a[0], float(a[3])) for a in table("primary/era5-daily-2t-global.csv")[1:]]
    yr_mean = lambda y, end="12-31": [v for d, v in era if d[:4] == str(y) and d[5:] <= end]
    avg = lambda v: sum(v) / len(v)
    last_day = era[-1][0]
    x["era5_vs_1850_1900"] = {
        "offset_added_c": OFF,
        "annual": {y: r(avg(yr_mean(y)) + OFF, 2) for y in (2023, 2024, 2025)},
        "year_to_%s" % last_day[5:]: {y: r(avg(yr_mean(y, last_day[5:])) + OFF, 2)
                                       for y in (2023, 2024, 2025, int(last_day[:4]))},
        "latest_full_month": {m: r(avg([v for d, v in era if d[:7] == m]) + OFF, 2)
                              for m in ("2023-10", "2024-10", "2025-10", "2026-10")},
        "last_day": last_day,
    }
    co2 = table("primary/noaa-co2-annmean-global.csv")
    gr = [a for a in table("primary/noaa-co2-growth-global.csv") if a[0].isdigit()]
    ch4 = [a for a in table("primary/noaa-ch4-annmean-global.csv") if a[0].isdigit()]
    n2o = [a for a in table("primary/noaa-n2o-annmean-global.csv") if a[0].isdigit()]
    x["noaa_gases"] = {
        "co2_ppm": {co2[-1][0]: float(co2[-1][1])},
        "co2_growth_ppm_per_year": {a[0]: float(a[1]) for a in gr[-4:]},
        "co2_growth_decade_means": {
            "1960s": r(avg([float(a[1]) for a in gr if 1960 <= int(a[0]) <= 1969]), 2),
            "2015-2024": r(avg([float(a[1]) for a in gr if 2015 <= int(a[0]) <= 2024]), 2)},
        "ch4_ppb": {ch4[-1][0]: float(ch4[-1][1])},
        "ch4_rise_ppb": {a[0]: r(float(a[1]) - float(b_[1]), 1) for b_, a in zip(ch4[-5:-1], ch4[-4:])},
        "n2o_ppb": {n2o[-1][0]: float(n2o[-1][1])},
    }
    oni = [l.split() for l in lines("primary/noaa-oni.txt")[1:]]
    peak = lambda a, b: max(float(o[3]) for o in oni if a <= int(o[1]) <= b)
    x["noaa_oni"] = {"latest": " ".join(oni[-1][:2]), "latest_anomaly": float(oni[-1][3]),
                     "peak_1982_83": peak(1982, 1983), "peak_1997_98": peak(1997, 1998),
                     "peak_2015_16": peak(2015, 2016), "peak_2023_24": peak(2023, 2024)}
    for key, rel in (("arctic_september", "primary/nsidc-arctic-september-extent.csv"),
                     ("antarctic_february", "primary/nsidc-antarctic-february-extent.csv")):
        ex = [(int(a[0]), float(a[4])) for a in table(rel)[1:] if float(a[4]) > 0]
        ranked = sorted(ex, key=lambda t: t[1])
        x["nsidc_%s_extent_mkm2" % key] = {
            "latest": ex[-1], "rank_from_lowest": ranked.index(ex[-1]) + 1, "years": len(ex),
            "lowest": ranked[0], "mean_1979_1990": r(avg([v for y, v in ex if y <= 1990]), 2),
            "mean_last_10": r(avg([v for y, v in ex[-10:]]), 2),
            "trend_percent_per_decade_vs_1981_2010": r(
                1000 * slope(*zip(*ex)) / avg([v for y, v in ex if 1981 <= y <= 2010]), 1)}
    sea = [(float(a[0]), float(next(v for v in a[1:] if v))) for a in table("primary/noaa-star-global-sea-level.csv")[1:]]
    x["noaa_star_sea_level_mm_per_year"] = {
        "1993-%d" % sea[-1][0]: r(slope(*zip(*sea)), 2),
        "first_10_years": r(slope(*zip(*[t for t in sea if t[0] < sea[0][0] + 10])), 2),
        "last_10_years": r(slope(*zip(*[t for t in sea if t[0] > sea[-1][0] - 10])), 2),
        "last_point": sea[-1][0]}
    jp = {int(a[0]): float(a[1]) for a in table("primary/jma-japan-annual-temp.csv", "cp932")[1:]}
    x["jma_japan_temp_vs_1991_2020"] = {
        "latest": {y: jp[y] for y in sorted(jp)[-3:]},
        "trend_c_per_century": r(100 * slope(*zip(*jp.items())), 2), "first_year": min(jp)}
    out["cross_checks"] = x

with open(os.path.join(HERE, "analysis.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, sort_keys=False)
    f.write("\n")
print("wrote analysis.json")
