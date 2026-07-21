# Universe of Frynance 🥔🍟

> Mapping the fate of every potato on Earth — from field to fork to french fry to
> waste bin. A sister project to [Universe of Finance](../universe-of-finance)
> and [Universe of Movement](../universe-of-movement).

## The Big Number

### **~375 million tonnes of potato / year**

Total global fresh-weight potato production, all varieties, all countries
(FAOSTAT). Everything downstream is a slice of this.

| Metric | Value | Meaning |
|--------|-------|---------|
| **Production** | **~375 Mt / yr** | The Big Number |
| **Per-capita** | **~46 kg/person/yr** | The average human's annual spud |
| **MUSHT (idealized)** | **~3.84 billion miles of fry** | A single 0.75 cm fry, *past Pluto* |
| **MUSHT (real)** | **~0.30 billion miles** | Only the ~7.9 % that actually becomes fries |
| **Curly fry** | **~12 M miles** | ~26 round-trips to the Moon — mostly Arby's |
| **TPS (Taters/sec)** | **~79,000/s** | > the world's financial transactions/sec (🥔 > 💸) |
| **PPC (cheapest fry cal)** | **0.24 ¢/cal** | Raw potato at home; fine-dining frites cost ~8× more |
| **Fry Index** | **4.7× range** | A McD fry calorie costs 4.7× more in Zurich than Mumbai |
| **CPI (Consumed Potato Index)** | **11 % → 2 %** | Potato's share of calories: Rwanda/Belarus ~11 %; fries: UK 2.5 % |
| **Conscience Number** | **~45 % wasted** | Spuds lost field→fork (roots & tubers waste most) |

## MUSHT — Make Underutilized Spuds Have Taste

If **100 % of every potato Earth grows** were extruded into one perfectly
straight french fry, **0.75 cm × 0.75 cm** square:

- **3.84 billion miles** long — **41 AU, past Pluto's average orbit**
- **154,000×** around the equator · **20.6** round-trips to the Sun
- a photon needs **5.7 hours** to travel its length

The sober companion — **Real MUSHT** — counts only the spuds that actually
become fries (~8.5 % of production). The **3.5-billion-mile gap** between the two
is a headline in itself: most of the spud is *not* a fry.

```bash
python3 tools/musht.py        # the fun number (idealized + real)
python3 tools/massbalance.py  # the Big Number + the 100% mass-balance gate
```

## Three counter-intuitive findings (Run-1 hypotheses)

1. **Only ~1 spud in 12 becomes a fry.** Fries loom huge culturally but are a
   thin slice (~8.5 %) of what Earth grows.
2. **The bin rivals the plate.** Food loss & waste (~1 in 3) is comparable in
   mass to the entire fresh-table fate — the Conscience Number.
3. **Fresh still beats processed, globally.** Despite the QSR image, most
   potatoes are still sold and cooked whole — for now.

## The Metric

- **Big Number** = annual production, in **Mt fresh weight**.
- **Per-capita** = production ÷ population, in **kg/person/yr**.
- **MUSHT** = miles of a 0.75 cm-square fry from raw-potato volume (ρ≈1.08 g/cm³).

The integrity spine is a **mass balance**: Tier-1 fates must sum to **100 %** of
production (`tools/massbalance.py` enforces it). Food Loss & Waste is a
cross-cutting *overlay*, reported separately, never summed into the 100 %. See
[BRIEF.md](BRIEF.md).

## Scope (Run 1)

Functional categories, not brands. Stops at Tier-2 processing + total fries.
Chain-level fry-cut breakdown (curly vs. crinkle vs. straight, by restaurant) is
an explicit **Run-2 stretch**. Fresh-weight basis; MUSHT on raw-potato volume.

## Project Structure

```
universe-of-frynance/
├── BRIEF.md                 # Mission, metric definitions, mass-balance principle
├── TAXONOMY.md              # Four-tier fate taxonomy (variety → fate → processing → fry)
├── data/
│   └── global_massbalance.json  # Big Number + Tier-1/2 shares + FLW overlay
├── analysis/
│   ├── README.md            # Research index + fate leaderboard
│   ├── aggregate/BIG_NUMBER.md  # The Big Number + MUSHT write-up
│   └── <fate>/<category>/   # Per-fate capsules (REPORT + data.json + workings + charts)
├── tools/
│   ├── musht.py             # MUSHT (idealized + real)
│   └── massbalance.py       # Big Number + 100% reconciliation gate
├── scout/                   # Data-source discovery + backlog ranking
├── architect/               # Research methodology design (SKILL.md)
├── elves/                   # Autonomous research protocol + validation gates
└── notes/                   # Inter-session continuity
```

## Pipeline

`Scout → Architect → Elves → Publish`.

```bash
./run.sh scout          # rank fates/categories into scout/backlog.yaml
python3 tools/massbalance.py   # recompute Big Number + check the 100% gate
python3 tools/musht.py         # recompute MUSHT
./run.sh elf-run        # full autonomous research run
```

## Status

**Run 7 — the Consumed Potato Index (2026-07-20):** added **CPI** — potato's
share of a country's calories, with a fries sub-share and US income deciles.
Headline: **Rwanda/Belarus are most potato-dependent (~11 %) but the UK/US are
most fry-dependent (2.5 %/2.0 %)** — staple vs fry culture; potato-calorie share
**falls with income** (4.6 %→2.4 %). Also **real fry-flation** (2.1× after
inflation, vs 3.9× nominal). New `tools/cpi.py`; dashboard CPI section (country
bar + decile line) + real-dollar line on fry-flation.

**Run 6 — the Fry Index & fry-flation (2026-07-20):** internationalised PPC — a
McDonald's medium (320 cal) priced across countries (Big Mac Index style): **a fry
calorie costs ~4.7× more in Zurich than Mumbai** (0.41→1.93 ¢/cal). Plus
**fry-flation** — the US McD fry is up **~3.9× since 2000**, dearer per calorie
than general inflation. New `tools/fry_index.py` + [deep dive](analysis/deep-dives/fry-index/REPORT.md)
+ dashboard (country bar + time series).

**Run 5 — PPC: Pennies Per Calorie (2026-07-20):** added the value metric —
where a fry calorie is cheapest to buy. **Home wins (~0.24 ¢/cal), ~8× cheaper
than fine-dining frites; among restaurants big-portion Five Guys (0.54) beats
McDonald's (1.11) 2:1.** New `tools/ppc.py` + [deep dive](analysis/deep-dives/ppc/REPORT.md)
+ dashboard PPC chart.

**Run 4 — grounding pass (2026-07-20):** put sourced numbers on the Run-3
scaffolds — processor corroboration (**McCain ~1 in 4 fries worldwide**; ~30 Mt
raw ≈ 15 Mt finished), the **chain-vs-independent** foodservice split
(independents ~422k units / ~55 % of fry volume — now 🟡), and a **both-hemisphere
global TPS** curve (holiday swing 24 % NH → ~10 % global; `tools/tps.py` prints
both). Dashboard gains the global TPS line and a tier-split bar.

**Run 3 — TPS, restaurant tiers & fry-companions tracker (2026-07-20):** added
**[TPS — Taters Per Second](analysis/aggregate/TPS.md)** (~79,000/s annual +
month-by-month, day-weighted-normalised, Nov peak / Jan trough; 🥔 > global
finance 💸); expanded the fry deep dive to **restaurant tiers** including the
independent/non-chain long tail; and launched the
**[fry-companions tracker](analysis/deep-dives/fry-companions/REPORT.md)** (burger
#1). New `tools/tps.py`; dashboard gains a TPS section with the monthly line chart
and a companions chart.

**Run 2 — country-weighted rebuild + fry-cut deep dive (2026-07-20):**
country-weighted processing share (US 70 % · EU ~45 % · China 15 % · India 7 % ·
RoW ~8 %, production-weighted → **17 %**), USDA-grounded frozen split, and the
**[fry-cuts-by-chain deep dive](analysis/deep-dives/fry-cuts-by-chain/REPORT.md)**
(curly ≈ 12 M miles/yr, mostly Arby's; waffle from Chick-fil-A). Fresh, processing
and frozen now 🟡. Dashboard upgraded with a Sankey and a cut-mix chart.
**Run 1** replaced placeholders with sourced FAO/CIP figures and shipped the
dashboard. **Run 0** forked the framework, mass-balance spine, 100 % gate, and
MUSHT calculator. **Next (Run 3):** processor-reported fry volumes (McCain/Lamb
Weston/Simplot) + trade data, stage-resolved FLW, historic arc. See
[`notes/research_agenda.md`](notes/research_agenda.md).

## License

Research outputs: CC BY 4.0. Code: MIT.
