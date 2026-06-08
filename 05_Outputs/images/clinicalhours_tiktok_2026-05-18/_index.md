---
title: ClinicalHours TikTok System - 2026-05-18
description: Capture inventory, render pipeline, QA, and handoff files for ClinicalHours TikTok slides
last_updated: 2026-06-07
---

# ClinicalHours TikTok System - 2026-05-18

This folder is the ClinicalHours counterpart to the Felt TikTok system, now with multiple documented deck variants and a clearer future-agent replication path.

Main working areas:

- `captures/` - truthful Playwright screenshots from the live site
- `composition/` - HTML source and render script
- `exports/` - versioned PNG outputs
- `qa/` - overlay screenshots and checks
- `docs/` - playbooks, QA rules, and handoff notes
- `pipeline/` - machine-readable config and deck spec

## Read This Order First

1. [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/_index|Campaign strategy hub]]
2. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19|Replication playbook]]
3. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19|Current system handoff]]
4. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v3bright7|Bright branch iteration notes]]
5. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v4impact|Student impact branch iteration notes]]
6. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v5firstpath|Student first-path branch iteration notes]]
7. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v6guestfirst|Student guest-first branch iteration notes]]
8. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v7semesterstart|Student semester-start branch iteration notes]]
9. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v10fallimpact|Student high-impact fall branch iteration notes]]
10. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/_index|Docs QA hub]]

Read first:

- `captures/clinicalhours_live_capture_notes_2026-05-18.md`
- `docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19.md`
- `docs/playbooks/clinicalhours_tiktok_playwright_future_agent_playbook_2026-05-18.md`
- `docs/qa/clinicalhours_tiktok_compliance_qa_checklist.md`
- `docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19.md`

## Current Variants

- `v1` - best-documented `clinic_ops_primary` export path with a matching pipeline spec
- `v2auth` - authenticated student-product export set documented in iteration notes
- `v4onboard` - issue-specific onboarding-visibility clinic-ops branch with a light-only shell, matching deck spec, QA screenshots, and iteration notes
- `v4expiry` - issue-specific expiring-clearances clinic-ops branch with a light-only shell, matching deck spec, QA screenshots, and iteration notes
- `v3bright` - brighter student-facing branch with current canonical exports in `v3bright7`, a dedicated iteration note, a matching pipeline deck spec, and a copy-audit workflow
- `v4impact` - issue-specific student-facing branch for students who struggle to show impact later, with a dedicated composition, deck spec, QA screenshots, and iteration notes
- `v4memory` - issue-specific bright student branch for losing track after discovery, with a dedicated composition, deck spec, and iteration note
- `v5firstpath` - issue-specific student branch for the first-click-through-first-log path, with a dedicated composition, deck spec, iteration note, and partial export set
- `v6realleads` - issue-specific student trust branch for stale lists, real-opportunity confidence, and proving a clinic is worth the click
- `v6guestfirst` - issue-specific student activation branch for browsing before signup and delaying account creation until it actually helps
- `v7semesterstart` - issue-specific student semester-start branch for students looking for hours during the semester, with a Houston Methodist proof chain and fresh judge-pass documentation
- `v8conciseops` - concise clinic-ops experiment preserved for reference, but not the preferred future baseline because the slides are too visually similar and the screenshot text still reads too slowly
- `v9impactops` - current concise clinic-ops correction branch built from the `v7semesterstart` quality benchmark with fewer words and clearer proof framing
- `v10fallimpact` - experimental student high-impact branch built on `2026-06-07` that keeps the `v7semesterstart` proof chain but upgrades the shell to a cleaner editorial layout

## Current Quality Preference

- Treat `v7semesterstart` as the best current benchmark for impact, slide-to-slide variation, and proof sequencing.
- Treat `v9impactops` as the current clinic-ops example of how to apply that benchmark without inheriting `v8conciseops`-style repetition.
- Treat `v10fallimpact` as the current student aesthetic experiment for a more modern shell, but not yet the safest default until it goes through a fresh judge loop.
- For future concise asks, keep fewer words than `v7semesterstart`, but preserve `v7semesterstart`-level visual variety and proof readability.

## Related strategy

- [[02_Analyst/projects/ClinicalHours/campaigns/_index|campaigns]]
- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/_index|tiktok-slideshow]]
- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/social_media_expert/_index|social_media_expert]]

## New Files

- [[captures/_index|captures/]] - Navigation hub for captures
- [[composition/_index|composition/]] - Navigation hub for composition
- [[docs/_index|docs/]] - Navigation hub for docs
- [[exports/_index|exports/]] - Navigation hub for exports
- [[pipeline/_index|pipeline/]] - Navigation hub for pipeline
- [[qa/_index|qa/]] - Navigation hub for qa
- [[clinicalhours_tiktok_iteration_notes_v1]] - Current notes for the canonical ClinicalHours clinic-ops TikTok deck after the evidence-tightening p
- [[clinicalhours_tiktok_iteration_notes_v2auth]] - ClinicalHours TikTok Iteration Notes - v2auth
- [[clinicalhours_tiktok_iteration_notes_v3bright5]] - Durable proof mapping and export notes for the brighter ClinicalHours student-facing deck
- [[clinicalhours_tiktok_iteration_notes_v4expiry]] - Issue-specific notes for the light-only expiring-clearances clinic-ops branch
- [[clinicalhours_tiktok_iteration_notes_v4memory]] - Issue-specific notes for the student search-memory branch built from the bright student system
- [[clinicalhours_tiktok_iteration_notes_v4onboard]] - Issue-specific notes for the light-only onboarding-visibility clinic-ops branch
- [[clinicalhours_tiktok_iteration_notes_v5firstpath]] - Issue-specific notes for the student first-path branch focused on the first click through the first logged shift
- [[clinicalhours_tiktok_iteration_notes_v6realleads]] - Issue-specific notes for the student real-leads trust branch
- [[clinicalhours_tiktok_iteration_notes_v6guestfirst]] - Issue-specific notes for the student guest-first activation branch
- [[clinicalhours_tiktok_iteration_notes_v7semesterstart]] - Issue-specific notes for the student semester-start branch focused on finding hours during the fall semester
- [[clinicalhours_tiktok_iteration_notes_v8conciseops]] - Light clinic-ops iteration note for the concise default operations branch
- [[clinicalhours_tiktok_iteration_notes_v9impactops]] - Impact-led clinic-ops iteration note for the corrected concise operations branch
- [[clinicalhours_tiktok_iteration_notes_v10fallimpact]] - High-impact student fall discovery iteration note that folds the summer editorial style back into the durable TikTok system
