# Deep Dive — The Value-Add Battery (potato → fry)

**Run 8 · Confidence 🔴 (elasticities from literature; VAM from price anchors)**

How many ways can we measure the value of turning a potato into a fry? Here are
several — and they all say the same thing from different angles.

## A. MCE-PF — Marginal Consumption Elasticity of Processing a Fry *(the headline)*

Income elasticity of demand ε = %Δquantity ÷ %Δincome.

| Good | ε (income elasticity) | Type |
|------|-----------------------|------|
| Raw potato | **−0.4 to −1.2** | inferior (richer → eat less) |
| Fries / processed | **~0 to +0.2** | ~normal (richer → don't cut back) |

> **MCE-PF = ε_fry − ε_potato ≈ +0.5** (up to +1.2)

**Processing adds ~+0.5 of income-elasticity: it converts an inferior good into a
normal one.** That is the economic essence of the fry. The raw potato is what you
eat when money is tight; the fry is what you keep eating when it isn't. Our own
[CPI deciles](../consumed-potato-index/REPORT.md) show the fingerprint — across
D1→D10 the potato-calorie share falls ~48 % but the fry share only ~29 %.

**MCE-PF is why the processing industry exists.** It is the mechanism by which the
potato sector grows revenue even as the world gets richer and eats fewer boiled
potatoes — the whole business model of McCain, Lamb Weston and Simplot.

## B. VAM — Value-Add Multiplier *(the visceral one)*

Farm-gate potato ≈ **$0.22/kg**. Trace the value of the ~220 g of potato inside a
single medium fry as it climbs the ladder:

| Venue | Price | Potato in it | **VAM** | Farmer's share |
|-------|-------|--------------|---------|----------------|
| Retail raw (boil at home) | $0.41 | $0.048 | **8×** | 11.8 % |
| Retail frozen (fry at home) | $0.36 | $0.048 | **7×** | 13.4 % |
| **QSR (McDonald's medium)** | $3.56 | $0.048 | **74×** | **1.4 %** |
| Fine dining (pommes frites) | $10.00 | $0.088 | **114×** | 0.9 % |

**A QSR fry is worth ~74× the farm-gate potato inside it — the farmer keeps ~1.4 %
(~5¢ of a $3.56 fry).** Of that 74×, only ~8× is getting a raw potato to a shop;
the remaining ~9× is the frying, cooking, serving and brand.

## C. CTM — Caloric Transformation Multiplier
Frying adds oil: **770 → ~3,100 kcal/kg = ~4× energy density.** Processing doesn't
just add price — it adds *calories* (relevant to [CPI](../consumed-potato-index/REPORT.md)).

## D. WTP — willingness-to-pay premium
From [PPC](../ppc/REPORT.md): a home-cooked potato calorie is **0.24 ¢**, a QSR fry
**1.11 ¢**, fine-dining frites **2.00 ¢** — people pay **up to ~8× more per
calorie** for the served, fried version. The gap *is* the convenience + craving +
service premium.

## The unifying punchline
Every lens — elasticity, price, calories, willingness-to-pay — is measuring one
thing: **the fry is what a potato becomes to survive rising income.** Boiling
keeps it an inferior staple; frying and serving buy it craveability, convenience,
shelf life and calorie density, and consumers reward all of it with a price they
*won't* cut when they get richer.

## Method & caveats
Elasticities from the literature (potato −0.4 to −1.19; processed ~normal), not a
fresh estimate (🔴). VAM uses a US processing-potato farm price (~$10/cwt) and the
[PPC](../ppc/REPORT.md) price anchors; per-fry raw input ~220 g (≈2:1 raw→finished).
Reproduce: `python3 tools/vam.py`.
