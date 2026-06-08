---
title: ClinicalHours TikTok Handoff v1 - 2026-05-18
description: Current-state handoff for the first ClinicalHours TikTok slideshow system build
last_updated: 2026-05-18
---

# ClinicalHours TikTok Handoff v1 - 2026-05-18

## Status

This is the first ClinicalHours TikTok system pass built by adapting the best parts of the Felt workflow to ClinicalHours.

What exists now:

- lane-aware strategy notes
- human + machine rubric
- Playwright capture guidance
- QA guardrails
- a local HTML render path
- a first `clinic_ops_primary` composition

Final `v1` status:

- render passes on all `5` slides
- QA passes on all `5` slides
- exported PNGs are all `1080 x 1920`
- the first-pass blank enterprise proof captures were replaced with element-level Playwright recaptures where needed

## What Is Different From Felt

- The lane selection logic matters more.
- Evidence tiers matter more.
- The default story is clinic operations, not consumer mastery/return.
- Compliance risk is about truthfulness, medical-adjacent claims, and audience confusion rather than gambling-coded language.

## Current Best Proof Inventory

Best `clinic_ops_primary` assets:

- `captures/enterprise/clinicalhours_enterprise_hero_section_live.png`
- `captures/enterprise/clinicalhours_enterprise_problem_section_live_recapture_v2.png`
- `captures/enterprise/clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png`
- `captures/enterprise/clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png`
- `captures/enterprise/clinicalhours_enterprise_platform_figure_2_live_recapture.png`
- `captures/enterprise/clinicalhours_enterprise_outputs_section_live_recapture_v2.png`
- `captures/enterprise/clinicalhours_enterprise_trust_section_live_recapture_v2.png`
- `captures/enterprise/clinicalhours_enterprise_mobile_430x932_live.png`

Best `student_discovery_secondary` assets:

- `captures/home/clinicalhours_home_hero_section_live.png`
- `captures/map/clinicalhours_map_panel_live.png`
- `captures/auth/clinicalhours_auth_desktop_1440x1200_live.png`

## Known Weak Spots

- The student homepage lower stat block is not trustworthy proof in the current public state because it shows visible `0+` placeholders.
- The student lane has weaker public product proof than the enterprise lane.
- The public enterprise page tells a broader story than the strongest internal pilot evidence. Future agents must keep evidence tiers explicit.

## Ground Rules For The Next Agent

- Start by deciding whether the request is clinic-facing or student-facing.
- Keep one lane per deck unless explicitly told otherwise.
- Capture new proof only when it materially beats the current screenshots.
- If an enterprise proof screenshot looks blank, do not design around it. Re-capture the exact DOM element with Playwright after scrolling it into view and waiting briefly.
- Weaken the copy if the visible asset cannot fully prove the stronger claim.
- Run the render script with QA enabled before shipping.
