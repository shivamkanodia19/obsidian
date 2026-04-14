---
title: FEDVT Introduction — Version 3 (Merged & Corrected)
type: research
status: draft
last-updated: 2026-04-13
source: merged from Draft 1 + Draft 2, corrected against literature-index
tags: [fedvt, feedlot, introduction, paper-section]
---

# 1. INTRODUCTION

Beef cattle production is one of the most economically significant agricultural enterprises in
the United States, generating approximately $112.1 billion in cash receipts in 2024 and
maintaining an inventory of approximately 11.8 million head of cattle on feed in commercial
feedlots at any given time (USDA, 2025). The feedlot finishing stage represents the most
capital-intensive phase of the beef supply chain, characterized by a 150- to 240-day
production cycle during which operators commit substantial capital to feeder cattle acquisition,
feed inputs, labor, fixed overhead, and interest expenses before receiving any revenue at
closeout. Profitability in this environment is exceptionally volatile: longitudinal analysis of
Kansas feedlot closeout data documented net returns swinging from gains of $457 to losses
exceeding $489 per head within a single production period (Dennis and Schroeder, 2023).
Foundational research by Langemeier, Schroeder, and Mintert (1992) established that
approximately 98% of this profit variability is attributable to just six variables — fed cattle
sale price, feeder cattle purchase price, corn price, interest rates, feed conversion ratio, and
average daily gain — confirming both the structural predictability of feedlot cost drivers and the
severe practical difficulty of managing them simultaneously under real market conditions.

Despite this well-documented cost structure, the decision-support tools available to most
feedlot operators have not kept pace with the operational complexity they face. The dominant
instruments in practice remain static enterprise budgets and fixed-parameter spreadsheet
calculators that require manual recalculation under each new price or cost scenario, present
outputs as tables of undifferentiated numbers, and offer no mechanism for real-time what-if
analysis. These tools cannot dynamically update as market conditions shift, fail to visually
communicate the relative sensitivity of margins to individual cost drivers, and demand a level
of spreadsheet proficiency that many producers lack. A systematic review of 110 published
decision-support studies for beef and dairy farming by Bang, Laugen, and Dreyer (2023) found
that the gap between academically sophisticated economic models and practically adopted,
user-friendly field tools has persisted as a structural problem in agricultural decision-support
research. Awasthi et al. (2024), reviewing 105 simulation modeling studies in the beef
production sector, similarly found that fewer than half included formal validation procedures
and that inconsistent reporting standards were a persistent barrier to practitioner adoption.
The problem is not a shortage of economic knowledge about feedlot profitability. The problem
is that this knowledge has not been translated into tools that operators can actually use at the
point of decision.

Advances in spreadsheet programming and data visualization software have created practical
pathways to address this gap. Platforms such as Microsoft Excel with Visual Basic for
Applications (VBA) and Tableau now support the construction of interactive dashboards that
recalculate complex multi-variable models in real time as users modify inputs, display results
graphically rather than numerically, and enable scenario comparison across a range of market
and cost assumptions. These capabilities have been demonstrated productively in agricultural
decision-support contexts: Flores et al. (2017) showed that analytics-based tools built on
statistical learning frameworks could meaningfully improve feedlot management decisions
around marketing timing and slaughter scheduling, and Stika (2025) demonstrated that a
Python-based simulation framework using a conventional feedlot variable cost structure could
identify optimal placement weights and feeding durations under varying market conditions.
What has been missing is a validated, interactive, and visually accessible implementation of
feedlot break-even economics that is grounded in the full operational cost structure of a
commercial feedlot, integrates live cattle market price data, and can be deployed by a
practicing manager without specialized modeling expertise.

The objective of this study is to develop and validate the Feedlot Economic Decision and
Valuation Tool (FEDVT), an integrated decision-support system designed to help feedlot
operators evaluate the economic viability of cattle placements across a range of operational
and market conditions. Grounded in the multi-parameter frameworks established by Lawrence,
Wang, and Loy (1999) and Mark, Schroeder, and Jones (2000), FEDVT employs a
dual-platform architecture: a Microsoft Excel and VBA computational engine that models 65
operational input parameters across six cost categories — feed costs, feeder cattle costs,
fixed costs, labor costs, interest costs, and other operating costs — paired with a
Tableau-based visualization layer. Unlike static calculators, FEDVT integrates a live data
pipeline linking CME Live Cattle futures prices to compute break-even prices and projected
margins in real time, enabling operators to observe how changes in feeder purchase price,
feed cost, days on feed, placement weight, or finishing price individually and jointly affect their
economic position. The contribution of this work is twofold: it provides a methodologically
grounded, validated implementation of feedlot break-even economics grounded in established
cost accounting literature, and it demonstrates the utility of interactive visualization in
communicating complex economic sensitivities to non-specialist stakeholders — closing the gap
between academic economic knowledge and on-farm decision-making capability.

The remainder of this paper is organized as follows. Section 2 reviews the relevant literature
on feedlot economics, existing decision-support tools, and the rationale for a
visualization-based approach. Section 3 describes the materials and methods underlying
FEDVT's development, including the economic variables modeled, the tool's architecture and
design process, and the validation approach. Section 4 presents results through a series of
scenario demonstrations, including a base-case profitability analysis, high feed-cost conditions,
a disease-outbreak scenario, and a sensitivity analysis. Section 5 discusses practical
implications for feedlot managers, veterinary stakeholders, and investors, addresses tool
limitations, and outlines pathways for future integration with real-time data sources and
precision livestock technologies. Section 6 summarizes the study's contributions and directions
for continued development.

---

## Change Log (v3 vs prior drafts)

### Corrections
- **Dennis & Schroeder figures**: Changed to +$457 / -$489 (confirmed by literature summary).
  Draft 1 had "$450 / $480" — WRONG. Draft 2 had correct figures.
- **Tool name**: "Feedlot Economic Decision and **Valuation** Tool (FEDVT)" — confirmed by
  research-tracker.md. Draft 1 used "Visualization" incorrectly.
- **USDA cattle on feed**: Updated to ~11.8M (USDA monthly data 2024 range: 11.6–12.0M).
  ⚠️ Verify against the specific USDA 2025 Cattle on Feed report before submitting.

### Structure
- Kept Draft 1's clean 5-paragraph flow and its strong "not a shortage of knowledge" closing line
- Kept Draft 2's twofold contribution framing and Lawrence/Mark grounding
- Moved Bina & Schroeder 2022, Tonsor & Schroeder 2011, Karle 2017, Blakebrough-Hall 2020,
  Coffey 2018, Dixon 2022 OUT of the intro — they belong in Section 2 per literature-index.md

### Citations in this intro (8 sources)
1. USDA (2025)
2. Dennis & Schroeder (2023)
3. Langemeier, Schroeder & Mintert (1992)
4. Bang, Laugen & Dreyer (2023)
5. Awasthi et al. (2024)
6. Flores et al. (2017)
7. Stika (2025)
8. Lawrence, Wang & Loy (1999)
9. Mark, Schroeder & Jones (2000)
