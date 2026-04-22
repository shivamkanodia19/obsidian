---
title: Scenario Stress Analysis
project: dairy-farms
status: stable
origin_dump: "[[05_Outputs/dairy-scenario-stress-analysis.md]]"
last_synced_dump: "[[05_Outputs/dairy-scenario-stress-analysis.md]]"
last_updated: 2026-04-16
tags: [scenario-analysis, stress-test, water, energy, feed, resilience]
---

# Scenario Stress Analysis

## Strategic Framework
Three sustainability scenarios (water reuse, renewable energy, feed optimization) are not independent. They form a sequential chain that cascades under stress.

**Key insight:** Rather than optimize each independently, model which constraint kills the farm first under adverse conditions (drought + price spike + grid outage).

## Scenario 1: Wastewater Reuse

### Current Weakness
Recycle 32% of non-drinking wastewater via feedback loop. Too simplistic to be viable.

### Stress Factors
1. **Treatment cost eats savings** — Recycling requires energy (pumping, UV/chemical). Evaporative loss in Texas summer may exceed water saved.
2. **Milk cooling is inelastic** — 39°F cooling is non-negotiable (food safety). Recycled water may not arrive cold/clean; defaults to grid.
3. **Mineral buildup cycles** — After 3-4 reuse cycles, salinity corrodes equipment. Requires system replacement (capital loss).

### Improved Scenario
- Reuse only for non-critical uses (pre-rinse, cattle drinking, yard cleanup) — NOT milk cooling
- Model treatment cost as % of water saved; calculate break-even threshold
- Add water quality degradation loop; model culling point
- Include capital payback period in ROI

### Bottom Line
Margin-improvement strategy, not game-changer. Works as supplemental system, not primary water strategy.

---

## Scenario 2: Renewable Energy

### Current Weakness
Solar + wind as backup assumes you can add capacity without constraint. Wrong framing.

### Stress Factors
1. **Peak demand misalignment** — Milking 150+ cows = 4-6 hour peak (~30-50kW cooling). Happens 4-10am and 4-8pm. West Texas wind peaks 8pm-4am. Solar peaks noon-2pm. Grid-dependent during peak milking anyway.
2. **Battery cost prohibitive** — 4 hours × 50kW = 200kWh storage ≈ $200k+ lithium cost. At $0.15/kWh savings = $2,700/year. **Payback = 74 years.**
3. **Grid connection is sunk cost** — Even with renewables, you keep grid infrastructure. Real savings ≠ elimination; just peak load reduction.

### Improved Scenario
Model 3 strategies head-to-head:
1. **Grid baseline** (current state) — Cost reference
2. **Solar-dominant** (capital cost + grid backup) — Peak shaving, keeps grid
3. **Wind-dominant** (aligns with milking windows) — Requires larger wind farm or taller turbine

Include:
- Seasonal variation (summer cooling >> winter heating)
- Degradation curves (solar -0.5%/year, wind maintenance $2-5k/year after Year 5)
- ROI over 25-year equipment lifetime

### Bottom Line
Full renewable independence is capital-prohibitive. **Hybrid (wind + grid backup)** likely beats solar-only. Or: 100% grid cheaper than renewable capital cost.

---

## Scenario 3: Feed-to-Energy Conversion

### Current Weakness
"Ensure enough food for maintenance while maximizing milk production" — vague, assumes feed unlimited.

### Stress Factors
1. **Feed cost is largest variable expense** — Corn/hay prices swing 30-40% year-to-year. Drought year = low hay supply, high prices; forces culling or lower production.
2. **Milk production has biological limits** — Cows can't convert feed faster by willpower. Over-feeding → metabolic disease, lower fertility, higher vet costs. Conversion efficiency is a curve with diminishing returns (not linear).
3. **Water-feed coupling you're missing** — High-producing cows need more water. In drought (low reuse capacity), you can't increase production without more feed AND more water. These constraints interact.

### Improved Scenario
- Model feed-to-milk as a curve with diminishing returns
- Add cost axis: Total margin = (milk price × volume) - (feed cost + water cost + energy cost)
- Optimize for **profitable production**, not production volume
- Model drought stress explicitly: when water is scarce, production must drop
- Include seasonal variation: winter maintenance cost > summer (cold stress, lower grazing)

### Bottom Line
Feed optimization is margin optimization, not volume optimization. Profitability is the real objective.

---

## The Real Stress Test: Sequential Bottlenecks

```
Water Availability → Energy (treatment/cooling) → Feed Supply → Milk Production → Farm Profitability
```

**Under stress (drought + grid outage + feed price spike):**
1. Water reuse system fails (no input wastewater to treat)
2. Solar insufficient (outage at night; wind can't cover all demand)
3. Feed cost spikes (can't reduce herd without welfare/vet losses)
4. Milk production collapses (dehydrated cows produce less)
5. Farm goes insolvent (fixed costs, zero revenue)

### The Question Worth Modeling
**"Under a 1-in-10-year stress scenario, what's the minimum viable herd size that stays profitable?"**

Not: "How much can we produce optimally?"  
But: "What's the smallest operation that survives a crisis?"

---

## Recommendation for Your Paper

**Structure around resilience, not optimization:**

1. **Baseline:** Current state with realistic price/weather volatility (Monte Carlo)
2. **Scenarios:** Each intervention improves baseline
3. **Stress Test:** Drought + high prices + grid outage; see which scenarios survive
4. **Recommendation:** Best strategy likely combines:
   - Wastewater reuse (water security, non-cooling use only)
   - Wind energy (aligns with milking hours) + grid backup (not batteries)
   - Feed cost hedging (futures, diverse forage mix)

This frames your work as **risk management**, not cost reduction. That's what farms care about.

---

## Next Steps for Vensim

1. Add renewable energy inflows with time-of-day profile
2. Model peak demand separately from average demand
3. Add water quality degradation loop
4. Include seasonal variation for all three stocks
5. Stress test: run scenarios under drought + price spike conditions
6. Sensitivity analysis: which parameter changes break the model?
