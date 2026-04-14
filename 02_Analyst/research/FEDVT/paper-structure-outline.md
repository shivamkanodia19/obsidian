# FEDVT Paper Structure & Outline

**Template:** Academic Research Paper (6-8K words)  
**Status:** Outline complete, Section 1-2 drafted, Sections 3-6 ready for development  
**Target:** Journal submission (Agricultural Economics, Decision Support focus)

---

## PAPER STRUCTURE MAP

```
ABSTRACT (1 paragraph, ~350 words) [WRITE LAST]
├─ Problem statement
├─ Objectives
├─ Methodology
├─ Key results
├─ Significance
└─ Stakeholder implications

1. INTRODUCTION (4-5 paragraphs)
├─ Global beef production context & economic pressure
├─ Knowledge gap: static tools vs. dynamic complexity
├─ Emerging solutions: visual analytics, real-time dashboards
├─ FEDVT objective statement
└─ Paper structure overview

2. BACKGROUND & LITERATURE REVIEW (5-6 paragraphs) ✓ DRAFTED
├─ Feedlot economics overview (costs, volatility, margins)
├─ Previous decision support tools & their limitations
├─ Research gaps in visual analytics & real-time tools
├─ Foundational economic research (Langemeier, Lawrence, Mark)
├─ Risk management literature (basis, BRD, health costs)
├─ Analytics-based tools emerging (Flores, Stika, Harrison)
└─ Figure 1: Conceptual model of feedlot operations

3. MATERIALS & METHODS (5-6 paragraphs) [NEXT]
├─ Tool development framework & software (Excel VBA + Tableau)
├─ Economic variables modeled (65 parameters, 6 cost categories)
│  ├─ Feed costs (type, quantity, pricing)
│  ├─ Feeder cattle costs (purchase price, lot characteristics)
│  ├─ Fixed costs (facility, equipment, permits)
│  ├─ Labor costs (pen riders, veterinary)
│  ├─ Interest costs (financing % and period)
│  └─ Other operating costs (trucking, processing)
├─ Visualization design (dashboard interface, interactivity)
├─ Data pipeline architecture (CME Live Cattle futures integration)
├─ Validation approach (expert feedback, historical backtesting)
├─ Figure 2: Architecture/system design diagram
└─ Figure 3: Dashboard screenshot/mockup

4. RESULTS & TOOL DEMONSTRATION (4-6 paragraphs)
├─ Use-case scenarios:
│  ├─ Base-case profitability analysis
│  ├─ High feed cost stress scenario
│  ├─ Disease outbreak scenario (BRD modeling)
│  └─ Placement weight sensitivity analysis
├─ Demonstrated outputs:
│  ├─ Break-even price projections
│  ├─ Margin sensitivity by input variable
│  ├─ Scenario comparison across market conditions
│  └─ Real-time price feed integration
├─ Comparative advantage vs. static spreadsheets
├─ Figure 4: Scenario simulation output (profitability curves)
└─ Figure 5: Sensitivity analysis (tornado/heatmap)

5. DISCUSSION (5-6 paragraphs)
├─ Interpretation of results & economic implications
├─ Decision support utility for stakeholders:
│  ├─ Feedlot managers (placement timing, feed strategy)
│  ├─ Veterinarians (health cost trade-offs)
│  ├─ Investors (risk-return profiles)
│  └─ Extension agents (farmer education)
├─ Practical implications:
│  ├─ Potential cost savings (per-head margins)
│  ├─ Risk management capability improvements
│  └─ Economic sustainability under volatility
├─ Tool limitations:
│  ├─ Data quality & availability
│  ├─ Regional specificity (basis variation)
│  ├─ Scalability across feedlot sizes
│  └─ Model assumptions
├─ Future integration potential:
│  ├─ Real-time data sources (CME, weather APIs)
│  ├─ IoT/precision livestock technologies
│  ├─ Machine learning price forecasting (Tonsor, Rahmani)
│  ├─ Multivariate commodity correlation modeling
│  └─ Individual animal-level tracking
└─ Recommendations for practitioners

6. CONCLUSION & FUTURE WORK (2-3 paragraphs)
├─ Summary of contributions:
│  ├─ Novel decision-support tool bridging academia-practice
│  ├─ Methodologically grounded economic modeling
│  ├─ Demonstration of visualization utility
│  └─ Transparent, standardized approach
├─ Next steps:
│  ├─ Commercial feedlot field testing & refinement
│  ├─ User adoption research & training
│  ├─ Integration with live data pipelines
│  └─ Expansion to other cattle production stages
├─ Broader significance:
│  ├─ Closes gap identified in Bang et al. (2023) & Dixon et al. (2022)
│  ├─ Addresses knowledge transfer barrier in agricultural decision support
│  └─ Model for industry-academic tool development
└─ Policy relevance for sector sustainability

7. REFERENCES
└─ APA citation format (alphabetized)

APPENDICES (Optional)
├─ Tool screenshots & user guide
├─ Detailed equations & parameter specifications
├─ Validation data & backtesting results
└─ Link to interactive demo
```

---

## SECTION DEVELOPMENT NOTES

### Section 3: Materials & Methods [PRIORITY]

**Current State:** Outlined only. Needs 1,200-1,500 words.

**Content to Include:**

1. **Tool Development Framework** (150 words)
   - Software: Microsoft Excel with VBA for computation engine
   - Visualization layer: Tableau for interactive dashboards
   - Architecture: Dual-platform (calculation → visualization)
   - Development methodology (iterative design)

2. **Economic Variables Modeled** (400 words)
   - List all 65 input parameters across 6 cost categories
   - Define each parameter's role and relationship
   - Justify parameter selection citing Lawrence et al. (1999) & Langemeier et al. (1992)
   - Explain how parameters map to break-even equations
   - Detail default values vs. user-customizable inputs

3. **Visualization Design & Interactivity** (300 words)
   - Dashboard layout and user interface description
   - Interactive elements (sliders, scenario switches, price feeds)
   - Real-time recalculation capability
   - Output types (graphs, tables, summary metrics)
   - Design principles (user-friendly for non-specialists)

4. **Data Pipeline & Live Price Integration** (200 words)
   - CME Live Cattle futures price connection
   - Data update frequency
   - Basis assumptions & customization
   - How prices feed into break-even calculations

5. **Validation Approach** (250 words)
   - Expert panel feedback (feedlot managers, veterinarians, extension agents)
   - Historical backtesting against Kansas Focus on Feedlots data
   - Scenario validation (realistic results under stress conditions)
   - Comparison to published economic models
   - Limitations of validation approach

**Figures Needed:**
- **Figure 2:** System architecture (Excel/VBA ↔ Data Pipeline ↔ Tableau Dashboard)
- **Figure 3:** Dashboard mockup/screenshot showing key interactive elements

---

### Section 4: Results & Tool Demonstration [PRIORITY]

**Current State:** Outlined only. Needs 1,200-1,500 words with visual outputs.

**Content to Include:**

1. **Base-Case Scenario** (300 words)
   - Define baseline parameters (realistic Kansas feedlot operation)
   - Show break-even price and projected margins
   - Interpret results in economic context
   - Use recent data from Dennis & Schroeder (2023)

2. **High Feed Cost Stress Scenario** (250 words)
   - Model conditions similar to 2022-2023 corn spike
   - Show how feed substitution affects profitability (FCR, ADG, DOF)
   - Demonstrate margin compression from both cost and performance angles
   - Illustrate value of scenario planning tool

3. **Disease Outbreak Scenario** (250 words)
   - Assume 15-20% BRD morbidity (realistic for placement stress)
   - Use treatment costs from Karle et al. (2017): $23.60/case
   - Model mortality impacts from Blakebrough-Hall et al. (2020): AUD $385/head lost
   - Show how health costs impact break-even and marketing decisions
   - Demonstrate machine learning prediction potential (Feuz et al., 2021)

4. **Sensitivity Analysis & Variable Ranking** (300 words)
   - Tornado/heatmap showing contribution of each input to profit variance
   - Demonstrate that feeder price and feed cost dominate (validating Stika 2025 & Mark et al. 2000)
   - Show how sensitivity shifts across placement scenarios (lighter vs. heavier cattle)
   - Compare to historical sensitivity rankings from research literature

5. **Comparative Advantage vs. Static Tools** (200 words)
   - Example: traditional spreadsheet scenario analysis (3 scenarios, manual recalculation)
   - vs. FEDVT approach (infinite scenarios, real-time updates, visual communication)
   - Time savings and decision quality improvements
   - Accessibility to non-specialist managers

**Figures Needed:**
- **Figure 4:** Multiple scenario profitability curves (base, high feed cost, disease outbreak) overlaid
- **Figure 5:** Sensitivity analysis heatmap or tornado diagram showing variable ranking and impact magnitude

---

### Section 5: Discussion

**Current State:** Outlined only. Needs 1,200-1,500 words.

**Content to Include:**

1. **Interpretation & Economic Implications** (250 words)
   - What do results tell us about feedlot profitability drivers?
   - How do scenario results align with empirical literature?
   - What's the practical meaning of break-even prices to an operator?
   - Why sensitivity analysis matters for risk management

2. **Stakeholder Utility** (300 words)
   - **Feedlot managers:** Real-time placement/marketing decisions, scenario planning
   - **Veterinarians:** Health cost trade-offs, preventative investment ROI
   - **Investors/lenders:** Risk assessment, margin projections under volatility
   - **Extension agents:** Farmer education, decision support dissemination
   - Cite McKendree et al. (2021) on multi-domain risk management

3. **Practical Implications & Cost-Saving Potential** (250 words)
   - Example: operator avoiding $50+ per-head loss through improved placement timing
   - BRD prevention ROI (Feuz et al. 2021: $14-45 per-head recovery)
   - Risk management value under volatile commodity markets
   - Sustainability implications (economic viability → continued beef production)

4. **Tool Limitations & Caveats** (200 words)
   - Data quality assumptions (does operator have accurate cost records?)
   - Regional basis variation (tool parameterized for individual operation)
   - Model assumptions (FCR, ADG) may not hold under extreme stress
   - Scalability: works for large commercial feedlots, may not suit very small operations
   - External factors not modeled (regulation, trade policy, labor availability)

5. **Future Integration Potential** (300 words)
   - **Real-time data sources:** Automated feed intake monitoring, individual animal weight
   - **IoT/Precision Livestock:** Sensor data feeding into performance predictions
   - **ML Price Forecasting:** Probabilistic forecasts (Rahmani et al. 2024) replacing fixed prices
   - **Multivariate commodity modeling:** Correlated price scenarios (Tonsor & Schroeder 2011)
   - **Individual animal-level decision support:** Moving beyond pen-level to per-animal optimization
   - **Supply chain integration:** Linking backward to cow-calf, forward to processing/retail

6. **Recommendations for Practitioners** (100 words)
   - Start with base-case parameterization, refine over 2-3 production cycles
   - Use tool for scenario planning, not deterministic prediction
   - Combine with market research and expert judgment
   - Track actual vs. projected outcomes to calibrate assumptions

---

### Section 6: Conclusion & Future Work

**Current State:** Outlined only. Needs 600-800 words.

**Content to Include:**

1. **Summary of Contributions** (200 words)
   - Novel tool bridging academia-practice gap (Bang et al. 2023, Dixon et al. 2022)
   - Methodologically grounded in 30+ years of feedlot economics literature
   - Demonstrates visualization utility for complex multi-variable decision problems
   - Transparent, standardized approach improving on fragmented practices
   - Addresses knowledge transfer barrier in agricultural research

2. **Next Steps & Roadmap** (200 words)
   - Beta testing with 5-10 commercial feedlots (data collection, feedback)
   - User adoption research (what features drive adoption? barriers?)
   - Field training & extension programming
   - Integration with CME API for live price feeds
   - Expansion to other cattle production stages (cow-calf, backgrounding)
   - Development of web/mobile version for on-farm access

3. **Broader Significance & Policy Context** (200 words)
   - Tool as model for industry-academic partnership in decision support
   - Addresses structural gap in ag decision support (proven by Bang et al. 2023)
   - Implications for sector sustainability (economic viability drives environmental stewardship)
   - Relevance to farmer profitability in volatile commodity markets
   - Model adaptable to other livestock commodities (dairy, swine, poultry)

4. **Final Thoughts** (100 words)
   - Restate importance of closing gap between economic knowledge and on-farm practice
   - Call to action: adoption, feedback, continued development

---

## ABSTRACT DEVELOPMENT [WRITE LAST]

**Target:** 1 paragraph, ~350 words

**Structure to Follow:**
1. **Problem:** Feedlot profitability is volatile; existing tools inadequate
2. **Gap:** Decision-support literature shows academia-to-practice disconnect
3. **Solution:** Develop FEDVT — interactive, visual, enterprise-level tool
4. **Methodology:** Excel/VBA + Tableau; 65 parameters; break-even economics
5. **Results:** Tool demonstrates multi-scenario analysis, sensitivity visualization
6. **Significance:** Closes gap identified in Bang et al. (2023) & Dixon et al. (2022)
7. **Implications:** Improves feedlot decision-making, risk management, profitability under volatility

---

## KEY CITATIONS BY SECTION

| Section | Primary Citations | Secondary Citations |
|---------|-------------------|---------------------|
| **1 Intro** | Dennis & Schroeder 2023, Langemeier et al. 1992 | USDA data |
| **2 Background** | Bang et al. 2023, Lawrence et al. 1999, Mark et al. 2000, Langemeier et al. 1992, Bina & Schroeder 2022, Karle et al. 2017, Herrington & Tonsor 2013, Stika 2025, Flores et al. 2017, Awasthi et al. 2024 | All 20 sources |
| **3 Methods** | Lawrence et al. 1999 (parameter justification), Dhuyvetter & Schroeder 2000 (pricing mechanics) | Harrison 2022, Stika 2025 |
| **4 Results** | Mark et al. 2000, Dennis & Schroeder 2023, Blakebrough-Hall et al. 2020, Karle et al. 2017, Feuz et al. 2021 | All 20 sources |
| **5 Discussion** | McKendree et al. 2021, Dixon et al. 2022, Feuz et al. 2021, Tonsor & Schroeder 2011, Rahmani et al. 2024, Harrison 2022 | Use case-specific |
| **6 Conclusion** | Bang et al. 2023, Dixon et al. 2022 | Tonsor & Schroeder 2011, Rahmani et al. 2024 |

---

## WRITING SEQUENCE RECOMMENDATION

1. **Expand Section 3 (Materials & Methods)** — Foundation for credibility
2. **Expand Section 4 (Results)** — Heart of the paper; demonstrate tool value
3. **Write Section 5 (Discussion)** — Interpret results, discuss implications
4. **Write Section 6 (Conclusion)** — Summarize contributions & next steps
5. **Refine Section 1 & 2** — Ensure intro flows to your completed work
6. **Write Abstract** — Last, after all sections finalized

---

## PRODUCTION CHECKLIST

- [ ] Section 3: ~1,500 words with Figures 2-3
- [ ] Section 4: ~1,500 words with Figures 4-5
- [ ] Section 5: ~1,500 words
- [ ] Section 6: ~800 words
- [ ] Abstract: ~350 words
- [ ] References: All 20+ citations in APA format, alphabetized
- [ ] Figures: 5 total (1 conceptual, 2 architecture, 2 results)
- [ ] Proofread & consistency check
- [ ] Format & citation validation
