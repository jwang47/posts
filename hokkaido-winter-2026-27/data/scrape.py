"""Download JMA daily (Part A) and monthly (Part B) winter data to CSV.

Usage:  python -X utf8 scrape.py [A|B]   (default: both)

Rules: ')' (quasi-normal) is stripped; a row gets flag=1 when any kept value
had ']' (insufficient data) or '#' (questionable). Missing / no-phenomenon
markers ('--', '///', 'x', blank) become empty cells. Raw pages are cached
in raw/ so the CSVs can be regenerated offline.
"""
import csv, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jma

OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today()
WINTER_MONTHS = (11, 12, 1, 2, 3)


def has(*words):
    return lambda lab: all(w in lab for w in words)


def lacks(pred, *bad):
    return lambda lab: pred(lab) and not any(b in lab for b in bad)


DAILY_COLS = [
    ("precip_mm", lambda l: l.startswith("降水量") and "合計" in l),
    ("temp_mean_c", lambda l: l.startswith("気温") and "平均" in l),
    ("temp_max_c", lambda l: l.startswith("気温") and "最高" in l),
    ("temp_min_c", lambda l: l.startswith("気温") and "最低" in l),
    ("wind_mean_ms", has("平均風速")),
    ("wind_max_ms", lambda l: "最大" in l and "瞬間" not in l and l.replace("(m/s)", "").split("/")[-1].startswith("風速")),
    ("gust_max_ms", lambda l: "最大瞬間" in l and l.replace("(m/s)", "").split("/")[-1].startswith("風速")),
    ("sunshine_h", has("日照")),
    ("snowfall_cm", has("降雪")),
    ("snow_depth_cm", has("最深積雪")),
]

MONTHLY_COLS = [
    ("snowfall_cm", lambda l: "降雪" in l and "合計" in l and "日合計" not in l),
    ("deepest_snow_cm", has("最深積雪")),
    ("temp_mean_c", lambda l: l.startswith("気温") and "日平均" in l),
]


def map_cols(labels, spec):
    idx = {}
    for name, pred in spec:
        hits = [i for i, l in enumerate(labels) if pred(l)]
        idx[name] = hits[0] if hits else None
    return idx


def extract(row, idx):
    out, flag = {}, False
    for name, i in idx.items():
        raw = row[i] if i is not None and i < len(row) else ""
        v, f = jma.clean(raw)
        if "#" in raw:
            f = True
        out[name] = "" if v is None else v
        flag = flag or f
    return out, flag


def winter_months(first_year):
    """(year, month) for Nov..Mar starting Nov first_year, up to today."""
    y = first_year
    while True:
        for m in WINTER_MONTHS:
            yy = y if m >= 11 else y + 1
            if datetime.date(yy, m, 1) > TODAY:
                return
            yield yy, m
        y += 1


def daily(name, prec, block, kind, first_year):
    page = "daily_s1" if kind == "s" else "daily_a1"
    cols = [c for c, _ in DAILY_COLS]
    rows, missing_cols = [], set()
    for y, m in winter_months(first_year):
        t = jma.fetch(f"view/{page}.php?prec_no={prec}&block_no={block}&year={y}&month={m}",
                      force=(y == TODAY.year and m == TODAY.month))
        labels, data = jma.parse_table(t)
        if not labels:
            print("  no table", y, m)
            continue
        idx = map_cols(labels, DAILY_COLS)
        missing_cols |= {k for k, v in idx.items() if v is None}
        for r in data:
            if not r[0].strip().isdigit():
                continue
            d = datetime.date(y, m, int(r[0]))
            if d >= TODAY:
                continue
            vals, flag = extract(r, idx)
            if not any(vals.values()):
                continue
            rows.append([d.isoformat()] + [vals[c] for c in cols] + ["1" if flag else ""])
    fn = os.path.join(OUT, f"{name}-daily.csv")
    with open(fn, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date"] + cols + ["flag"])
        w.writerows(rows)
    print(f"{fn}: {len(rows)} rows; columns absent on page: {sorted(missing_cols)}")
    return len(rows)


def monthly(name, prec, block, kind, first_winter=1981, last_winter=2025):
    page = "monthly_s1" if kind == "s" else "monthly_a1"
    cols = [c for c, _ in MONTHLY_COLS]
    rows = []
    for y in range(first_winter, last_winter + 2):
        t = jma.fetch(f"view/{page}.php?prec_no={prec}&block_no={block}&year={y}",
                      force=(y == TODAY.year))
        labels, data = jma.parse_table(t)
        if not labels:
            continue
        idx = map_cols(labels, MONTHLY_COLS)
        for r in data:
            if not r[0].strip().isdigit():
                continue
            m = int(r[0])
            if m not in WINTER_MONTHS:
                continue
            winter = y if m >= 11 else y - 1
            if not (first_winter <= winter <= last_winter):
                continue
            if datetime.date(y, m, 1) > TODAY:
                continue
            vals, flag = extract(r, idx)
            if not any(vals.values()):
                continue
            rows.append([y, m] + [vals[c] for c in cols] + ["1" if flag else ""])
    rows.sort(key=lambda r: (r[0], r[1]))
    fn = os.path.join(OUT, f"{name}-monthly.csv")
    with open(fn, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["year", "month"] + cols + ["flag"])
        w.writerows(rows)
    print(f"{fn}: {len(rows)} rows")
    return len(rows)


MONTHLY_STATIONS = [
    # name, prec_no, block_no, kind
    ("kutchan", 16, "47433", "s"),
    ("sapporo", 14, "47412", "s"),
    ("otaru", 16, "47411", "s"),
    ("iwamizawa", 15, "47413", "s"),
    ("asahikawa", 12, "47407", "s"),
    ("furano", 12, "0021", "a"),
    ("kimobetsu", 16, "0060", "a"),   # near Rusutsu
    ("akaigawa", 16, "1091", "a"),    # near Kiroro (no temperature sensor)
    ("yoichi", 16, "0052", "a"),      # near Kiroro, coastal
    ("shimukappu", 12, "1189", "a"),  # near Tomamu
    ("biei", 12, "1052", "a"),        # near Asahidake (Higashikawa has no snow gauge)
    ("hakuba", 48, "0396", "a"),
    ("nozawaonsen", 48, "0393", "a"),
    ("sekiyama", 54, "0998", "a"),
    ("yuzawa", 54, "0544", "a"),
    ("takada", 54, "47612", "s"),
]

if __name__ == "__main__":
    parts = sys.argv[1:] or ["A", "B"]
    if "A" in parts:
        daily("kutchan", 16, "47433", "s", 1961)
        daily("furano", 12, "0021", "a", 1981)
    if "B" in parts:
        for st in MONTHLY_STATIONS:
            monthly(*st)
