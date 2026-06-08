---
title: ClinicalHours TikTok Iteration Notes v6guestfirst - 2026-05-29
description: Issue-specific notes for the student guest-first branch focused on reducing signup friction before students even know if the search is worth it
last_updated: 2026-05-29
---

# ClinicalHours TikTok Iteration Notes v6guestfirst

## Final output

- composition source: `composition/clinicalhours_tiktok_student_guest_first.html`
- export suffix: `v6guestfirst`
- render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_guest_first.html" -VersionSuffix v6guestfirst -RunQa -GenerateQaShots
```

- result:
  - `COPY AUDIT PASS`
  - `5/5` slides passed layout QA
  - all exports verified at `1080 x 1920`
  - live public auth and map surfaces rechecked with Playwright on `2026-05-29`

## Topic selection

- Strategy gap filled: the earlier student decks treated `browse first` as a closing move, but not as the whole marketing topic.
- This branch isolates signup resistance as the actual student pain:
  - the first click should not demand commitment
  - guest browsing is the structural payoff
  - the map proves there is something worth seeing
  - the account is repositioned as optional follow-through, not the first hurdle

## Final proof mapping

- Slide `1`:
  - `captures/derived/clinicalhours_auth_actions_focus_v2.png`
- Slide `2`:
  - `captures/auth/clinicalhours_auth_live_2026-05-29.png`
- Slide `3`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
  - `captures/derived/clinicalhours_auth_guest_actions_v1.png`
- Slide `4`:
  - `captures/derived/clinicalhours_dashboard_welcome_panel_v1.png`
  - `captures/derived/clinicalhours_dashboard_records_band_v1.png`
  - `captures/derived/clinicalhours_journal_toolbar_tile_v2.png`
- Slide `5`:
  - `captures/auth/clinicalhours_auth_live_2026-05-29.png`

## What changed from nearby branches

- This branch is not about first-run workflow sprawl like `v5firstpath`.
- It is not about saved-search memory like `v4memory`.
- It is not about later reflections or impact recall like `v4impact`.
- It is the cleanest low-friction activation branch so far:
  - auth friction named early
  - guest-first proof shown explicitly
  - map proof arrives after the friction break
  - the account is reframed as useful later, not mandatory now

## Proof limits to preserve

- Keep the promise at `guest first`, `see the map`, `sign in when ready`, and `follow through later`.
- Do not imply the guest flow exposes the full authenticated workflow.
- Do not imply saved opportunities, application management, or a complete tracking system unless the screenshot proves it.
- Do not imply guaranteed placements, guaranteed hours, or guaranteed admissions outcomes.
- Slide `4` still relies on authenticated and empty-state-adjacent proof, so the copy must stay at account usefulness and return-point framing, not finished outcomes.
