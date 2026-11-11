"""El Nino and La Nina composites of Kutchan monthly snowfall.

Run: python3 enso_composite.py   (needs numpy)

Data: kutchan-snowfall.csv, JMA station 47433, monthly snowfall totals
(see README.md for the URL). Each winter is compared with the median of the
ten winters around it (five before, five after). This removes the long
downward drift in the raw series, part of which may be a change in the
measuring method.

ENSO years are the usual NOAA ONI classification, keyed by the December
year. STRONG has a peak ONI of about 1.5 or more.
"""
import csv
import pathlib

import numpy as np

EL_NINO = [1963, 1965, 1968, 1969, 1972, 1976, 1977, 1979, 1982, 1986, 1987,
           1991, 1994, 1997, 2002, 2004, 2006, 2009, 2014, 2015, 2018, 2023]
LA_NINA = [1964, 1970, 1971, 1973, 1974, 1975, 1983, 1984, 1988, 1995, 1998,
           1999, 2000, 2005, 2007, 2008, 2010, 2011, 2016, 2017, 2020, 2021,
           2022]
STRONG = [1965, 1972, 1982, 1991, 1997, 2009, 2015, 2023]

rows = list(csv.DictReader(open(pathlib.Path(__file__).with_name("kutchan-snowfall.csv"))))
years = [int(r["winter_start_year"]) for r in rows]
months = np.array([[float(r[k]) for k in ("dec_cm", "jan_cm", "feb_cm")] for r in rows])
series = {"Dec": months[:, 0], "Jan": months[:, 1], "Feb": months[:, 2], "DJF": months.sum(1)}


def percent_of_neighbours(values):
    out = []
    for i in range(len(values)):
        near = [j for j in range(max(0, i - 5), min(len(values), i + 6)) if j != i]
        out.append(values[i] / np.median(values[near]) * 100)
    return dict(zip(years, out))


for name, values in series.items():
    pct = percent_of_neighbours(values)
    for label, group in (("El Nino", EL_NINO), ("La Nina", LA_NINA), ("strong El Nino", STRONG)):
        vals = [pct[y] for y in group]
        below = sum(v < 100 for v in vals)
        print(f"{name:3} {label:14} median {np.median(vals):4.0f}%  below neighbours {below}/{len(vals)}")
    print("    strong winters:", " ".join(f"{y}-{(y + 1) % 100:02d}:{pct[y]:.0f}%" for y in STRONG))
