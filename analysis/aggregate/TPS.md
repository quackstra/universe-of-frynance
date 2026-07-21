# TPS — Taters Per Second

**The rate metric.** How fast does Earth produce potatoes, counted as whole
tubers? A deliberate cross-universe nod to
[Universe of Finance](https://quackstra.github.io/universe-of-finance)'s TPS
(transactions per second).

## Annual TPS ≈ **79,220 taters / second**

```
production 375 Mt / avg potato 150 g            = 2.50 trillion taters / yr
2.50e12 / 31,557,600 s                          ≈ 79,220 taters / second
```

### 🥔 vs 💸 — the easter egg
At ~**79,000 TPS**, **Earth grows potatoes faster than the entire global
financial system settles transactions** (~73,750 TPS, the Universe of Finance Big
Number) — about **1.07×**. Two universes, nearly the same Big Number, one in
spuds and one in dollars.

## Monthly TPS — two views, as requested

1. **Annual-averaged TPS** — the flat 79,220/s above.
2. **Month-by-month TPS** — the same annual total redistributed by a
   Northern-Hemisphere-weighted **consumption seasonality index**, normalised by
   its day-weighted mean so the twelve months reconcile exactly to the annual
   figure.

| Month | Index | TPS | vs annual |
|-------|-------|-----|-----------|
| Jan | 0.90 | 69,821 | −11.9 % |
| Feb | 0.94 | 72,925 | −7.9 % |
| Mar | 0.97 | 75,252 | −5.0 % |
| Apr | 0.99 | 76,804 | −3.1 % |
| May | 1.01 | 78,355 | −1.1 % |
| Jun | 1.04 | 80,683 | +1.8 % |
| Jul | 1.06 | 82,234 | +3.8 % |
| Aug | 1.05 | 81,458 | +2.8 % |
| Sep | 1.01 | 78,355 | −1.1 % |
| Oct | 1.03 | 79,907 | +0.9 % |
| **Nov** | **1.15** | **89,216** | **+12.6 %** |
| Dec | 1.10 | 85,337 | +7.7 % |

**Peak: November (~89,200 TPS)** — Thanksgiving, when 75 % of people eat potatoes
and US retailers move ~214 M lb of spuds in the run-up. **Trough: January
(~69,800 TPS)** — the post-holiday diet dip. A secondary summer bump (Jul) tracks
the QSR fry season.

### Run-4: Northern-Hemisphere vs both-hemisphere GLOBAL

The table above is **NH-weighted**. A true **global** index damps it, because the
Southern Hemisphere's seasons are offset by six months and most of the world's
potato eaters (India, China, the tropics) have weak seasonality:

> **global index = 1 + 0.4 × (NH index − 1)**

| View | Peak | Trough | Peak-to-trough swing |
|------|------|--------|----------------------|
| NH-weighted | Nov 89,216 | Jan 69,821 | **24 % of annual** |
| Both-hemisphere global | Nov 83,269 | Jan ~76,300 | **~10 % of annual** |

**The holiday spike is largely a Northern/Western phenomenon** — measured across
the whole planet, Taters-Per-Second is far flatter (a ~10 % swing, not 24 %). The
dashboard plots both curves. 🔴 on the exact damping factor; a future run would
build it from hemisphere-resolved consumption data.

## Assumptions & confidence

| Input | Value | Confidence |
|-------|-------|------------|
| Production | 375 Mt/yr | 🟢 FAOSTAT 2022 |
| Avg potato weight | 150 g (range 130–180) | 🟡 global-avg tuber; US medium russet ~170–180 g |
| Monthly seasonality | NH-weighted index | 🔴 estimate; global is smoother (hemispheres offset) |

**Sensitivity:** TPS scales inversely with avg potato weight — at 130 g it is
~91,400 TPS; at 180 g, ~66,000 TPS. The 150 g central case is the headline.

Reproduce: `python3 tools/tps.py`.
