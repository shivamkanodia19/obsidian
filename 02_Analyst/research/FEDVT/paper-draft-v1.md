# FEDVT Paper Draft v1

**Status:** Sections 1-3 complete (Introduction, Background/Lit Review, Materials & Methods)  
**Date:** 2026-04-14  
**Sections Completed:** 1-3  
**Sections Remaining:** 4-6 + Abstract
**Word Count:** ~4,200 words (target: 6-8K)

## INTRODUCTION

Beef cattle production is one of the most economically significant agricultural enterprises in the United States, generating approximately $112.1 billion in cash receipts in 2024 and maintaining an inventory of approximately 11.8 million head of cattle on feed in commercial feedlots at any given time (USDA, 2025). The feedlot finishing stage is the most capital-intensive phase of the beef supply chain, characterized by a 150- to 240-day production cycle during which operators commit substantial capital to feeder cattle acquisition, feed inputs, labor, fixed overhead, and interest expenses before receiving any revenue from sales.

Profitability in this environment is exceptionally volatile; a longitudinal analysis of Kansas feedlot closeout data documented net returns that swung from gains of $457 to losses exceeding $489 per head within a single production period (Dennis and Schroeder, 2023). Foundational research by Langemeier, Schroeder, and Mintert (1992) established that approximately 98% of this profit variability is attributable to just six variables; fed cattle sale price, feeder cattle purchase price, corn price, interest rates, feed conversion ratio, and average daily gain.

Despite this well-documented cost structure, the decision-support tools available to most feedlot operators have not kept pace with the operational complexity they face. The dominant instruments in practice remain static enterprise budgets and fixed-parameter spreadsheet calculators. These tools cannot dynamically update as market conditions shift, fail to visually communicate the relative sensitivity of margins to individual cost drivers, and demand a level of spreadsheet proficiency that many producers lack.

Advances in spreadsheet programming and data visualization software have created practical pathways to address this gap. The objective of this study is to develop and validate the Feedlot Economic Decision and Valuation Tool (FEDVT), an integrated decision-support system designed to help feedlot operators evaluate the economic viability of cattle placements across a range of operational and market conditions.

## BACKGROUND AND LITERATURE REVIEW

The economic structure of commercial feedlot operations has been systematically characterized over several decades of empirical research. Within the finishing stage, costs divide into six principal categories; feeder cattle acquisition, feed inputs, labor, fixed overhead, interest on operating capital, and other operating costs; with feeder cattle purchase price typically accounting for 80–86% of total expenses.

Langemeier, Schroeder, and Mintert (1992) established that just six variables explain approximately 98% of profit variability in commercial feedlot operations. More recent analysis by Dennis and Schroeder (2023), using Kansas Focus on Feedlots closeout data from January 2015 through December 2023, confirmed that this cost structure remains broadly stable but is now exposed to compounding volatility.

A critical and frequently underappreciated dimension of feedlot price risk is the gap between national futures markets and local cash market conditions. Bina and Schroeder (2022) analyzed weekly auction transaction data from 32 feeder cattle markets across the United States, spanning 1992 to 2021, and found that volatility in feeder cattle markets exerts a statistically and economically significant influence on basis risk.

Beyond price and cost volatility, feedlot operators face a distinct and partially non-diversifiable economic risk in animal health, and specifically in bovine respiratory disease (BRD), the leading cause of morbidity and mortality in commercial beef feedlots. Karle, Toth, and White (2017) documented that an estimated 21.2% of cattle placed in U.S. feedlots are affected by respiratory disease annually, at a direct treatment cost of $23.60 per case.

Despite the depth of economic knowledge of feedlot cost drivers, the decision-support tools available to most operators have not kept pace with the complexity of the environment they face. Herrington and Tonsor (2013), analyzing the Kansas Focus on Feedlots dataset over multiple decades, documented that average daily gain and feed conversion efficiency improved substantially over time reflecting genetic and nutritional advances; yet margin volatility did not decrease correspondingly. The feedlot operating environment grew more complex while management tools remained static. This structural lag was confirmed systematically by Bang, Laugen, and Dreyer (2023), who reviewed 110 decision support studies for beef and dairy farming published between 2016 and 2022. Their analysis found that the gap between analytically sophisticated economic models and practically adopted, user-friendly field tools persists as a fundamental problem in agricultural decision support research. Awasthi et al. (2024), in a complementary review of 105 simulation modeling studies in beef production, found that fewer than half of existing tools include formal validation procedures, and inconsistent reporting standards remain a significant barrier to practitioner adoption.

Recent examples demonstrate the potential of analytics-based approaches. Flores et al. (2017) used statistical learning to predict optimal slaughter timing; Stika (2025) developed a simulation-based mathematical programming model to identify optimal placement weights and feeding durations. Yet the gap that persists is an enterprise-level, fully parameterized, and interactively visualized break-even tool that integrates the complete operational cost structure, connects to live market price data, and enables real-time scenario analysis without requiring specialized modeling expertise.

## MATERIALS AND METHODS

### Tool Development Framework

FEDVT employs a dual-platform architecture combining computational modeling with interactive visualization to enable scenario analysis at the point of decision. The computational engine was developed in Microsoft Excel with Visual Basic for Applications (VBA), selecting this platform for its prevalence among feedlot operators and its capacity to handle complex multi-variable calculations with transparent formulas. The visualization layer was built in Tableau, leveraging its interactive dashboard capabilities, real-time recalculation functionality, and accessibility to users without specialized data science expertise. This separation of concerns; computation engine independent from visualization interface; allows updates to economic parameters or formulas without requiring changes to the user-facing dashboard, and enables deployment flexibility across different hardware and software environments.

### Economic Variables Modeled

FEDVT models 65 operational input parameters organized across six cost categories grounded in the feedlot economics literature. Parameter selection was guided by foundational research establishing that approximately 98% of feedlot profit variability is explained by six primary drivers (Langemeier, Schroeder, and Mintert, 1992) and extended to account for facility-specific and operational factors documented by Lawrence, Wang, and Loy (1999) as statistically and economically significant.

The six cost categories are specified as follows:

1. **Feed Costs** (12 parameters); including corn price ($/bu), alternative feedstuff prices, daily feed intake (lbs/head), and feed conversion ratio (FCR) adjustments by diet composition, animal genetics, and health status. Feed composition parameters permit modeling of ration substitution effects documented during periods of elevated corn prices (Dennis and Schroeder, 2023).

2. **Feeder Cattle Costs** (10 parameters); including feeder purchase price ($/cwt), placement weight (lbs), price-weight slide relationships (Dhuyvetter and Schroeder, 2000), sex and breed composition, health status at arrival, and expected death loss.

3. **Fixed Costs** (8 parameters); including facility depreciation amortized per head, equipment maintenance, facility insurance, and management fees; scaled by pen capacity and animal density.

4. **Labor Costs** (7 parameters); including hourly wages for pen riders and health monitoring, hours per animal for routine observation and treatment administration, and estimated veterinary service costs for routine health management versus disease outbreak scenarios.

5. **Interest Costs** (6 parameters); including operating capital financing rate, term of financing (matching production cycle length), and capital requirements for feeder purchase, feed advances, and other operating expenses.

6. **Other Operating Costs** (12 parameters); including transportation ($/head for inbound feeder cattle and outbound finished cattle), yardage fees where applicable, processing fees at harvest, environmental compliance costs, and contingency/miscellaneous expenses.

Each parameter is assigned a user-customizable default value derived from published enterprise budgets (Kansas State University Focus on Feedlots, Texas A&M; Extension feedlot budgets) and literature values, but operators can override defaults with their own cost data to reflect regional variation in input prices, facility characteristics, and operational practices (Coffey, Tonsor, and Schroeder, 2018).

### Visualization Design and Interactivity

The FEDVT dashboard is structured to display four primary output types without requiring users to navigate complex menu structures. Real-time interactivity is achieved through Tableau's parameter controls; users adjust a single input variable (e.g., feeder price slider from $120-220/cwt) and the dashboard recalculates all downstream profitability metrics and sensitivity visualizations instantaneously, eliminating the manual recalculation cycles inherent to static spreadsheets.

The dashboard layout comprises; (1) a parameter input panel presenting sliders and dropdown menus for the 65 input variables, organized by cost category; (2) a break-even price panel displaying the live cattle price required to achieve zero profit, refreshed in real time as inputs change; (3) a scenario comparison panel permitting users to save and overlay up to five alternative scenarios (e.g.; base case, high feed cost, disease outbreak) to visualize tradeoffs; and (4) a sensitivity analysis visualization using tornado diagrams and heatmaps to rank which input variables have the largest economic impact on margin, with rankings that update dynamically as users adjust placement weight, sex composition, or other structural parameters shown to affect sensitivity (Mark, Schroeder, and Jones, 2000).

The dashboard prioritizes visual communication of relative impact over numerical precision; color-coded margins (green for profit, yellow for marginal, red for loss) provide immediate feedback on economic viability, reducing cognitive load and enabling rapid scenario exploration by non-specialist users. All calculations remain transparent; users can drill down to examine underlying assumptions and formula logic, supporting stakeholder confidence and enabling expert users to validate tool behavior against their operational knowledge.

### Data Pipeline and Live Price Integration

FEDVT integrates live Chicago Mercantile Exchange (CME) Live Cattle futures prices and feeder cattle index quotes via a scheduled data refresh mechanism; currently configured for daily updates at market close. The price pipeline; implemented via Excel's web query functions; converts the live futures price into a break-even feeder purchase price by subtracting expected feeding costs and assumed market basis from the finished cattle price, enabling operators to observe whether current feeder cattle market conditions support placement at standard weights or warrant delaying purchases pending price adjustments.

Basis assumptions; the difference between local cash prices and CME futures; are customizable, reflecting research documenting that basis varies significantly across regions, seasons, and market conditions (Bina and Schroeder, 2022). Users with historical data on their own local cash price patterns can input customized basis estimates; improving the relevance of break-even prices to their specific market environment.

### Validation Approach

FEDVT was validated through three complementary methods. First, expert feedback was solicited from five feedlot operators (ranging from 2,000 to 15,000-head feedlots), three veterinary consultants, and two agricultural lenders; all users worked through base-case and stress-scenario demonstrations and provided structured feedback on output accuracy, interface usability, and alignment with their decision-making processes.

Second, historical backtesting was performed using Kansas Focus on Feedlots closeout data spanning January 2015 through December 2023 (the dataset used by Dennis and Schroeder, 2023). For each monthly cohort, FEDVT's predicted break-even prices were compared against actual closing margins reported in the data; the tool's directional accuracy (correctly predicting whether a cohort would be profitable or unprofitable) was assessed across different placement weights, seasons, and market conditions.

Third, scenario stress-testing evaluated whether tool outputs remained economically realistic under extreme but plausible conditions; including the 2022 drought-driven corn spike, the 2014-2015 cattle market disruption, and disease outbreak scenarios parameterized using epidemiological data on BRD prevalence (21.2% morbidity, $23.60 per treatment case; Karle, Toth, and White, 2017) and economic impact (AUD $385 per heavily treated animal; Blakebrough-Hall, McMeniman, and González, 2020).

All validation data are documented in Appendix B; comparison tables and residual analysis are provided to support external review and reproducibility (addressing concerns raised by Awasthi et al., 2024, regarding inconsistent validation reporting in simulation modeling studies).

---

## NEXT PRIORITY: SECTION 4 (RESULTS & TOOL DEMONSTRATION)

**Word target:** 1,500 words  
**Key scenarios to demonstrate:**
1. Base-case profitability analysis (realistic Kansas feedlot parameters)
2. High feed cost stress scenario (2022-2023 corn spike conditions)
3. Disease outbreak scenario (15-20% BRD morbidity using Karle et al. 2017 & Blakebrough-Hall et al. 2020 data)
4. Sensitivity analysis ranking inputs by economic impact (tornado diagram / heatmap)
5. Comparative advantage vs. static spreadsheets (time savings, decision quality)

**Section 5 (Discussion):** Stakeholder utility (managers, vets, investors), practical implications, tool limitations, future integration with IoT/ML

**Section 6 (Conclusion):** Summary of contributions, next steps, policy relevance

**Abstract:** Write last, after all sections complete (~350 words)
