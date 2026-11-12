"""Sapporo upper-air temperatures from NOAA IGRA v2 (stdlib only).

Usage:  python -X utf8 igra.py JAM00047412-data.txt.zip [sapporo-upper.csv]

Input: the IGRA v2 period-of-record file for station JAM00047412
https://www.ncei.noaa.gov/data/integrated-global-radiosonde-archive/access/data-por/JAM00047412-data.txt.zip
Output: one row per sounding in November to March from 1961 on, with the
925, 850 and 700 hPa temperatures and the 850 hPa height. Only standard
pressure-level records (LVLTYP1 = 1) are used. TEMP is in tenths of a
degree C; -9999 and -8888 are missing and give an empty cell. Soundings with
none of the four values (wind-only ascents) are left out. No other quality
control is applied.
"""
import csv, io, os, sys, zipfile

LEVELS = {92500: "t925_c", 85000: "t850_c", 70000: "t700_c"}
COLS = ["date", "hour_utc", "t925_c", "t850_c", "t700_c", "z850_m"]
MISSING = (-9999, -8888)


def num(s):
    s = s.strip()
    if not s:
        return None
    v = int(s)
    return None if v in MISSING else v


def soundings(fileobj):
    head, levels = None, {}
    for line in fileobj:
        if line.startswith("#"):
            if head:
                yield head, levels
            head = (int(line[13:17]), int(line[18:20]), int(line[21:23]), int(line[24:26]))
            levels = {}
        elif head and line[0] == "1":  # standard pressure level
            p = num(line[9:15])
            if p is not None:
                levels[p] = (num(line[16:21]), num(line[22:27]))
    if head:
        yield head, levels


def main(src, dst):
    with zipfile.ZipFile(src) as z:
        name = [n for n in z.namelist() if n.endswith(".txt")][0]
        f = io.TextIOWrapper(z.open(name), encoding="ascii", errors="replace")
        rows = []
        for (y, m, d, h), lv in soundings(f):
            if y < 1961 or m not in (11, 12, 1, 2, 3) or (y == 1961 and m < 11):
                continue
            row = [f"{y:04d}-{m:02d}-{d:02d}", "" if h == 99 else h]
            for p, col in LEVELS.items():
                t = lv.get(p, (None, None))[1]
                row.append("" if t is None else f"{t / 10:.1f}")
            z850 = lv.get(85000, (None, None))[0]
            row.append("" if z850 is None else z850)
            if any(v != "" for v in row[2:]):  # skip wind-only soundings
                rows.append(row)
    with open(dst, "w", newline="", encoding="utf-8") as out:
        w = csv.writer(out)
        w.writerow(COLS)
        w.writerows(rows)
    print(f"{dst}: {len(rows)} rows, {rows[0][0]} to {rows[-1][0]}")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, "sapporo-upper.csv"))
