---
title: ClinicalHours TikTok Iteration Notes v3bright7 - 2026-05-19
description: Durable notes for the bright student deck after the copy-audit and screenshot-text cleanup pass
last_updated: 2026-05-19
---

# ClinicalHours TikTok Iteration Notes v3bright7

## Final output

- composition source: `composition/clinicalhours_tiktok_student_auth_v3bright.html`
- export suffix: `v3bright7`
- render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_auth_v3bright.html" -VersionSuffix v3bright7 -RunQa -GenerateQaShots
```

- result:
  - `5/5` slides passed copy audit
  - `5/5` slides passed layout QA
  - all exports verified at `1080 x 1920`

## What changed in this pass

- Removed internal strategy language from visible slide copy.
- Reframed the bright student deck around a cleaner marketing sequence:
  - start
  - map
  - preview
  - account
  - browse
- Replaced raw weak proof assets with safer crops or alternate captures.
- Added a pre-render copy and asset audit at `composition/audit_clinicalhours_tiktok_copy.ps1`.
- Wired the render entrypoint to fail early if the deck contains banned phrases or known weak raw screenshot assets.

## Final proof mapping

- Slide `1`:
  - `captures/derived/clinicalhours_map_tall_controls_focus_v1.png`
- Slide `2`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
- Slide `3`:
  - `captures/auth/clinicalhours_dashboard_hero_auth_live_v2.png`
  - `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
- Slide `4`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
  - `captures/derived/clinicalhours_journal_toolbar_tile_v2.png`
  - `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
- Slide `5`:
  - `captures/derived/clinicalhours_auth_actions_focus_v2.png`

## Canonical branch notes

- Treat `v3bright7` as the current bright student-facing export set.
- Treat `clinicalhours_tiktok_student_auth_v3bright.html` as the composition source for that branch.
- Use `pipeline/specs/clinicalhours_tiktok_student_bright_v3bright7_deck_spec.json` when a future agent needs machine-readable proof mapping.
- Read `docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19.md` before extending the bright student lane.

## Remaining judgment calls

- `v1` is still the safer default whenever the assignment does not explicitly require student marketing.
- The bright branch is now much safer against AI-sounding overlay copy, but screenshot proof still needs human taste review after every major crop change.
