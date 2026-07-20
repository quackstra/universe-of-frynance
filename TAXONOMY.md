---
title: "Potato Taxonomy"
nav_order: 3
---

# Universe of Frynance — Potato Fate Taxonomy

> A living catalogue of every fate a potato can meet, organised into four tiers.
> Every Tier-1 fate gets its own research track; the tiers below it refine where
> the tonnes go.

**Counting rule (the mass-balance gate):** Tier-1 fates partition **100 % of
fresh-weight production**. They must sum to 100 %. Food Loss & Waste is a
*cross-cutting overlay* (it spans several fates) and is reported separately — it
is never added into the Tier-1 total. See `tools/massbalance.py`.

**Basis:** all shares are on a **fresh-weight** basis unless a capsule states a
product-weight conversion. MUSHT uses **raw-potato volume** (density ≈ 1.08
g/cm³).

---

## Tier 0: Variety Lens (cross-cutting)

Not a fate — a property that constrains fate. High-solids, low-sugar varieties
fry and crisp well; waxy varieties hold shape for fresh/boiling; specific
cultivars dominate each processing stream.

| Variety group | Typical fate bias | Examples |
|---------------|-------------------|----------|
| Russet / high-starch | Fries, baking, dehydrated mash | Russet Burbank, Innovator |
| Yellow / all-purpose | Fresh table, roasting | Yukon Gold, Agria |
| Red / waxy | Fresh, boiling, salads | Red Pontiac, Desiree |
| Crisping | Crisps/chips | Lady Rosetta, Atlantic |
| Fingerling / specialty | Fresh premium | Ratte, French fingerling |

---

## Tier 1: Fate of the Harvest — the Mass Balance (sums to 100 %)

| Fate | Description | Run-1 share (🔴 placeholder) | Key sources |
|------|-------------|------------------------------|-------------|
| **Fresh / table food** | Sold whole for home & foodservice cooking | ~44 % | FAO FBS, USDA ERS |
| **Processing (food)** | Potatoes entering food factories → Tier 2 | ~20 % | USDA ERS, Eurostat, processor reports |
| **Feed** | Animal feed (culls, surplus, by-product) | ~11 % | FAO FBS |
| **Seed** | Held back / grown for replanting | ~9 % | FAO FBS, seed-potato bodies |
| **Waste & loss (accounted)** | Post-harvest losses booked in utilisation accounts | ~10 % | FAO FBS "losses" line |
| **Industrial (non-food)** | Native/modified starch, alcohol, bioplastics | ~6 % | Starch industry, FAO |

> Shares are Run-1 placeholders pending the Scout/Architect pass — flagged 🔴.
> They currently sum to 100 % by construction; the Elves' job is to replace each
> with a sourced, confidence-tagged figure while keeping the sum at 100 %.

---

## Tier 2: Processing Split (of the ~20 % that is processed)

| Category | Description | Run-1 share of processing (🔴) | Key sources |
|----------|-------------|-------------------------------|-------------|
| **Frozen** | Fries, wedges, hash browns, tots — the fry engine | ~50 % | Lamb Weston, McCain, Simplot, USDA |
| **Crisps / chips** | Thin-sliced fried/baked snack | ~22 % | Snack industry, Euromonitor |
| **Dehydrated** | Flakes & granules → *mashed potato*, ingredients | ~15 % | USDA ERS, processor data |
| **Canned / other** | Canned whole/diced, refrigerated, salads | ~13 % | National food data |

**Starch** appears both here (food-grade) and in Tier-1 Industrial (non-food).
Capsules must state which lane a starch figure belongs to, to avoid double-count.

---

## Tier 3: Fry Taxonomy — the Fun Deep-Dive (Run-2 stretch for chain-level)

Within **Frozen → Fries**, three orthogonal splits:

### 3a. Cut geometry
| Cut | Note |
|-----|------|
| Straight / regular | The MUSHT reference geometry (0.75 cm square is a classic 3/8" cut) |
| Crinkle-cut | Ridged cross-section |
| **Curly** | Spiral-extruded/seasoned (the Run-2 headline) |
| Waffle / lattice | Cross-cut grid |
| Steak / wedge | Thick-cut, skin-on |
| Shoestring | Thin julienne |
| Tots / hash / smiles | Reformed/shaped |

### 3b. Channel
QSR chains (McDonald's, Burger King, Wendy's, Chick-fil-A, …) · full-service
restaurants · retail frozen (home) · institutional foodservice.

### 3c. Geography
By producing country and by consuming country — the two rarely match (trade in
frozen fries is large; e.g. Belgium/Netherlands export, Asia imports).

> **Scope note:** Run 1 stops at Tier 2 + total fries. Cut-geometry-by-chain
> (curly vs. crinkle by restaurant) is an explicit **Run-2 stretch** — it needs
> menu-level and processor-mix data that is 🔴 confidence today.

---

## MUSHT Geometry (reference)

- Fry cross-section: **0.75 cm × 0.75 cm** = 0.5625 cm².
- Potato density: **≈ 1.08 g/cm³** (raw; potatoes sink in water).
- Idealized MUSHT uses **100 % of production** (all varieties, all sizes).
- Real MUSHT uses the **fries fraction** derived from Tiers 1–2 above.

---

## Adding New Categories

When the Scout or Architect identifies a new fate/category:

1. Find the appropriate tier (or propose a new one).
2. Add it with description and key sources.
3. If it changes Tier-1 shares, **re-balance so the sum stays 100 %**.
4. Update this file via PR; the Architect designs a `METHODOLOGY.md` for it.
