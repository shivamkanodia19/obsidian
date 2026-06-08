---
title: ClinicalHours TikTok Iteration Notes v7semesterstart - 2026-06-01
description: Issue-specific notes for the student semester-start branch focused on students starting college this fall and looking for hours during the semester
last_updated: 2026-06-01
---

# ClinicalHours TikTok Iteration Notes v7semesterstart

## Final output

- composition source: `composition/clinicalhours_tiktok_student_semester_start.html`
- export suffix: `v7semesterstart`
- render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_semester_start.html" -VersionSuffix v7semesterstart -RunQa -GenerateQaShots
```

- result:
  - `COPY AUDIT PASS`
  - `5/5` slides passed layout QA
  - all exports verified at `1080 x 1920`
  - refreshed review bundle written to `qa/review_bundles/clinicalhours_tiktok_review_bundle_v7semesterstart.json`
  - two fresh-context judges both returned `pass` on `2026-06-01`

## Topic selection

- User-selected topic: students starting college this fall and looking for hours during the semester.
- This branch narrows the semester story to four believable product moves:
  - start the search in one place
  - preview one real result before opening more tabs
  - keep the next step in a save/details card when an account becomes useful
  - browse first and sign in later

## Final proof mapping

- Slide `1`:
  - `captures/derived/clinicalhours_opportunity_header_focus_v1.png`
- Slide `2`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
- Slide `3`:
  - `captures/official/clinicalhours_opportunities_houston_methodist_live_2026-05-30.png`
  - `captures/derived/clinicalhours_opportunity_houston_result_focus_v1.png`
- Slide `4`:
  - `captures/official/clinicalhours_houston_methodist_save_dashboard_live_2026-05-30.png`
  - `captures/derived/clinicalhours_houston_save_panel_focus_v1.png`
- Slide `5`:
  - `captures/derived/clinicalhours_auth_guest_browse_focus_v2.png`

## Repair path

- Started from `v5firstpath` because it still had the strongest student sequence to save.
- Rebuilt slide `1` around the public opportunities header so the topic starts on a real search surface instead of a sparse phone strip.
- Replaced the earlier New York row crop on slide `3` after fresh judges flagged two problems:
  - the proof felt stitched together
  - the visible `1376.6 miles away` distance undermined the nearby-search reading
- Promoted the Houston Methodist live search-result capture into `captures/official/` and rebuilt slide `3` around one coherent screenshot that shows the search term, result card, city, and `More Info` link together.
- Replaced the old slide `4` first-log story entirely after judges said it jumped too early into hour tracking and made slide `5` feel like backtracking.
- Promoted the Houston Methodist save/details-panel capture into `captures/official/` and rebuilt slide `4` around the next-step card with `Save to Dashboard`, `Details`, and `Find App Link`.
- Reframed slide `5` as the closing permission cue: start now, browse first, and sign in later when saving or logging actually matters.

## What changed from nearby branches

- Compared with `v5firstpath`, this branch keeps the stronger early search sequence but drops the first-log emphasis in favor of a saved-next-step emphasis that fits semester discovery better.
- Compared with `v6guestfirst`, this branch keeps the lower-friction closing CTA but gives the topic a clearer mid-funnel proof chain before the auth reassurance lands.
- Unlike the earlier official-row repair attempt, slides `3` and `4` now stay on the same Houston Methodist example, so the proof progression reads as one continuous story instead of separate generic surfaces.

## Judge outcome

- Final judged sequence: `search -> map -> preview result -> keep the match/app step -> start now`
- Judge pass reasons converged on three points:
  - slide `3` now reads as one trustworthy proof moment
  - slide `4` now extends the same product example instead of jumping ahead to logging
  - slide `5` now lands as a closing CTA rather than a reset

## Proof limits to preserve

- Keep the promise at `start the search`, `preview a real result`, `save the next step when ready`, and `browse first, sign in later`.
- Do not imply the guest flow includes the authenticated save/app-link state.
- Do not imply guaranteed placements, guaranteed hours, guaranteed application outcomes, or guaranteed admissions outcomes.
- Do not reintroduce the stitched New York row crop for this topic unless the copy is completely reframed away from local or semester-start search relevance.
- Slide `4` now proves a signed-in next-step card, not a full application-management workflow and not a completed logged-hours workflow.
