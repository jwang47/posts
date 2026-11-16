# Carbon removal: trees, rocks and machines

Written 2026-11-12 by Claude, with two research workers. This is a
second part of the [climate analysis](README.md). That report is about
how to stop emissions. This one asks a different question: can we take
CO2 out of the air again, with trees or with technology, and how much
does that help?

## Answer

1. **Removal is necessary, but it is the small part of the solution.**
   Paths that keep warming well below 2 °C cut emissions by about 80 to
   90% and remove the rest. They need about 7 to 9 Gt of CO2 removal
   per year by 2050 [S]. The world emits about 43 Gt of CO2 per year
   [D]. Removal cannot replace the cuts.
2. **Almost all removal today is trees.** People remove about 2.2 Gt
   per year, and more than 99.9% of that is forest [S]. All the
   technical methods together remove about 2 million tonnes per year
   [C]. That is 0.005% of emissions.
3. **Each 0.1 °C costs about 180 to 220 Gt.** That is four to five
   years of the present CO2 emissions [C]. To lower the temperature by
   0.1 °C in 50 years, the world must remove about 4 Gt per year more
   than it emits [C]. So removal can shave a peak. It cannot bring
   back the old climate.
4. **Trees are cheap and ready, but they need much land and they are
   not permanent.** One Gt per year needs about 90 million hectares of
   new tropical forest, or about 200 million hectares in the temperate
   zone [C]. A realistic share for new forest is about 1 to 4 Gt per
   year [S]. Fire, drought and logging can release the carbon again.
   To protect the forests that exist gives more than to plant new
   ones.
5. **Machines are permanent, but they are tiny, expensive and they
   need much energy.** Direct air capture costs about $670 per tonne
   now [S]. One Gt per year needs about 2,000 TWh, which is 6% of the
   world's electricity [C]. The largest plant in operation removed
   675 tonnes in half a year [S]. That is half a second of world
   emissions [C].
6. **The technical methods must grow about 450 to 750 times by 2050.**
   That is about 29 to 32% per year for 24 years [C]; the range comes
   from the 2026 and 2024 counts of today's removal. Solar power grew 27% per year in
   the last ten years [D]. It is possible, but solar sells a product.
   Removal sells a waste service that nobody must buy.
7. **The largest risk is not the technology. It is the excuse.** A
   promise of future removal makes it easier to delay cuts today. A
   tonne that is not emitted costs less than $100 for most sources. A
   tonne removed by machine costs $200 to $700. The correct order is:
   cut emissions, protect the forests and the sinks, then use removal
   for the last 10 to 20%.

## Source labels

The labels are the same as in the [main report](README.md):

- **[D]** computed from a raw data file in `data/`.
- **[C]** computed by `removal.py` from numbers that the text cites.
  The result is in `removal.json`. It is only as good as its inputs.
- **[S]** from search-result text. The page could not be opened from
  the cloud container. Treat the number as provisional.
- **[M]** from model memory, not checked.

No web page could be opened for this part. All facts from papers and
news are [S] or [M]. The full notes, with all links, are in
[research/research-removal-nature.md](research/research-removal-nature.md)
and
[research/research-removal-engineered.md](research/research-removal-engineered.md).

## 1. Why removal, when we can stop emissions?

There are three reasons.

- **Some emissions are very hard to stop.** Examples are methane and
  nitrous oxide from farms, CO2 from the chemistry of cement, and long
  flights. National plans expect that about 18% of today's emissions
  remain in 2050 [S]
  [Buck et al. 2023](https://eprints.lancs.ac.uk/id/eprint/184736).
  "Net zero" means that removal balances this rest.
- **The CO2 stays.** When emissions stop, warming stops, but the
  temperature does not go down again for centuries [M]. Only removal
  lowers it.
- **The world will pass 1.5 °C.** UNEP says that an overshoot is now
  almost certain, and that removal must take out about five years of
  current CO2 emissions for each 0.1 °C that the world wants to come
  back [S]
  [UNEP Emissions Gap Report 2025](https://www.unep.org/en/publications/report/emissions-gap-report-2025).

My own numbers agree with UNEP. The carbon budget table in the data
gives 183 Gt of CO2 for each 0.1 °C between 1.5 and 1.7 °C [D]. The
IPCC relation between CO2 and temperature (0.45 °C per 1,000 Gt) gives
222 Gt, with a range of 159 to 370 Gt [C]. The world emits 43.4 Gt of
CO2 per year (fossil 39.0, land use 4.35) [D]. So 0.1 °C is 4.2 to 5.1
years of emissions [C].

This also works in the other direction. Each year of emissions at the
present rate adds about 0.02 °C [C], and it needs 43 Gt of later
removal to undo.

## 2. What nature does without us

The ocean and the land already take up about half of the CO2 that
people emit.

| Sink, 2024 | Gt CO2 per year | Share of emissions, 2015-2024 |
| --- | --- | --- |
| Ocean | 12.5 | 29% |
| Land (plants and soils) | 7.0 | 21% |

Source: [Global Carbon Budget 2025](https://essd.copernicus.org/articles/18/3211/2026/)
[S]; the conversion from carbon to CO2 is [C].

Three facts about these sinks are important.

- **They are not "removal".** They happen without our action, because
  there is more CO2 in the air. The carbon budgets and the temperature
  numbers already include them. If a country counts this natural
  uptake against its fossil emissions, the sum says "net zero" but the
  warming continues [S]
  [Allen et al. 2024](https://www.inet.ox.ac.uk/publications/geological-net-zero-and-the-need-for-disaggregated-accounting-for-carbon-sinks).
  National inventories already do this: they report 6.7 Gt per year
  more land uptake than the science models [S]
  [Grassi et al. 2023](https://pure.iiasa.ac.at/id/eprint/18687/).
- **The land sink becomes weaker.** Climate change has made the land
  sink 25% smaller and the ocean sink 7% smaller than they would be
  [S]
  [Global Carbon Project](https://cger.nies.go.jp/gcp/news/20251113.html).
  In the hot year 2023, the land took up about 1.6 Gt, the least since
  2003 [S]
  [Ke et al. 2024](https://futureearth.org/droughts-fires-dramatically-weakened-land-carbon-sinks-last-year-new-paper-reports/).
  The fires in Canada in 2023 emitted about 2.4 Gt [S]
  [Byrne et al. 2024](https://phys.org/news/2024-08-nasa-tallies-carbon-emissions-massive.html).
  The south-east Amazon is now a source [S]. The forests of Finland
  have been a source since 2021 [S]
  [Statistics Finland](https://stat.fi/en/publication/cm1942l1d9jk606uk6ltkwntx).
- **To keep them is the first task.** A sink of 19 Gt per year is nine
  times all deliberate removal [C]. A loss of 10% of it cancels all
  the tree planting in the world.

## 3. The size of the job

| | Gt CO2 per year | Label |
| --- | --- | --- |
| CO2 emissions now | 43.4 | [D] |
| Deliberate removal now | 2.2 | [S] |
| of this, technical methods | 0.002 | [C] |
| Removal needed in 2050 | 7 to 9 (latest report: 8.75) | [S] |
| Removal in the national plans for 2050 | about 3.6 | [S] |
| Technical methods needed in 2050 | more than 1 | [S] |

Sources:
[State of Carbon Dioxide Removal, 3rd edition, June 2026](https://www.stateofcdr.org/asset/The-State-of-CDR-Executive-summary_June-2026.pdf)
and [Carbon Brief](https://www.carbonbrief.org/qa-the-current-state-of-carbon-dioxide-removal-around-the-world/).

Total removal must become four times larger [C]. The technical methods
must become about 450 times larger, which is 29% growth per year until
2050 [C]. With the 2024 count of today's removal (1.3 Mt), it is 770
times and 32% per year [C]. The report says novel removal already grows
about 40% per year [S], but from a very small base. For comparison, solar electricity grew 26.9% per year from
2015 to 2025 [D]. The report itself says that removal "might need to
scale faster than solar" [S].

In the IPCC scenarios, the removal in 2050 comes from three places:
forests and soils 3.0 Gt, bioenergy with capture 2.75 Gt, and direct
air capture 0.02 Gt (medians) [S]
[IPCC AR6 WG3, chapter 12](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-12/).
The models choose bioenergy because it was the cheapest method in
their cost tables, not because it is easy.

Even the full 8.75 Gt per year does not cool the planet much. If the
world removed that much for 50 years, and emitted nothing, the
temperature would fall by about 0.2 °C [C]. In the scenarios, most of
that removal only balances the emissions that remain.

## 4. Trees

### How much they can do

The estimates fall when the method becomes more careful.

| Study | Result | Note |
| --- | --- | --- |
| [Bastin et al. 2019](https://www.pubmed.gov/31624179/) | 205 Gt of carbon (750 Gt CO2) on 0.9 billion ha | Disputed. Critics found it about five times too large; the authors published a correction [S] |
| [Mo et al. 2023](https://pure.iiasa.ac.at/19186) | 226 Gt of carbon (828 Gt CO2), range 151-363 | 61% is in forests that exist, if we let them grow old. New forest is 87 Gt of carbon [S] |
| [Cook-Patton et al. 2020](https://www.wri.org/insights/young-forests-capture-carbon-quicker-previously-thought) | 8.9 Gt CO2 per year to 2050 on 678 million ha | The technical maximum for natural regrowth [S] |
| [Griscom et al. 2017](https://pubmed.ncbi.nlm.nih.gov/29078344/) | 11.3 Gt CO2e per year below $100 per tonne | All "natural climate solutions"; much of it is avoided emissions, not removal [S] |
| [IPCC AR6 WG3, chapter 7](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-7/) | 3.9 Gt per year technical (0.5-10.1); 1.2 to 1.6 Gt below $100 | New forest only [S] |
| [Busch et al. 2024](https://www.conservation.org/research/cost-effectiveness-of-natural-forest-regeneration-and-plantations-for-climate-mitigation) | 31 Gt in 30 years below $50 per tonne | About 1 Gt per year, in poor and middle-income countries [S] |

A fair summary: new forest can remove about 1 to 4 Gt per year for some
decades, at $10 to $50 per tonne. That is real and useful. It is 2 to
9% of present CO2 emissions.

The upper limit is also useful. If the complete Mo et al. potential
were reached, it would be 828 Gt, or 19 years of present emissions, and
it would lower the temperature by at most 0.37 °C [C]. The new-forest
part is 0.14 °C [C]. This takes 50 to 100 years, and it happens only
once: a grown forest takes up no more.

### Land and time

- A young tropical forest takes up about 11 tonnes of CO2 per hectare
  per year in the first 20 years, and needs a median of 66 years to
  reach 90% of the biomass of an old forest [S]
  [Poorter et al. 2016](https://www.sciencedaily.com/releases/2016/02/160208135436.htm).
- So 1 Gt per year needs about 90 million hectares in the wet tropics
  [C]. With a temperate rate of 5 tonnes it is 200 million hectares,
  and with a boreal rate of 2 tonnes it is 500 million [C], but these
  two rates are from memory [M].
- The 3.0 Gt per year in the IPCC median needs about 265 million
  hectares of tropical land [C]. India is 329 million hectares [M].
  The Cook-Patton maximum needs 678 million hectares, which is two
  times India or 45% of the world's cropland [C].

### What goes wrong

- **The carbon can come back.** California keeps a reserve of offset
  credits against fire for 100 years. Fires used at least 95% of it in
  less than ten years [S]
  [Badgley et al. 2022](https://frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2022.930426/full).
  Fossil CO2 stays in the air for thousands of years. A forest must
  stand that long to balance it.
- **Planted trees die.** At 176 sites in tropical Asia, 44% of the
  young trees were dead after five years [S]
  [Banin et al.](https://www.abdn.ac.uk/news/16531/). A study of 430
  plantations in north India found no increase in tree cover after
  decades [S]
  [Coleman et al. 2021](https://ideas.repec.org/a/nat/natsus/v4y2021i11d10.1038_s41893-021-00761-z.html).
- **Plantations are not forests.** About 45% of the national pledges
  are commercial plantations, which are cut every ten years or so.
  Natural forest stores about 40 times more carbon in the long term
  [S]
  [Lewis et al. 2019](https://pubmed.ncbi.nlm.nih.gov/30940972).
- **Dark trees warm.** Forest is darker than snow, grass or desert and
  absorbs more sunlight. A count of carbon alone can be up to 81% too
  high. The effect is largest in the north and in dry land [S]
  [Hasler et al. 2024](https://doaj.org/article/d9b93922234d4b66abdd0736ce8541e6).
  So the tropics are the correct place for new forest.
- **Land is in use.** New forest competes with food, and trees on
  natural grassland damage it.

### Protect first

A hectare of old tropical forest that is cut releases in a few years
what a new hectare needs about 66 years to take up again. Regrowth in
the humid tropics balances only 26% of the emissions from forest loss
there [S]
[Heinrich et al. 2023](https://www.carbonbrief.org/regrowth-of-degraded-tropical-forests-offsets-a-quarter-of-deforestation-emissions/).
The world still loses 4.3 million hectares of primary tropical forest
per year (main report, section 8). To stop that loss is faster, cheaper
and more certain than to plant.

## 5. Soil, biochar, coasts and the open ocean

| Method | Potential, Gt CO2 per year | Cost per tonne | How long it stays | State |
| --- | --- | --- | --- | --- |
| Soil carbon on farms | up to about 5 in theory; much less in practice | low | Years to decades; lost if the practice stops | Long field trials show that large gains need extreme measures [S] [Poulton et al. 2018](https://repository.rothamsted.ac.uk/item/84663) |
| Biochar | 0.3 to 6.6 | $125 to $165 on the market | Centuries | 80% of all durable removal delivered until now [S] |
| Mangroves, salt marsh, seagrass | 0.03 to 0.84 | not found | Centuries if not disturbed | Small; good for coasts and fish also [S] |
| Peat: make drained peat wet again | stops about 2 of emissions | low | - | This avoids emissions; it is not removal [S] |
| Ocean iron, sunk seaweed | not known | not known | Not shown | Running Tide closed in 2024; sunk kelp decays fast [S] |

Biochar is charcoal from plant waste that is put into soil. It is the
one method between the trees and the machines that delivers real
tonnes now, because it is simple and it can be measured. Its limit is
the supply of waste biomass.

Sources: biochar potential
[IPCC AR6 WG3 chapter 12](https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-12/),
deliveries
[CDR.fyi](https://www.cdr.fyi/blog/durable-cdr-market-update-carbon-unbound-east-coast-2026),
coasts
[Macreadie et al. 2021](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D875C9D7C90D0A5D8ED96F62D1180520/S275472052400009Xa.pdf/restoring-blue-carbon-ecosystems.pdf),
peat
[Ramsar](https://www.ramsar.org/sites/default/files/documents/library/rpb5_restoring_drained_peatlands_e.pdf),
kelp
[Bauer et al. 2026](https://carbondioxide-removal.eu/2026/03/20/bauer-et-al-2026-in-situ-deep-ocean-monitoring-reveals-rapid-kelp-degradation-limits-marine-biomass-based-carbon-sequestration-potential-and-alters-benthic-ecosystems/).

## 6. Machines: direct air capture

A direct air capture (DAC) plant moves air across a chemical that binds
CO2. Heat then releases the CO2, and a pump puts it deep into rock.

### The physics

CO2 is 0.04% of air. To separate it needs energy, and physics sets a
minimum of about 0.12 MWh per tonne [S]. Real plants need about 1.5 to
2.5 MWh per tonne, which is 12 to 20 times the minimum [C]
[Keith et al. 2018](https://www.belfercenter.org/publication/process-capturing-co2-atmosphere).
There is room to improve, but not to zero.

| For 1 Gt per year | Value | Label |
| --- | --- | --- |
| Energy at 2 MWh per tonne | 2,000 TWh | [C] |
| Share of world electricity (31,772 TWh in 2025) | 6.3% (range 4.7 to 7.9%) | [C] from [D] |
| Compared with all solar power in 2025 (2,779 TWh) | 72% | [C] from [D] |
| Range of the Belfer Center | 1,400 to 4,200 TWh | [S] [Belfer](https://www.belfercenter.org/publication/prospects-direct-air-carbon-capture-and-storage-costs-scale-and-funding) |
| Plants of the size of Stratos (0.5 Mt per year) | 2,000 | [C] |
| Plants of the size of Mammoth (36,000 t per year) | about 28,000 | [C] |

If machines did all of the 8.75 Gt, they would need 17,500 TWh, which
is 55% of the electricity that the world makes today [C].

**Clean power is better used on the grid first.** Two MWh of clean
electricity remove 1 tonne with DAC. The same two MWh avoid 1.9 tonnes
if they replace coal power [C, with a coal value from memory], and
0.9 tonnes if they replace average grid power (458 g per kWh [D]). DAC
makes sense only where the grid is already clean or where the power
cannot be used for something else. Iceland is such a place.

### The state today

- **Mammoth** (Climeworks, Iceland, 2024) is the largest plant in
  operation. Its design is 36,000 tonnes per year. Its net removal was
  119 tonnes in the first half of 2025 and 675 tonnes in the first half
  of 2026 [S]
  [Net Zero Compare](https://netzerocompare.com/articles/climeworks-increases-co2-removal-at-mammoth-as-operating-costs-fall).
  That is 4% of the design [C]. The world emits 1,374 tonnes of CO2
  per second [C].
- **Stratos** (Occidental, Texas) has a design of 500,000 tonnes per
  year. Its start moved from 2025 to the end of 2026. I found no report
  that it has captured CO2 [S]
  [E&E News](https://www.eenews.net/articles/worlds-largest-carbon-removal-plant-to-open-at-the-end-of-2026/).
  Its owner is an oil company, and US law now pays the same $180 per
  tonne when the CO2 is used to push more oil out of old fields [S]
  [Global CCS Institute](https://www.globalccsinstitute.com/u-s-preserves-and-increases-45q-credit-in-one-big-beautiful-bill-act/).
  That use is not removal.
- **All plants in the world** capture about 0.01 Mt per year. The
  planned projects give about 3 Mt in 2030, and the IEA net zero path
  needs about 75 Mt [S]
  [IEA](https://www.iea.org/reports/direct-air-capture). This number
  is from about 2023.

### The cost

| | $ per tonne | Label |
| --- | --- | --- |
| Supplier break-even, 2025 | 670 | [S] [CDR.fyi and OPIS](https://www.cdr.fyi/blog/cdr-pricing-survey-may-2026) |
| Climeworks target for 2030 | 400 to 600 | [S] |
| Independent estimate at 1 Gt per year | 340 (226 to 835) | [S] [Sievert et al. 2024](https://sciencedaily.com/releases/2024/03/240304135808.htm) |
| US government target | below 100 | [S] [DOE](https://www.energy.gov/fecm/carbon-negative-shot) |
| Most emission cuts | below 100, half of them below 20 | [S] main report, section 9 |

Will DAC follow the cost curve of solar? I think only partly. Solar
panels are small, identical and made in factories by the billion. A
DAC plant is partly like that (the capture boxes) and partly a chemical
plant with large fans, heat and pipes, and chemical plants become
cheaper slowly. The energy cost also has a floor. The independent
estimate of about $340 at very large scale looks more credible to me
than $100.

## 7. Other technical methods, and the storage

| Method | How it works | Potential, Gt per year | Cost per tonne now | State |
| --- | --- | --- | --- | --- |
| Bioenergy with capture (BECCS) | Burn or ferment plants, capture the CO2, store it in rock | 0.5 to 5 with limits for land | about 230 | Two US ethanol plants have a capacity of about 1.8 Mt per year. Stockholm builds 0.8 Mt per year for 2028. Drax in the UK left its project in 2026 [S] |
| Enhanced rock weathering | Spread crushed basalt on fields; it binds CO2 as it dissolves | 0.5 to 2 | 270 to 350 | Thousands of tonnes verified. Hard to measure in the field; some trials found nothing [S] |
| Ocean alkalinity | Add alkaline minerals to seawater, which then takes up more CO2 | not known; large in theory | about 270 | First 626 verified tonnes in 2025. A trial in Cornwall was stopped after protests [S] |
| Storage in rock | Pump CO2 into deep saline rock or basalt | prudent total 1,460 Gt | 10 to 30 [M] | Works. In Iceland more than 95% became stone in two years [S] |

BECCS has the same land problem as trees, and a larger one. The 1.5 °C
scenarios used 93 to 724 million hectares of energy crops [S]
[Chatham House](https://www.chathamhouse.org/2023/11/emerging-global-crisis-land-use/03-land-and-climate-pressures).
It makes most sense with waste: ethanol plants, paper mills, and the
burning of household waste.

Storage is not the limit in this century, but it is not without limit.
A study in 2025 put the prudent world capacity at 1,460 Gt, after it
excluded places with earthquake risk, groundwater or many people [S]
[Gidden et al. 2025](https://www.carbonbrief.org/guest-post-how-the-role-of-carbon-storage-has-been-hugely-overestimated).
If all of it were used for removal, it would lower the temperature by
about 0.7 °C [C].

**Capture at a chimney is not removal.** A filter on a gas power plant
or a cement kiln stops new fossil CO2. That is a cut in emissions. Only
CO2 that came from the air (through a plant or a machine) and stays
out of the air counts as removal [S]
[State of CDR, chapter 1](https://www.stateofcdr.org/asset/SoCDR_ED3_Chpater-1_June-2026.pdf).

Sources for the table:
[CDR.fyi and OPIS prices](https://www.opis.com/blog/pricing-gap-in-durable-carbon-dioxide-removal-revealed-in-new-survey/),
[Stockholm Exergi](https://www.eib.org/en/press/all/2025-172-eib-finances-ground-breaking-carbon-capture-plant-in-stockholm),
[Drax](https://www.eenews.net/articles/energy-giant-drax-pulls-out-of-uk-climate-plan/),
[Beerling et al. 2020](https://eprints.soton.ac.uk/442331/),
[weathering trials](https://bg.copernicus.org/articles/23/7727/2026/),
[Planetary credits](https://isometric.com/writing-articles/worlds-first-verified-ocean-alkalinity-enhancement-credits),
[Cornwall](https://gasworld.com/story/uk-ocean-carbon-capture-trial-scrapped-over-viability-concerns/2154523.article),
[Carbfix](https://meetingorganizer.copernicus.org/EGU24/EGU24-16577.html).

## 8. All methods side by side

| | Trees and soils | Biochar | BECCS | Rocks and ocean | DAC |
| --- | --- | --- | --- | --- | --- |
| Removal now, per year | about 2.2 Gt | about 1 Mt | 1 to 2 Mt | thousands of tonnes | about 0.01 Mt |
| Realistic in 2050, Gt per year | 1 to 4 more | 0.5 to 2 | 0.5 to 3 | 0.5 to 2 | 0.1 to 1 |
| Cost per tonne now | $10 to $50 | $140 to $190 | about $230 | $270 to $350 | about $670 |
| How long it stays | Decades; can burn | Centuries | 10,000 years or more | 10,000 years or more | 10,000 years or more |
| Main limit | Land, fire, honest counting | Waste biomass | Land, biomass | Measurement | Energy, cost |
| Easy to measure | No | Yes | Yes | No | Yes |

The "realistic in 2050" row is my judgement from the ranges in the
studies above, not a result from one source. The sum is about 3 to 12
Gt per year. The need is 7 to 9. So the target can be reached only if
several methods work, and none of them is certain.

No method is cheap, permanent and large at the same time. Trees are
cheap and large but not permanent. Machines are permanent but not cheap
and not yet large.

## 9. Who pays?

A removed tonne has no buyer by nature. It is a waste service, like
sewage treatment. Somebody must be made to pay, or the state must pay.

- Buyers have ordered about 49 Mt of durable removal in total, and
  1.67 Mt has been delivered, which is 3.4% [C] from
  [CDR.fyi](https://www.cdr.fyi/blog/durable-cdr-market-update-carbon-unbound-east-coast-2026)
  [S]. All durable removal that was ever delivered equals 20 minutes
  of world CO2 emissions [C].
- One company, Microsoft, made about 90% of the purchases in 2025. In
  April 2026 it was reported to have paused new purchases; the company
  denies that the programme has ended [S]
  [Heatmap](https://heatmap.news/carbon-removal/microsoft-carbon-removal-pause).
  A market with one buyer is fragile.
- Public demand starts slowly. The EU certified its first permanent
  removal methods in 2026 and proposes to let removals into its carbon
  market after 2030. Sweden and Denmark buy bioenergy capture by
  auction. The US kept its tax credit of $180 per tonne [S].

The cost at full scale [C]:

| Removal per year | at $100 | at $340 | at $600 |
| --- | --- | --- | --- |
| 1 Gt | $100 billion (0.09% of world GDP) | $340 billion (0.29%) | $600 billion (0.51%) |
| 8.75 Gt | $0.9 trillion (0.75%) | $3.0 trillion (2.5%) | $5.3 trillion (4.5%) |
| To lower the temperature by 0.1 °C, once | $18 to 22 trillion | $62 to 76 trillion | $110 to 133 trillion |

World GDP is about $117 trillion [S]. The world spends about 2.5% of
GDP on its armies [M], so the middle case is of that size. It is
possible to pay. But the last row shows the main point: each 0.1 °C
that we let pass now costs tens of trillions of dollars to take back
later. To avoid the same emissions costs less than a third of that.

## 10. The risks of the idea itself

- **Delay.** If governments and companies count on cheap removal in
  2050, they cut less now. The removal then does not arrive, or it
  arrives late and small. Researchers call this "mitigation
  deterrence" and propose separate targets for cuts and for removal
  [S]
  [McLaren et al. 2019](https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2019.00004/full).
  "Net-zero oil" from Occidental is the clearest example.
- **A tonne is not a tonne.** A tonne in a tree for 40 years does not
  balance a tonne of fossil CO2 that stays for thousands of years. The
  Oxford principles say: use removal only for the emissions that
  cannot be avoided, and move to permanent storage by the net zero
  date [S]
  [Oxford](https://www.ox.ac.uk/news/2024-02-28-oxford-researchers-launch-updated-carbon-offsetting-principles).
- **Weak credits.** Forest credits sell for about $22 per tonne and
  the low price reflects the doubt [S]. The main report cites a review
  in which less than 16% of offset credits were real reductions.
- **Removal cools a little less than emission warms** [M]. The ocean
  gives back part of the CO2 that it took up when the air had more of
  it. So my numbers per 0.1 °C are a best case.

## 11. My judgement

1. **Removal is the last 10 to 20% of the solution, and it is not a
   reason to wait.** The cheap tonnes are the ones that are never
   emitted.
2. **The best "removal" action now is to keep the forests and the
   natural sinks.** They do 19 Gt per year without payment, and they
   become weaker as the planet warms.
3. **Plant and regrow forest where it fits:** in the wet tropics, with
   native trees, with the people who live there, and counted as a
   bonus for some decades. Do not sell it as a licence to burn fossil
   fuel.
4. **Build the technical methods now, with public money, because they
   need 20 years to grow.** The target is not tonnes today. The target
   is to learn what works and what it costs: about 30% growth per year, as
   solar had. Governments should buy removal as they buy waste
   treatment, by auction, with strict measurement.
5. **Keep two separate accounts,** one for emission cuts and one for
   removal, and inside removal one for permanent and one for
   temporary storage.
6. **For one person:** to pay for removal is a gift to a young
   industry, not a way to cancel a flight. At $200 to $700 per durable
   tonne, the same money cuts far more through the groups in section
   11 of the main report. Forest credits at $10 to $25 are useful for
   nature but they do not balance fossil CO2.

## What could not be verified

- No page was opened. Every fact from a paper, a report or a news
  site is [S], and the numbers for 2026 cannot be checked from memory.
- The IPCC numbers come from summaries and one draft chapter text, not
  from the final chapters.
- The 8.75 Gt need in 2050 is from secondary reports on the State of
  CDR 2026. An errata file exists for that edition and was not read.
- The removal by technical methods (about 2 Mt per year) is 0.1% of
  2.2 Gt. The 2024 edition gave 1.3 Mt.
- Temperate and boreal growth rates, the coal emission factor, the
  storage cost, the area of India and of cropland, and military
  spending are from memory.
- Mammoth numbers differ between sources (gross or net). Stratos may
  have started after the search.
- The "realistic in 2050" row in section 8 is my judgement.
- The cost table uses one price for all tonnes. Real costs differ by
  method and fall with time.

## Data and how to redo it

```
python3 removal.py
```

`removal.py` reads `analysis.json`, the carbon budget file in
`data/igcc/carbon_budget/`, and a list of cited parameters (`PARAMS`,
each with its label and source). It writes `removal.json`. Every [C]
number in this report is in that file. Change a parameter and run it
again to see what depends on it.
