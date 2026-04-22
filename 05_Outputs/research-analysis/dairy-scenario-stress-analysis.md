# Dairy Farm Scenario Stress Analysis

## Executive Summary
Your three scenarios—wastewater reuse, renewable energy, feed optimization—are not independent. They interact as sequential bottlenecks. A robust strategy requires identifying which constraints actually bind under stress (drought, price spikes, grid failure).

---

## Scenario 1: Wastewater Reuse

**Current approach:** Recycle 32% of non-drinking wastewater via feedback loop back to water storage.

### Stress Factors
- **Treatment cost eats savings.** Recycling costs energy (pumping, UV/chemical treatment). In Texas summer heat, evaporative loss from storage/treatment cycles may exceed water saved.
- **Milk cooling is inelastic.** Immediate cooling to 39°F is food-safety non-negotiable. Recycled water may not arrive cold/clean enough; defaults to grid water anyway.
- **Mineral buildup after 3-4 cycles.** Salinity concentrates. Corrodes equipment. Requires system replacement (capital loss).

### Improved Scenario
- **Reuse only for non-critical uses:** pre-rinse, cattle drinking, yard cleanup—NOT milk cooling.
- **Model treatment cost as % of savings:** When does the system break even?
- **Add water quality degradation loop:** Each cycle reduces usability; model culling point.
- **Include capital payback:** Treatment system cost ÷ annual savings = years to ROI.

### Bottom Line
Wastewater reuse is margin-improvement, not game-changer. Works best as *supplemental* system, not primary water strategy.

---

## Scenario 2: Renewable Energy

**Current approach:** Solar + wind as backup to grid, with batteries for storage.

### Stress Factors
- **Peak demand misalignment.** Milking 150+ cows = 4–6 hour demand spike (~30–50kW for cooling). This happens 4–10am and 4–8pm. West Texas wind peaks 8pm–4am. Solar peaks noon–2pm. You're grid-dependent during peak milking *anyway*.
- **Battery cost is brutal.** 4 hours × 50kW = 200kWh storage. Lithium cost = $200k+. Do the ROI math: even at $0.15/kWh, you save $2,700/year. Payback = 74 years.
- **Grid connection is sunk cost.** You still need grid infrastructure (transformers, lines). If you're keeping it as backup, the "savings" are just load reduction on peak hours, not elimination.

### Improved Scenario
**Model three strategies head-to-head:**
1. **Grid baseline** (current state)
2. **Solar-dominant** (capital cost + grid backup) — reduces peak load, keeps grid connection
3. **Wind-dominant** (aligns with milking windows) — requires bigger wind farm or taller turbine

**Include seasonality:** Summer cooling load >> winter heating load in dairy. Solar helps summer; wind could help year-round.

**Account for degradation:** Solar panels degrade ~0.5%/year. Wind turbines need maintenance ($2–5k/year after Year 5).

### Bottom Line
Full renewable independence is capital-prohibitive. Hybrid (wind-dominant + grid backup) may beat solar-only. Or: stay 100% grid if grid is cheaper than capital cost of renewables.

---

## Scenario 3: Feed-to-Energy Conversion

**Current approach:** Ensure enough food for maintenance while maximizing milk production.

### Stress Factors
- **Feed cost is largest variable expense.** Corn/hay prices swing 30–40% year-to-year. Drought year = low hay supply, high prices → forces culling or lower production.
- **Milk production has biological limits.** Cows can't convert feed to milk faster by willpower. Over-feeding causes metabolic disease, lower fertility, higher vet costs. Conversion efficiency is a curve with diminishing returns, not a linear function.
- **Water-feed coupling you're missing.** High-producing cows need more water (more milk = more metabolic water). In drought (low water reuse), you *can't* increase production without more feed *and* more water. These constraints interact.

### Improved Scenario
- **Model feed-to-milk as a curve:** Production = f(feed input), where marginal returns decline. Add a cost axis: feed cost + water cost must stay below milk revenue.
- **Add seasonal variation:** Winter maintenance cost > summer (cold stress, lower grazing). Milk price also seasonal.
- **Include profitability constraint:** Total margin = (milk price × volume) - (feed cost + water cost + energy cost). Optimize for margin, not just production volume.
- **Model drought stress explicitly:** When water is scarce, production must drop. You can't optimize away a physical constraint.

### Bottom Line
Feed optimization is not about maximizing production; it's about maximizing *profitable* production. Profit margin is the real objective, not milk volume.

---

## The Real Stress Test: Sequential Bottlenecks

Your three scenarios are not independent. They form a chain:

```
Water Availability → Energy (treatment/cooling) → Feed Supply → Milk Production → Profit
```

**Under stress (drought + high feed prices + grid outage), they cascade:**
1. Water reuse system fails (no wastewater input → can't treat → can't recycle)
2. Solar insufficient (grid outage happens at night → no renewable backup)
3. Feed cost spikes (can't reduce herd fast enough without vet/welfare costs)
4. Milk production collapses (dehydrated cows produce less)
5. Farm goes insolvent (fixed costs, zero revenue)

### The Real Question to Model
**"Under a 1-in-10-year stress scenario (drought + grid outage + feed price spike), what's the minimum viable operation?"**

Instead of "implement all three scenarios," ask: 
- What's the smallest herd size that stays profitable?
- Which constraint kills the farm first (water, energy, feed, or market price)?
- What's the emergency protocol (sell herd? reduce production? accept losses)?

---

## Recommendation for Your Paper

**Structure the analysis around a resilience framework, not just optimization:**

1. **Baseline:** Model current state with realistic price/weather volatility
2. **Scenarios:** Each intervention (water reuse, renewables, feed efficiency) improves baseline
3. **Stress test:** Drought + high prices + grid outage; see which scenarios survive
4. **Recommendation:** Best scenario likely combines:
   - Wastewater reuse (water security)
   - Wind (aligns with milking hours) + grid backup (not batteries)
   - Feed cost hedging (futures contracts, diverse forage mix)

This frames your work as **risk management**, not just cost reduction. That's what farms actually care about.

---

## Next Steps
1. **Get operational data:** Current herd size, water/energy/feed costs, seasonal variation
2. **Model baseline state** with price/weather volatility (Monte Carlo simulation)
3. **Layer scenarios** and stress test each
4. **Identify break-even thresholds** (when does reuse pay off? when does wind beat grid?)

