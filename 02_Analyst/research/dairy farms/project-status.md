---
title: Dairy Farms Project Status
project: dairy-farms-research
status: active
origin_dump: null
last_synced_dump: null
last_updated: 2026-05-21
tags: [dairy, wef-nexus, system-dynamics, vensim, sustainability]
scope: dairy-farms/project-status
---

# Dairy Farms Research — Project Status

## Current Phase
Scenario stress analysis + resilience modeling. Moving from optimization-focused to risk-focused framing.

## What We Know (From Vault)

### Three Scenario Pillars
**1. Wastewater Reuse**
- Non-drinking water (~32%) is recyclable
- Current Vensim model: one-way flow (water → wastewater → discharge)
- Proposed: Add feedback loop (fraction of treated wastewater → Water Storage)
- **Problem:** Treatment cost, mineral buildup, milk cooling inelasticity

**2. Renewable Energy**
- Solar misalignment: milking at sunrise/sunset (peak cow demand ≠ peak solar output)
- Milk cooling requires immediate energy (most energy-intensive process)
- Options: batteries (expensive), wind (better alignment), grid backup
- **Problem:** Peak demand misalignment, battery cost (74-year payback), grid dependency inevitable

**3. Feed-to-Energy Conversion**
- Critical relationship: feed input → milk production
- Goal: Ensure maintenance feed while maximizing production
- **Problem:** Non-linear conversion, seasonal variation, water-feed coupling ignored

## Strategic Shift
**From:** Independent scenario optimization  
**To:** Resilience framework (what breaks under stress?)

### The Real Stress Test
Under 1-in-10-year scenario (drought + high feed prices + grid outage):
- Water reuse fails (no wastewater input)
- Solar insufficient (outage at night)
- Feed costs spike
- Production collapses

**Question to model:** Which constraint kills the farm first?

## Immediate Next Steps

1. **Vensim Modeling**
   - Add renewable energy inflows (solar, wind, grid) to model
   - Model peak demand profile (not average)
   - Add water quality degradation (reuse cycles)
   - Add seasonal variation (feed + energy + water)

2. **Scenario Refinement**
   - Model 3 strategies head-to-head (grid baseline vs. solar vs. wind)
   - Include capital payback analysis for each
   - Stress test each scenario under drought/price spike

3. **Weekly Reports**
   - Document findings + assumptions
   - Track model iterations
   - Surface key constraints

4. **Research Papers** (2 due end of semester)
   - Paper 1: Resilience framework for dairy operations
   - Paper 2: WEF nexus optimization (water reuse + renewable energy + feed efficiency)

## Data Gaps

- Actual herd size (for Vensim baseline)
- Current water/energy/feed costs (for ROI analysis)
- Seasonal demand profile (for peak demand modeling)
- Grid electricity pricing structure (for renewable comparison)

## Collaborators
- **Economics Team:** Aarav Pulsani (leading cost analysis)
- **System Dynamics Team:** Multiple students on Vensim modeling
- **Machine Learning Team:** Data-driven insights (TBD integration)

---

## Notes from /save Synthesis (2026-04-16)

This project was discussed in conversation but not yet documented in vault. Initial insights:
- Three scenarios are sequential bottlenecks (not independent)
- Resilience > optimization should drive framing
- Stress scenario reveals which constraint actually binds
- Research papers should position work as risk management, not cost reduction
