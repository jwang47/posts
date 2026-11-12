#!/usr/bin/env python3
"""Download the raw data for the climate analysis. Standard library only.

    python -X utf8 data/fetch.py            # all sources
    python -X utf8 data/fetch.py noaa nasa  # only names that contain a word

Each source is tried once. A blocked host is recorded in manifest.csv as
`failed`; the other sources still run. The cloud container reaches only
GitHub and the Berkeley Earth bucket; run the script on a home machine for
the agency sites (NOAA, NASA, Met Office, ECMWF, NSIDC, JMA).

Large files go to data/cache/ (not committed) and a trimmed extract is
written beside this script. Small files are committed as downloaded.
"""
import csv
import datetime
import hashlib
import os
import shutil
import subprocess
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
UA = "posts-climate-analysis (github.com/jwang47/posts)"
IGCC_REPO = "https://github.com/ClimateIndicator/data.git"
IGCC_COMMIT = "d9726573dccd9381652432b58b38f670af493c1c"

# name, url, path under data/ (None = cache only, an extract is made)
SOURCES = [
    ("owid-co2", "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv", None),
    ("owid-co2-codebook", "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-codebook.csv", "owid/owid-co2-codebook.csv"),
    ("owid-energy", "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv", None),
    ("owid-energy-codebook", "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-codebook.csv", "owid/owid-energy-codebook.csv"),
    ("berkeley-earth-annual", "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_summary.txt", "primary/berkeley-earth-land-ocean-annual.txt"),
    ("noaa-co2-mlo-annual", "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.csv", "primary/noaa-co2-annmean-mlo.csv"),
    ("noaa-co2-mlo-monthly", "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv", "primary/noaa-co2-mm-mlo.csv"),
    ("noaa-co2-global-annual", "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_gl.csv", "primary/noaa-co2-annmean-global.csv"),
    ("noaa-co2-global-growth", "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_gr_gl.csv", "primary/noaa-co2-growth-global.csv"),
    ("noaa-ch4-global-annual", "https://gml.noaa.gov/webdata/ccgg/trends/ch4/ch4_annmean_gl.csv", "primary/noaa-ch4-annmean-global.csv"),
    ("noaa-n2o-global-annual", "https://gml.noaa.gov/webdata/ccgg/trends/n2o/n2o_annmean_gl.csv", "primary/noaa-n2o-annmean-global.csv"),
    ("nasa-gistemp", "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv", "primary/nasa-gistemp-global-monthly.csv"),
    ("hadcrut5-annual", "https://www.metoffice.gov.uk/hadobs/hadcrut5/data/HadCRUT.5.1.0.0/analysis/diagnostics/HadCRUT.5.1.0.0.analysis.summary_series.global.annual.csv", "primary/hadcrut5-global-annual.csv"),
    ("hadcrut5-monthly", "https://www.metoffice.gov.uk/hadobs/hadcrut5/data/HadCRUT.5.1.0.0/analysis/diagnostics/HadCRUT.5.1.0.0.analysis.summary_series.global.monthly.csv", "primary/hadcrut5-global-monthly.csv"),
    ("noaa-globaltemp-annual", "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/12/12/1850-2026/data.csv", "primary/noaa-globaltemp-annual.csv"),
    ("era5-daily-global", "https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv", "primary/era5-daily-2t-global.csv"),
    ("nsidc-arctic-september", "https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/N_09_extent_v4.0.csv", "primary/nsidc-arctic-september-extent.csv"),
    ("nsidc-antarctic-february", "https://noaadata.apps.nsidc.org/NOAA/G02135/south/monthly/data/S_02_extent_v4.0.csv", "primary/nsidc-antarctic-february-extent.csv"),
    ("noaa-oni", "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt", "primary/noaa-oni.txt"),
    ("noaa-sea-level", "https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_gbl_free_ref_90.csv", "primary/noaa-star-global-sea-level.csv"),
    ("jma-japan-annual-temp", "https://www.data.jma.go.jp/cpdinfo/temp/list/csv/an_jpn.csv", "primary/jma-japan-annual-temp.csv"),
    ("jma-world-annual-temp", "https://www.data.jma.go.jp/cpdinfo/temp/list/csv/an_wld.csv", "primary/jma-world-annual-temp.csv"),
]

CO2_ENTITIES = [
    "World", "China", "United States", "European Union (27)", "India", "Japan",
    "Russia", "Indonesia", "Brazil", "United Kingdom", "Germany",
    "High-income countries", "Upper-middle-income countries",
    "Lower-middle-income countries", "Low-income countries", "Africa",
    "International aviation", "International shipping",
]
CO2_COLUMNS = [
    "country", "year", "population", "co2", "co2_per_capita",
    "co2_including_luc", "land_use_change_co2", "coal_co2", "oil_co2",
    "gas_co2", "cement_co2", "flaring_co2", "consumption_co2",
    "consumption_co2_per_capita", "cumulative_co2", "share_global_co2",
    "share_global_cumulative_co2", "methane", "nitrous_oxide", "total_ghg",
    "total_ghg_excluding_lucf", "ghg_per_capita", "temperature_change_from_ghg",
    "share_of_temperature_change_from_ghg",
]
ENERGY_ENTITIES = ["World", "China", "United States", "European Union (27)", "India", "Japan"]
ENERGY_COLUMNS = [
    "country", "year", "electricity_generation", "electricity_demand",
    "coal_electricity", "gas_electricity", "oil_electricity",
    "fossil_electricity", "nuclear_electricity", "hydro_electricity",
    "solar_electricity", "wind_electricity", "renewables_electricity",
    "low_carbon_electricity", "coal_share_elec", "gas_share_elec",
    "fossil_share_elec", "nuclear_share_elec", "hydro_share_elec",
    "solar_share_elec", "wind_share_elec", "renewables_share_elec",
    "low_carbon_share_elec", "primary_energy_consumption",
    "fossil_share_energy", "low_carbon_share_energy", "carbon_intensity_elec",
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def download(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r, open(dest + ".part", "wb") as f:
        shutil.copyfileobj(r, f)
    os.replace(dest + ".part", dest)


def extract(src, dest, entities, columns, first_year):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(src, newline="", encoding="utf-8") as f, \
            open(dest, "w", newline="", encoding="utf-8") as g:
        rows = csv.DictReader(f)
        out = csv.DictWriter(g, columns, extrasaction="ignore", lineterminator="\n")
        out.writeheader()
        for row in rows:
            if row["country"] in entities and int(row["year"]) >= first_year:
                out.writerow(row)


def fetch_igcc():
    """Copy data/base from the Indicators of Global Climate Change repo."""
    repo = os.path.join(CACHE, "igcc-repo")
    if not os.path.isdir(repo):
        os.makedirs(CACHE, exist_ok=True)
        subprocess.run(["git", "clone", "-q", IGCC_REPO, repo], check=True)
    subprocess.run(["git", "-C", repo, "fetch", "-q", "origin"], check=False)
    subprocess.run(["git", "-C", repo, "checkout", "-q", IGCC_COMMIT], check=True)
    dest = os.path.join(HERE, "igcc")
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(os.path.join(repo, "data", "base"), dest)
    for name in ("LICENSE", "CITATION.cff", "README.md"):
        shutil.copy(os.path.join(repo, name), os.path.join(dest, "UPSTREAM-" + name))


def main():
    words = [w.lower() for w in sys.argv[1:]]
    want = lambda name: not words or any(w in name for w in words)
    today = datetime.date.today().isoformat()
    path = os.path.join(HERE, "manifest.csv")
    rows = {}
    if os.path.exists(path):
        with open(path, newline="", encoding="utf-8") as f:
            rows = {r["name"]: r for r in csv.DictReader(f)}

    for name, url, rel in SOURCES:
        if not want(name):
            continue
        dest = os.path.join(HERE, rel) if rel else os.path.join(CACHE, name + ".csv")
        try:
            download(url, dest)
            rows[name] = dict(name=name, file=rel or "(cache; see extract)", url=url,
                              read_on=today, bytes=os.path.getsize(dest),
                              sha256=sha256(dest), status="ok")
            print("ok    ", name)
        except Exception as e:  # a blocked host must not stop the others
            old = rows.get(name, {})
            if old.get("status") != "ok":
                rows[name] = dict(name=name, file=rel or "", url=url, read_on=today,
                                  bytes="", sha256="", status="failed: %s" % str(e)[:80])
            print("FAILED", name, e)

    if want("owid-co2") and os.path.exists(os.path.join(CACHE, "owid-co2.csv")):
        extract(os.path.join(CACHE, "owid-co2.csv"),
                os.path.join(HERE, "owid", "co2-extract.csv"), CO2_ENTITIES, CO2_COLUMNS, 1850)
    if want("owid-energy") and os.path.exists(os.path.join(CACHE, "owid-energy.csv")):
        extract(os.path.join(CACHE, "owid-energy.csv"),
                os.path.join(HERE, "owid", "energy-extract.csv"), ENERGY_ENTITIES, ENERGY_COLUMNS, 1985)
    if want("igcc"):
        try:
            fetch_igcc()
            rows["igcc"] = dict(name="igcc", file="igcc/", url=IGCC_REPO, read_on=today,
                                bytes="", sha256="git " + IGCC_COMMIT, status="ok")
            print("ok     igcc")
        except Exception as e:
            print("FAILED igcc", e)

    with open(path, "w", newline="", encoding="utf-8") as f:
        out = csv.DictWriter(f, ["name", "file", "url", "read_on", "bytes", "sha256", "status"],
                             lineterminator="\n")
        out.writeheader()
        for name in sorted(rows):
            out.writerow(rows[name])


if __name__ == "__main__":
    main()
