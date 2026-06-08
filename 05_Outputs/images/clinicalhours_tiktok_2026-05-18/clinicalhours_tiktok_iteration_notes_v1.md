---
title: ClinicalHours TikTok Iteration Notes v1 - 2026-05-19
description: Current notes for the canonical ClinicalHours clinic-ops TikTok deck after the evidence-tightening pass
last_updated: 2026-05-20
---

# ClinicalHours TikTok Iteration Notes v1

## Final output

- Render command:
  - `.\render_clinicalhours_tiktok_carousel.ps1 -VersionSuffix v1 -RunQa -GenerateQaShots`
- Result:
  - `5/5` slides passed copy audit
  - `5/5` slides passed QA
  - all exports verified at `1080 x 1920`

## Important fixes during the latest pass

- Replaced blank or washed enterprise proof captures with element-level Playwright recaptures.
- Fixed hidden-slide QA false positives by removing non-target slides during single-slide export.
- Fixed slide 4 proof/text overlap.
- Fixed slide 5 CTA overflow.
- Fixed human-QA text-stack collisions on slides 2 and 3.
- Tightened the clinic-ops copy so the default deck stays closer to the validated small-clinic workflow wedge.
- Replaced broader supply-heavy activation copy with narrower applications, onboarding, and status language.
- Shortened the slide 5 close so the headline renders cleanly without crowding the CTA.

## Final proof mapping

- Slide 1:
  - `clinicalhours_enterprise_problem_section_live_recapture_v2.png`
- Slide 2:
  - `clinicalhours_enterprise_hero_section_live.png`
  - `clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png`
- Slide 3:
  - `clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png`
- Slide 4:
  - `clinicalhours_enterprise_platform_figure_2_live_recapture.png`
  - `clinicalhours_enterprise_trust_section_live_recapture_v2.png`
- Slide 5:
  - `clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png`
  - `clinicalhours_enterprise_mobile_430x932_live.png`

## Remaining judgment calls

- Slide 4 is intentionally more spacious than the others because the status proof reads best as a smaller, truthful landscape asset rather than a stretched portrait mockup.
- The clinic-ops lane is currently stronger than the student lane because public enterprise proof is better than the public logged-out homepage proof.
- The enterprise screenshots still contain broader site language than the internal product evidence fully validates, so future copy should keep the overlay narrower than the screenshot narrative.
