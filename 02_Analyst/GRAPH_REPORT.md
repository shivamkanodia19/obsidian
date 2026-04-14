# Graph Report - C:/Users/shiva/claude  (2026-04-13)

## Corpus Check
- Corpus is ~14,427 words - fits in a single context window. You may not need a graph.

## Summary
- 124 nodes · 156 edges · 8 communities detected
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.83)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_FEDVT Paper Citations|FEDVT Paper Citations]]
- [[_COMMUNITY_Career and Fellowships|Career and Fellowships]]
- [[_COMMUNITY_FEDVT Tool and Data Pipeline|FEDVT Tool and Data Pipeline]]
- [[_COMMUNITY_ClinicalHours Startup|ClinicalHours Startup]]
- [[_COMMUNITY_Feedlot Literature Summaries|Feedlot Literature Summaries]]
- [[_COMMUNITY_BRD and Health Economics|BRD and Health Economics]]
- [[_COMMUNITY_Vault Protocols|Vault Protocols]]
- [[_COMMUNITY_Dashboard and Programs|Dashboard and Programs]]

## God Nodes (most connected - your core abstractions)
1. `FEDVT Literature Index (20 Sources)` - 24 edges
2. `FEDVT Feedlot Economics Visualization Tool` - 17 edges
3. `FEDVT ASAS-CSAS 2025 Working Paper` - 11 edges
4. `Shivam Kanodia` - 10 edges
5. `Shivam Kanodia Resume` - 10 edges
6. `ClinicalHours Pitch Deck` - 10 edges
7. `ClinicalHours Pitch Deck` - 9 edges
8. `FEDVT Tool (Excel/VBA + Tableau)` - 7 edges
9. `FEDVT Research Overview` - 7 edges
10. `Second Brain Vault` - 5 edges

## Surprising Connections (you probably didn't know these)
- `System Dynamics Research (WEF Nexus, Vensim)` --semantically_similar_to--> `FEDVT Research Overview`  [INFERRED] [semantically similar]
  career/resume/resume-current.md → research/fedvt/research-tracker.md
- `System Dynamics Research (WEF Nexus, Vensim)` --conceptually_related_to--> `FEDVT Feedlot Economics Visualization Tool`  [INFERRED]
  career/resume/resume-current.md → documents/processed/Literature Summaries.pdf
- `Summer 2026 Internship Search â€” DFW PM/ML/TPM` --references--> `Shivam Kanodia Resume`  [INFERRED]
  career/internships/summer-2026-search.md → documents/processed/ShivamKanodiaResume (20).pdf
- `Shivam Kanodia` --references--> `FEDVT Research Overview`  [INFERRED]
  career/resume/resume-current.md → research/fedvt/research-tracker.md
- `Shivam Kanodia` --references--> `Raghav Tirupati (Co-Founder, ClinicalHours)`  [INFERRED]
  career/resume/resume-current.md → projects/clinicalhours/pitch-deck.md

## Hyperedges (group relationships)
- **FEDVT Dual-Platform Architecture (Excel/VBA + Tableau + CME Pipeline)** — tracker_paper1_excel_vba, tracker_excel_workflow_5stage, tracker_google_sheets_middleware, fedvt_intro_cme_live_cattle_futures [EXTRACTED 0.95]
- **FEDVT ML Forecasting Model Suite** — working_paper_lstm_model, working_paper_sarima_model, working_paper_arima_model, working_paper_yahoo_finance_data [EXTRACTED 0.95]
- **ClinicalHours Co-Founder Team and Platform** — resume_shivam_kanodia, pitch_raghav_tirupati, platform_clinicalhours_platform, platform_bcs_free_health_clinic [EXTRACTED 0.90]
- **FEDVT Tool Justified by Core Feedlot Economics Literature** — lit_summaries_langemeier1992, lit_summaries_lawrence1999, lit_summaries_mark2000, lit_summaries_fedvt [EXTRACTED 0.95]
- **BRD Disease Scenario Validated by Epidemiology and Market Literature** — lit_summaries_blakebrough2020, lit_summaries_karle2017, outline_fedvt_scenarios [EXTRACTED 0.90]
- **Shivam Kanodia Career and Project Ecosystem** — resume_shivam, pitch_clinicalhours, career_avf_prep, career_fellowships, career_internship_search [INFERRED 0.85]

## Communities

### Community 0 - "FEDVT Paper Citations"
Cohesion: 0.11
Nodes (25): Awasthi et al. (2024) â€” Simulation Modeling in Beef Production, Bang, Laugen & Dreyer (2023) â€” DSS Adoption Gap, Dennis & Schroeder (2023) â€” Feedlot Net Returns Swing, Flores et al. (2017) â€” Analytics Tools for Feedlot Marketing, Langemeier, Schroeder & Mintert (1992) â€” 98% Profit Variability, Lawrence, Wang & Loy (1999) â€” 65-Parameter Framework, Mark, Schroeder & Jones (2000) â€” Risk Across Scenarios, Stika (2025) â€” Python Feedlot Simulation (+17 more)

### Community 1 - "Career and Fellowships"
Cohesion: 0.1
Nodes (24): Aggie Venture Fund (AVF) â€” Student-Led VC Fund at TAMU, Aggie Venture Fund Second Round Interview Prep, Fellowships and Leadership Programs Tracker, Summer 2026 Internship Search â€” DFW PM/ML/TPM, Meloy Launch Accelerator â€” Accepted, Active, Zachry Leadership Program â€” Deadline June 2026, ClinicalHours Competitors â€” Volgistics, Vsys, Handshake, VolunteerMatch, ClinicalHours Exit Strategy â€” Athenahealth Marketplace Acquisition (+16 more)

### Community 2 - "FEDVT Tool and Data Pipeline"
Cohesion: 0.12
Nodes (21): U.S. Beef Cattle Production, USDA (2025) Cattle on Feed Report, CME Live Cattle Futures Price Pipeline, FEDVT Paper Outline (7 Sections), Visualization-Based Decision Support Tool, Session Log: Vault Git Setup + Document Extraction (2026-04-13), GitHub Repo: shivamkanodia19/obsidian, Obsidian Git Auto-Sync Plugin (+13 more)

### Community 3 - "ClinicalHours Startup"
Cohesion: 0.14
Nodes (17): Athenahealth Marketplace Exit Strategy, ClinicalHours Market (TAM $24.8M), ClinicalHours Pitch Deck, McFerrin Ideas Challenge (Finalist), Meloy Kickstart Accelerator, Pre-Med Clinical Hours Discovery Problem, Raghav Tirupati (Co-Founder, ClinicalHours), BCS Free Health Clinic (Partner) (+9 more)

### Community 4 - "Feedlot Literature Summaries"
Cohesion: 0.14
Nodes (16): Simulation Approaches for Management and Decision Making in Beef Production (Awasthi et al. 2024), Recent Advances in Decision Support for Beef and Dairy Farming (Bang, Laugen, Dreyer 2023), Feeder Cattle Basis Risk and Determinants (Bina, Schroeder 2022), Impacts of Market Fundamentals and Price Momentum on Hedging Live Cattle (Coffey, Tonsor, Schroeder 2018), Feed Prices, Substitution Patterns, and Technical Efficiency in Feedlot Cattle (Dennis, Schroeder 2023), Price-Weight Relationships for Feeder Cattle (Dhuyvetter, Schroeder 2000), FEDVT Feedlot Economics Visualization Tool, Improvement of Feedlot Operations Through Statistical Learning and Business Analytics (Flores et al. 2017) (+8 more)

### Community 5 - "BRD and Health Economics"
Cohesion: 0.18
Nodes (11): Economic Effects of BRD on Feedlot Cattle (Blakebrough-Hall, McMeniman, Gonzalez 2020), Bovine Respiratory Disease (BRD) Economic Impact, Economic Assessments from Feedlot Cattle Health and Performance Trials (Dixon et al. 2022), Improving Feedlot Profitability Using Operational Data in Mortality Prediction Modeling (Feuz, Feuz, Johnson 2021), Application of Models in Feedlot Systems: Growth and Cost Curves (Harrison 2022), Market Impacts of Reducing BRD Prevalence in US Feedlots (Karle, Toth, White 2017), Identifying Economic Risk in Cattle Feeding (Mark, Schroeder, Jones 2000), FEDVT Break-Even Analysis Output (+3 more)

### Community 6 - "Vault Protocols"
Cohesion: 0.29
Nodes (8): Documents Processing Protocol, Inbox Processing Protocol, Second Brain Vault, Session Protocol (resume/save), ClinicalHours Codebase Knowledge Graph (graphify-out), Session Log: Tooling + Skills Audit (2026-04-13), Session Log: Vault Setup + Graphify (2026-04-13), Graphify Knowledge Graph Tool (v0.4.11)

### Community 7 - "Dashboard and Programs"
Cohesion: 1.0
Nodes (2): Second Brain Dashboard, Zachry Leadership Program

## Knowledge Gaps
- **61 isolated node(s):** `Inbox Processing Protocol`, `Documents Processing Protocol`, `Second Brain Dashboard`, `Zachry Leadership Program`, `Bina & Schroeder (2022) â€” Feeder Cattle Basis Risk` (+56 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Dashboard and Programs`** (2 nodes): `Second Brain Dashboard`, `Zachry Leadership Program`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `System Dynamics Research (WEF Nexus, Vensim)` connect `Career and Fellowships` to `FEDVT Tool and Data Pipeline`, `ClinicalHours Startup`, `Feedlot Literature Summaries`?**
  _High betweenness centrality (0.528) - this node is a cross-community bridge._
- **Why does `FEDVT Research Overview` connect `FEDVT Tool and Data Pipeline` to `FEDVT Paper Citations`, `Career and Fellowships`, `ClinicalHours Startup`?**
  _High betweenness centrality (0.429) - this node is a cross-community bridge._
- **Why does `FEDVT Feedlot Economics Visualization Tool` connect `Feedlot Literature Summaries` to `Career and Fellowships`, `BRD and Health Economics`?**
  _High betweenness centrality (0.365) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `FEDVT Feedlot Economics Visualization Tool` (e.g. with `Optimizing Feedlot Placement Weights Using Simulation-Based Mathematical Programming (Stika 2025)` and `System Dynamics Research (WEF Nexus, Vensim)`) actually correct?**
  _`FEDVT Feedlot Economics Visualization Tool` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Shivam Kanodia` (e.g. with `FEDVT Research Overview` and `Raghav Tirupati (Co-Founder, ClinicalHours)`) actually correct?**
  _`Shivam Kanodia` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Shivam Kanodia Resume` (e.g. with `ClinicalHours Pitch Deck` and `Summer 2026 Internship Search â€” DFW PM/ML/TPM`) actually correct?**
  _`Shivam Kanodia Resume` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Inbox Processing Protocol`, `Documents Processing Protocol`, `Second Brain Dashboard` to the rest of the system?**
  _61 weakly-connected nodes found - possible documentation gaps or missing edges._