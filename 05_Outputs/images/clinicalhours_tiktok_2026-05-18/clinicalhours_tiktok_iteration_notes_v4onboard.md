---
title: ClinicalHours TikTok Iteration Notes v4onboard - 2026-05-20
description: Issue-specific notes for the light-only onboarding-visibility clinic-ops branch
last_updated: 2026-05-20
---

# ClinicalHours TikTok Iteration Notes v4onboard

## Final output

- Render command:
  - `.\render_clinicalhours_tiktok_carousel.ps1 -HtmlFile clinicalhours_tiktok_clinic_onboarding_visibility.html -VersionSuffix v4onboard -RunQa -GenerateQaShots`
- Result:
  - `COPY AUDIT PASS`
  - `5/5` slides passed QA
  - all exports verified at `1080 x 1920`

## Direction change from review

- Shivam feedback on `2026-05-20`: the branch was too dark and should use light colors only.
- The onboarding branch now uses a light-only shell with pale backgrounds, dark ink copy, and blue/green/red accents instead of the inherited dark-tech stage.
- That preference was added to the research master brief and the onboarding future-agent prompt so later ClinicalHours clinic-ops work sees it early.

## Issue framing kept on purpose

- The deck stays inside `clinic_ops_primary`.
- The pain is onboarding visibility loss, not generic clinic-ops sprawl.
- The copy stays focused on manual chase, queue visibility, pending credentials, and live status.
- The CTA stays believable for a small clinic that wants onboarding follow-up in one place.

## Final proof mapping

- Slide 1:
  - `clinicalhours_enterprise_problem_section_live_recapture_v2.png`
- Slide 2:
  - `clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png`
- Slide 3:
  - `clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png`
- Slide 4:
  - `clinicalhours_enterprise_platform_figure_2_live_recapture.png`
- Slide 5:
  - `clinicalhours_enterprise_trust_section_live_recapture_v2.png`
  - `clinicalhours_enterprise_mobile_430x932_live.png`

## What changed from v1

- Narrowed the story from broad clinic workflow relief to onboarding blind spots.
- Rebuilt slide 2 around a single larger queue proof card.
- Enlarged the slide 4 status proof so the control claim reads faster.
- Replaced the dark composition shell with a light-only editorial healthcare treatment.

## Remaining limitations

- This is still a `product_surface` / `public_site` proof set, not broad outcome validation.
- The public enterprise page still tells a broader platform story than the safest overlay copy supports.
- Slide 5 keeps the truthful public mobile enterprise screenshot as CTA context, so one asset remains visually darker than the rest of the light-only shell.
