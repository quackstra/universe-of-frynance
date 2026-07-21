# Last Session — Universe of Frynance

## Run 6 — the Fry Index & fry-flation (2026-07-20)

Internationalised + time-extended the PPC metric. Live at
quackstra.github.io/universe-of-frynance.

### The Fry Index (international PPC) — `tools/fry_index.py`, `fry_index` block
- McDonald's medium (320 cal) priced across countries, Big Mac Index style:
  India 0.41 · Japan 0.69 · UK 0.71 · Eurozone 1.09 · USA 1.11 · Switzerland 1.93
  ¢/cal. **A fry calorie costs ~4.7× more in Zurich than Mumbai.**
- Local icons: UK chippy chips 0.55 ¢/cal (great rich-world deal), Belgian
  friterie frites 0.75.

### Fry-flation (over time) — `fry_flation` block
- US McD medium: 2000 $1.09 → 2025 $4.29 = **3.9× nominal** (PPC 0.34 → 1.34
  ¢/cal). McD prices rose ~100% in the decade to 2024 — ~2× general inflation.

### Dashboard
PPC section now also has a **Fry Index country bar** (green<0.75<orange<1.5<red)
and a **fry-flation line** (2000→2025). New insight card. Run 6 badge/footer.

### Data anchors
gobankingrates (US vs Europe McD); Switzerland CHF 5.60; UK chippy chips £~3;
Belgian frites €3.20/468 cal; Visual Capitalist McD inflation 2014-24 (+~100%);
McD-reported 2019 avg $2.29, 2024 $4.19. FX 2025: ₹83/¥150/£0.79/€0.92/CHF0.91.

## Full metric stack
Big Number (375 Mt) · per-capita · MUSHT (3.84B mi) · TPS (~79k/s) · PPC
(0.24-2.00 ¢/cal) · **Fry Index (4.7× range) + fry-flation (3.9×)** · Conscience
(~45%). Tools: massbalance, musht, tps, ppc, fry_index, scout. Gate PASS.

## Next (Run 7)
- PPP-adjust the Fry Index (currently nominal FX); add more countries.
- Inflation-adjust fry-flation (real vs nominal); overlay CPI.
- Ground casual/fine-dining PPC rows (still 🔴).
- Still-open from earlier: exact processor tonnages; POS companion attach; FBS
  feed/seed/industrial pull.
