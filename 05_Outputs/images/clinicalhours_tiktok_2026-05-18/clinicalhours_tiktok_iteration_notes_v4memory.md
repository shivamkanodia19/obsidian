---
title: ClinicalHours TikTok Iteration Notes v4memory - 2026-05-21
description: Issue-specific notes for the student search-memory branch built from the bright student system
last_updated: 2026-05-21
---

# ClinicalHours TikTok Iteration Notes v4memory

## Final output

- composition source: `composition/clinicalhours_tiktok_student_search_memory.html`
- export suffix: `v4memory`
- render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_search_memory.html" -VersionSuffix v4memory -RunQa -GenerateQaShots
```

- result:
  - `5/5` slides passed copy audit
  - `5/5` slides passed layout QA
  - all exports verified at `1080 x 1920`

## Issue framing

- The student problem here is not that discovery is impossible.
- The student problem is that the search loses memory after a clinic is worth keeping.
- The truthful claim is narrower than a full application or admissions workflow:
  - one clearer map
  - a clinic preview before the next click
  - account and journal surfaces that give the search somewhere to save, track, and log
- The branch stays inside `product_surface` with `mixed_public_and_authenticated_preview`.

## Final proof mapping

- Slide `1`:
  - `captures/derived/clinicalhours_map_tall_controls_focus_v1.png`
- Slide `2`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
- Slide `3`:
  - `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
  - `captures/derived/clinicalhours_dashboard_welcome_panel_v1.png`
- Slide `4`:
  - `captures/derived/clinicalhours_dashboard_records_band_v1.png`
  - `captures/derived/clinicalhours_journal_controls_band_v1.png`
  - `captures/derived/clinicalhours_journal_prompt_focus_v1.png`
- Slide `5`:
  - `captures/derived/clinicalhours_auth_guest_actions_v1.png`

## What changed from nearby branches

- This branch no longer reuses the same cream-blue bright student shell as `v3bright7` or `v4impact`.
- It moves into a quieter paper-and-organizer direction with muted sage, clay, and fog accents so the slideshow feels issue-specific instead of template-repeated.
- It does not reuse `9,512 openings. One map.` as the dominant message.
- It treats map and preview as setup, then shifts the main payoff to follow-through memory after discovery.
- It stays separate from `v4impact` by avoiding post-shift recall, reflections, and admissions-story framing.
- It also tightens the screenshot hierarchy:
  - slide `3` now makes the featured clinic card the dominant readable proof
  - slide `4` replaces the awkward tall dashboard crop with records and journal control bands
  - slide `5` swaps to the tighter guest-action crop so `Browse as guest` reads cleanly

## Proof limits to preserve

- Keep the promise at `save clinics`, `track opportunities`, and `log hours`.
- Do not imply guaranteed placements, guaranteed hours, or guaranteed admissions outcomes.
- Do not imply authenticated dashboard states are the same as the guest flow.
- Do not imply AMCAS-ready export, application standardization, or a filled application pipeline unless a visible screenshot proves it.
- Slide `4` now uses stronger records and journal controls as the main proof, but the small prompt crop is still an empty-state support element, so the copy should stay at setup and follow-through, not a finished workflow.
