---
title: ClinicalHours TikTok Playwright Future-Agent Playbook - 2026-05-18
description: Capture and render workflow for rebuilding or extending the ClinicalHours TikTok slideshow
last_updated: 2026-05-29
---

# ClinicalHours TikTok Slideshow Playwright Future-Agent Playbook - 2026-05-18

## Purpose

This is the end-to-end execution playbook for future agents who need to rebuild or extend the ClinicalHours TikTok slideshow with Playwright and the local HTML export system.

Read this after the higher-level replication contract:

- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]

## Read Before Touching Anything

Read these first:

- `02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18.md`
- `02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18.md`
- `02_Analyst/projects/ClinicalHours/Strategy/ClinicalHours-Product-Map.md`
- `02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07.md`
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_skill_mcp_guardrails_2026-05-18.md`
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist.md`
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19.md`
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/clinicalhours_live_capture_notes_2026-05-18.md`

## MCP Setup In This Environment

- Codex reads MCP servers from `C:\Users\shiva\.codex\config.toml`.
- Keep `[mcp_servers.playwright]` for truthful browser capture and `[mcp_servers.rube]` for Replicate-backed support imagery in the same registry.
- If you add or change an MCP server, start a fresh Codex session before expecting those tools to appear.

## Current Composition Variants

- `composition/clinicalhours_tiktok_carousel.html` - canonical clinic-ops `v1`
- `composition/clinicalhours_tiktok_clinic_onboarding_visibility.html` - light-only clinic-ops branch for onboarding visibility loss
- `composition/clinicalhours_tiktok_clinic_expiring_clearances.html` - light-only clinic-ops branch for quiet expirations and renewal visibility
- `composition/clinicalhours_tiktok_student_auth_v2.html` - authenticated student-product `v2auth`
- `composition/clinicalhours_tiktok_student_auth_v3bright.html` - brighter student-facing `v3bright`, with the current canonical exports in `v3bright7`
- `composition/clinicalhours_tiktok_student_impact_story.html` - issue-specific student-facing `v4impact` branch for reflections, recall, and later impact articulation
- `composition/clinicalhours_tiktok_student_real_leads.html` - issue-specific student-facing `v6realleads` branch for stale lists, trust, and lead quality
- `composition/clinicalhours_tiktok_student_guest_first.html` - issue-specific student-facing `v6guestfirst` branch for browsing before signup

## Mission

Do not treat the first ClinicalHours deck as the final creative system.

Use the current system for:

- lane selection
- proof inventory
- safe-zone QA
- export reliability

The next version should outperform the current one on:

- proof clarity
- screenshot quality
- lane discipline
- copy precision
- deck pacing
- technical cleanliness

## Interactive Intake Rule

If Shivam is asking directly for a new ClinicalHours deck, ask what content or topic the slides should cover before choosing a lane, capturing proof, or writing copy.

If that is still ambiguous, ask one short follow-up about audience or CTA.

## Current Public States Confirmed On 2026-05-18

Strongest `clinic_ops_primary` states:

- enterprise hero
- enterprise problem section
- enterprise platform figures
- enterprise outputs list
- enterprise trust signals
- enterprise demo CTA

Strongest `student_discovery_secondary` states:

- home hero
- map page
- auth page

Weak state to avoid:

- student-home placeholder stat cards with visible `0+`

## Capture Rules

- Always capture the full truthful screen first.
- Save the uncropped original before making derived crops.
- Prefer stable logged-out public states unless a private test state is explicitly approved.
- Do not capture browser chrome.
- Do not capture private or patient-identifiable data.
- Do not invent stronger proof by redrawing or "cleaning up" the UI into something the product does not actually show.
- Even when Replicate MCP is used later for support imagery, every claim-bearing screenshot or crop must originate from a truthful live capture saved under `captures/`.
- On the enterprise page, prefer element screenshots for real `figure` and `section` blocks instead of rough viewport crops.
- For platform figures and proof sections, call `scrollIntoViewIfNeeded()` and wait roughly `1-2` seconds before the screenshot. Some first-pass captures looked blank when this step was skipped.

## Suggested Naming Pattern

- `clinicalhours_<surface>_<device>_<dimensions>_live.png`
- `clinicalhours_<surface>_<detail>_live.png`

## Workflow

### 1. Pick one lane first

Choose:

- `clinic_ops_primary`
- `student_discovery_secondary`
- `two_sided_network_explainer`

Do not mix them casually.

### 2. Critique the current deck before capturing new proof

Look for:

- repeated layout rhythm
- proof assets that are too small
- copy stronger than the screenshot
- decorative support crops
- unclear lane selection

### 3. Capture better proof states

For `clinic_ops_primary`, prioritize:

- enterprise hero
- enterprise problem section
- applications figure
- credentialing / HIPAA figure
- live status figure
- outputs list
- trust signals
- demo CTA

Best currently validated element-level proof assets:

- `clinicalhours_enterprise_problem_section_live_recapture_v2.png`
- `clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png`
- `clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png`
- `clinicalhours_enterprise_platform_figure_2_live_recapture.png`
- `clinicalhours_enterprise_trust_section_live_recapture_v2.png`
- `clinicalhours_enterprise_outputs_section_live_recapture_v2.png`

For `student_discovery_secondary`, prioritize:

- home hero
- map and filter panel
- auth page
- how-it-works section

After the proof capture is locked, optional Replicate support imagery can be added for atmosphere, devices, or editorial framing, but it must remain secondary to the saved proof.

### 4. Write copy only after proof selection

Rule:

- screenshot first
- copy second

Why:

- ClinicalHours can easily drift into claims that outrun the visible asset

### 5. Use local composition and render

Canonical files:

- `composition/clinicalhours_tiktok_carousel.html`
- `composition/clinicalhours_tiktok_clinic_onboarding_visibility.html`
- `composition/clinicalhours_tiktok_clinic_expiring_clearances.html`
- `composition/clinicalhours_tiktok_student_impact_story.html`
- `composition/render_clinicalhours_tiktok_carousel.ps1`

Render command:

```powershell
.\render_clinicalhours_tiktok_carousel.ps1 -VersionSuffix v1 -RunQa -GenerateQaShots
```

### 6. Machine QA

The local HTML + script system should enforce:

- safe-zone compliance
- no essential-text overflow
- no essential-text overlap with proof
- exact `1080 x 1920`

### 7. Human QA

Ask:

1. can I understand the slide in under 2 seconds?
2. does the hero asset actually prove the claim?
3. is the lane obvious?
4. is any claim stronger than the current evidence tier supports?
5. does the CTA feel calm and credible?

## Fast Decision Rules

If choosing between two proof assets:

- pick the one that makes the claim more believable

If choosing between two copy options:

- pick the weaker copy if it is the truthful one

If a crop depends on tiny text:

- enlarge it or replace it

If a slide mixes student and clinic language:

- split the lane or rewrite it

## Practical Brief For The Next Agent

`Build one five-slide ClinicalHours TikTok deck inside a single lane. Use real public ClinicalHours captures as the hero proof. Keep every claim inside its evidence tier. Before export, run the local render script with QA enabled and fix every warning.`
