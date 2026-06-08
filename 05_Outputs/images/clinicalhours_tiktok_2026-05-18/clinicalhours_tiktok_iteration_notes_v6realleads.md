---
title: ClinicalHours TikTok Iteration Notes v6realleads - 2026-05-29
description: Issue-specific notes for the student real-leads branch focused on stale lists, trust, and proving a clinic is worth the click
last_updated: 2026-05-29
---

# ClinicalHours TikTok Iteration Notes v6realleads

## Final output

- composition source: `composition/clinicalhours_tiktok_student_real_leads.html`
- export suffix: `v6realleads`
- render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_real_leads.html" -VersionSuffix v6realleads -RunQa -GenerateQaShots
```

- result:
  - `COPY AUDIT PASS`
  - `5/5` slides passed layout QA
  - all exports verified at `1080 x 1920`
  - live site rechecked with Playwright on `2026-05-29`

## Topic selection

- Strategy gap filled: the earlier student branches covered discovery, search memory, impact recall, and the first practical path, but they did not isolate the trust problem around stale lists and weak lead quality.
- This branch is for skeptical students who do not just want more options; they want a clearer signal that the opportunity is real and current.
- The marketing angle is narrower than `find hours faster`:
  - outdated lists and word of mouth are the pain
  - one live map is the structural payoff
  - one featured clinic card proves the lead is worth the click
  - browse-first auth keeps the CTA calm instead of pushy

## Final proof mapping

- Slide `1`:
  - `captures/home/clinicalhours_home_our_story_live_2026-05-29.png`
- Slide `2`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
- Slide `3`:
  - `captures/auth/clinicalhours_dashboard_hero_auth_live_v2.png`
  - `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
- Slide `4`:
  - `captures/home/clinicalhours_home_our_story_live_2026-05-29.png`
  - `captures/derived/clinicalhours_dashboard_welcome_panel_v1.png`
  - `captures/derived/clinicalhours_auth_actions_focus_v2.png`
- Slide `5`:
  - `captures/auth/clinicalhours_auth_live_2026-05-29.png`

## What changed from nearby branches

- This branch is not about the first click through the first logged shift.
- It does not center later recall like `v4impact`, and it does not center losing track after discovery like `v4memory`.
- It uses a warmer trust-and-signal frame:
  - story proof that names the pain
  - map proof that concentrates the search
  - clinic-card proof that shows a lead is active now
  - a browse-first CTA that reduces signup skepticism

## Proof limits to preserve

- Keep the promise at `real opportunities`, `one map`, `featured clinic preview`, and `browse first`.
- Do not imply all listed opportunities are verified in real time.
- Do not imply guaranteed placements, guaranteed hours, or guaranteed admissions outcomes.
- Do not turn the student founder-story screenshot into a claim about national trust or universal success.
- The browse-first auth proof supports a low-friction CTA, not a full application or saved-shortlist workflow.
