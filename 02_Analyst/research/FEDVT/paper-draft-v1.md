# FEDVT Paper Draft v1

**Status:** Introduction + Section 2 (Background/Lit Review) complete  
**Date:** 2026-04-14  
**Sections Completed:** 1-2  
**Sections Remaining:** 3-6 + Abstract

## INTRODUCTION

Beef cattle production is one of the most economically significant agricultural enterprises in the United States, generating approximately $112.1 billion in cash receipts in 2024 and maintaining an inventory of approximately 11.8 million head of cattle on feed in commercial feedlots at any given time (USDA, 2025). The feedlot finishing stage is the most capital-intensive phase of the beef supply chain, characterized by a 150- to 240-day production cycle during which operators commit substantial capital to feeder cattle acquisition, feed inputs, labor, fixed overhead, and interest expenses before receiving any revenue from sales.

Profitability in this environment is exceptionally volatile: a longitudinal analysis of Kansas feedlot closeout data documented net returns that swung from gains of $457 to losses exceeding $489 per head within a single production period (Dennis and Schroeder, 2023). Foundational research by Langemeier, Schroeder, and Mintert (1992) established that approximately 98% of this profit variability is attributable to just six variables — fed cattle sale price, feeder cattle purchase price, corn price, interest rates, feed conversion ratio, and average daily gain.

Despite this well-documented cost structure, the decision-support tools available to most feedlot operators have not kept pace with the operational complexity they face. The dominant instruments in practice remain static enterprise budgets and fixed-parameter spreadsheet calculators. These tools cannot dynamically update as market conditions shift, fail to visually communicate the relative sensitivity of margins to individual cost drivers, and demand a level of spreadsheet proficiency that many producers lack.

Advances in spreadsheet programming and data visualization software have created practical pathways to address this gap. The objective of this study is to develop and validate the Feedlot Economic Decision and Valuation Tool (FEDVT), an integrated decision-support system designed to help feedlot operators evaluate the economic viability of cattle placements across a range of operational and market conditions.

## BACKGROUND AND LITERATURE REVIEW

The economic structure of commercial feedlot operations has been systematically characterized over several decades of empirical research. Within the finishing stage, costs divide into six principal categories — feeder cattle acquisition, feed inputs, labor, fixed overhead, interest on operating capital, and other operating costs — with feeder cattle purchase price typically accounting for 80–86% of total expenses.

Langemeier, Schroeder, and Mintert (1992) established that just six variables explain approximately 98% of profit variability in commercial feedlot operations. More recent analysis by Dennis and Schroeder (2023), using Kansas Focus on Feedlots closeout data from January 2015 through December 2023, confirmed that this cost structure remains broadly stable but is now exposed to compounding volatility.

A critical and frequently underappreciated dimension of feedlot price risk is the gap between national futures markets and local cash market conditions. Bina and Schroeder (2022) analyzed weekly auction transaction data from 32 feeder cattle markets across the United States, spanning 1992 to 2021, and found that volatility in feeder cattle markets exerts a statistically and economically significant influence on basis risk.

Beyond price and cost volatility, feedlot operators face a distinct and partially non-diversifiable economic risk in animal health, and specifically in bovine respiratory disease (BRD), the leading cause of morbidity and mortality in commercial beef feedlots. Karle, Toth, and White (2017) documented that an estimated 21.2% of cattle placed in U.S. feedlots are affected by respiratory disease annually, at a direct treatment cost of $23.60 per case.

Despite the depth of economic knowledge of feedlot cost drivers, the decision-support tools available to most operators have not kept pace with the complexity of the environment they face. Bang, Laugen, and Dreyer (2023), in a systematic review of 110 decision support studies for beef and dairy farming, confirmed that the gap between analytically sophisticated economic models and practically adopted, user-friendly field tools has persisted as a structural problem.

A smaller but growing body of work has begun demonstrating the practical value of analytics-based approaches in feedlot decision support. Flores et al. (2017) used statistical learning methods to predict optimal slaughter timing. Stika (2025) developed a simulation-based mathematical programming model to identify optimal placement weights and feeding durations. The gap that persists is an enterprise-level, fully parameterized, and interactively visualized break-even tool that integrates the complete operational cost structure, connects to live market price data, and enables real-time scenario analysis.

---

## NOTES FOR NEXT SECTIONS

- **Section 3 (Materials & Methods):** Describe Excel/Tableau architecture, 65 parameters across 6 cost categories, validation approach
- **Section 4 (Results):** Use-case scenarios (base case, high feed cost, disease outbreak, sensitivity analysis)
- **Section 5 (Discussion):** Stakeholder utility, limitations, IoT/ML integration potential
- **Section 6 (Conclusion):** Summary and future work directions
