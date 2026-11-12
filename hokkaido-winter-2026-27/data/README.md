# Hokkaido / Honshu winter station data (JMA)

Produced by `scrape.py` and `jma.py` (stdlib only). Run `python -X utf8 scrape.py A B C D E F` to redo it. The script reads from the page cache in `raw/` (or the folder in `JMA_CACHE`) and only re-fetches the current month and year. Do not commit the cache.

Source: https://www.data.jma.go.jp/stats/etrn/ , pages daily_s1/daily_a1 and monthly_s1/monthly_a1.

Files:

| Files | Part | Content |
| --- | --- | --- |
| `kutchan-daily.csv`, `furano-daily.csv` | A | Daily, November to March |
| `<name>-monthly.csv` (16 stations) | B | Monthly, November to March, winters 1981-82 to 2025-26 |
| `kimobetsu-daily.csv`, `akaigawa-daily.csv`, `rankoshi-daily.csv`, `sukayu-daily.csv`, `shumarinai-daily.csv` | C | Daily, November to March, first winter on the page (not before 1976-77) to yesterday. Same columns as `kutchan-daily.csv` |
| `rankoshi-monthly.csv`, `sukayu-monthly.csv`, `shumarinai-monthly.csv` | D | Same as part B |
| `suttsu-monthly-long.csv`, `kutchan-monthly-long.csv`, `sapporo-monthly-long.csv`, `otaru-monthly-long.csv` | E | Monthly, November to March only, from the first year on the station page to November 2026 (incomplete month, `flag=1`). Same columns as the monthly files |
| `stations.csv` | F | Name, `prec_no`, `block_no`, kind (`s` staffed, `a` AMeDAS), Japanese name, latitude and longitude (decimal degrees, and degrees and minutes as JMA shows them), elevation in m. From the `viewPoint(...)` data of the JMA prefecture station lists (`select/prefecture.php?prec_no=NN`) |
| `sapporo-upper.csv` | `igra.py` | Sapporo radiosonde (see below) |
| `nino34-long.csv` | download | Monthly Niño 3.4 anomaly (`year,month,anom_c`), HadISST1, 1870 on; -99.99 (missing) months left out |

Niño 3.4 long index: NOAA PSL, https://psl.noaa.gov/data/timeseries/month/data/nino34.long.anom.data (the old `gcos_wgsp/Timeseries/Data/` path returns 404). The file states "HadISST, Anomaly from 1981-2010", region 5N-5S 170W-120W. Read on 2026-11-12.

New stations (parts C and D): Rankoshi 蘭越 16/0055 (39 m), Sukayu 酸ケ湯 in Aomori 31/1079 (890 m), Shumarinai 朱鞠内 in Horokanai 12/1279 (255 m; JMA lists it under prec 12, Kamikawa). All three have a snow gauge, so no substitute station was needed. Snow depth starts in winter 1981-82 at Kimobetsu, Rankoshi and Shumarinai, in 1979-80 at Sukayu and in 1988-89 at Akaigawa. Rows before that hold precipitation (and temperature) only. Akaigawa has no temperature, wind or sunshine sensor, so those columns are empty.

Caveats for part E:
- Snowfall totals start in 1953 at all four stations. Deepest snow starts in 1890 (Sapporo), 1891 (Suttsu), 1943 (Otaru) and 1944 (Kutchan).
- Sapporo's first rows are January 1877, Suttsu's November 1884.

Upper air (`sapporo-upper.csv`). Source: NOAA NCEI IGRA v2, period-of-record file `JAM00047412-data.txt.zip` (https://www.ncei.noaa.gov/data/integrated-global-radiosonde-archive/access/data-por/). Run `python -X utf8 igra.py JAM00047412-data.txt.zip`; do not commit the zip. One row per sounding in November to March from November 1961: `date`, `hour_utc`, `t925_c`, `t850_c`, `t700_c`, `z850_m`. Only standard pressure-level records (LVLTYP1 = 1) are used; temperature is converted from tenths of a degree; -9999 and -8888 become empty cells. Soundings with none of the four values (wind-only ascents) are left out. Caveats:
- No quality control beyond the IGRA flags is applied. A few values are clearly wrong, for example t850 = 27.2 °C on 1989-01-19 18 UTC. Use the 00 and 12 UTC soundings for climate work; the 06 and 18 UTC ones are fewer and less reliable.
- 925 hPa is often missing in the early decades.

How cells were cleaned:
- `)` (quasi-normal value) was removed.
- A row gets `flag=1` when any kept value carried `]` (insufficient data) or `#` (questionable value).
- `--`, `///`, `×` and blank cells are left empty.

Caveat: on JMA pages `--` means the phenomenon did not occur (for example, no snowfall that day), so it is effectively 0. Staffed stations (`*_s1` pages: Kutchan, Sapporo, Otaru, Iwamizawa, Asahikawa, Takada) write `--` for days with no precipitation or snowfall, so those cells are empty here. AMeDAS pages usually write `0` instead. For sums, treat empty snowfall/precip at staffed stations as 0 when the other columns of the row are present. The raw pages in `raw/` keep the original markers.

Homogeneity breaks, from the red lines on the JMA annual pages (annually_s / annually_a):
- Kutchan snowfall total: dotted red line starting cold-season year 2006 (Aug 2005 to Jul 2006). The data are not homogeneous across that point, but extremes are still comparable. There is also a solid line at cold-season year 1953.
- Kutchan deepest snow: no line.
- Furano: no line on snowfall or snow depth. There are dotted lines on temperature and max wind at 2003 and 2008.
- Staffed stations, checked by `scrape.py E` (a line is given as the year where the new part starts; cold-season years for snow):

| Station | Snowfall total | Deepest snow | Mean temperature |
| --- | --- | --- | --- |
| Suttsu 47421 | solid 1953, dotted 2006 | none | none |
| Kutchan 47433 | solid 1953, dotted 2006 | none | none |
| Sapporo 47412 | solid 1953, dotted 2006 | none | none |
| Otaru 47411 | solid 1953, dotted 1999 | none | none |

  JMA's legend: a red line means the station moved, the instrument changed or the observation interval changed, so the data before and after it are not homogeneous. Across a solid line the values and records cannot be compared; across a dotted line the extremes can. The 1953 line is where the snowfall series starts. No line was found on deepest snow or mean temperature at these four stations.
