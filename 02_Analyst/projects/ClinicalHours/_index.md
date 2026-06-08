---
title: ClinicalHours
description: Clinical hours marketplace and automation platform
project: clinicalhours
scope: projects/clinicalhours
status: active
agent_context: true
surface_in_root: true
current_focus:
  - validate the evaluation-automation MVP with the current pilot clinic
  - keep onboarding reminders and deadline workflows as the main adjacent wedge to test next
  - use the admin-dashboard brief to clean up metric trust, hierarchy, and approval-based automation planning for `/admin`
active_tasks:
  - turn the next-wedge memo into a concrete pilot experiment with success signals
  - keep pricing as a parallel workstream instead of the main product claim
  - reconcile conflicting admin metrics across `Overview`, `Students`, `Guests`, and `Activity`
  - translate the admin-dashboard brief into an implementation plan for Claude Code
prompt_context:
  - "[[02_Analyst/projects/ClinicalHours/Strategy/next-wedge-priority-2026-05-10]]"
  - "[[02_Analyst/projects/ClinicalHours/Strategy/ClinicalHours-Product-Map]]"
  - "[[02_Analyst/projects/ClinicalHours/Strategy/niche-refinement]]"
  - "[[02_Analyst/projects/ClinicalHours/Strategy/clinicalhours-admin-dashboard-revamp-claude-code-brief-2026-05-28]]"
definition_of_done:
  - the next workflow wedge is explicit and tied to current pilot evidence
  - the next experiment, success signal, and caveat are explicit
  - admin metrics have clear definitions, trusted sources, and no unexplained cross-tab mismatches
  - the admin redesign separates platform ops from clinic workflow ops and exposes the highest-priority action queue
blocked_by:
  - broad clinic-ops positioning still exceeds the current evidence base
  - the current admin surface appears to mix inconsistent data definitions across tabs, which weakens trust in analytics and future AI insights
task_cards:
  - "[[02_Analyst/tasks/clinicalhours-next-wedge-priority-2026-05-10]]"
last_updated: 2026-05-28
---

# ClinicalHours

Clinical hours marketplace connecting students with free clinics for volunteer service plus email and workflow automation.

## Subfolders

- **Campaigns/** - campaign planning, asset-generation strategy, and TikTok slideshow system notes
- **History/** - archived root-level indexes and early session summaries that should not compete with the live hub
- **Strategy/** - Pricing, market analysis, positioning, niche refinement, competitive landscape
- **Market/** - TAM analysis and competitive positioning
- **Outreach/** - DFW clinic research, personas, and targeting strategy

## Current Canonical Notes

- **[[Strategy/next-wedge-priority-2026-05-10]]** - current best-hypothesis memo on the next workflow wedge to test
- **[[Strategy/ClinicalHours-Product-Map]]** - current product wedge map and validated-vs-speculative split
- **[[Strategy/niche-refinement]]** - small-clinic positioning, competitive landscape, and product-fit questions
- **[[Strategy/clinicalhours-admin-dashboard-revamp-claude-code-brief-2026-05-28]]** - durable admin redesign brief covering IA, metric trust, AI insights, and approval-based automation

## Historical Execution Notes

- **[[clinicalhours_email_outreach_strategy]]** - earlier execution-ready outreach cluster from the clinic-first wave
- **[[Outreach/Clinic-Email-Send-Strategy-2026-04-19]]** - April outreach send plan and targeting logic
- **[[Market/DFW-Clinic-Market-Analysis-2026-04]]** - DFW TAM and target profile used during the earlier clinic-outreach phase

## Current Focus

- Pilot-clinic workflow automation beyond volunteer coordination
- Evaluation automation MVP design and testing
- Market positioning for small clinics with 15-100 volunteers
- Admin-dashboard redesign focused on trustworthy metrics, operator visibility, and recommendation-first automation

## Current Status (As of 2026-05-28)

- The older clinic-outreach system remains useful historical proof, but it is no longer the default product-direction note.
- Pilot evidence currently points more toward evaluation workflows, onboarding reminders, and admin coordination than toward treating the broad clinic-ops platform as already validated.
- Strategy notes in `Strategy/` are now the canonical routing layer for the next wedge decision.
- Outreach notes in `Outreach/` should be treated as execution history unless a new send cycle explicitly reactivates them.
- The `2026-05-28` admin-dashboard brief is now the durable entry point for `/admin` redesign, metric-trust cleanup, and approval-based automation planning.
- The student-side TikTok system now includes a `v5firstpath` branch for the first-click-through-first-log story, but it is an additive branch rather than a replacement for the earlier student variants.

## Next Actions

- [ ] Prototype and test an evaluation-automation MVP with the pilot clinic
- [ ] Track whether onboarding reminders and deadline workflows should be the second product wedge
- [ ] Treat pricing as a parallel business-model workstream, not the main next experiment-log claim
- [ ] Reconcile admin metric definitions and source-of-truth logic across `Overview`, `Students`, `Guests`, and `Activity`
- [ ] Turn the admin-dashboard brief into a concrete Claude Code implementation plan with phased UI and data-trust work
- [ ] Implement B2B sales workflow (calls -> demos -> pilots)
- [ ] Develop a hospital and larger-clinic tier
- [ ] Consider adapting the Felt marketing pipeline pattern later: image/asset grading, multi-asset set assembly, and approved-output email release for ClinicalHours marketing assets if that becomes the higher-priority destination for this automation.

## New Files

- [[campaigns/_index|campaigns/]] - Campaigns
- [[history/_index|history/]] - early project indexes and session summaries moved out of the vault root
- [[Strategy/ClinicalHours-Product-Map]] - ClinicalHours product map for the marketing and wedge-priority system
- [[Strategy/clinicalhours-admin-dashboard-revamp-claude-code-brief-2026-05-28]] - admin console redesign brief with accuracy, IA, and automation guidance
- [[clinicalhours-experiment-log-framing-2026-05-07]] - Durable save for the May 7 accelerator experiment-log and pilot-learning framing cluster
- [[pear-founder-application-2026-05-01]] - Pear founder application framing built around ClinicalHours pivots
- [[Market/_index|Market/]] - Market
- [[Outreach/_index|Outreach/]] - Outreach
- [[Strategy/_index|Strategy/]] - Strategy
- [[clinicalhours_email_outreach_strategy]] - ClinicalHours email outreach strategy
- [[Market-Research-Data-2026-04]] - Clinical Hours market data and clinic inventory
- [[05_Outputs/images/clinicalhours-product-audit-2026-05-18/_index|clinicalhours-product-audit-2026-05-18]] - authenticated product-surface capture pack moved out of the vault root
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v5firstpath]] - partial student first-path branch focused on the first click through the first logged shift
