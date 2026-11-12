"""Week-by-week odds at Kutchan and Furano, and the El Nino effect by station.

Run: python3 weekly_odds.py   (needs numpy; writes analysis.json)

Data: data/*.csv, JMA station records (see data/README.md).
Weeks are 7-day blocks that start on 1 December. Week 13 ends on 1 March.
A winter is named by its December year.

Definitions (daily values at the town station, not on the mountain):
- powder day: 20 cm or more of new snow
- snow day: 10 cm or more of new snow
- thaw day: daily mean temperature above 0 C
- rain-risk day: thaw day with 1 mm or more of precipitation
- sunny day: 3 hours or more of sunshine
- windy day: maximum 10-minute wind of 8 m/s or more
"""
import csv
import datetime as dt
import json
import pathlib
from collections import defaultdict

import numpy as np

HERE = pathlib.Path(__file__).parent
DATA = HERE / "data"
STRONG = [1965, 1972, 1982, 1991, 1997, 2009, 2015, 2023]
STAFFED = {"kutchan", "sapporo", "otaru", "iwamizawa", "asahikawa", "takada"}


def num(text):
    return float(text) if text not in ("", None) else None


def load_daily(name):
    rows = []
    for r in csv.DictReader(open(DATA / f"{name}-daily.csv", encoding="utf-8")):
        d = dt.date.fromisoformat(r["date"])
        row = {k: num(v) for k, v in r.items() if k not in ("date", "flag")}
        row["date"] = d
        row["flag"] = r["flag"] == "1"
        if name in STAFFED:  # "--" on a staffed-station page means none fell
            for key in ("snowfall_cm", "precip_mm"):
                if row[key] is None and row["temp_mean_c"] is not None:
                    row[key] = 0.0
            if row["snow_depth_cm"] is None and row["temp_mean_c"] is not None:
                row["snow_depth_cm"] = 0.0
        rows.append(row)
    return rows


def week_of(d):
    """(winter, week 1..13) for dates from 1 Dec to 1 Mar, else None."""
    winter = d.year if d.month == 12 else d.year - 1
    off = (d - dt.date(winter, 12, 1)).days
    return (winter, off // 7 + 1) if 0 <= off < 91 else None


def weekly(name, first, last, only=None):
    days = defaultdict(list)
    for r in load_daily(name):
        w = week_of(r["date"])
        if not w or r["flag"] or not first <= w[0] <= last or (only and w[0] not in only):
            continue
        days[w[1]].append(r)
    out = []
    for wk in range(1, 14):
        rs = days[wk]

        def share(test, need):
            ok = [r for r in rs if all(r[k] is not None for k in need)]
            return round(100 * sum(1 for r in ok if test(r)) / len(ok)) if ok else None

        depth = [r["snow_depth_cm"] for r in rs if r["snow_depth_cm"] is not None]
        sun = [r["sunshine_h"] for r in rs if r["sunshine_h"] is not None]
        snow = [r["snowfall_cm"] for r in rs if r["snowfall_cm"] is not None]
        start = dt.date(2026, 12, 1) + dt.timedelta(days=7 * (wk - 1))
        out.append({
            "week": wk,
            "starts": start.strftime("%-d %b"),
            "powder": share(lambda r: r["snowfall_cm"] >= 20, ["snowfall_cm"]),
            "snow10": share(lambda r: r["snowfall_cm"] >= 10, ["snowfall_cm"]),
            "thaw": share(lambda r: r["temp_mean_c"] > 0, ["temp_mean_c"]),
            "rain": share(lambda r: r["temp_mean_c"] > 0 and r["precip_mm"] >= 1, ["temp_mean_c", "precip_mm"]),
            "sunny": share(lambda r: r["sunshine_h"] >= 3, ["sunshine_h"]),
            "windy": share(lambda r: r["wind_max_ms"] >= 8, ["wind_max_ms"]),
            "snow_per_week": round(7 * float(np.mean(snow))) if snow else None,
            "sun_h": round(float(np.mean(sun)), 1) if sun else None,
            "depth_median": round(float(np.median(depth))) if depth else None,
            "depth_low": round(float(np.percentile(depth, 10))) if depth else None,
            "depth_high": round(float(np.percentile(depth, 90))) if depth else None,
            "temp": round(float(np.mean([r["temp_mean_c"] for r in rs if r["temp_mean_c"] is not None])), 1),
            "days": len(rs),
        })
    return out


def load_monthly(name):
    """{winter: {12: cm, 1: cm, 2: cm}} of monthly snowfall."""
    out = defaultdict(dict)
    for r in csv.DictReader(open(DATA / f"{name}-monthly.csv", encoding="utf-8")):
        y, m = int(r["year"]), int(r["month"])
        if m in (12, 1, 2) and r["snowfall_cm"] != "" and r["flag"] != "1":
            out[y if m == 12 else y - 1][m] = float(r["snowfall_cm"])
    return out


def enso_percent(name, breaks=()):
    """Median snowfall in strong El Nino winters as % of the ten winters around
    each one. Neighbours never cross a measuring-method break."""
    data = load_monthly(name)
    res = {}
    for key, months in (("dec", [12]), ("jan", [1]), ("feb", [2]), ("djf", [12, 1, 2])):
        series = {w: sum(v[m] for m in months) for w, v in data.items() if all(m in v for m in months)}
        vals = {}
        for w in STRONG:
            if w not in series:
                continue
            near = [series[x] for x in range(w - 5, w + 6)
                    if x != w and x in series and not any(min(x, w) < b <= max(x, w) for b in breaks)]
            if len(near) >= 4:
                vals[w] = round(100 * series[w] / float(np.median(near)))
        res[key] = {"median": round(float(np.median(list(vals.values())))) if vals else None, "winters": vals}
    recent = [sum(v[m] for m in (12, 1, 2)) for w, v in data.items() if w >= 1991 and all(m in v for m in (12, 1, 2))]
    res["djf_mean_cm"] = round(float(np.mean(recent)))
    return res


STATIONS = {
    "kutchan": ("Niseko (Kutchan)", 140.76, 42.90, "west", (2005,)),
    "kimobetsu": ("Rusutsu (Kimobetsu)", 140.94, 42.80, "west", ()),
    "akaigawa": ("Kiroro (Akaigawa)", 140.82, 43.08, "west", ()),
    "otaru": ("Otaru", 141.02, 43.18, "west", ()),
    "sapporo": ("Sapporo", 141.33, 43.06, "west", ()),
    "iwamizawa": ("Iwamizawa", 141.79, 43.21, "west", ()),
    "asahikawa": ("Asahikawa", 142.37, 43.76, "central", ()),
    "biei": ("Asahidake side (Biei)", 142.47, 43.59, "central", ()),
    "furano": ("Furano", 142.40, 43.33, "central", ()),
    "shimukappu": ("Tomamu (Shimukappu)", 142.40, 42.98, "central", ()),
    "hakuba": ("Hakuba", 137.86, 36.70, "honshu", ()),
    "nozawaonsen": ("Nozawa Onsen", 138.44, 36.92, "honshu", ()),
    "sekiyama": ("Myoko (Sekiyama)", 138.23, 36.93, "honshu", ()),
    "yuzawa": ("Yuzawa", 138.82, 36.94, "honshu", ()),
    "takada": ("Takada (Joetsu)", 138.25, 37.11, "honshu", ()),
}

if __name__ == "__main__":
    result = {
        "kutchan_all": weekly("kutchan", 1991, 2025),
        "kutchan_recent": weekly("kutchan", 2005, 2025),
        "kutchan_strong": weekly("kutchan", 1991, 2025, only=STRONG),
        "furano_all": weekly("furano", 1991, 2025),
        "furano_strong": weekly("furano", 1991, 2025, only=STRONG),
        "stations": {k: {"label": v[0], "lon": v[1], "lat": v[2], "group": v[3], **enso_percent(k, v[4])} for k, v in STATIONS.items()},
    }
    (HERE / "analysis.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    cols = ["starts", "powder", "snow10", "thaw", "rain", "sunny", "windy", "snow_per_week", "sun_h", "depth_low", "depth_median", "depth_high", "temp"]
    for key in ("kutchan_recent", "kutchan_all", "kutchan_strong", "furano_all", "furano_strong"):
        print(key)
        print("  " + " ".join(f"{c[:7]:>7}" for c in cols))
        for w in result[key]:
            print("  " + " ".join(f"{str(w[c]):>7}" for c in cols))
    print("station              djf_cm  dec  jan  feb  djf   winters(djf)")
    for k, s in result["stations"].items():
        print(f"{s['label']:22}{s['djf_mean_cm']:5} {s['dec']['median']:4} {s['jan']['median']:4} {s['feb']['median']:4} {s['djf']['median']:4}   {s['djf']['winters']}")
