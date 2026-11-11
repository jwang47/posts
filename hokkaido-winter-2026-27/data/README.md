# Hokkaido / Honshu winter station data (JMA)

Produced by `scrape.py` and `jma.py` (stdlib only). Run `python -X utf8 scrape.py A B` to redo it. The script reads from the page cache in `raw/` and only re-fetches the current month and year.

Source: https://www.data.jma.go.jp/stats/etrn/ , pages daily_s1/daily_a1 and monthly_s1/monthly_a1.

How cells were cleaned:
- `)` (quasi-normal value) was removed.
- A row gets `flag=1` when any kept value carried `]` (insufficient data) or `#` (questionable value).
- `--`, `///`, `×` and blank cells are left empty.

Caveat: on JMA pages `--` means the phenomenon did not occur (for example, no snowfall that day), so it is effectively 0. Staffed stations (`*_s1` pages: Kutchan, Sapporo, Otaru, Iwamizawa, Asahikawa, Takada) write `--` for days with no precipitation or snowfall, so those cells are empty here. AMeDAS pages usually write `0` instead. For sums, treat empty snowfall/precip at staffed stations as 0 when the other columns of the row are present. The raw pages in `raw/` keep the original markers.

Homogeneity breaks, from the red lines on the JMA annual pages (annually_s / annually_a):
- Kutchan snowfall total: dotted red line starting cold-season year 2006 (Aug 2005 to Jul 2006). The data are not homogeneous across that point, but extremes are still comparable. There is also a solid line at cold-season year 1953.
- Kutchan deepest snow: no line.
- Furano: no line on snowfall or snow depth. There are dotted lines on temperature and max wind at 2003 and 2008.
