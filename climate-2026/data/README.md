# Climate analysis: raw data

Produced by `fetch.py` (standard library only). Run
`python -X utf8 fetch.py` to redo all downloads, or
`python -X utf8 fetch.py noaa nasa` for the sources whose name contains a
word. `manifest.csv` has one row per source: file, URL, date read, size,
SHA-256 and status. Large downloads go to `cache/` (not committed). All
files outside `cache/` are committed as downloaded, with no edits (the
OWID files are extracts).

The cloud container reaches only GitHub and the Berkeley Earth bucket.
The agency sites (NOAA, NASA, Met Office, ECMWF, NSIDC, JMA) return
`403` there. Run the script on a home machine for those; a failed source
stays in the manifest as `failed`. The agency files in `primary/` were
downloaded from a home machine on 2026-11-12 with curl, from the URLs in `fetch.py`
and with its User-Agent. Each was checked for HTTP 200 and for data, not
an HTML error page.

| Files | Source | Content | Licence |
| --- | --- | --- | --- |
| `igcc/` | Indicators of Global Climate Change data repository, https://github.com/ClimateIndicator/data, commit `d9726573` (19 Oct 2026). Paper: Forster et al., ESSD 18, 3889 (2026) | The `data/base` folder as published: annual global temperature 1850-2025, human-caused warming, greenhouse gas concentrations 1750-2025, radiative forcing, Earth heat inventory, sea level 1901-2025, remaining carbon budgets, emissions by gas, land precipitation, temperature extremes, marine heatwaves | CC BY 4.0 (`igcc/UPSTREAM-LICENSE`, `igcc/UPSTREAM-CITATION.cff`) |
| `owid/co2-extract.csv` | Our World in Data CO2 and greenhouse gas dataset, https://github.com/owid/co2-data. It collects the Global Carbon Budget, Jones et al. and others | 18 countries and groups, 1850 on, 24 columns. The lists are in `fetch.py`. Units are in `owid/owid-co2-codebook.csv` (CO2 in million tonnes) | CC BY 4.0 |
| `owid/energy-extract.csv` | Our World in Data energy dataset, https://github.com/owid/energy-data. It collects Ember and the Energy Institute Statistical Review | World, China, US, EU, India and Japan, 1985 on: electricity by source in TWh and in percent. Units are in `owid/owid-energy-codebook.csv` | CC BY 4.0 |
| `primary/berkeley-earth-land-ocean-annual.txt` | Berkeley Earth, https://berkeleyearth.org/data/ | Annual global land and ocean temperature anomaly against 1951-1980 | CC BY 4.0 |
| other files in `primary/` | NOAA GML (CO2, CH4, N2O), NASA GISTEMP, Met Office HadCRUT5, NOAA NCEI, ECMWF Climate Pulse (ERA5), NSIDC Sea Ice Index, NOAA CPC (ONI), NOAA STAR (sea level), JMA | Cross-checks of the IGCC values from the agencies. One row per file in the next table | Public data of each agency |

## Agency files in `primary/`

URLs are in `manifest.csv`. "Last row" is the newest data row on 2026-11-12.

| File | Source | Content | Last row |
| --- | --- | --- | --- |
| `berkeley-earth-land-ocean-annual.txt` | Berkeley Earth | Annual global anomaly, °C against 1951-1980; one set of columns with air temperature over sea ice, one with water temperature | 2024 |
| `era5-daily-2t-global.csv` | ECMWF Climate Pulse | Daily global 2 m temperature, °C, with the 1991-2020 climatology and anomaly; `status` is FINAL or PRELIMINARY | 2026-11-09 (PRELIMINARY) |
| `hadcrut5-global-annual.csv` | Met Office HadCRUT.5.1.0.0, analysis summary series | Annual global anomaly, °C against 1961-1990, with 95 % limits | 2026 (part year, to July) |
| `hadcrut5-global-monthly.csv` | same | Monthly global anomaly, °C against 1961-1990 | 2026-07 |
| `jma-japan-annual-temp.csv` | JMA | Annual Japan mean temperature anomaly, °C | 2025 |
| `jma-world-annual-temp.csv` | JMA | Annual anomaly, °C: world, Northern and Southern Hemisphere | 2025 |
| `nasa-gistemp-global-monthly.csv` | NASA GISS GISTEMP v4, GLB.Ts+dSST | Monthly and seasonal global anomaly, °C against 1951-1980; `***` = not yet available | 2026, to September |
| `noaa-ch4-annmean-global.csv` | NOAA GML | Global annual mean CH4, ppb | 2025 |
| `noaa-co2-annmean-global.csv` | NOAA GML | Global annual mean CO2, ppm | 2025 |
| `noaa-co2-annmean-mlo.csv` | NOAA GML | Mauna Loa annual mean CO2, ppm | 2025 |
| `noaa-co2-growth-global.csv` | NOAA GML | Global annual CO2 growth rate, ppm per year | 2025 |
| `noaa-co2-mm-mlo.csv` | NOAA GML | Mauna Loa monthly CO2, ppm (average and deseasonalized) | 2026-09 |
| `noaa-globaltemp-annual.csv` | NOAA NCEI Climate at a Glance | Annual global land and ocean anomaly, °C against 1901-2000 | 2025 |
| `noaa-n2o-annmean-global.csv` | NOAA GML | Global annual mean N2O, ppb | 2025 |
| `noaa-oni.txt` | NOAA CPC | Oceanic Niño Index, 3-month seasons; `TOTAL` and `ANOM` in °C | ASO 2026 (+2.46) |
| `noaa-star-global-sea-level.csv` | NOAA STAR Laboratory for Satellite Altimetry | Global mean sea level anomaly, mm, one column per altimeter mission | 2025.1268 (Sentinel-6MF) |
| `nsidc-antarctic-february-extent.csv` | NSIDC Sea Ice Index G02135 v4.0 | Antarctic February extent and area, million km² | 2026 |
| `nsidc-arctic-september-extent.csv` | same | Arctic September extent and area, million km² | 2026 |

Notes:

- The IGCC annual temperature is a mean of several datasets, so it is a
  little lower than Copernicus ERA5 or Berkeley Earth alone.
- In `igcc/earth_energy_imbalance/earth_energy_imbalance.csv` the
  `total` column stops at 2020. The ocean columns continue to 2024. The
  last row has no year.
- Our World in Data `co2` is fossil fuel and cement CO2 before the
  subtraction of cement carbonation. The Global Carbon Budget headline
  is lower for that reason.
- The download through `archive/<sha>.tar.gz` is blocked in the cloud
  container, so `fetch.py` uses `git clone` for the IGCC repository.
- Each agency dataset uses its own baseline (see the table). Rebase
  before you compare anomalies.
- The NOAA GML and NOAA STAR files start with `#` comment lines
  (citation, method, notes). The NOAA NCEI file has three `#` lines
  (title, units, base period). Skip them when you parse.
- GISTEMP has a title line (`Land-Ocean: Global Means`) before the
  header row.
- The two JMA files are Shift-JIS (cp932), not UTF-8. Read them with
  `encoding="cp932"`. Headers: `年,偏差` (year, anomaly) and
  `年,世界全体,北半球,南半球` (year, world, NH, SH). Values carry an
  explicit `+` sign.
- HadCRUT.5.0.2.0 is superseded; its monthly file stops at 2025-02.
  `fetch.py` reads HadCRUT.5.1.0.0 since 2026-11-12.
- The 2026 row of HadCRUT5 annual and the ERA5 days after the last FINAL
  date are not final values.
- NSIDC changed the source dataset from NSIDC-0051 to NSIDC-0803 in
  recent years (column `source_dataset`).
