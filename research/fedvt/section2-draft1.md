---
title: FEDVT Section 2 — Background and Literature Review (Draft 1)
type: research
status: draft
last-updated: 2026-04-13
tags: [fedvt, feedlot, background, literature-review, paper-section]
---

# 2. BACKGROUND AND LITERATURE REVIEW

The economic structure of commercial feedlot operations has been systematically
characterized over several decades of empirical research. Within the finishing stage, costs
divide into six principal categories — feeder cattle acquisition, feed inputs, labor, fixed
overhead, interest on operating capital, and other operating costs — with feeder cattle
purchase price typically accounting for 80–86% of total expenses and constituting the
dominant driver of enterprise risk (Lawrence, Wang, and Loy, 1999). Langemeier, Schroeder,
and Mintert (1992) established that just six variables — fed cattle sale price, feeder cattle
purchase price, corn price, interest rates, feed conversion ratio, and average daily gain —
explain approximately 98% of profit variability in commercial feedlot operations, with the
relative importance of each factor varying systematically by placement weight. More recent
analysis by Dennis and Schroeder (2023), using Kansas Focus on Feedlots closeout data
from January 2015 through December 2023, confirmed that this cost structure remains
broadly stable but is now exposed to compounding volatility: when feed prices rise, feedlots
substitute toward alternative feedstuffs, which simultaneously alters feed conversion ratios,
average daily gain, and days on feed, compressing margins from both the cost and
performance dimensions. Net returns over that period ranged from gains of $457 to losses
of $489 per head — a span that illustrates the financial exposure operators face within a
single production cycle and the importance of tools that can quantify sensitivity to each
driver individually.

A critical and frequently underappreciated dimension of feedlot price risk is the gap between
national futures markets and local cash market conditions. Bina and Schroeder (2022)
analyzed weekly auction transaction data from 32 feeder cattle markets across the United
States spanning 1992 to 2021, finding that feeder cattle market volatility exerts a
statistically and economically significant influence on basis risk. Basis variation is driven by
lot characteristics, seasonal timing, and regional market conditions, with the 2014–2015
cattle market disruption producing a historically elevated basis environment that had only
partially normalized by 2018. On the live cattle side, Coffey, Tonsor, and Schroeder (2018)
found that cost-of-gain volatility and delivery cost variation are larger contributors to hedging
difficulty than market-wide price trends, with basis prediction errors differing substantially
across the five major Mandatory Livestock Price Reporting regions. The joint implication of
these findings is that effective risk management in feedlot operations cannot be achieved by
consulting national futures prices alone. Tools grounded in an individual operation's own cost
structure — accounting for local procurement conditions, lot-specific characteristics, and
region-specific basis patterns — are necessary to translate market signals into operational
decisions. This requirement has direct implications for the design of FEDVT, which builds
break-even economics from the operation's own parameterized cost inputs rather than
applying industry-average assumptions.

Beyond price and cost volatility, feedlot operators face a distinct and partially
non-diversifiable economic risk in animal health, and specifically in bovine respiratory disease
(BRD), the leading cause of morbidity and mortality in commercial beef feedlots. BRD is a
polymicrobial syndrome involving viral and bacterial co-infection, most commonly triggered by
the physiological stress of weaning, transport, and commingling at placement. Karle, Toth,
and White (2017) used National Animal Health Monitoring System data to document that an
estimated 21.2% of cattle placed in U.S. feedlots are affected by respiratory disease
annually — approximately 2.29 million head — at a direct treatment cost of $23.60 per case,
with BRD accounting for approximately 45–55% of all feedlot deaths. Blakebrough-Hall,
McMeniman, and González (2020) quantified BRD's economic impact at the individual animal
level, tracking 898 crossbred steers through an Australian feedlot: cattle requiring three or
more treatments produced carcasses 39.6 kilograms lighter than untreated animals and
returned AUD $385 less per head at closeout, while animals with subclinical BRD — defined
by the presence of lung lesions at slaughter with no treatment history — lost AUD $67 per
head relative to healthy cohorts. Feuz, Feuz, and Johnson (2021) demonstrated that
machine-learning-based mortality prediction models can recover a meaningful share of these
losses: applying logistic regression and cost-sensitive ensemble approaches to data from
over 4,400 feedlot cattle, the study found that data-driven culling decisions improved average
net returns by $14.01 to $45.27 per head on previously treated animals, with less than 1%
probability of a net loss under the cost-sensitive specification. These findings collectively
establish BRD as both a quantifiable cost input and a decision variable that an enterprise-level
tool should be capable of modeling under alternative health-event assumptions.

Despite the depth of economic knowledge about feedlot cost drivers, risk sources, and
health costs, the decision support tools available to most operators have not kept pace with
the complexity of the environment they face. Herrington and Tonsor (2013), using the Kansas
Focus on Feedlots dataset spanning multiple decades, documented that average daily gain
and feed conversion efficiency improved substantially over time — reflecting advances in
genetics, nutrition, and animal husbandry — but that margin volatility did not decrease
correspondingly. The feedlot operating environment grew more complex while management
tools remained static. Bang, Laugen, and Dreyer (2023), in a systematic review of 110
decision support studies for beef and dairy farming published between 2016 and 2022,
confirmed that the gap between analytically sophisticated economic models and practically
adopted, user-friendly field tools has persisted as a structural problem in agricultural
decision-support research, with most tools never advancing beyond proof-of-concept
implementation. Awasthi et al. (2024), reviewing 105 simulation modeling studies in beef
production, found that fewer than half included formal validation procedures and that
inconsistent reporting standards were a primary barrier to reproducibility and practitioner
adoption. Dixon et al. (2022), in a scoping review of 113 feedlot cattle research trials from
91 peer-reviewed articles, found that only 28% fully reported economic outcomes,
methodology, price values, and data sources together; the review identified break-even
analysis and partial budgeting as the most practically relevant economic assessment
frameworks in feedlot research, yet these approaches have not been implemented in
interactive, dynamically recalculating, and visually accessible tools for practicing managers.

A smaller but growing body of work has begun demonstrating the practical value of
analytics-based approaches in feedlot decision support. Flores et al. (2017) used statistical
learning methods incorporating individual animal measurements — ultrasound backfat,
marbling scores, and feeding performance data — to predict optimal slaughter timing and
reduce unnecessary feed costs, showing that predictive models can meaningfully improve
marketing decisions even with limited data. Stika (2025) developed a simulation-based
mathematical programming model using real-world Kansas feedlot data and Python to
identify optimal placement weights and feeding durations, finding an optimal placement of
approximately 704 pounds with a 166-day feeding duration and confirming that feeder cattle
purchase price and feed cost dominate enterprise-level sensitivity results. Harrison (2022)
integrated mechanistic growth models with cost-and-profit curves derived from operational
feeding data, demonstrating that connecting biological performance trajectories to economic
outcomes enables individualized harvest timing decisions that reduce overfeeding costs and
improve carcass uniformity. Across these implementations, a consistent structural limitation
emerges: existing tools either operate at the individual-animal level rather than the enterprise
level, address a single decision variable in isolation, or require data infrastructure and
technical expertise that most commercial feedlot operators do not routinely maintain. The
gap that persists is an enterprise-level, fully parameterized, and interactively visualized
break-even tool that integrates the complete operational cost structure documented in the
literature, connects to live market price data, and enables real-time scenario analysis across
the range of cost and performance variables that jointly determine feedlot profitability.
FEDVT is developed to address this gap.

---

## Sources Used in This Section (in order of appearance)

1. Lawrence, Wang & Loy (1999) — 80–86% feeder cost dominance, parameter breadth
2. Langemeier, Schroeder & Mintert (1992) — 98% variability, 6 variables
3. Dennis & Schroeder (2023) — substitution effects, +$457/-$489 range
4. Bina & Schroeder (2022) — feeder cattle basis risk, local conditions
5. Coffey, Tonsor & Schroeder (2018) — live cattle hedging, cost-of-gain volatility
6. Karle, Toth & White (2017) — BRD 21.2% morbidity, $23.60/case
7. Blakebrough-Hall, McMeniman & González (2020) — AUD $385/head (⚠️ figures are AUD)
8. Feuz, Feuz & Johnson (2021) — ML mortality prediction, $14–$45/head improvement
9. Herrington & Tonsor (2013) — complexity grew, tools didn't
10. Bang, Laugen & Dreyer (2023) — 110 DSS studies, adoption gap
11. Awasthi et al. (2024) — 105 simulation studies, <50% validated
12. Dixon et al. (2022) — 28% full reporting, break-even as best practice
13. Flores et al. (2017) — analytics DSS, individual animal level
14. Stika (2025) — simulation, optimal 704 lbs / 166 days
15. Harrison (2022) — growth models + cost curves

## Links
- [[introduction-v3]] — Section 1
- [[literature-index]] — full source index with section placements
- [[paper-outline]] — full paper structure
