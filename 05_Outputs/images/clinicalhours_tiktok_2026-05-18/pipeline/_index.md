---
title: ClinicalHours TikTok Pipeline
description: Automation files and deck-spec inputs for the ClinicalHours TikTok slideshow
last_updated: 2026-06-02
---

# ClinicalHours TikTok Pipeline

This folder holds the first-pass automation layer for assembling the ClinicalHours TikTok slideshow assets.

## Files

- `clinicalhours_tiktok_pipeline_config.json` - shared campaign config and file routing
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/qa/review_bundles/_index|qa/review_bundles/]] - machine-readable review packets emitted by the render script for fresh-context judges
- `specs/clinicalhours_tiktok_clinic_ops_v1_candidate_deck_spec.json` - candidate deck input spec with slide roles and proof sources for the canonical clinic-ops deck
- `specs/clinicalhours_tiktok_clinic_onboarding_visibility_v1_deck_spec.json` - issue-specific clinic-ops spec for the light-only onboarding-visibility `v4onboard` branch
- `specs/clinicalhours_tiktok_clinic_expiring_clearances_v1_deck_spec.json` - issue-specific clinic-ops spec for the light-only expiring-clearances `v4expiry` branch
- `specs/clinicalhours_tiktok_clinic_ops_concise_v1_deck_spec.json` - concise light clinic-ops spec for the `v8conciseops` branch
- `specs/clinicalhours_tiktok_clinic_ops_impact_v1_deck_spec.json` - impact-led concise clinic-ops spec for the corrected `v9impactops` branch
- `specs/clinicalhours_tiktok_student_bright_v3bright5_deck_spec.json` - historical bright student-facing spec for the earlier canonical set
- `specs/clinicalhours_tiktok_student_bright_v3bright7_deck_spec.json` - bright student-facing deck spec with copy-audit contract for the current `v3bright7` export set
- `specs/clinicalhours_tiktok_student_impact_story_v1_deck_spec.json` - issue-specific student-facing deck spec for the `v4impact` branch focused on impact recall, reflections, and account surfaces
- `specs/clinicalhours_tiktok_student_search_memory_v1_deck_spec.json` - bright student-facing deck spec for the issue-specific `v4memory` search-memory branch
- `specs/clinicalhours_tiktok_student_first_path_v1_deck_spec.json` - issue-specific student-facing deck spec for the `v5firstpath` branch focused on the first click through the first logged shift
- `specs/clinicalhours_tiktok_student_real_leads_v1_deck_spec.json` - issue-specific student-facing deck spec for the `v6realleads` branch focused on stale lists, trust, and real lead quality
- `specs/clinicalhours_tiktok_student_guest_first_v1_deck_spec.json` - issue-specific student-facing deck spec for the `v6guestfirst` branch focused on reducing signup friction before account creation

## Coverage Notes

- The pipeline is currently strongest for `clinic_ops_primary`, with reproducible specs for `v1`, the onboarding `v4onboard` branch, the expiring-clearances `v4expiry` branch, the concise cautionary `v8conciseops` branch, and the corrected concise `v9impactops` branch, while `v3bright7`, `v4impact`, `v4memory`, `v5firstpath`, `v6realleads`, and `v6guestfirst` now have matching student-facing deck specs as well.
- `v2auth` is still the only visible student-facing variant without a matching machine-readable deck spec in this folder.
- The render script now emits a JSON review bundle for each suffix under `qa/review_bundles/` so fresh-context agents can judge the latest branch without inheriting the builder's thread history.
- If a future agent promotes another bright export suffix or extends `v2auth`, updating the spec and documenting the proof mapping should be part of the task.

## Navigation

- Parent: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/_index|clinicalhours_tiktok_2026-05-18]]
- Related rubric: [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/social_media_expert/_index|social_media_expert]]
- Related replication guide: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]

## New Files

- [[specs/_index|specs/]] - Navigation hub for specs
