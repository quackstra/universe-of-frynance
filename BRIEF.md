# Universe of Frynance — Project Brief

> Fry + Finance. Map the fate of every potato on Earth: from field to fork to
> french fry to waste bin — a transparent, reproducible mass balance of the
> global spud, and the gloriously large **MUSHT** number it implies.

## Mission

Build the definitive open dataset of what happens to the world's potatoes —
how much is grown, and where every tonne ends up (fresh table, frozen fries,
crisps, mashed flakes, animal feed, seed, industrial starch, and waste).
Published as transparent research with full source attribution, in the house
style of [Universe of Finance](../universe-of-finance) and
[Universe of Movement](../universe-of-movement).

## The Question We're Answering

**How many potatoes does Earth grow each year, and what becomes of them?**

We answer it with a linked metric stack derived from one underlying dataset.

### 1. The Big Number — Global Potato Production

> **~375 million tonnes / year** (FAOSTAT).

The headline aggregate: total fresh-weight potato production across all
varieties and sizes, all countries, per year. This is the Frynance analogue of
UoF's global TPS and UoM's AHV — a single summed quantity that anchors
everything downstream.

### 2. Per-Capita Potato (the intuitive companion)

> **≈ 46 kg / person / year** = Production ÷ world population.

"The average human's annual potato." Normalises for population so we can compare
across decades and countries.

### 3. MUSHT — Make Underutilized Spuds Have Taste (the hero / fun number)

> If **100 % of every potato grown on Earth** were extruded into one perfectly
> straight french fry, **0.75 cm × 0.75 cm** square in cross-section, how long is
> the line?
>
> **≈ 3.84 billion miles** — a single fry stretching *past Pluto's orbit*.

MUSHT is our MEST-analogue: a deliberately absurd, geometrically exact number
that makes the Big Number visceral. It is computed on a **raw-potato-volume**
basis (all spuds as grown, density ≈ 1.08 g/cm³) — the honest reading of "all
potatoes produced." See `tools/musht.py`.

- **Idealized MUSHT** — 100 % of production → the full 3.84 billion miles.
- **Real MUSHT** — only the spuds that actually become fries (~8–9 % of
  production), the sober companion that exposes how little of the harvest is
  fry.

### 4. The Conscience Number — Spuds Lost to Waste

> **~1 in 3 potatoes never reaches a human mouth.**

Roots & tubers have among the highest food-loss-and-waste rates of any crop.
Tracked as a cross-cutting overlay with its own methodology (see below).

## The Rigorous Spine: a Potato Mass Balance

Where UoF has the overlap matrix and UoM has flow-vs-snapshot reconciliation,
Frynance's integrity gate is a **mass-balance Sankey**: every tonne produced
must be accounted for downstream, and the Tier-1 fates **must sum to exactly
100 %** of production. This is the whole scientific backbone and it is
well-sourced — FAO Food Balance Sheets track potato utilisation accounts
directly. See `tools/massbalance.py` (enforces the 100 % gate) and
`data/global_massbalance.json`.

**Two definitional lanes that must not be conflated:**

- **Utilisation accounts** (the mass balance): fresh food, processing, feed,
  seed, industrial, and *accounted post-harvest losses* — these partition 100 %
  of production. This is the canonical Sankey.
- **Food Loss & Waste (FLW)**: a *cross-cutting overlay* measured along the whole
  chain (field → storage → processing → retail → consumer). FLW spans several
  utilisation lanes and is reported separately as the Conscience Number — never
  summed into the same total as the utilisation accounts (that would
  double-count). This is our anti-double-count rule.

## Core Principles

### 1. Measure, Don't Guess
Every number has a source. When exact data isn't available we use bounded
estimates with explicit methodology, tagged by confidence:
- 🟢 **High** — direct measurement or audited/official report (e.g. FAOSTAT)
- 🟡 **Medium** — derived from reliable partial data
- 🔴 **Low** — estimate based on limited data or extrapolation

### 2. Consistent Units
- **million tonnes (Mt)** fresh weight — the primary production/fate unit
- **% of production** — for every fate share (must sum to 100 %)
- **miles of fry** — MUSHT
- **kg/person/yr** — per-capita
- **CAGR** — growth over time

### 3. Fates & Categories, Not Brands
Run 1 measures *functional categories* ("frozen fries", "crisps", "dehydrated
mash"), not companies. Chain-level fry-cut breakdown (curly vs. crinkle vs.
straight, by restaurant) is an explicit **Run-2 stretch**, not a Run-1 headline.

### 4. Transparent Methodology
Every output includes sources, method, assumptions, confidence, and
reproducibility instructions.

### 5. Multiple Futures
Three projection scenarios minimum:
- **Baseline** — production tracks population; processing share keeps rising.
- **High-Processing** — QSR expansion across Asia/Africa; frozen fry demand
  booms; processed overtakes fresh globally.
- **Sustainability / Substitution** — waste reduction, cull upcycling, home
  air-fryer shift and alt-tuber diversification decouple fries from spud growth.

## Taxonomy (four tiers — see TAXONOMY.md)

- **Tier 0 — Variety lens** (russet / yellow / red / fingerling) — cuts across
  everything; determines whether a spud *can* be a fry, a crisp, or a mash.
- **Tier 1 — Fate of the harvest** (must sum to 100 %): fresh food · processing ·
  feed · seed · waste/loss · industrial non-food.
- **Tier 2 — Processing split**: frozen (fries/wedges/tots) · crisps · dehydrated
  (flakes → mashed) · starch · canned.
- **Tier 3 — Fry taxonomy** (the fun deep-dive): cut geometry (straight, crinkle,
  curly, waffle, wedge, shoestring, tots) · channel · geography.

## Pipeline Architecture

```
Scout → Architect → Elves → Publish
```

- **Scout** — discovers and ranks data sources (FAOSTAT, USDA ERS Potato
  Yearbook, Eurostat, CIP, Potatoes USA, World Potato Congress, and the big-three
  frozen-fry processor reports: Lamb Weston, McCain, Simplot).
- **Architect** — writes a `METHODOLOGY.md` per fate/category: scope, sources,
  fresh-weight conversions, projection models, double-counting risks, gaps.
- **Elves** — autonomous research agents that collect data, normalise to Mt and
  % of production, build timeseries and projections, chart, and write reports.
- **Publish** — per-fate capsules, master index, the Big Number, and MUSHT.

## Quality Gates

Before any research output publishes:

- [ ] All figures have cited sources
- [ ] Confidence levels assigned to every estimate
- [ ] Fresh-weight basis stated; any product-weight → fresh-weight conversion shown
- [ ] **Tier-1 fate shares reconcile to 100 % of production** (mass-balance gate)
- [ ] Food-Loss-and-Waste kept as an overlay, never summed with utilisation accounts
- [ ] Charts render with labelled axes and units
- [ ] Projection assumptions explicitly stated
- [ ] Data structured in machine-readable JSON
