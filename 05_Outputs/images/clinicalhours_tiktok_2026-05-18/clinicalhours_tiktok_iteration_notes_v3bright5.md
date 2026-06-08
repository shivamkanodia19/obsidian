---
title: ClinicalHours TikTok Iteration Notes v3bright5 - 2026-05-19
description: Durable proof mapping and export notes for the brighter ClinicalHours student-facing deck
last_updated: 2026-05-19
---

# ClinicalHours TikTok Iteration Notes v3bright5

## Final output

- composition source: `composition/clinicalhours_tiktok_student_auth_v3bright.html`
- export suffix: `v3bright5`
- render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_auth_v3bright.html" -VersionSuffix v3bright5 -RunQa -GenerateQaShots
```

- result:
  - `5/5` slides passed QA
  - all exports verified at `1080 x 1920`

## What changed in the polish pass

- Replaced the weaker slide `3` dashboard crop with the fuller authenticated overview plus a direct featured-clinic card.
- Collapsed slide `4` into a denser three-panel proof board: overview, journal, and saved opportunity.
- Swapped slide `5` to the tighter sign-in-card capture so the auth proof reads larger and cleaner in-feed.
- Normalized the slide `3` explainer copy to plain ASCII quotes.
- Kept the brighter editorial palette and the `Bricolage Grotesque` plus `Instrument Sans` type system from the original `v3bright` exploration.

## Final proof mapping

- Slide `1`:
  - `captures/home/clinicalhours_home_mobile_430x932_live.png`
- Slide `2`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
- Slide `3`:
  - `captures/auth/clinicalhours_dashboard_overview_auth_live_v3.png`
  - `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
- Slide `4`:
  - `captures/auth/clinicalhours_dashboard_overview_auth_live_v3.png`
  - `captures/auth/clinicalhours_journal_section_auth_live_v3.png`
  - `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
- Slide `5`:
  - `captures/auth/clinicalhours_auth_signin_card_auth_live_v3.png`

## Canonical branch notes

- Treat `v3bright5` as the current bright student-facing export set.
- Treat `clinicalhours_tiktok_student_auth_v3bright.html` as the composition source for that branch.
- Use `pipeline/specs/clinicalhours_tiktok_student_bright_v3bright5_deck_spec.json` when a future agent needs machine-readable proof mapping.
- Keep `composition/build_clinicalhours_tiktok_crop_derivatives.ps1` in the workflow because slide `2` still depends on the canonical derived map crop.

## Remaining judgment calls

- `v1` is still the safer default whenever the assignment does not explicitly require student marketing.
- The bright branch is durable now, but its proof tier still mixes public student surfaces with authenticated preview captures, so copy should stay conservative.
