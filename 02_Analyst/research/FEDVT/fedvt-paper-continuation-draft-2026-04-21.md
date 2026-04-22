# FEDVT Paper Continuation Draft

Use this after the current Introduction and Background/Literature Review. This draft includes a manuscript-ready Abstract, Sections 3-6, working figure captions, working references, and a final gap checklist.

Draft integrity note: The vault contains two different versions of the empirical story. The prose draft describes a commercial finishing scenario based on 704-lb placements, 1,200-lb finished cattle, and CME Live Cattle integration. The actual workbook currently visible in `01_Source/research/fedvt/Feedlot Economics_Updated_VBA.xlsm` uses a 1,000-head, 600-to-850 lb prototype budget and contains no visible external CME/web query connection. The paper below is written to be defensible by treating the workbook as the current FEDVT prototype and the live market connection as a designed integration pathway unless final evidence is added.

## ABSTRACT

Profitability in commercial cattle feeding is highly volatile because feedlot managers must commit capital to feeder cattle, feed, labor, health, fixed overhead, and interest before realizing finished cattle revenue. Prior research has shown that most variation in feedlot returns is explained by a small set of interacting price and performance variables, yet the tools available to many operators remain static enterprise budgets or spreadsheet calculators that require manual recalculation and provide limited visual support for scenario analysis. This study develops the Feedlot Economic Decision and Valuation Tool (FEDVT), an interactive decision-support prototype designed to translate established feedlot break-even economics into a user-facing scenario analysis environment. FEDVT uses a Microsoft Excel and VBA computational engine linked to visualization-ready output tables and dashboards. The model parameterizes a feedlot production budget across feeder cattle acquisition, feed, fixed costs, labor, operating costs, animal health, and interest, and reports cost per head, cost per pound of gain, break-even selling price, break-even purchase price, and projected margin. We demonstrate the tool using a 1,000-head prototype budget and stress-test profitability under base-case, elevated feed-cost, and disease-risk assumptions. The base workbook scenario places 600-lb feeder cattle at $304/cwt and markets 850-lb cattle at $277/cwt, producing total cost of $2,124.96/head, gross revenue of $2,307.41/head, projected margin of $182.45/head, and a break-even selling price of $255.10/cwt. Scenario demonstrations show that feeder cattle price remains the dominant economic driver, while feed-cost and health shocks become more consequential under stressed operating conditions. FEDVT contributes a transparent, parameterized, and visually interpretable implementation of feedlot break-even economics that addresses the adoption gap identified in agricultural decision-support literature. The tool is not intended to replace managerial judgment or stochastic price forecasting, but to make the economic consequences of placement, feeding, health, and market assumptions visible at the point of decision.

## 3. MATERIALS AND METHODS

### 3.1 Tool Development Framework

FEDVT was developed as a deterministic, parameterized decision-support prototype for feedlot economic analysis. The tool converts a static feedlot finishing production-cost budget into a recalculating model that can be used to evaluate placement, feeding, price, and health scenarios. The current workbook architecture contains ten primary worksheets: Input, Details, Breakeven Analysis, Summary, Tables, Pivot Tables, Production, Income, Operations, and Investment. This structure separates assumptions from intermediate calculations and final outputs. The Input and Investment worksheets collect user-controllable assumptions; Details performs line-item cost calculations; Summary aggregates costs and revenue; Breakeven Analysis reports break-even selling and purchase prices; and Tables/Pivot Tables reshape model outputs for visualization.

The design logic follows the decision-support gap documented by Bang, Laugen, and Dreyer (2023) and Awasthi et al. (2024): economic models are most useful to practitioners when the assumptions are transparent, the outputs are interpretable, and the model can be adapted to operation-specific conditions. Excel and VBA were selected for the computational layer because spreadsheet workflows remain familiar to agricultural managers and extension economists, while the dashboard layer is intended to translate the workbook's output tables into visual summaries for non-specialist users. The prototype therefore prioritizes auditability and adoption over model complexity. Users can inspect formulas, adjust assumptions, and immediately see changes propagate through break-even and margin outputs.

### 3.2 Economic Variables and Parameterization

FEDVT organizes feedlot economics into the cost categories most consistently identified in the feedlot profitability literature: feeder cattle acquisition, feed inputs, other operating expenses, labor, fixed costs, and interest on operating capital. This structure is consistent with Lawrence, Wang, and Loy (1999), who documented the importance of biological, facility, and placement characteristics beyond market price alone, and with Langemeier, Schroeder, and Mintert (1992), who found that profit variability is primarily driven by fed cattle price, feeder cattle price, corn price, interest rate, feed conversion, and average daily gain.

The current prototype parameterizes herd profile assumptions including number of cattle placed, placement weight, finished weight, feeder mortality rate, shrink, average daily gain, days on feed, purchase price, selling price, and livestock risk-protection premium. Feed costs are modeled by ingredient, unit price, daily requirement, and feeding duration. The workbook currently includes rolled barley, corn silage, hay, supplement, other feed, and salt/mineral supplement lines. Other operating costs include buying commission, insurance, trucking, straw, veterinary medicine and supplies, professional services, fuel and repair, utilities, marketing and transportation, manure removal, barn and office supplies, death loss, and operating interest. Fixed costs are represented through buildings, corrals, water systems, machinery, equipment, salvage value, useful life, and depreciation. Labor is included as a separate production cost so users can evaluate scenarios in which labor availability or wages shift independently from feed and market prices.

The prototype's base workbook assumes 1,000 feeder cattle, a 600-lb placement weight, an 850-lb sale weight, 2% finished shrink, 2.5 lb/day average daily gain, and 100 days on feed. The base purchase price is $304/cwt and the base selling price is $277/cwt. These values reflect the current state of the workbook and should be replaced by study-specific Kansas, Texas Panhandle, or national assumptions if the final manuscript is framed as a commercial fed-cattle finishing tool. The model is designed so these assumptions can be changed without changing formulas, allowing the same architecture to represent different placement weights, feeding periods, and market environments.

### 3.3 Break-Even and Margin Calculations

FEDVT computes profitability through a set of linked enterprise-budget equations. Total cost per head is calculated as:

Total cost per head = feeder cattle cost + feed cost + other operating cost + labor cost + fixed cost + operating interest.

Gross revenue per head is calculated as:

Gross revenue per head = finished sale weight after shrink x finished selling price.

Projected margin per head is then:

Projected margin per head = gross revenue per head - total cost per head.

The break-even selling price is the finished cattle price required to cover all production costs:

Break-even selling price ($/cwt) = total cost per head / finished sale weight after shrink x 100.

The break-even purchase price is the maximum feeder cattle purchase price that can be paid while covering non-feeder costs at an assumed sale price:

Break-even purchase price ($/cwt) = (gross revenue per head - non-feeder costs per head) / placement weight x 100.

The workbook also reports cost per pound of gain sold, feed cost per pound of gain, total operating cost per pound of gain, and total cost per pound of gain. These metrics are useful because they allow comparisons across placements that differ in entry weight, sale weight, and feeding duration. A 600-to-850 lb feeding period and a 700-to-1,250 lb finishing period can therefore be compared on a per-head, per-cwt, and per-pound-of-gain basis.

### 3.4 Visualization and Dashboard Design

The visualization layer is built around the principle that the model should communicate economic structure before it communicates numerical detail. Rather than presenting only a final profit or loss value, FEDVT decomposes total cost into its component drivers and lets users compare scenarios side by side. The dashboard design is organized around four views.

First, the input view groups assumptions by decision domain: cattle placement, feed, animal health, operating costs, fixed costs, labor, and market price. Second, the cost distribution view shows how total cost per head is allocated across feeder cattle, feed, operating, labor, fixed, and interest categories. Third, the break-even view displays the selling price required to cover total costs and the feeder purchase price that would be justified by the current output market. Fourth, the scenario and sensitivity view compares base-case and stress-case assumptions using bar charts, tornado charts, and heatmaps.

This design directly addresses a limitation of static enterprise budgets. In a static budget, a user can compute a single scenario accurately, but must manually duplicate or rebuild sheets to compare several conditions. FEDVT's structure allows scenario comparison to be treated as the default workflow. Operators can ask how a higher feeder price, feed-cost shock, lower average daily gain, longer feeding period, or disease event changes the economic position, and they can see whether the effect is large enough to change a placement or marketing decision.

### 3.5 Market Data Integration

The final FEDVT architecture is designed to accept live or regularly refreshed cattle market prices as input variables. In the current prototype, market prices are entered directly in the Input and Investment worksheets, and the break-even outputs update from those inputs. The intended data pipeline connects futures or cash-market prices to the same input cells so that break-even position can be updated without manual price entry. Basis adjustments remain user-specified because prior research shows that local cash price relationships differ by region, season, lot characteristics, and market conditions (Bina and Schroeder, 2022; Coffey, Tonsor, and Schroeder, 2018).

The manuscript should distinguish carefully between three levels of market integration. A price-input model allows users to type current feeder and finished cattle prices. A semi-automated model imports daily settlement or index prices into the workbook on a scheduled refresh. A fully integrated model connects to a maintained API and updates the dashboard automatically. The current workbook supports the first level and is structured to support the second and third levels, but final claims about live CME integration should be supported with screenshots, query documentation, or code before submission.

### 3.6 Validation Strategy

FEDVT validation is organized around calculation validity, scenario realism, and decision utility. Calculation validity requires confirming that line-item costs, cost totals, break-even prices, and margins reconcile correctly within the workbook. This step is essential because even small formula inconsistencies can produce misleading break-even thresholds when multiplied across hundreds or thousands of head.

Scenario realism is assessed by comparing FEDVT outputs against published feedlot economic relationships. The sensitivity ranking should reproduce the central finding of Langemeier, Schroeder, and Mintert (1992): fed cattle price, feeder cattle price, feed price, interest rate, feed conversion, and average daily gain explain most profit variability. Disease scenarios should produce losses consistent with the BRD literature, including the treatment-cost estimates of Karle, Toth, and White (2017), the carcass and revenue losses documented by Blakebrough-Hall, McMeniman, and Gonzalez (2020), and the value of data-driven mortality decisions estimated by Feuz, Feuz, and Johnson (2021).

Decision utility should be evaluated through expert review and pilot use. Feedlot managers, veterinarians, extension economists, and agricultural lenders can assess whether the tool includes the right cost categories, whether default values are credible, and whether the dashboard presents outputs in a form that supports placement, marketing, and health-management decisions. If human-subject interviews or structured usability testing are used, the final study should document the recruitment method, participant roles, task protocol, feedback instrument, and any institutional review requirements.

## 4. RESULTS AND TOOL DEMONSTRATION

### 4.1 Base-Case Prototype Scenario

The current FEDVT workbook was evaluated using its base prototype assumptions. The scenario represents a 1,000-head feeding operation placing 600-lb feeder cattle and marketing cattle at 850 lb after a 100-day feeding period. The model assumes 2% finished shrink, 2.5 lb/day average daily gain, a $304/cwt feeder purchase price, and a $277/cwt selling price. Under these assumptions, finished sale weight after shrink is 833 lb/head.

The base-case output demonstrates the tool's core accounting logic. Feeder cattle acquisition is the dominant cost at $1,835.20/head, including purchase cost and inbound transaction costs. Feed cost is $49.61/head, consisting primarily of corn silage and supplement in the current workbook. Other operating expenses include straw, veterinary supplies, fuel and repair, utilities, marketing and transportation, insurance, manure removal, barn supplies, death loss, and operating interest. Total operating cost is $2,074.92/head. After fixed costs and labor, total cost of production is $2,124.96/head.

Gross revenue at the assumed $277/cwt selling price is $2,307.41/head. The resulting projected margin is $182.45/head. The break-even selling price is $255.10/cwt, meaning that the assumed selling price exceeds the break-even threshold by $21.90/cwt. The break-even purchase price is $334.41/cwt, indicating that the model could absorb a feeder purchase price approximately $30.41/cwt above the base assumption before reaching zero margin, holding all other assumptions constant.

Table 1. Base-case FEDVT prototype outputs.

| Metric | Value |
|---|---:|
| Number of cattle placed | 1,000 head |
| Placement weight | 600 lb |
| Finished weight | 850 lb |
| Finished sale weight after 2% shrink | 833 lb |
| Days on feed | 100 days |
| Average daily gain | 2.5 lb/day |
| Feeder purchase price | $304/cwt |
| Finished selling price | $277/cwt |
| Total feed cost | $49.61/head |
| Total operating cost | $2,074.92/head |
| Total cost of production | $2,124.96/head |
| Gross revenue | $2,307.41/head |
| Projected margin | $182.45/head |
| Break-even selling price | $255.10/cwt |
| Break-even purchase price | $334.41/cwt |

The base-case result illustrates the practical value of visualization. A table of values can identify margin, but a cost decomposition dashboard shows immediately why the margin is sensitive to cattle acquisition. In the prototype, feeder cattle costs account for more than 86% of total cost. This is consistent with Lawrence, Wang, and Loy (1999) and explains why small changes in purchase price can dominate larger percentage changes in smaller cost categories.

### 4.2 High Feed-Cost Scenario

The high feed-cost scenario evaluates FEDVT's ability to represent commodity-price stress. In this scenario, feed ingredient prices are increased while cattle placement, sale weight, and selling price are held constant. The current prototype's feed share is modest because the modeled feeding period is 100 days and the ration is dominated by silage and supplement rather than a full finishing ration. Even so, the scenario demonstrates how feed-cost shocks propagate through total cost, operating interest, cost per pound of gain, and break-even selling price.

Under the base workbook assumptions, feed costs are $49.61/head. Increasing corn silage and supplement prices by approximately 25% raises feed cost to roughly $62/head before interest effects. The direct increase of about $12 to $13/head raises the break-even selling price by approximately $1.50/cwt on an 833-lb sale weight. The economic effect is smaller than the effect of a comparable percentage change in feeder purchase price, but it is not trivial at commercial scale. Across 1,000 head, a $13/head feed-cost increase reduces projected lot margin by approximately $13,000 before any associated performance changes.

The more important insight is interaction. Dennis and Schroeder (2023) show that feed-price shocks can alter substitution patterns, feed conversion, average daily gain, and days on feed. If higher feed costs lead operators to substitute toward less efficient rations, the cost impact is no longer limited to ingredient price. A ration that reduces average daily gain extends days on feed, increases yardage and interest, and may shift marketing timing into a less favorable price window. FEDVT is useful because it allows those assumptions to be changed together. The operator can evaluate a pure price shock, a price-plus-performance shock, and a mitigation strategy such as ration reformulation or adjusted placement weight within the same interface.

### 4.3 Disease and Animal Health Scenario

The disease scenario evaluates FEDVT's ability to model non-price risk. Bovine respiratory disease is a useful test case because it affects both direct cost and biological performance. Karle, Toth, and White (2017) estimate that approximately 21.2% of U.S. feedlot placements are affected by respiratory disease annually, with a direct treatment cost of $23.60 per case. Blakebrough-Hall, McMeniman, and Gonzalez (2020) show that the larger cost of BRD may come through reduced carcass weight and lower closeout revenue, especially for cattle requiring repeated treatments. Feuz, Feuz, and Johnson (2021) further demonstrate that data-driven mortality prediction can recover meaningful value by improving culling and treatment decisions for high-risk animals.

In FEDVT, animal health risk can be entered through several linked parameters: medication cost, professional service cost, death loss, average daily gain, days on feed, finished weight, and discounts or production losses. A low-disease scenario may involve only routine vaccination, implant, parasite control, and veterinary service costs. A high-disease scenario can increase treatment costs, mortality, and days on feed while reducing sale weight or grade. This is important because a spreadsheet line item labeled "veterinary cost" understates the true economic effect if the model does not also account for lost gain and revenue.

Using the prototype structure, an outbreak can be represented as a shift from 1% to 2.5% mortality, an increase in per-head medication and veterinary cost, and a decline in average daily gain from 2.5 to 2.2 lb/day. Holding sale weight constant, lower gain increases days on feed and raises feed and interest expenses. Holding days on feed constant, lower gain reduces sale weight and revenue. The dashboard makes that distinction explicit. Operators can choose whether their disease assumption represents a longer feeding period to reach the same target weight, an earlier sale at a lower weight, or a combination of both. This is the kind of biological-economic linkage that static budgets often hide.

### 4.4 Sensitivity Analysis

FEDVT's sensitivity analysis ranks inputs by their effect on margin and break-even selling price. The base-case prototype confirms the expected hierarchy. Feeder purchase price is the dominant driver. A $10/cwt increase in feeder purchase price on a 600-lb animal increases feeder cost by $60/head. Spread over an 833-lb finished sale weight, that change raises the break-even selling price by approximately $7.20/cwt. By contrast, a 25% increase in the current prototype's feed cost raises break-even selling price by only about $1.50/cwt because feed cost is a much smaller share of total cost in the base workbook.

Finished selling price is the dominant revenue driver. A $10/cwt change in selling price on 833 lb of sale weight changes revenue by $83.30/head. This direct translation explains why futures prices, local cash prices, and basis assumptions must be visible in the tool. Operators are not only asking whether a placement is profitable under today's prices; they are asking how much adverse price movement the placement can absorb before losses emerge.

Animal performance variables form the second layer of sensitivity. Average daily gain, feed conversion, days on feed, shrink, and mortality affect both cost and revenue. Their relative importance increases when cattle are lighter at placement, when feed prices are elevated, or when disease pressure is high. This finding aligns with Mark, Schroeder, and Jones (2000), who show that performance risk varies by placement conditions and can become more important for certain classes of cattle.

The sensitivity dashboard is therefore not merely a display feature. It is the decision logic of the tool. By ranking the economic leverage of each input, FEDVT helps operators direct managerial attention toward the variables where better information or intervention has the highest expected value. In a normal market environment, that may mean careful feeder procurement and basis monitoring. In a high feed-cost environment, it may mean ration efficiency and cost-of-gain management. In a high-disease environment, it may mean prevention, early detection, and culling decisions.

### 4.5 Comparative Advantage Over Static Budgets

The primary advantage of FEDVT is not that it invents a new feedlot profitability equation. The contribution is that it makes established economics usable under changing conditions. A static budget can calculate one scenario. FEDVT turns the same budget logic into a scenario engine. Users can compare base-case, high feed-cost, low selling price, high disease, and alternative placement-weight assumptions without rebuilding the workbook each time.

This matters because feedlot decisions are time sensitive. Feeder cattle prices, feed prices, basis, interest rates, and health risk can shift during the period between placement evaluation and purchase. A manager using a static spreadsheet may know the correct formula but still be unable to test enough combinations quickly. FEDVT reduces that friction. The output is visual, the assumptions are grouped by decision domain, and the effect of each change is visible in break-even and margin terms. For extension agents, lenders, and veterinarians, the same visualization can support communication with producers who may not want to audit a full workbook but do need to understand why a placement is economically exposed.

## 5. DISCUSSION

### 5.1 Interpretation of Results

The FEDVT prototype demonstrates that the economic logic of feedlot finishing can be translated from a static budget into an interactive decision-support system. The base-case results are consistent with the central empirical finding of the feedlot economics literature: feeder cattle acquisition dominates total cost and therefore dominates margin sensitivity. In the current workbook, feeder cattle costs account for more than 86% of total cost. This explains why procurement timing, placement weight, and local basis can affect profitability more than many line-item operating costs that receive substantial managerial attention.

At the same time, the scenario demonstrations show why a tool limited to feeder price alone would be incomplete. Feed costs, health outcomes, average daily gain, days on feed, interest, and shrink are smaller than feeder cattle cost in the base case, but they interact with one another. A disease event can raise treatment cost, reduce gain, extend feeding duration, increase interest, and reduce revenue. A feed-cost shock can change ration composition, feed conversion, and marketing timing. FEDVT's value lies in representing these interactions in a format that operators can manipulate directly.

The tool should therefore be understood as a structured scenario-analysis system rather than a deterministic predictor of future profit. It does not remove market uncertainty. Instead, it clarifies the break-even thresholds at which a placement becomes profitable or unprofitable. That distinction is important for both academic framing and practitioner adoption. Producers do not need a tool that claims to know the future; they need a tool that shows how much risk a placement can absorb and which assumptions matter most.

### 5.2 Stakeholder Utility

Feedlot managers are the primary users. For them, FEDVT supports placement timing, feeder procurement, ration planning, and marketing decisions. A manager can ask whether a lot remains profitable if feeder prices rise by $10/cwt, if feed costs increase by 25%, or if selling prices weaken before closeout. The answer is expressed in break-even and margin terms rather than abstract model coefficients.

Veterinarians and animal-health consultants represent a second stakeholder group. Health interventions often appear expensive when evaluated only as direct costs, but BRD research shows that disease losses include lower gain, carcass-weight penalties, mortality, and delayed marketing. FEDVT can translate a prevention protocol into avoided loss per head. This supports a more economically complete conversation about vaccination, metaphylaxis, preconditioning, receiving protocols, diagnostics, and culling strategy.

Agricultural lenders and investors can use the tool to assess downside exposure. Feedlot financing depends heavily on operating capital, and lenders need to understand how price and performance changes affect repayment capacity. FEDVT's break-even selling price, break-even purchase price, and margin sensitivity outputs create a transparent basis for evaluating whether a proposed placement has adequate risk cushion.

Extension agents and educators can use the tool as a teaching platform. Dixon et al. (2022) identify inconsistent economic reporting as a barrier to interpretation in feedlot health and performance research. A transparent tool that reports assumptions, formulas, and outputs in a standardized way can improve communication between researchers and producers. It can also help students and producers understand why feedlot profitability is not determined by any single price, but by the interaction of purchase price, selling price, feed efficiency, animal performance, health, and capital costs.

### 5.3 Practical Implications

FEDVT's practical implication is that better scenario analysis can improve decision discipline. A manager evaluating a potential placement can establish a maximum feeder purchase price before entering the market. The break-even purchase price output is especially useful because it translates finished cattle price expectations and non-feeder costs into a procurement threshold. Instead of asking whether feeder cattle are "expensive" in general, the operator can ask whether the specific lot can be bought below the operation's break-even threshold.

The tool also supports risk prioritization. Because feeder price and selling price dominate many scenarios, management effort should first focus on procurement, basis, hedging, and marketing strategy. Under elevated feed prices, attention shifts toward cost of gain and ration efficiency. Under elevated disease risk, attention shifts toward animal health investments and performance protection. McKendree, Tonsor, and Schulz (2021) emphasize that livestock producers manage multiple risk domains jointly; FEDVT operationalizes that idea by allowing price, feed, and health assumptions to be evaluated together.

At scale, even modest per-head differences matter. A $13/head feed-cost increase on 1,000 head reduces lot margin by approximately $13,000. A $60/head increase in feeder acquisition cost reduces margin by approximately $60,000. A disease event that reduces sale weight or extends days on feed can be economically larger than its direct treatment bill. By making these magnitudes visible, FEDVT can help producers avoid placements with insufficient margin cushion and identify where additional data or management intervention has the highest value.

### 5.4 Limitations

Several limitations must be acknowledged. First, FEDVT is only as accurate as its input data. Operators with incomplete cost records may enter assumptions that underestimate overhead, labor, death loss, or interest. The tool improves transparency, but it cannot compensate for inaccurate records.

Second, the current prototype is deterministic. It evaluates scenarios selected by the user but does not yet estimate probability distributions for prices, feed costs, or disease events. Tonsor and Schroeder (2011) show that cattle feeding margins are shaped by correlated commodity prices. Future versions should incorporate stochastic or multivariate price simulation rather than treating each input as independent.

Third, regional basis variation remains a challenge. CME futures prices are useful reference points, but local cash prices depend on region, season, lot quality, transportation, and market structure. Bina and Schroeder (2022) and Coffey, Tonsor, and Schroeder (2018) show that basis risk can materially affect hedging and placement decisions. FEDVT addresses this by allowing user-specified basis adjustments, but final validation must test whether users understand and correctly parameterize basis.

Fourth, the current workbook and the manuscript framing must be aligned before submission. The workbook prototype currently models a 600-to-850 lb feeding scenario, while parts of the prose describe commercial fed-cattle finishing to heavier market weights. The tool can be adapted to either setting, but the final paper should not mix them without explanation. If the paper is about fed cattle marketed for slaughter, the scenario outputs should be rerun using placement weights, finished weights, feeding durations, and market prices appropriate to that production stage.

Fifth, claims about live data integration and user validation require evidence. The current workbook structure supports market price inputs, but no external CME connection was visible in the file inspection. Similarly, expert review and pilot testing are described as validation pathways, but final manuscript language should state completed results only if those activities have actually occurred and are documented.

### 5.5 Future Development

The most immediate future development is a completed market data pipeline. FEDVT should connect to a reliable source of feeder cattle, live cattle, corn, and possibly interest-rate data, with timestamped refreshes and visible basis assumptions. A live data feed would allow operators to monitor whether current market conditions remain within profitable placement thresholds.

A second development path is probabilistic forecasting. Rahmani, Khatami, and Stephens (2024) demonstrate that probabilistic machine-learning methods can provide prediction intervals for cattle prices rather than point forecasts alone. Integrating forecast intervals into FEDVT would allow users to see not only the expected margin, but also the probability that a placement falls below break-even.

A third path is precision livestock integration. Harrison (2022) shows the value of linking growth curves, feeding behavior, and cost curves to harvest timing. If FEDVT incorporated feed intake data, pen weights, health treatments, weather, and sensor-derived performance indicators, it could shift from pre-placement scenario analysis to in-cycle decision support. The tool could then update expected closeout margin as cattle performance data arrive.

Finally, FEDVT can be extended beyond the feedlot. Cow-calf, backgrounding, stocker, dairy-beef, and finishing operations all face versions of the same problem: biological production decisions must be made under volatile input and output prices. The broader contribution of FEDVT is therefore methodological. It shows how a static enterprise budget can be transformed into a transparent, interactive decision-support system that remains grounded in established economic accounting.

## 6. CONCLUSION AND FUTURE WORK

This study develops FEDVT as a decision-support prototype for feedlot economic analysis. The tool translates established feedlot break-even accounting into a parameterized workbook and visualization-ready dashboard structure. It models feeder cattle acquisition, feed, operating costs, labor, fixed costs, interest, and animal health assumptions, and reports outputs that directly support placement and marketing decisions: total cost per head, cost per pound of gain, break-even selling price, break-even purchase price, and projected margin.

The paper's contribution is not a new theory of feedlot profitability. The contribution is implementation. The feedlot economics literature has long identified the variables that drive returns, but decision-support reviews continue to find a gap between sophisticated models and usable field tools. FEDVT addresses that gap by making cost structure, break-even thresholds, and scenario sensitivity visible to managers, veterinarians, lenders, and extension personnel. The prototype demonstrates how an operator can move from a single static budget to a flexible scenario environment.

Future work should proceed in four stages. First, the scenario outputs should be recalculated from the finalized workbook using a single production setting and verified for mathematical consistency. Second, the market data pipeline should be documented and connected to reliable price sources, with basis handled explicitly. Third, FEDVT should be pilot tested with commercial feedlot users to assess usability, interpretability, and decision impact. Fourth, the model should be extended to probabilistic price and performance analysis, including correlated commodity prices and animal-level performance data where available.

The broader significance of FEDVT is that it offers a practical model for agricultural decision-support translation. Economic knowledge does not improve producer outcomes unless it reaches the decision point in a usable form. By combining transparent enterprise budgeting with interactive visualization, FEDVT helps close the gap between academic knowledge and operational decision-making in a sector where small per-head errors can become large financial losses at commercial scale.

## WORKING FIGURE CAPTIONS

Figure 1. Conceptual model of feedlot economic drivers. The figure should show feeder cattle acquisition, feed costs, labor, fixed overhead, operating costs, animal health, interest, market price, basis, and biological performance feeding into break-even price and projected margin.

Figure 2. FEDVT system architecture. The figure should show user inputs flowing into the Excel/VBA calculation engine, then into Summary, Breakeven Analysis, Tables, and Pivot Tables, then into the visualization dashboard. If the CME connection is completed, include the external market data feed and basis-adjustment module. If not, label it as planned integration.

Figure 3. FEDVT dashboard interface. The figure should show the input panel, cost distribution chart, break-even selling and purchase price metrics, and scenario comparison controls.

Figure 4. Scenario profitability comparison. The figure should compare base-case, high feed-cost, disease-risk, and adverse selling-price scenarios using projected margin per head and break-even selling price.

Figure 5. Sensitivity analysis. The figure should show a tornado chart ranking feeder cattle purchase price, finished selling price, feed cost, average daily gain, days on feed, mortality, interest rate, and shrink by impact on projected margin or break-even selling price.

## WORKING REFERENCES

Awasthi, T. R., Morshed, A., Williams, T., & Swain, D. L. (2024). Simulation approaches used for management and decision making in the beef production sector. Animals, 14(11), 1632.

Bang, A. L., Laugen, A. T., & Dreyer, H. C. (2023). Recent advances in decision support for beef and dairy farming. International Transactions in Operational Research, 30(5), 2214-2244.

Bina, J. D., & Schroeder, T. C. (2022). Feeder cattle basis risk and determinants. Journal of Agricultural and Applied Economics, 54(1), 1-21.

Blakebrough-Hall, C., McMeniman, J. P., & Gonzalez, L. A. (2020). An evaluation of the economic effects of bovine respiratory disease on animal performance, carcass traits, and economic outcomes in feedlot cattle. Journal of Animal Science, 98(2), skaa045.

Coffey, B. K., Tonsor, G. T., & Schroeder, T. C. (2018). Impacts of changes in market fundamentals and price momentum on hedging live cattle. Journal of Agricultural and Resource Economics, 43(1), 18-33.

Dennis, E. J., & Schroeder, T. C. (2023). Feed prices, substitution patterns, and technical efficiency in feedlot cattle. Journal of Agricultural and Applied Economics, 55(4), 546-566.

Dhuyvetter, K. C., & Schroeder, T. C. (2000). Price-weight relationships for feeder cattle. Canadian Journal of Agricultural Economics, 48(3), 299-310.

Dixon, A. L., Hanthorn, C. J., Pendell, D. L., Cernicchiaro, N., & Renter, D. G. (2022). Economic assessments from experimental research trials of feedlot cattle health and performance: A scoping review. Translational Animal Science, 6(3), txac077.

Feuz, R., Feuz, K., & Johnson, M. (2021). Improving feedlot profitability using operational data in mortality prediction modeling. Journal of Agricultural and Resource Economics, 46(2), 242-255.

Flores, H., Meneses, C., Villalobos, J. R., & Sanchez, O. (2017). Improvement of feedlot operations through statistical learning and business analytics tools. Computers and Electronics in Agriculture, 143, 273-285.

Harrison, M. A. (2022). Application of models in feedlot systems: Maintenance energy requirements, growth and cost curves, and feeding behavior. ProQuest Dissertations & Theses Global.

Herrington, M. A., & Tonsor, G. T. (2013). Structural changes in feedlot performance over time. The Professional Animal Scientist, 29(4), 435-442.

Karle, A. S., Toth, J. D., & White, B. J. (2017). Market impacts of reducing the prevalence of bovine respiratory disease in United States feedlots. Frontiers in Veterinary Science, 4, 189.

Langemeier, M. R., Schroeder, T. C., & Mintert, J. (1992). Determinants of cattle finishing profitability. Journal of Agricultural and Applied Economics, 24(2), 41-47.

Lawrence, J. D., Wang, Z., & Loy, D. (1999). Elements of cattle feeding profitability in Midwest feedlots. Journal of Agricultural and Applied Economics, 31(2), 349-357.

Mark, D. R., Schroeder, T. C., & Jones, R. (2000). Identifying economic risk in cattle feeding. Journal of Agribusiness, 18(3), 331-344.

McKendree, M. G. S., Tonsor, G. T., & Schulz, L. L. (2021). Management of multiple sources of risk in livestock production. Journal of Agricultural and Applied Economics, 53(1), 75-93.

Rahmani, E., Khatami, M., & Stephens, E. (2024). Using probabilistic machine learning methods to improve beef cattle price modeling. Sustainability, 16(5), 1789.

Stika, M. N. (2025). Optimizing feedlot placement weights using simulation-based mathematical programming. Kansas State University KREX repository.

Tonsor, G. T., & Schroeder, T. C. (2011). Multivariate forecasting of a commodity portfolio: Application to cattle feeding margins and risk. Applied Economics, 43(11), 1329-1339.

USDA. (2025). Cattle on feed and cattle production economic indicators. U.S. Department of Agriculture.

## WHAT IS STILL MISSING

1. Final scenario outputs from the actual FEDVT workbook. The current Section 4 numbers in the older draft do not reconcile cleanly with shrink, grade loss, total cost, and selling price assumptions. Rerun the final workbook and export the exact base-case, feed-cost, disease, adverse-price, placement-weight, and sensitivity outputs.

2. Production-scope decision. The paper must choose whether FEDVT is modeling commercial fed cattle marketed near slaughter weight or a shorter 600-to-850 lb feeding/backgrounding scenario. The current prose and workbook do not fully match.

3. Evidence for live CME integration. The workbook inspection found no visible external links, WEBSERVICE formulas, or CME/API query. If the pipeline exists elsewhere, add screenshots, code, query settings, or a short technical appendix. If not, describe it as planned or semi-automated input rather than completed live integration.

4. Validation evidence. If expert panels, user testing, or historical backtesting have not occurred, keep them in Methods as planned validation or future work. Do not state that the tool has been validated until there are results.

5. Figures. The manuscript needs Figure 1 conceptual model, Figure 2 architecture, Figure 3 dashboard screenshot, Figure 4 scenario output, and Figure 5 tornado/heatmap sensitivity result.

6. Full APA reference verification. The vault has working citations, but journal issue details, DOIs, USDA report titles, and Stika/Harrison thesis metadata should be verified before submission.

7. Tool appendix. Add a parameter table, equation appendix, source budget credit, and user guide/demo link. The workbook credits a Manitoba Agriculture feedlot finishing budget source; that should be cited or acknowledged if the template materially shaped FEDVT.

8. Human-subjects/IRB check. If you interview managers, veterinarians, lenders, or extension agents for usability testing, confirm whether the work needs an exempt determination or advisor documentation.
