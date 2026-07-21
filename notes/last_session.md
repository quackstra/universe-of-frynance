# Last Session — Universe of Frynance

## Run 9 — the Fry Bill / induced supply chain (2026-07-20)

Quantified the demand the fry induces and the sector inputs it takes. Live at
quackstra.github.io/universe-of-frynance.

### Induced potato demand (`tools/fry_bill.py`, `fry_bill` block, capsule)
- Counterfactual: without the fry, ~40% of the 29.8 Mt fries stream reverts to
  fresh boiled; ~60% (~17.9 Mt) vanishes (income-elastic demand the fry sustains,
  MCE-PF). **~18 Mt = ~4.8% of ALL world potato production exists only because we
  fry.** Modeled split 🔴 (sensitivity: 25% revert -> 22 Mt, 55% -> 13 Mt).

### The sector bill (per 14.9 Mt finished fries, ~135B servings)
- Frying oil 1.94 Mt (~0.9% of world veg oil ~220 Mt) [headline]
- Salt 0.18 Mt · Energy 44.7 TWh (~1.4x Ireland) · Water 8.6 km3 (mostly green)
- Labor 1.8 B hours = ~900,000 FTE jobs [headline]
- Packaging 2.0 Mt · CO2e 67 Mt (small-nation footprint)
- Intensities: oil 13% finished wt, salt 1.2%, water 574 L/kg (waterfootprint.org),
  CO2e 4.5 kg/kg, energy 3 kWh/kg, labor 48 s/serving, packaging 15 g/serving.

### Dashboard
Fry Bill section: sector stat grid + induced-demand doughnut (revert vs induced) +
"fry's share of each global sector" bar. 2 insight cards, nav link, Run 9 badge.

## Full metric stack (9 runs)
Big Number · per-capita · MUSHT · TPS · PPC · Fry Index (+fry-flation) · CPI ·
MCE-PF/VAM · **Fry Bill** · Conscience. Tools: massbalance, musht, tps, ppc,
fry_index, cpi, vam, fry_bill, scout. Gate PASS every run.

## Next (Run 10 candidates)
- Estimate ε_fry/ε_potato directly from CPI decile curves (close MCE-PF loop).
- Fry Bill: split each sector by farm/processing/foodservice/consumer stage;
  ground labor with foodservice employment data; add cooking-oil waste/UCO stream.
- PPP Fry Index; real FAO FBS DES for CPI; processor tonnages; dining PPC rows.
