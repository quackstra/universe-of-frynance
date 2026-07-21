# Deep Dive — The Fry Economy (total economic impact)

**Run 10 · Confidence 🔴 (modeled: market size × standard multipliers)**

The whole point of [MCE-PF](../value-add/REPORT.md) is that frying keeps an
inferior good on richer tables. So what's the *entire* economic footprint of that
effort? An IMPLAN/Type-II style impact model: direct + indirect (suppliers) +
induced (the spending of those workers' wages).

## Output — the money

| | $/yr |
|---|------|
| Final demand (consumer fry spend) | **$150 B** |
| × output multiplier (1.9) | **$285 B total economic output** |
| Value-added (GDP contribution, ~45 %) | **$128 B** |

The frozen-fry *manufacturing* market alone (~$26 B, 65 % foodservice) sits inside
that final-demand figure — the rest is the restaurant/retail service layer where
most of the [VAM](../value-add/REPORT.md) value-add is captured.

## Jobs — the employment pyramid

| Tier | Jobs | What |
|------|------|------|
| **Direct** | **0.90 M** | frying, serving, processing |
| **Indirect** | **0.90 M** | suppliers (below) |
| **Induced** | **0.45 M** | those workers spending their wages |
| **TOTAL** | **~2.25 M** | employment multiplier ~2.5× |

**Keeping the world eating potatoes as fries employs ~2.25 million people** — a
mid-large city's entire population — every one of them working so an inferior good
stays desirable as incomes rise.

## Downstream support (indirect) jobs, by supplier sector

| Sector | Jobs |
|--------|------|
| 🥔 Potato farming & storage (for fries) | 300 k |
| ❄️ Cold chain, freight & logistics | 200 k |
| 🚚 Distribution & retail support | 150 k |
| 📦 Packaging | 80 k |
| 🛢️ Vegetable oil production | 70 k |
| 🏭 Equipment (fryers, freezers) | 60 k |
| 🧂 Salt, seasonings & other inputs | 40 k |
| **Total indirect** | **900 k** |

Each direct fry job pulls ~1 supplier job and ~0.5 induced job into being — the
farm, the freezer truck, the oil refinery, the box factory, and the shops those
paychecks are spent in.

## The full stack, connected
This is where the whole Universe of Frynance argument lands. **MCE-PF** says
processing converts an inferior good into a normal one; the **Fry Bill** counts
the ~18 Mt of induced potato demand and its oil/salt/energy/labor inputs; the **Fry
Economy** puts a dollar and a headcount on all of it: **a ~$285 B, ~2.25 M-job
engine that exists to keep the humble potato on the plate as the world gets
richer.**

## Method & caveats
Final demand ≈ 135 B servings × ~$1.2 blended price (🔴 — the softest input;
market reports value the *manufacturing* layer at ~$18–29 B). Output multiplier
1.9 and total employment multiplier 2.5 are standard food-sector Type-II values
(food manufacturing runs ~3.0; blended down here for the service-heavy mix).
Supplier-job split is an allocation, not a census. Reproduce:
`python3 tools/fry_economy.py`.
