# Climate change: where it stands and what can be done

Written 2026-11-12 by Claude, with four research workers (physical
science, emissions and policy, solutions, impacts and personal action).
Their raw notes are in
`research/`. The raw data is in `data/`, and `analyze.py` computes every
number marked [D].

Question: what is the state of climate change and global warming, and
what can we do about them?

## Answer

1. **The world is about 1.4 °C warmer than in 1850-1900, and humans
   caused almost all of it.** The 2025 global mean was 1.39 °C above
   1850-1900 [D]. The human-caused part was 1.38 °C [D]. The long-term
   level will pass 1.5 °C in about 2029 or 2030.
2. **Warming is now faster: about 0.27 °C per decade**, against about
   0.18 °C per decade in 1970-2010. Scientists agree on the faster rate.
   They do not agree on how much of it will last (section 3).
3. **The path has improved, but not enough.** In 2015 the expected
   warming by 2100 was about 3.6 °C. It is now about 2.5 to 2.8 °C under
   current policies. The worst scenarios are now unlikely. The 1.5 °C
   limit without overshoot is also gone.
4. **Emissions are near a peak but have not started to fall.** Growth of
   fossil CO2 slowed from 2.7% per year (2000-2010) to 0.9% per year
   (2019-2025) [D]. In 2025, clean electricity grew more than demand for
   the first time outside a crisis, and fossil electricity fell [D].
5. **Electricity and cars are the solved part.** Solar, wind, batteries
   and electric cars are now the cheap option in most markets. The work
   there is to build faster: grids, permits, storage and cheap finance
   for poorer countries.
6. **The unsolved part is about 40% of emissions**: steel, cement,
   chemicals, aviation, shipping, farming and land use. Methane cuts and
   an end to deforestation are the fastest and cheapest actions that are
   not being done.
7. **Each tenth of a degree is worth the effort.** No temperature is a
   cliff edge for humanity as a whole, and no temperature is safe.
   Damage grows with each step, and it falls first on people who emitted
   least. Human extinction from climate change alone is very unlikely.
   Large and permanent losses are certain.
8. **For one person in a rich country, the order is:** vote and act as a
   citizen, give to effective climate groups, then cut the big four
   (flights, car, heating, beef). Small actions such as recycling change
   little. Section 11 has numbers.

## How to read the source labels

The cloud container that wrote this report could not open most web
sites. The data files in `data/` were downloaded directly, the agency
files from a home machine. Most other facts come from search-result
text.

- **[D]** data: computed by `analyze.py` from a raw file in `data/`.
  The number is in `analysis.json`. You can check it yourself.
- **[V]** verified: the page was read directly.
- **[S]** search snippet only: the page could not be opened. The fact
  comes from search-result text for that page. Treat the number as
  provisional.
- **[M]** from model memory, not checked.

Most facts about events in 2026 are [S]. The model that wrote this
report was trained before those events, so it cannot check them from
memory. Section "What could not be verified" lists the weak points.

All temperatures are relative to 1850-1900 unless the text says
otherwise. "Gt" is a billion tonnes. "CO2e" adds the other greenhouse
gases to CO2 with their 100-year warming effect.

## 1. Where the climate is now

**Temperature.** The global mean surface temperature in 2025 was
1.39 °C above 1850-1900 [D]. This value is from the Indicators of Global Climate Change
(IGCC) record, which is a mean of several datasets. The three warmest
years are 2024 (1.51 °C), 2023 (1.44 °C) and 2025 (1.39 °C) [D]. The
mean of the last 10 years is 1.26 °C [D]. Each agency gives a slightly different value. These are from the agency
files in `data/primary/`, set to the 1850-1900 baseline [D]:

| Dataset | 2023 | 2024 | 2025 |
| --- | --- | --- | --- |
| IGCC mean | 1.44 | 1.51 | 1.39 |
| Copernicus ERA5 (1991-2020 anomaly + 0.88 °C) | 1.48 | 1.60 | 1.47 |
| Met Office HadCRUT5 | 1.47 | 1.53 | 1.41 |
| NOAA GlobalTemp | 1.34 | 1.42 | 1.29 |
| Berkeley Earth | 1.54 | 1.62 | no data in the file |

All of them put 2024 first, and all show the same step up of about
0.3 °C from 2022 to 2023.

**2026.** A very strong El Niño is in progress. The NOAA index (ONI)
for August to October 2026 is +2.46 °C [D]. That is already above the
peaks of 1982-83 (2.14) and 1997-98 (2.37), and near the record of
2015-16 (2.59) [D]. October 2026 was 1.78 °C above 1850-1900 in ERA5,
the warmest October in the record [D]. From 1 January to 9 November,
2026 is at 1.54 °C, against 1.60 °C for the same days of 2024 [D]. To
pass 2024, the rest of 2026 must be at about 1.96 °C. So 2026 will
probably be the second warmest year. Copernicus expects the same, with
a 2026 mean of 1.56 to 1.61 °C [S]
[Copernicus](https://climate.copernicus.eu/copernicus-warmest-october-record-2026-virtually-certain-exceed-15degc).
Carbon Brief gives a 67% chance of a record in the mean of six
datasets, and expects about 1.7 °C in 2027 [S]
[Carbon Brief](https://www.carbonbrief.org/state-of-the-climate-2026-likely-to-tie-with-2024-as-the-warmest-year-on-record).
The heat of an El Niño comes mostly in the year after it starts, so
2027 is the probable record year.

**One year is not the long-term level.** The Paris limits refer to a
mean over about 20 years. El Niño years are above that mean and La Niña
years are below it. The best estimate of the long-term level is the
human-caused warming: 1.38 °C in 2025 (range 1.1 to 1.7) [D]. The IGCC
authors extrapolate 1.41 °C for 2026 [D]. At 0.27 °C per decade, the
level passes 1.5 °C in about 2029 or 2030. Copernicus gets early 2029
from its own trend [S]
[Copernicus](https://climate.copernicus.eu/how-fast-world-has-moved-closer-15degc-global-warming-paris-agreement).

**Greenhouse gases** [D], 2025 against 1750:

| Gas | 1750 | 2025 | Rise | Rise per year, last 10 years |
| --- | --- | --- | --- | --- |
| CO2 | 278 ppm | 425.6 ppm | +53% | 2.6 ppm |
| Methane (CH4) | 729 ppb | 1,936 ppb | +166% | 10.2 ppb |
| Nitrous oxide (N2O) | 270 ppb | 339.4 ppb | +26% | 1.1 ppb |

The NOAA files agree: 425.62 ppm of CO2, 1,936 ppb of methane and
338.9 ppb of nitrous oxide in 2025 [D]. CO2 rose 0.8 ppm per year in
the 1960s and 2.6 ppm per year in 2015-2024 [D]. The rise of 3.76 ppm
in 2024 was the largest on record [D], because fires were large and the
land absorbed less carbon in the El Niño year [S]
[WMO](https://wmo.int/publication-series/wmo-greenhouse-gas-bulletin-no-21).
The same will probably occur in 2026-27. The rise of methane has slowed
from 16 ppb in 2022 to 7 ppb in 2025 [D].

**Heat.** The planet takes in more energy than it sends out. From 1971
to 2020 it gained about 479 ZJ of heat, and 91% of that went into the
ocean [D]. The rate of gain was 0.49 W/m² in 1971-2006 and 0.91 W/m² in
2006-2020 [D]. Satellites show about 1.3 W/m² in recent years [S]
[Eos](https://eos.org/editor-highlights/earths-energy-imbalance-is-growing-faster-than-expected).
Surface temperature can go up and down from year to year. This number
cannot, and it has about doubled.

**Sea level.** The global mean sea level in 2025 was 230 mm above 1901
[D]. The rate was 1.3 mm per year in 1901-1971 and 3.8 mm per year in
2015-2025 [D]. The NOAA satellite record gives 2.7 mm per year for its
first ten years (from 1993) and 3.7 mm per year for its last ten [D].
The WMO gives 4.75 mm per year for 2012-2025 [S]
[WMO](https://wmo.int/node/38410).

**Ice.** Glaciers lost about 390 Gt per year in 2016-2025 [S]
[WGMS](https://wgms.ch/ncc_glaciers_in_2025/). Greenland lost about
139 Gt in 2025, a mild year [S]
[Copernicus](https://climate.copernicus.eu/esotc/2025/greenland-ice-sheet).
Arctic sea ice in September was 7.1 million km² on average in
1979-1990 and 4.6 million km² in the last ten years, a fall of about
12% per decade [D]. September 2026 (4.81 million km²) was the 13th
lowest of 48 years [D]. The record low is still 2012.

## 2. Why it is warming

The IPCC says: "It is unequivocal that human influence has warmed the
atmosphere, ocean and land" [S]
[IPCC AR6 WG1 SPM](https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/).

The IGCC record divides the 1.38 °C of human-caused warming in 2025 as
follows [D]: greenhouse gases +1.63 °C, other human effects (mostly air
pollution that reflects sunlight) -0.26 °C. Natural causes (sun and
volcanoes) add 0.04 °C.

By emitted substance [D]: CO2 has caused about 1.10 °C, methane 0.56 °C,
nitrous oxide 0.12 °C and fluorinated gases 0.19 °C. Sulphur dioxide
pollution has hidden about 0.44 °C. These facts have two results:

- **Methane is about a third of the gross warming.** It stays in the air
  for about 12 years [M]. A cut in methane lowers the temperature within
  20 years. A cut in CO2 only stops the rise.
- **Clean air shows hidden warming.** Sulphur pollution kills millions
  of people, so countries remove it. Each removal adds some warming.

## 3. Is warming accelerating?

The human-caused warming rate is about 0.27 °C per decade, the highest
on record [S]
[Forster et al. 2026](https://essd.copernicus.org/articles/18/3889/2026/).
A simple trend through the data gives 0.18 °C per decade for 1970-2010
and 0.24 °C per decade for 1996-2025 [D]. So the rate is higher. The
disagreement is about the cause and the future.

- **Mainstream view.** Emissions are at a record and aerosol pollution
  is falling. Models expected a faster rate from these two causes.
  Cleaner ship fuel since 2020 adds about 0.05 °C by 2029 [S]
  [Jordan and Henry 2024](https://doaj.org/article/69479e59acac43adbb2681c718d4bd7a).
  The clean-up of East Asian air adds about 0.07 °C [S]
  [Samset et al. 2025](https://centaur.reading.ac.uk/123626).
- **Hansen's view.** James Hansen's group says aerosols hid much more
  warming than the IPCC assumes, and that the climate is more sensitive
  (4.8 °C for doubled CO2, against the IPCC's 3 °C) [S]
  [Hansen et al. 2025](https://www.columbia.edu/~jeh1/mailings/2025/Hansen_etal2025.Envir_Global.Warming.Acceleration_FULL.abs.main.SM.pdf).
  If this is correct, warming by 2050 is well above current projections.
- **The open question is clouds.** The Earth reflected less sunlight in
  2023 than in any year since 1940, because low cloud decreased. Without
  that, 2023 would have been about 0.23 °C cooler [S]
  [AWI](https://www.awi.de/en/about-us/service/press/single-view/sprunghafter-anstieg-der-erderwaermung-ist-massgeblich-auf-geringere-rueckstrahlkraft-des-planeten-zurueckzufuehren.html).
  The cause can be natural variation, less pollution, or a feedback of
  warming itself. Models show less than half of the observed rise in
  the energy imbalance [S]
  [Eos](https://eos.org/editor-highlights/earths-energy-imbalance-is-growing-faster-than-expected).

My reading: the acceleration is real. The energy imbalance is the
strongest evidence, because it does not depend on El Niño. The data do
not yet show whether sensitivity is higher than the IPCC range. The
record El Niño of 2026-27 will add high temperatures that say little
about that question. The useful test comes in about 2028-2030, when the
El Niño heat is gone.

## 4. Where it is going

**Sensitivity.** A doubling of CO2 gives about 3 °C of warming in the
end: likely range 2.5 to 4 °C, very likely range 2 to 5 °C [S]
[Carbon Brief](https://www.carbonbrief.org/guest-post-why-low-end-climate-sensitivity-can-now-be-ruled-out).

**Carbon budget.** For a 50% chance to stay below 1.5 °C, about 130 Gt
of CO2 remained at the start of 2026 [D]. The world emits about 43 Gt
of CO2 per year, so the budget ends in about 3 years. For 2 °C the
budget is about 1,055 Gt, or about 25 years at the current rate [S]
[Carbon Brief](https://www.carbonbrief.org/analysis-fossil-fuel-co2-emissions-to-set-new-record-in-2025-as-land-sink-recovers/).
Warming stops, to a first approximation, when net CO2 emissions reach
zero. It does not go down again for centuries unless CO2 is removed.

**Projected warming by 2100:**

| Source | Current policies | If all pledges are met |
| --- | --- | --- |
| UNEP Emissions Gap 2026 (Oct 2026) | about 2.8 °C | about 2.6 °C; 2.1 °C with net-zero targets |
| Climate Action Tracker (Nov 2025) | 2.6 °C | 2.1 to 2.2 °C |
| IEA World Energy Outlook 2025 | 2.5 to 2.9 °C | |

All [S]: [UNEP](https://www.unep.org/en/news-and-stories/press-release/new-unep-report-lays-out-emission-cuts-needed-return-15degc),
[Climate Action Tracker](https://climateactiontracker.org/publications/warming-projections-global-update-2025/),
[Carbon Brief on the IEA](https://www.carbonbrief.org/iea-fossil-fuel-use-will-peak-before-2030-unless-stated-policies-are-abandoned/).

Three points follow.

- In 2015 the Climate Action Tracker estimate for current policies was
  about 3.6 °C [S]
  [CAT](https://climateactiontracker.org/global/historical-progress/).
  Policy and cheap clean energy removed about 1 °C in ten years.
- The estimate has not moved in four years. UNEP gives a 6% chance to
  stay below 2 °C on current policies [S].
- UNEP now says that 1.5 °C without overshoot is not possible. The best
  path peaks at about 1.7 to 1.8 °C and comes back to 1.5 °C by 2100.
  That path needs cuts of 18% by 2030, 45% by 2035 and 69% by 2040 from
  2025 levels [S].

The very high scenario (SSP5-8.5, about 4.4 °C) is no longer thought
plausible, because coal use did not grow as it assumed [S]
[summary of CMIP7 scenarios](https://www.warpnews.org/human-progress/research-committee-that-provides-input-to-the-ipcc-drops-the-worst-climate-scenarios/).
Warming above 3 °C is still possible if sensitivity is high or if the
land and ocean absorb less carbon.

## 5. What warming does

**Already measured.**

- Heat killed about 546,000 people per year in 2012-2021 [S]
  [Lancet Countdown 2025](https://lancetcountdown.org/2025-report/).
- Weather disasters caused 45.8 million displacements in 2024, a record
  [S] [IDMC](https://www.internal-displacement.org/grid2025).
- Insured disaster losses were above $100 billion in 2024 and in 2025
  [S] [Swiss Re](https://www.swissre.com/institute/research/sigma-research/sigma-2026-01-natcat-2025-wildfire-storm-risk.html).
  More buildings in risky places explain part of this trend.
- In 2010-2020, floods, droughts and storms killed 15 times more people
  per head in highly vulnerable regions than in the least vulnerable
  regions. 3.3 to 3.6 billion people live in highly vulnerable
  conditions [S]
  [IPCC AR6 WG2](https://www.ipcc.ch/report/ar6/wg2/resources/spm-headline-statements/).

**With more warming.**

- Each 1 °C cuts the world yield of maize by 7.4%, wheat by 6.0%, rice
  by 3.2% and soy by 3.1%, before adaptation [S]
  [Zhao et al. 2017](https://hal.archives-ouvertes.fr/hal-01594919).
- Warm-water coral reefs decline 70 to 90% at 1.5 °C and more than 99%
  at 2 °C [S] IPCC SR1.5. The Global Tipping Points Report 2025 says
  the reefs have already passed their tipping point, at about 1.2 °C
  [S] [Stockholm Resilience Centre](https://www.stockholmresilience.org/research/research-stories/2025-10-13-world-reaches-first-climate-tipping-point---widespread-mortality-of-coral-reefs.html).
- Sea level is committed to rise 2 to 3 m over 2,000 years at 1.5 °C,
  and 2 to 6 m at 2 °C [S]
  [IPCC AR6 WG1](https://www.ipcc.ch/report/ar6/wg1/figures/chapter-9/figure-9-30/).
  By 2100 the likely rise is about 0.4 to 0.8 m on the middle path [M].

**Tipping points.** The same report puts the Greenland and West
Antarctic ice sheets, permafrost and the North Atlantic subpolar gyre at
"around 1.5 °C", and the Atlantic overturning circulation (AMOC) at
"around 2 °C" [S]. These are thresholds where a change starts and then
continues by itself. The ice sheets then melt over centuries. The AMOC
is the largest disagreement in the field. Some studies find a possible
collapse this century or soon after
([van Westen et al.](https://skepticalscience.com/amoc-tipping-course.html),
Drijfhout et al. 2025). A study of 34 models finds that it weakens but
does not collapse before 2100
([Scientific American on Baker et al.](https://www.scientificamerican.com/article/the-atlantic-meridional-overturning-circulation-amoc-is-safe-from-climate/)).
All [S].

**Economic cost.** The estimates differ by a factor of 10: from about
2% of world GDP at 3 °C (older models) to more than 12% per 1 °C
(Bilal and Känzig) [S] [NBER](https://www.nber.org/papers/w32450). One
well-known study (19% of income by 2049) was retracted in December 2025
[S] [Retraction Watch](https://retractionwatch.com/2025/12/03/authors-retract-nature-paper-projecting-high-costs-of-climate-change).
A central estimate of the damage from one tonne of CO2 is $185 (range
$44 to $413) [S]
[Rennert et al. 2022](https://rff.org/publications/journal-articles/comprehensive-evidence-implies-a-higher-social-cost-of-co2).
The average carbon price in force is about $21, on 29% of emissions [S]
[World Bank](https://www.worldbank.org/en/news/press-release/2026/05/19/direct-carbon-pricing-covers-nearly-one-third-of-global-emissions).

**How bad?** Two wrong ideas are common. The first is that humanity is
doomed: 56% of young people in a 10-country survey agreed with this [S]
[Grist on Hickman et al.](https://grist.org/article/climate-anxiety-study-young-people-think-humanity-is-doomed/).
Researchers who estimate extinction risk put climate change at about 1
in 1,000 this century [S]
[Toby Ord](https://www.tobyord.com/writing/the-precipice-revisited).
The second wrong idea is that 2.7 °C is acceptable because it is not
4 °C. At 2.7 °C the reefs are gone, the ice sheets are committed to
metres of sea level rise, and heat makes parts of the tropics very hard
to live in. The severe outcomes above 3 °C are less likely than before,
and they are also the least studied [S]
[Kemp et al. 2022](https://www.cam.ac.uk/stories/climateendgame).

## 6. Emissions: how much, from what, from whom

**How much.** Greenhouse gas emissions were 56.8 Gt CO2e in 2024 [D]:

| Part | Gt CO2e | Share |
| --- | --- | --- |
| CO2 from fossil fuels and industry | 38.6 | 68% |
| CO2 from land use (mostly deforestation) | 4.6 | 8% |
| Methane | 9.3 | 16% |
| Nitrous oxide | 2.6 | 5% |
| Fluorinated gases | 1.7 | 3% |

UNEP gives 58.4 Gt CO2e for 2025, about equal to 2024 [S]
[Carbon Brief](https://carbonbrief.org/unep-opportunity-has-been-lost-to-meet-1-5c-warming-limit-without-overshoot).

**The trend.** Fossil CO2 grew 2.7% per year in 2000-2010, 1.2% per
year in 2010-2019 and 0.9% per year in 2019-2025 [D]. The Global Carbon
Budget 2026 projects a fall of about 0.4% in 2026, the first since 2020
[S] [Global Carbon Budget](https://globalcarbonbudget.org/fossil-co2-emissions-decrease-in-2026/).
Part of that fall comes from the 2026 oil supply crisis (the closure of
the Strait of Hormuz), and the authors expect a rebound. Total CO2 still
rises in 2026, because fires in Southeast Asia increased land-use
emissions [S].

**From what** (2024, all gases) [S]
[EDGAR summary](https://www.industrialenergyaccelerator.org/wp-content/uploads/Explainer-Brief_02_updated.pdf):
electricity and heat about 28%, industry about 22%, transport 16%,
agriculture 12%, fuel production 11%, buildings 7%, waste 4%. Food
systems as a whole (farms, land clearing, transport, waste) are about
one third [S]
[Carbon Brief](https://www.carbonbrief.org/food-systems-responsible-for-one-third-of-human-caused-emissions/).

**From whom** (fossil CO2, 2025) [D]:

| | Gt CO2 | Share | Tonnes per person | Share of all CO2 since 1750 | Change from peak |
| --- | --- | --- | --- | --- | --- |
| China | 12.4 | 31.8% | 8.8 | 15.8% | at peak |
| United States | 5.0 | 12.9% | 14.5 | 23.3% | -18% (2005) |
| India | 3.2 | 8.2% | 2.2 | 3.7% | at peak |
| EU (27) | 2.4 | 6.2% | 5.4 | 16.1% | -41% (1979) |
| Russia | 1.8 | 4.5% | 12.3 | 6.5% | -31% (1990) |
| Japan | 1.0 | 2.5% | 7.8 | 3.8% | -27% (2013) |
| World | 39.0 | | 4.7 | | at peak |

These numbers are from Our World in Data, which uses the Global Carbon
Budget. The Global Carbon Budget headline (38.1 Gt for 2025) is lower,
mostly because it subtracts the CO2 that cement absorbs [M].

Three facts make the politics difficult:

- High-income countries have 16% of the population [M] and 62% of the
  historic emissions [D]. Low-income countries emit 0.3 t per person
  [D] and have the largest damage.
- Inside each country the same is true. The richest 10% of people cause
  about 47% of emissions [S]
  [World Inequality Lab](https://prod.wid.world/www-site/uploads/2025/10/Climate_Inequality_Report_2025_Final.pdf).
- Future emissions depend mostly on China, India and other growing
  economies. China's CO2 has been flat or falling since March 2024 [S]
  [Carbon Brief](https://www.carbonbrief.org/analysis-chinas-quarterly-co2-falls-3-in-largest-drop-since-covid).
  If that continues, the world peak is here.

**Policy in 2026** (all [S]). The United States left the Paris
Agreement in January 2026 and removed the legal base for federal
greenhouse gas rules in February 2026
([Harvard tracker](https://eelp.law.harvard.edu/tracker/paris-climate-agreement)).
Its emissions rose 2.4% in 2025. Rhodium still projects a fall of 26 to
29% below 2005 by 2030, because the market continues to replace coal
([Rhodium](https://rhg.com/research/taking-stock-2026/)). China
promised its first absolute cut: 7 to 10% below the peak by 2035
([Carbon Brief](https://www.carbonbrief.org/qa-what-does-chinas-new-paris-agreement-pledge-mean-for-climate-action/)).
The EU agreed a 90% cut by 2040. COP30 in Belém asked for $1.3 trillion
per year of climate finance by 2035 but agreed no plan to leave fossil
fuels ([UN News](https://news.un.org/en/story/2025/11/1166433)). COP31
is in progress in Antalya until 20 November 2026 and has no result yet.
Governments still subsidise fossil fuels: about $7.4 trillion in 2024
if unpaid damage is counted, of which about 10% is direct subsidy
([IMF](https://www.imf.org/en/publications/wp/issues/2025/12/20/underpriced-and-overused-fossil-fuel-subsidies-data-2025-update-572729)).

## 7. What is working

**Electricity.** World electricity by source [D]:

| | 2010 | 2020 | 2024 | 2025 |
| --- | --- | --- | --- | --- |
| Coal | 39.8% | 35.3% | 34.1% | 33.0% |
| All fossil | 67.5% | 62.1% | 59.1% | 57.4% |
| Solar | 0.2% | 3.2% | 6.9% | 8.7% |
| Wind | 1.6% | 6.0% | 8.1% | 8.5% |
| All low-carbon | 32.5% | 37.9% | 40.9% | 42.6% |

In 2025, world generation grew 842 TWh. Low-carbon sources grew 883 TWh,
of which solar was 636 TWh. Fossil generation fell 41 TWh and coal fell
67 TWh [D]. Renewables (33.8%) passed coal (33.0%) for the first time
[D]. Solar output went from 327 TWh in 2016 to 2,779 TWh in 2025 [D]: it
doubled about every three years.

**Why: cost.** Battery packs cost $108 per kWh, 93% less than in 2010
[S] [BNEF](https://about.bnef.com/insights/clean-energy/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/).
New solar power costs $0.043 per kWh and onshore wind $0.034. In 2024,
91% of new renewable projects were cheaper than the cheapest new fossil
plant [S]
[IRENA](https://www.irena.org/Publications/2025/Jun/Renewable-Power-Generation-Costs-in-2024).
These costs do not include the storage and grid that a high share of
solar and wind needs.

**Scale.** In 2025 the world added about 650 GW of solar, 165 GW of
wind and 112 GW of batteries, all records [S]
([SolarPower Europe](https://www.solarpowereurope.org/press-releases/new-report-global-solar-market-hits-new-record-of-664-gw-installation-in-2025-as-global-solar-fleet-passes-3-tw),
[GWEC via Mercom](https://mercomindia.com/global-wind-energy-installations-hit-165-gw-in-2025-up-40-yoy),
[BNEF](https://about.bnef.com/insights/clean-energy/energy-storage-enters-the-100-gigawatt-era-three-things-to-know/)).
China built more than half of the solar and wind. Solar additions are expected to
fall about 8% in 2026, the first fall, because China changed its
pricing rules [S].

**Cars.** More than 20 million electric cars were sold in 2025, about
one new car in four: almost 55% in China, 27% in the EU and under 10%
in the US [S]
[IEA](https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars).
They replaced about 1.2 million barrels of oil per day, about 1% of
demand. The IEA expects oil and coal demand to peak at about 2030 [S].

**Money.** Clean energy investment is about $2.2 trillion per year,
about twice the fossil fuel investment [S]
[IEA](https://www.iea.org/reports/world-energy-investment-2026/regional-dashboards).
Very little of it goes to poor countries: Africa gets about 2% [S].

## 8. What is not working yet

- **Grids and permits.** In the US, about 2,060 GW of power plants and
  batteries wait for a grid connection [S]
  [LBNL](https://emp.lbl.gov/queued-2026-edition-characteristics-power-plants-seeking-transmission-interconnection-end-2025).
  The world must build or replace about 80 million km of lines by 2040
  [S] [IEA](https://www.iea.org/news/lack-of-ambition-and-attention-risks-making-electricity-grids-the-weak-link-in-clean-energy-transitions).
- **New demand.** Data centres used 415 TWh in 2024 and can use about
  945 TWh in 2030 [S]
  [IEA](https://www.iea.org/reports/energy-and-ai/executive-summary).
  That is about 10% of world demand growth, but almost half of the
  growth in the US, where it kept coal plants in use in 2025.
- **Methane.** More than 150 countries promised a 30% cut by 2030.
  Current policies give about 8% [S]
  [CCAC](https://www.ccacoalition.org/content/global-methane-status-report-2025).
  Methane from the energy sector is still near its record [S]
  [IEA](https://iea.org/reports/global-methane-tracker-2026).
- **Forests.** Tropical primary forest loss was 4.3 million hectares in
  2025. That is 36% less than the record of 2024 and 46% more than ten
  years ago [S]
  [WRI](https://www.wri.org/news/release-tropical-rainforest-loss-drops-36-2025-fires-threaten-global-progress).
- **Steel, cement, chemicals.** Clean steel with hydrogen is delayed:
  ArcelorMittal cancelled its German plants, and the Swedish plant
  Stegra needed a rescue [S]
  [Eurometal](https://eurometal.net/arcelormittal-cancels-dri-eaf-decarbonisation-investment-in-germany/).
  Green hydrogen costs $3.7 to $11.7 per kg, against $1 to $2.5 for
  hydrogen from gas [S]. One cement plant in the world (Brevik, Norway)
  captures its CO2 at full scale [S]
  [Heidelberg Materials](https://www.heidelbergmaterials.com/en/pr-2025-06-18).
- **Aviation and shipping.** Sustainable aviation fuel was 0.6% of jet
  fuel in 2025 [S]
  [IATA](https://www.iata.org/en/pressroom/2025-releases/2025-12-09-04/).
  The shipping carbon price at the IMO was postponed in October 2025
  [S].
- **Food.** No country has a serious policy to reduce beef and dairy
  emissions. Feed additives cut cattle methane by about 30% in barns
  [S], but most cattle graze. Investment in alternative proteins fell
  for four years [S].
- **Carbon removal.** Trees and soils remove about 2 Gt of CO2 per
  year. All engineered methods together remove about 1.3 million tonnes
  per year, less than 0.1% of that [S]
  [State of CDR](https://ox.ac.uk/news/2024-06-05-new-report-states-7-9-billion-tonnes-co2-must-be-sustainably-removed-year-hit).
  Paths that keep warming below 2 °C need 7 to 9 Gt per year by 2050.
  The largest direct air capture plant removed 675 t in half a year,
  against a design of 36,000 t per year [S]. Offsets are worse: a
  review of 2,346 projects found that less than 16% of credits were
  real reductions [S]
  [Max Planck Society](https://www.mpg.de/23737687/climate-impact-of-carbon-crediting-projects-substantially-overestimated).
- **Firm clean power.** Nuclear is steady at about 9% of electricity
  [D]; 63 reactors are in construction, half of them in China [S].
  Enhanced geothermal produced its first commercial power in September
  2026 (Fervo, Utah) [S]. Fusion has not produced net electricity and
  cannot help before about 2040 [M].

## 9. What can be done: the levers in order

The IPCC found that actions that cost less than $100 per tonne can cut
emissions in 2030 to half of the 2019 level, and that more than half of
that potential costs less than $20 per tonne [S]
[IPCC AR6 WG3, figure SPM.7](https://www.ipcc.ch/report/ar6/wg3/figures/summary-for-policymakers/figure-spm-7/).
The damage per tonne is about $185. So most of the necessary action is
cheaper than the damage it prevents. The problem is not the total cost.
The problems are who pays, who loses income, and how fast things can be
built.

This is my order of the levers. It uses three tests: the size of the
cut by 2040, the cost, and whether the technology is ready. The shares
are approximate and come from the sector numbers in section 6.

| Lever | Share of emissions it addresses | State | What blocks it |
| --- | --- | --- | --- |
| 1. Clean electricity: solar, wind, storage, grids, plus nuclear and geothermal where they fit | about 28%, and more as other sectors move to electricity | Cheapest option now; grows faster than demand | Grid connections, permits, cost of capital in poor countries, coal plants that are still young in Asia |
| 2. Electrify cars, heating and low-temperature industry | about 25% | Cars are on course; heat pumps are stalled (sales -2% in 2025) | Purchase cost, electricity that is taxed more than gas, charging, landlords |
| 3. Cut methane from oil, gas, coal and waste | about 8% of emissions, and up to 0.2 °C less warming by 2050 | Mostly cheap, technology ready, not done | No price on leaks; weak enforcement; satellite data not used |
| 4. Stop deforestation | about 8% | Works when a government wants it (Brazil -42% in 2025) | Farm profits, weak land rights, fire in a hotter climate |
| 5. Efficiency: buildings, motors, less waste | cuts demand in all sectors | Cheap, slow | Many small decisions; split incentives |
| 6. Food: less beef and dairy, less waste, better fertiliser use | about 12 to 30% | Almost no policy | Culture and farm politics |
| 7. Clean heavy industry, aviation and shipping | about 20% | Pilot stage; projects delayed | Costs 20 to 100% more with no carbon price; needs standards and public purchase |
| 8. Carbon removal | needed for the last 10% and for a return below a peak | Trees work now; engineered removal is 1,000 times too small | $500 or more per tonne; honest accounting |

Policies that make these levers work:

- **A price or a rule on carbon.** Either works. The EU border tax
  (from 2026) pushes its carbon price onto its trade partners.
- **Cheaper finance for poor countries.** A solar plant in Africa pays
  about two to three times the interest rate of one in Europe [M]. This
  is the main reason why only 2% of clean investment goes there.
- **Faster permits and more grid.** This is the main bottleneck in rich
  countries.
- **Public purchase of clean steel, cement and fuels**, to create the
  first market.
- **An end to fossil fuel subsidies**, with direct payments to poor
  households in their place.

## 10. Adaptation and sun-reflection methods

**Adaptation is necessary at every level of warming.** It works: in
Bangladesh, deaths from cyclones fell more than 100 times after 1970,
with warnings, shelters and volunteers [S]
[Dialogue Earth](https://dialogue.earth/en/climate/how-bangladesh-is-beating-the-odds-on-climate-disaster-deaths/).
The heat plan of Ahmedabad prevents about 1,190 deaths per year [S]
[Hess et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6236972).
Countries with complete early warning systems have about 6 times fewer
disaster deaths, and 40% of countries have no such system [S]
[WMO](https://wmo.int/news/media-centre/early-warning-systems-reach-new-heights-critical-gaps-jeopardize-global-progress).
Poor countries need $310 to $365 billion per year by 2035 and receive
$26 billion [S]
[UNEP](https://www.unep.org/en/publications/report/adaptation-gap-report-2025).
Adaptation has limits: it cannot keep coral reefs or low islands.

**Sun-reflection methods (solar geoengineering).** Particles in the
stratosphere can cool the planet within a year, for a few billion
dollars per year [S] [Smith and Wagner](https://gwagner.com/?p=4417).
They do not remove CO2, do not stop ocean acidification, and change
rainfall. If the injection stops suddenly, the hidden warming returns
in a few years. No international rule exists. The UK funds research
(£56.8 million) and a private company raised $60 million, while about
60 countries want an agreement not to use it [S]
[Climate Home](https://www.climatechangenews.com/2026/05/08/eu-warns-on-solar-geoengineering-but-research-debate-grinds-on/).
My judgement: with a peak near or above 2 °C now likely, some state
will consider this method in the 2030s or 2040s. Public research and
rules made before that time are safer than no research. The method
must not replace emission cuts, because it must then continue for
centuries.

## 11. What one person can do

The average person in the world emits 4.7 t of CO2 per year; in the US
14.5 t, in Japan 7.8 t, in the EU 5.4 t [D]. A lifestyle on a 1.5 °C
path is about 2.5 t CO2e by 2030 [S]
[Hot or Cool Institute](https://hotorcool.org/1-5-degree-lifestyles/).

**Personal emissions, largest first** (tonnes CO2e saved per year; [S]
[Ivanova et al. 2020](https://eprints.whiterose.ac.uk/159418) and
[Wynes and Nicholas 2017](https://www.thelocal.com/20170712/want-to-save-the-planet-have-fewer-children-researchers-in-lund-sweden-say)):

| Action | Saving |
| --- | --- |
| Live without a car | 2.0 to 2.4 |
| One long-haul return flight less | 1.6 to 3 |
| Electric car in place of a petrol car | 1.2 to 2.0 |
| Renewable electricity at home | about 1.6 |
| Heat pump in place of a gas or oil boiler | 1 to 1.7 |
| Vegan diet (most of the gain comes from no beef) | 0.8 to 0.9 |
| Home insulation | about 0.9 |
| Less food waste | about 0.3 |
| Recycling | about 0.2 [M] |

A return flight from the US west coast to Tokyo is about 1.6 t of CO2
per economy seat, and about 3 t CO2e with the effect of contrails. This
number is an estimate from the workers' notes [S]. For a person who
flies long-haul a few times a year, flights are the largest item.

**Actions that are larger than the personal footprint:**

- **Vote, and say so.** 89% of people in 125 countries want more
  political action on climate, and most of them think they are in a
  minority [S]
  [Andre et al. 2024](https://www.nature.com/articles/s41558-024-01925-3.pdf).
  Policy caused the 1 °C improvement in section 4. Local decisions on
  housing, power lines and solar or wind farms are also climate votes.
- **Give money to groups that change policy or technology.** Giving
  Green recommends, among others, Clean Air Task Force, Future Cleantech
  Architects, Good Food Institute, Opportunity Green and Project
  InnerSpace [S]
  [Giving Green](https://www.givinggreen.earth/post/2025-2026-top-climate-nonprofits).
  Estimates near $1 per tonne are very uncertain. If the true cost is
  even 20 times higher, $1,000 per year does more than most changes in
  the table. Do not buy cheap offsets (section 8).
- **Use your work.** An engineer, a buyer or a manager often controls
  more emissions at work than at home.
- **Buy the clean option early and be seen.** One more solar roof in a
  postal area increases the chance of the next one [S]
  [Bollinger and Gillingham 2012](https://econpapers.repec.org/RePEc:inm:ormksc:v:31:y:2012:i:6:p:900-912).
  The same is found for electric cars.
- **Pensions and banks.** The evidence that divestment changes the
  cost of capital of fossil companies is weak. Its effect is mostly
  political [S].

The phrase "carbon footprint" was made popular by a BP advertising
campaign in 2004 [S]
[Grist](https://grist.org/energy/footprint-fantasy/). That does not
make personal action useless. It means that personal action is one of
four tools, and for most people not the strongest one.

## 12. Note for a Hokkaido skier

This report started after the Hokkaido ski forecast. In short: cold
inland Hokkaido is among the last places in Japan to lose its snow.

- Snow loss speeds up where the mean winter temperature is above about
  -8 °C [S]
  [Gottlieb and Mankin 2024](https://www.sciencedaily.com/releases/2024/01/240110120210.htm).
- At 2 °C of global warming, the maximum snow depth in Japan falls
  about 30%, except in Hokkaido and some other areas. At 4 °C it falls
  about 70%, except in parts of Hokkaido [S]
  [JMA 2020](https://www.data.jma.go.jp/cpdinfo/ccj/2020/pdf/cc2020_gaiyo_en.pdf).
- Heavy snowfalls in western and central Hokkaido can become larger,
  because a warmer Sea of Japan gives more moisture [S].
- Of 349 Japanese ski areas, 53 stay fully open on natural snow at
  +2 °C and 7 at +4 °C [S]
  [Yoshizawa and Katsuyama](https://www.jstage.jst.go.jp/article/seppyo/88/4/88_295/_article/-char/en).

So the difference between the current path (about 2.7 °C) and a 2 °C
path is, for Japanese skiing, the difference between Hokkaido and high
Nagano only, and most of the country.

## 13. My judgement

- **Good news that is firm:** clean electricity and electric cars now
  win on cost, and they grow on an S-curve. Projections made from
  current policies have been too pessimistic about them every year.
  The world emission peak is probably within two years of now.
- **Bad news that is firm:** a peak is not a fall. Warming continues
  until net CO2 emissions are zero. On the current path that is after
  2070, at about 2.5 to 2.8 °C. The 1.5 °C limit will be passed in
  about 2030.
- **Largest uncertainty in the science:** clouds and sensitivity
  (section 3). If Hansen is right, add about 0.5 °C to every number.
- **Largest uncertainty in the response:** politics. The US reversal
  costs about 0.1 °C. China's decisions on coal count for more than
  those of all other countries.
- **Best value now:** methane, forests, grids and finance for poor
  countries. All four are cheap compared with their effect, and all
  four are blocked by institutions, not by technology.
- **A realistic good result** is a peak below 2 °C, at about 1.7 to
  1.9 °C, and then a slow fall with carbon removal. This needs world
  emissions to fall by about half by 2040. It is difficult and it is
  still possible.

## What could not be verified

- **All [S] facts.** The cloud container could not open the pages. A
  later pass from a home machine can open each link and change [S] to
  [V], as the Hokkaido report did.
- **Events of 2026**: the Global Carbon Budget 2026, the UNEP Emissions
  Gap Report 2026, the oil crisis and COP31 come from search text only.
  The El Niño and the 2026 temperatures are now confirmed by the NOAA
  and ERA5 files [D].
- **The ERA5 baseline.** The file gives anomalies against 1991-2020.
  This report adds 0.88 °C for 1850-1900. That offset reproduces the
  annual values that Copernicus publishes (1.60 °C for 2024, 1.47 °C for
  2025), but the offset itself was not read on a Copernicus page.
- **UNEP 2026 gives 2.6 °C for full pledges; UNEP 2025 gave 2.3 to
  2.5 °C.** The definitions can differ. Not resolved.
- **Chance that 2026 is the warmest year**: Copernicus says second
  warmest is likely; Carbon Brief says 67% for a record. The ERA5 file
  to 9 November supports Copernicus. Other datasets can differ.
- **Sector shares** for steel, cement, aviation and shipping, the
  methane lifetime, the cost of capital in poor countries, the IPCC sea
  level range for 2100 and the fusion date are from memory [M].
- **The flight estimate** (west coast to Tokyo) has no authoritative
  source.
- **AMOC collapse odds** are quoted in the press with no clear source,
  so this report gives none.
- **Energy imbalance for 2021-2025**: the IGCC file gives the full
  heat inventory only to 2020. The later values here are ocean only.

## Data and how to redo it

```
python -X utf8 climate/data/fetch.py    # downloads; see data/README.md
python -X utf8 climate/analyze.py       # writes climate/analysis.json
```

`data/manifest.csv` lists each file with its URL, the date it was read,
its size and its SHA-256. `data/README.md` describes each file and its
licence.

| Data | Source | Used for |
| --- | --- | --- |
| `data/igcc/` | Indicators of Global Climate Change, data repository at commit `d972657` (CC BY 4.0), https://github.com/ClimateIndicator/data | Temperature, human-caused warming, gases, forcing, heat, sea level, carbon budget, emissions by gas |
| `data/owid/co2-extract.csv` | Our World in Data CO2 dataset (from the Global Carbon Budget), https://github.com/owid/co2-data | Emissions by country |
| `data/owid/energy-extract.csv` | Our World in Data energy dataset (from Ember and the Energy Institute), https://github.com/owid/energy-data | Electricity mix |
| `data/primary/` | Berkeley Earth, NOAA GML, NASA GISTEMP, Met Office HadCRUT5, NOAA NCEI, ECMWF Climate Pulse (ERA5), NSIDC, NOAA CPC, NOAA STAR and JMA, as downloaded on 2026-11-12 from a home machine | Agency values for temperature, gases, El Niño, sea ice and sea level (`cross_checks` in `analysis.json`) |

## Sources

The main reports, with the label that applies to this report's use of
them. The full list, with one line per fact, is in `research/`.

- Forster et al., Indicators of Global Climate Change 2025, ESSD 18,
  3889 (2026): https://essd.copernicus.org/articles/18/3889/2026/ (data
  [D], text [S])
- IPCC AR6: https://www.ipcc.ch/assessment-report/ar6/ [S]
- Copernicus Climate Change Service: https://climate.copernicus.eu/ [S]
- WMO State of the Global Climate 2025: https://wmo.int/node/38410 [S]
- Global Carbon Budget: https://globalcarbonbudget.org/ [S]; data
  through Our World in Data [D]
- UNEP Emissions Gap Report 2026:
  https://unep.org/en/publications/report/emissions-gap-report-2026 [S]
- Climate Action Tracker: https://climateactiontracker.org/ [S]
- Ember Global Electricity Review 2026:
  https://ember-energy.org/latest-insights/global-electricity-review-2026/
  [S]; data through Our World in Data [D]
- IEA World Energy Outlook 2025, Global EV Outlook 2026, World Energy
  Investment 2026, Global Methane Tracker 2026: https://www.iea.org/ [S]
- IRENA Renewable Power Generation Costs in 2024:
  https://www.irena.org/Publications/2025/Jun/Renewable-Power-Generation-Costs-in-2024 [S]
- Global Tipping Points Report 2025: https://global-tipping-points.org/ [S]
- Lancet Countdown 2025: https://lancetcountdown.org/2025-report/ [S]
- UNEP Adaptation Gap Report 2025:
  https://www.unep.org/en/publications/report/adaptation-gap-report-2025 [S]
- Carbon Brief analyses (China, India, state of the climate):
  https://www.carbonbrief.org/ [S]
- Hansen et al. 2025, doi 10.1080/00139157.2025.2434494 [S]
- Ivanova et al. 2020, Environ. Res. Lett. 15 093001;
  Wynes and Nicholas 2017, Environ. Res. Lett. 12 074024 [S]
- Probst et al. 2024, Nature Communications 15:9562 [S]
- Andre et al. 2024, Nature Climate Change 14:253 [S]
- JMA, Climate Change in Japan 2020 and 2025:
  https://www.data.jma.go.jp/cpdinfo/ccj/ [S]
