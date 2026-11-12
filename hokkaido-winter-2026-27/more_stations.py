"""Second round of analysis: the air at mountain height, the long records,
and week-by-week odds at more stations.

Run: python3 more_stations.py   (needs numpy; writes analysis2.json)

1. Upper air. data/sapporo-upper.csv holds the Sapporo weather balloon
   soundings (NOAA IGRA v2, 00 and 12 UTC). The 850 hPa level is at about
   1,450 m. The temperature at a slope height h is estimated as
   t850 + LAPSE * (z850 - h), with LAPSE = 6.5 C per km. This is an estimate
   for free air 60 km from Niseko, not a measurement on the slope.
2. Long records. data/nino34-long.csv (HadISST1 Nino 3.4, NOAA PSL) picks
   the strong El Nino winters back to 1877. Each one is compared with the ten
   winters around it at Suttsu and Sapporo (December mean temperature and
   deepest snow, which have no homogeneity break).
3. Weekly odds at Rusutsu (Kimobetsu), Kiroro (Akaigawa), west Niseko
   (Rankoshi), Sukayu (890 m, northern Honshu) and Shumarinai.
"""
import csv
import datetime as dt
import json
import math
import pathlib
from collections import defaultdict

import numpy as np

import weekly_odds as wo

HERE = pathlib.Path(__file__).parent
DATA = HERE / "data"
LAPSE = 6.5
HEIGHTS = {"base": 250, "mid": 800, "top": 1200}
STRONG = wo.STRONG


def clean(o):
    if isinstance(o, float) and math.isnan(o):
        return None
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, list):
        return [clean(v) for v in o]
    return o


# ---------- 1. upper air ----------
def load_upper():
    """{date: (mean t850, mean z850)} from the 00 and 12 UTC soundings."""
    acc = defaultdict(list)
    for r in csv.DictReader(open(DATA / "sapporo-upper.csv", encoding="utf-8")):
        if r["hour_utc"] not in ("0", "12") or r["t850_c"] == "" or r["z850_m"] == "":
            continue
        t, z = float(r["t850_c"]), float(r["z850_m"])
        if -40 <= t <= 15 and 1000 <= z <= 1700:  # drop the few bad values
            acc[dt.date.fromisoformat(r["date"])].append((t, z))
    return {d: (float(np.mean([x[0] for x in v])), float(np.mean([x[1] for x in v]))) for d, v in acc.items()}


def at_height(t850, z850, h):
    return t850 + LAPSE * (z850 - h) / 1000


def upper_air():
    up = load_upper()
    # Sanity check against the Kutchan thermometer at 176 m.
    kut = {r["date"]: r["temp_mean_c"] for r in wo.load_daily("kutchan") if r["temp_mean_c"] is not None}
    pairs = [(at_height(*up[d], 176), kut[d]) for d in up if d in kut and d.year >= 1991 and d.month in (12, 1, 2)]
    est, obs = np.array(pairs).T
    check = {"days": len(pairs), "bias_c": round(float(np.mean(est - obs)), 1), "corr": round(float(np.corrcoef(est, obs)[0, 1]), 2),
             "kutchan_thaw_pct": round(100 * float(np.mean(obs > 0))), "estimate_thaw_pct": round(100 * float(np.mean(est > 0)))}

    def weeks(only=None, first=1991, last=2025):
        days = defaultdict(list)
        for d, (t, z) in up.items():
            w = wo.week_of(d)
            if w and first <= w[0] <= last and (not only or w[0] in only):
                days[w[1]].append((t, z))
        out = []
        for wk in range(1, 14):
            v = days[wk]
            row = {"week": wk, "starts": (dt.date(2026, 12, 1) + dt.timedelta(days=7 * (wk - 1))).strftime("%-d %b"), "days": len(v), "t850": round(float(np.mean([x[0] for x in v])), 1)}
            for k, h in HEIGHTS.items():
                row[k] = round(100 * float(np.mean([at_height(t, z, h) > 0 for t, z in v])))
            out.append(row)
        return out

    # Month by month: strong El Nino winters against the ten winters around each.
    month = defaultdict(lambda: defaultdict(list))
    for d, (t, z) in up.items():
        if d.month in (12, 1, 2):
            month[d.year if d.month == 12 else d.year - 1][d.month].append((t, z))
    enso = {}
    for m, name in ((12, "dec"), (1, "jan"), (2, "feb")):
        series = {w: v[m] for w, v in month.items() if len(v.get(m, [])) >= 20}
        rows = {}
        for w in STRONG:
            near = [x for x in range(w - 5, w + 6) if x != w and x in series]
            if w not in series or len(near) < 6:
                continue
            mean = lambda vs: float(np.mean([t for t, _ in vs]))
            thaw = lambda vs: 100 * float(np.mean([at_height(t, z, HEIGHTS["mid"]) > 0 for t, z in vs]))
            rows[w] = {"t850_diff": round(mean(series[w]) - float(np.mean([mean(series[x]) for x in near])), 1),
                       "mid_thaw": round(thaw(series[w])), "mid_thaw_near": round(float(np.mean([thaw(series[x]) for x in near])))}
        enso[name] = {"winters": rows, "t850_diff_median": round(float(np.median([r["t850_diff"] for r in rows.values()])), 1),
                      "mid_thaw_median": round(float(np.median([r["mid_thaw"] for r in rows.values()]))),
                      "mid_thaw_near_median": round(float(np.median([r["mid_thaw_near"] for r in rows.values()])))}
    return {"lapse_c_per_km": LAPSE, "heights_m": HEIGHTS, "check_vs_kutchan": check, "weeks_all": weeks(), "weeks_strong": weeks(only=STRONG), "enso": enso}


# ---------- 2. long records ----------
def load_nino():
    path = DATA / "nino34-long.csv"
    if not path.exists():
        return None
    v = {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        v[(int(r["year"]), int(r["month"]))] = float(r["anom_c"])
    out = {}
    for y in range(1870, 2026):
        ks = [(y, 11), (y, 12), (y + 1, 1)]
        if all(k in v for k in ks):
            # Take out the slow warming of the ocean: compare with the 30 years around.
            out[y] = float(np.mean([v[k] for k in ks]))
    base = {}
    for y in out:
        near = [out[x] for x in range(y - 15, y + 16) if x in out]
        base[y] = out[y] - float(np.mean(near))
    return base


def load_long(name, field):
    out = defaultdict(dict)
    for r in csv.DictReader(open(DATA / f"{name}-monthly-long.csv", encoding="utf-8")):
        y, m = int(r["year"]), int(r["month"])
        if m in (12, 1, 2) and r[field] != "" and r["flag"] != "1":
            out[y if m == 12 else y - 1][m] = float(r[field])
    return out


def long_records(threshold=1.3):
    nino = load_nino()
    if nino is None:
        return None
    strong = sorted(y for y, a in nino.items() if a >= threshold)
    res = {"index": "HadISST1 Nino 3.4, November to January mean, against the 31 years around each winter", "threshold_c": threshold,
           "strong_winters": {y: round(nino[y], 2) for y in strong}, "stations": {}}
    for name in ("suttsu", "sapporo"):
        st = {}
        for field, kind in (("temp_mean_c", "diff"), ("deepest_snow_cm", "pct"), ("snowfall_cm", "pct")):
            data = load_long(name, field)
            for m, mn in ((12, "dec"), (1, "jan"), (2, "feb")):
                series = {w: v[m] for w, v in data.items() if m in v}
                if field == "snowfall_cm":  # not comparable across the 2005-06 method change
                    series = {w: x for w, x in series.items() if w >= 1953}
                rows = {}
                for w in strong:
                    near = [series[x] for x in range(w - 5, w + 6) if x != w and x in series and not (field == "snowfall_cm" and (min(x, w) < 2005 <= max(x, w)))]
                    if w not in series or len(near) < 6:
                        continue
                    ref = float(np.median(near))
                    rows[w] = round(series[w] - ref, 1) if kind == "diff" else (round(100 * series[w] / ref) if ref > 0 else None)
                vals = [x for x in rows.values() if x is not None]
                early = [x for w, x in rows.items() if x is not None and w < 1961]
                st[f"{field}_{mn}"] = {"winters": rows, "n": len(vals), "median": round(float(np.median(vals)), 1) if vals else None,
                                      "below": sum(1 for x in vals if x < (0 if kind == "diff" else 100)),
                                      "n_before_1961": len(early), "median_before_1961": round(float(np.median(early)), 1) if early else None}
        res["stations"][name] = st
    return res


# ---------- 3. more stations ----------
MORE = {
    "kutchan": ("Niseko (Kutchan)", 176, ()),
    "rankoshi": ("West Niseko (Rankoshi)", 39, ()),
    "kimobetsu": ("Rusutsu (Kimobetsu)", 264, ()),
    "akaigawa": ("Kiroro (Akaigawa)", 148, ()),
    "furano": ("Furano", 174, ()),
    "shumarinai": ("Shumarinai", 255, ()),
    "sukayu": ("Sukayu, Honshu", 890, ()),
}


def more_stations():
    out = {}
    for key, (label, elev, breaks) in MORE.items():
        first = 1991
        with np.errstate(all="ignore"):
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                allw = wo.weekly(key, first, 2025)
                strong = wo.weekly(key, first, 2025, only=STRONG)
        o = {"label": label, "elevation_m": elev, "weeks": allw, "weeks_strong": strong}
        if key not in ("kutchan", "furano"):
            o["enso"] = wo.enso_percent(key, breaks)
        out[key] = o
    return out


if __name__ == "__main__":
    result = clean({"upper_air": upper_air(), "long_records": long_records(), "stations": more_stations()})
    (HERE / "analysis2.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    ua = result["upper_air"]
    print("check", ua["check_vs_kutchan"])
    print("week  t850  base mid top | strong: base mid top")
    for a, b in zip(ua["weeks_all"], ua["weeks_strong"]):
        print(f"{a['starts']:>7} {a['t850']:6} {a['base']:4} {a['mid']:4} {a['top']:4} | {b['base']:4} {b['mid']:4} {b['top']:4}")
    for m, e in ua["enso"].items():
        print(m, "t850 diff", e["t850_diff_median"], "mid thaw", e["mid_thaw_median"], "vs", e["mid_thaw_near_median"], {w: (r["t850_diff"], r["mid_thaw"], r["mid_thaw_near"]) for w, r in e["winters"].items()})
    lr = result["long_records"]
    if lr:
        print("strong", lr["strong_winters"])
        for name, st in lr["stations"].items():
            for k, v in st.items():
                print(name, k, "n", v["n"], "median", v["median"], "below", v["below"], "| before 1961: n", v["n_before_1961"], "median", v["median_before_1961"])
    print("station              week: powder% / base cm / thaw%   (weeks of 1 Dec, 22 Dec, 19 Jan, 9 Feb)")
    for key, s in result["stations"].items():
        pick = [s["weeks"][i] for i in (0, 3, 7, 10)]
        print(f"{s['label']:24}" + "  ".join(f"{w['powder']}/{w['depth_median']}/{w['thaw']}" for w in pick) + ("   enso dec/jan/feb " + "/".join(str(s['enso'][m]['median']) for m in ('dec', 'jan', 'feb')) if 'enso' in s else ""))
