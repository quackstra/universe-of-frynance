# Last Session — Universe of Frynance

## Run 8 — the Value-Add Battery (MCE-PF & VAM) (2026-07-20)

Brainstormed then built: how many ways to measure the value of turning a potato
into a fry. Live at quackstra.github.io/universe-of-frynance.

### The battery (`tools/vam.py`, `value_add` block, deep-dives/value-add capsule)
- **A. MCE-PF — Marginal Consumption Elasticity of Processing a Fry (headline).**
  ε_potato ≈ −0.4 to −1.2 (inferior good, lit-grounded); ε_fry ≈ 0 to +0.2
  (normal). MCE-PF = ε_fry − ε_potato ≈ **+0.5** (up to +1.2). Processing turns an
  inferior good into a normal one — the reason the processing industry exists.
  Fingerprint already in our CPI deciles (potato share −48% vs fry −29% across
  income).
- **B. VAM — Value-Add Multiplier.** Farm-gate potato $0.22/kg. A medium fry's
  ~220 g of potato (~5¢ farm value) sells for: retail raw 8× · retail frozen 7× ·
  **QSR 74×** · fine dining 114×. Farmer keeps **~1.4%** of a QSR fry.
- **C. CTM** — calorie density 770→3100 kcal/kg = ~4× (oil).
- **D. WTP** — PPC gap: 0.24 (DIY) → 2.00 (fine) ¢/cal = up to ~8× per calorie.

### Dashboard
New Value-Add section: MCE-PF stat grid + VAM ladder bar. 2 new insight cards,
nav link, Run 8 badge/footer.

### Design decisions (from the brainstorm, confirmed by Ferg "do it")
- MCE-PF as DIFFERENCE (ε_fry − ε_potato), not ratio.
- VAM shows both baselines; headline the farm-gate multiple (74×).

## Full metric stack (8 runs)
Big Number · per-capita · MUSHT · TPS · PPC · Fry Index (+fry-flation) · CPI ·
**MCE-PF/VAM** · Conscience. Tools: massbalance, musht, tps, ppc, fry_index, cpi,
vam, scout. Gate PASS every run.

## Next (Run 9 candidates)
- Estimate ε_fry/ε_potato directly from the CPI decile curves (replace lit values).
- Add convenience/time value (F) + shelf-life optionality (G) + industry GVA (I)
  lenses to the battery.
- PPP-adjust the Fry Index; ground CPI with real FAO FBS DES shares; processor
  tonnages; casual/fine-dining PPC rows.
