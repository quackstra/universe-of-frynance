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
| **MUSHT (real)** | **~0.33 billion miles** | Only the ~8.5 % that actually becomes fries |
| **Conscience Number** | **~1 in 3 wasted** | Spuds that never reach a mouth |

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

**Run 0 — framework fork (2026-07-20):** forked the house framework from Universe
of Movement; established the potato mass-balance spine, the 100 % gate, and a
working MUSHT calculator (idealized 3.84 B miles / real 0.33 B miles). All Tier-1
and Tier-2 shares are 🔴 placeholders that reconcile to 100 % by construction.
**Next (Run 1):** replace every placeholder with sourced FAOSTAT / USDA ERS /
Eurostat figures, write per-fate capsules inside-out (fresh → processing →
fries), and build the Sankey chart. See [`notes/research_agenda.md`](notes/research_agenda.md).

## License

Research outputs: CC BY 4.0. Code: MIT.
