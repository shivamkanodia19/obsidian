---
title: ClinicalHours TikTok QA Docs
description: Durable QA rules, guardrails, and review checklists for the ClinicalHours TikTok slideshow
last_updated: 2026-05-19
---

# ClinicalHours TikTok QA Docs

Use these notes before approving any new slide or export set.

## Files

- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist]] - messaging, truthfulness, and technical export checks
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_skill_mcp_guardrails_2026-05-18]] - workflow and tool guardrails for future agents
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_iteration_loop_v1_2026-05-31]] - required fresh-context review loop before a branch can ship
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/qa/review_bundles/_index|qa/review_bundles]] - machine-readable review packets emitted after render for cold judges

## Current hard gate

- Student-facing variants now require both the render QA and the copy plus screenshot-text audit enforced by `composition/audit_clinicalhours_tiktok_copy.ps1`.
- Durable variants should also produce a review bundle in `qa/review_bundles/` and pass at least two independent fresh-context judge reviews before shipping.

## Navigation

- Parent: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/_index|docs]]
- Related QA screenshots: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/qa/_index|qa]]
