# Deep Dive — PPC: Pennies Per Calorie

**Run 5 · Confidence 🟡 (prices) / 🟢 (calories)**

Where is it cheapest to *consume* a fry? PPC prices the only thing a fry really
delivers — energy.

> **PPC = price in US cents ÷ calories**

PPC is a ratio, so it is **portion-independent**: a medium chain fry and a whole
retail bag compare on the same axis.

## The ranking — cheapest fry calorie first

| # | Source | Price | kcal | **¢/cal** | Tier |
|---|--------|-------|------|-----------|------|
| 1 | Raw potato (home) | $0.85/lb | 350 | **0.24** | 🏠 |
| 2 | Retail frozen (home oven) | $2.97/bag | 1067 | **0.28** | 🏠 |
| 3 | **Five Guys** | $5.19 | 953 | **0.54** | 🍟 fast casual |
| 4 | In-N-Out | $2.15 | 370 | 0.58 | 🍟 |
| 5 | Burger King | $2.70 | 380 | 0.71 | 🍔 QSR |
| 6 | Chick-fil-A | $3.09 | 420 | 0.74 | 🍔 |
| 7 | Arby's curly | $3.09 | 410 | 0.75 | 🍔 |
| 8 | Wendy's | $2.99 | 350 | 0.85 | 🍔 |
| 9 | Casual dining (side) | $4.50 | 450 | 1.00 | 🍽️ |
| 10 | **McDonald's** | $3.56 | 320 | **1.11** | 🍔 |
| 11 | Fine dining (pommes frites) | $10.00 | 500 | **2.00** | ✨ |

## The three findings

1. **Home wins outright — by ~2–8×.** A raw-potato calorie costs **0.24 ¢**;
   cooking a retail bag, **0.28 ¢**. That's roughly **half** the cheapest
   restaurant and **one-eighth** of fine dining. The cheapest way to eat a fry is
   to make it yourself.
2. **The big-portion paradox: Five Guys is the cheapest restaurant fry per
   calorie** (0.54 ¢/cal) — even though it *feels* expensive at $5+. Its enormous
   953-cal portion makes each calorie cheap. Price-per-order and
   price-per-calorie disagree.
3. **McDonald's is among the priciest QSR per calorie** (1.11 ¢/cal) — **2× Five
   Guys** — because a medium is a modest 320 cal at a premium price. **Fine dining
   frites (2.00 ¢/cal) cost ~8× a home fry.**

## Method & caveats
US 2025 medium/regular menu prices (🟡, vary widely by location — McDonald's
alone ranges $1.89–$5.90 across states) ÷ published nutrition calories (🟢).
Casual- and fine-dining rows are representative estimates (🔴). PPC measures
*price efficiency of energy*, not health or value-for-satisfaction — a fry is a
fry, but this is deliberately a cost-of-calories lens. Reproduce:
`python3 tools/ppc.py`.
