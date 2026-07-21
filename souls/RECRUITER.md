---
title: "Recruiter Overview"
parent: SLE Profiles
grand_parent: Explore
nav_order: 100
---

# Intergalactic Recruiter — Soul Less Employee Framework (Frynance)

> "The right question, asked by the right mind, holding the right potato."

## What This Is

The Intergalactic Recruiter maintains a roster of **Soul Less Employees (SLEs)** —
expert personas grounded in real job descriptions from the world's agricultural
statistics, crop-science, food-processing, food-loss, agribusiness, and nutrition
organizations. When an Elf researches a potato fate, a processing stream, or a
consumer metric, it consults this framework to decide **which expert(s) would best
answer it**, then adopts their perspective.

Frynance's headline gate is the **fate mass balance**: Tier-1 fates
(fresh / processing / feed / seed / accounted-loss / industrial) sum to 100% of
fresh-weight production, and Food Loss & Waste is a cross-cutting overlay reconciled
against the FBS loss line — never added on top. Different SLEs own different fates
and conversions; the recruiter pairs them so a capsule never breaks the 100% gate.

## The Roster

| # | Slug | Role Title | Pillar | Primary Coverage | Basis Owned |
|---|------|-----------|--------|------------------|-------------|
| 1 | `agricultural-economist` | Agricultural Economist & Utilisation Analyst | Gov / Academia | Production, Tier-1 fate mass balance | Fresh-weight ledger |
| 2 | `potato-agronomist` | Potato Agronomist & Crop Scientist | Academia / Gov | Tier-0 variety lens, seed fate, yield | Dry-matter / variety |
| 3 | `food-processing-technologist` | Processing Technologist & Food Engineer | Academia / Industry | Processing → Tier 2, fries cut mix, oil | Product→fresh conversions |
| 4 | `postharvest-loss-researcher` | Food Loss & Waste Researcher | Academia / NGO | Waste overlay (Conscience Number) | FLW Protocol |
| 5 | `agribusiness-commodity-analyst` | Agribusiness & Frozen-Fry Market Analyst | Industry | Frozen-fry market, QSR demand, Fry Economy | Demand / trade / value |
| 6 | `nutrition-food-scientist` | Nutrition Economist & Food Scientist | Academia / Gov | Calories, CPI, PPC, Fry Index | Calories / composition |

**Pillar balance (by design):** government statistics, academic crop/nutrition
science, NGO food-loss research, and industry market intelligence each check the
others' blind spots.

## Dispatch Matrix

### Fate / Capsule → SLE Routing

| Capsule | Primary SLE | Secondary SLE(s) |
|---------|-------------|-------------------|
| **Production** (Big Number, per-capita) | `agricultural-economist` | `potato-agronomist` |
| **Fresh / table fate** (home vs foodservice) | `agricultural-economist` | `agribusiness-commodity-analyst` |
| **Processing fate → Tier 2** (frozen/crisps/dehydrated/canned) | `food-processing-technologist` | `agricultural-economist`, `agribusiness-commodity-analyst` |
| **Fries** (tonnage + cut mix, Real MUSHT) | `food-processing-technologist` | `agribusiness-commodity-analyst` |
| **Feed fate** | `agricultural-economist` | `potato-agronomist` |
| **Seed fate** | `potato-agronomist` | `agricultural-economist` |
| **Waste & loss** (Conscience Number) | `postharvest-loss-researcher` | `agricultural-economist` |
| **Industrial** (starch/alcohol/bioplastics) | `food-processing-technologist` | `agricultural-economist` |
| **Tier-0 variety lens** | `potato-agronomist` | `food-processing-technologist` |

### Cross-Cutting Question Routing

| Question Archetype | Lead SLE | Supporting SLE(s) |
|-------------------|----------|-------------------|
| "What fresh-weight conversion do I use?" | `food-processing-technologist` | `agricultural-economist` |
| "Which varieties can even become fries?" | `potato-agronomist` | `food-processing-technologist` |
| "How much is wasted, and where?" | `postharvest-loss-researcher` | `agricultural-economist` |
| "How big is the frozen-fry market / trade?" | `agribusiness-commodity-analyst` | `food-processing-technologist` |
| "What's the Fry Economy (jobs, oil, CO2)?" | `agribusiness-commodity-analyst` | `nutrition-food-scientist`, `food-processing-technologist` |
| "What's a fry-calorie cost / worth?" (PPC, Fry Index) | `nutrition-food-scientist` | `agribusiness-commodity-analyst` |
| "What share of the diet is potato?" (CPI) | `nutrition-food-scientist` | `agricultural-economist` |
| "Is this in scope / mass-balance ok?" | `agricultural-economist` | `postharvest-loss-researcher` |

## The Mass-Balance Reconciliation Panel

Frynance's headline sanity check: every capsule must leave the Tier-1 fates summing
to exactly 100% of fresh-weight production. When a new figure threatens the gate,
convene the panel.

1. **`agricultural-economist` holds the ledger** — restates production and the
   Tier-1 fate shares, ensuring the new figure still sums to 100% on a fresh-weight
   basis.
2. **`food-processing-technologist` checks the conversions** — verifies any
   product-weight figure (frozen fry, crisp, dehydrated) was converted back to
   fresh-weight before it entered the balance.
3. **`postharvest-loss-researcher` guards against double-counting** — confirms the
   FLW overlay is reconciled against FBS's accounted-loss line and not added into
   the Tier-1 total.

**Output:** a reconciliation note stating which conversion or overlay was at risk,
the revised shares, and the confidence tag (🟢/🟡/🔴). The fries fraction stays 🔴
until an independent source pins it.

## Multi-SLE Protocol

1. **Ledger SLE frames the number** — `agricultural-economist` fixes production and
   the fate share before any downstream, market, or nutrition claim is built on it.
2. **Fate/stage SLE builds outward** — processing, agronomy, or waste specialist
   extends to their fate with explicit, sourced conversions.
3. **A demand/consumer SLE stress-tests** — agribusiness or nutrition analyst checks
   the tonnage against market pull and dietary reality.
4. **Blind spots are cross-checked** — each SLE's documented bias (e.g., the
   processing technologist's frozen-fry gravity, the loss researcher's advocacy pull)
   is reviewed against the finding.

## When to Add a New SLE

- A new fate or Tier-2 stream enters TAXONOMY.md with no natural home
- The Fry Bill's environmental line outgrows a shared owner (e.g., a dedicated
  `lca-sustainability-analyst` for oil/water/CO2e if the footprint becomes a core track)
- A fate's confidence stays 🔴 after two runs and the current SLE's sources are
  exhausted (the fries fraction and cut-mix are the current watch-list)
- A major data source needs specialist interpretation (e.g., satellite acreage for
  the China production reconciliation, or processor-level line data for cut mix)

## Integration with Elf Pipeline

```
Scout → Architect → [RECRUITER dispatch] → Elf (with SLE persona) → Mass-Balance Panel → Publish
                           ↓
                    Read SOUL.md for:
                    - Activation phrase (prepend to research prompt)
                    - Data sources (prioritized lookup order)
                    - Mental models (analytical lens)
                    - Blind spots (explicit bias check)
```

The Elf adopts the fate primary's perspective, pulls a demand/consumer SLE for the
market or nutrition angle, and uses each SLE's "Blind Spots" section as a built-in
adversarial check before a capsule passes the mass-balance panel.
