# Deep Dive — CPI: the Consumed Potato Index

**Run 7 · Confidence 🔴 (modeled from FAO consumption + income surveys)**

What share of a country's calories comes from potatoes — and from **fries**
specifically? And how does it split by income? (A deliberate pun on the *other*
CPI, the Consumer Price Index.)

## By country — the staple-vs-fry divide

Potato's share of dietary energy **supply** (as-eaten, including frying oil), with
a fries-only sub-share:

| Country | Potato % of calories | of which **fries** |
|---------|----------------------|--------------------|
| 🇷🇼 Rwanda | **11.0 %** | 0.2 % |
| 🇧🇾 Belarus | **11.0 %** | 1.0 % |
| 🇺🇦 Ukraine | 9.0 % | 0.8 % |
| 🇵🇪 Peru | 6.0 % | 0.6 % |
| 🇵🇱 Poland | 6.0 % | 1.0 % |
| 🇬🇧 UK | 5.5 % | **2.5 %** |
| 🇮🇪 Ireland | 5.0 % | 1.8 % |
| 🇺🇸 USA | 3.5 % | **2.0 %** |
| 🇨🇳 China | 2.5 % | 0.5 % |
| 🇮🇳 India | 2.0 % | 0.3 % |
| 🌍 World | 2.4 % | 0.4 % |

**The headline finding: highest potato-dependence is *not* highest
fry-dependence.** Belarus, Rwanda, Ukraine and Peru lean hardest on the
potato (~9–11 % of all calories) — but almost entirely as **boiled, baked or
fresh** staple. The **fry**-dependent countries are the Anglo/Western fry
cultures — the **UK (2.5 %)** and **USA (2.0 %)** get more of their calories from
*fried* potato than anyone, despite eating far less potato overall. Two totally
different relationships with the same tuber.

## By income decile (USA, representative)

| Decile | Potato % | Fry % |
|--------|----------|-------|
| D1 (poorest) | 4.6 % | 2.4 % |
| D5 | 3.6 % | 2.0 % |
| D10 (richest) | 2.4 % | 1.7 % |

**Potato-calorie share falls steadily with income** (4.6 % → 2.4 %): the cheap
staple — and cheap fried calories — are leaned on more at the bottom, which ties
directly to [PPC](../ppc/REPORT.md) (a fry is one of the cheapest calories money
can buy).

**The fry curve is deliberately flatter, and the reason is subtle.** The lazy
assumption "poor people eat more fries" is only half-right:
- Fast-food **frequency** actually *rises* with income (CDC: 31.7 % of lower-income
  vs 42.0 % of higher-income adults ate fast food on a given day).
- But lower-income diets draw a **higher share** of their away-from-home calories
  from cheap fried food (ERS: 16.4 % vs 15.3 %), and more cheap **retail frozen**
  fries at home.
- Net: richer people eat fries more *often*, but fries are a *smaller slice* of
  their larger, more varied diet — so the fry-share curve tilts only gently toward
  the bottom decile.

## Method & caveats
Country shares = per-capita potato supply (FAO/industry, e.g. Belarus 181 kg/yr,
Rwanda 125 kg/yr) × calorie density ÷ dietary energy supply; fries sub-share from
each country's processing/fry culture. Supply-based (includes some waste) — an
**upper bound** on intake. Deciles are modeled from ERS/CDC income-diet patterns,
not a direct potato-by-decile survey (🔴). Reproduce: `python3 tools/cpi.py`.
