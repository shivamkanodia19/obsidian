---
title: FEDVT - Feedlot Economics
project: fedvt
strategic: false
status: stable
origin_dump: "[[01_Source/Dumps/2026-04-14_fedvt-baseline]]"
last_synced_dump: "[[01_Source/Dumps/2026-04-14_fedvt-baseline]]"
last_updated: 2026-04-14
tags: [research, economics, forecasting, ml, time-series]
---

# FEDVT — Feedlot Economics Data Visualization Tool

## Overview

Research project: feedlot cattle futures forecasting with Excel/VBA cost model + ML layer. Advisor: Dr. Kaniyamattam (TAMU Animal Science).

**Current state:** Paper 1 introduction complete (v3). Introduction poster presented at Student Research Week. 65-input cost model with 6 cost categories. Second paper scoped but not started.

## Paper 1: "Feedlot Economics"

### Status
- **Introduction:** v3 complete ✓
- **Sources verified:** 20 (relevant literature on feedlot economics, cattle futures markets)
- **Methods:** In progress (model description)
- **Results:** Pending (requires data runs)
- **Discussion:** Pending

### Cost Model (Excel/VBA)

**Inputs:** 65 parameters across 6 cost categories
- Feed costs (grain, hay, supplements)
- Labor
- Equipment & facilities
- Veterinary & health
- Marketing
- Miscellaneous

**Output:** Break-even price (BEP) for feedlot operation

### ML Layer

Algorithms scoped:
- **SARIMA** — seasonal time-series forecasting
- **LSTM** — long-form temporal dependencies
- **XGBoost** — feature importance + prediction accuracy

## Paper 2

**Status:** Scoped but not started. Architecture planned. No active work yet.

## Sources

- [[01_Source/Dumps/2026-04-14_fedvt-init]]

## History

[2026-04-14] Vault initialization. Paper 1 at poster presentation stage, introduction v3 complete.

## Next Actions

- [ ] Complete methods section (cost model description)
- [ ] Run model to generate results dataset
- [ ] Draft discussion section
- [ ] Prepare Paper 1 for submission (target: mid-2026)
- [ ] Begin literature review for Paper 2
- [ ] Coordinate with Dr. Kaniyamattam on next steps

## Changelog

- 2026-04-14: Vault initialization

