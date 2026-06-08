---
title: ClinicalHours TikTok Iteration Notes v4expiry - 2026-05-20
description: Issue-specific notes for the light-only expiring-clearances clinic-ops branch
last_updated: 2026-05-20
---

# ClinicalHours TikTok Iteration Notes v4expiry

## Final output

- Render command:
  - `.\render_clinicalhours_tiktok_carousel.ps1 -HtmlFile clinicalhours_tiktok_clinic_expiring_clearances.html -VersionSuffix v4expiry -RunQa -GenerateQaShots`
- Result:
  - `COPY AUDIT PASS`
  - `5/5` slides passed QA
  - all exports verified at `1080 x 1920`

## Direction and issue framing

- This branch inherits Shivam's `2026-05-20` light-only preference for clinic-ops issue decks.
- The story is renewal visibility loss, not generic onboarding chaos and not broad compliance automation.
- The copy stays focused on quiet expirations, missing updates, reminder burden, and one visible status view.
- The light shell keeps pale backgrounds, dark ink copy, and blue/green/red accents instead of the inherited dark-tech stage.

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

## What changed from nearby branches

- Narrowed the story from broad clinic workflow relief to quiet renewal and expiration blind spots.
- Kept the brighter clinic-ops shell from `v4onboard` but changed the copy to center renewal follow-up, missing credential updates, and visible expiring status.
- Preserved the strong status proof on slide 4 because it is the clearest truthful support for the issue.
- Kept the CTA believable for a small clinic that wants renewal status and follow-up in one place.

## Remaining limitations

- This is still a `product_surface` / `public_site` proof set, not broad outcome validation.
- The public enterprise page still tells a broader platform story than the safest overlay copy supports.
- The expiring / overdue state is visible on the status figure, but the deck still does not prove that ClinicalHours prevents every missed renewal event.
- Slide 5 keeps the truthful public mobile enterprise screenshot as CTA context, so one asset remains visually darker than the rest of the light-only shell.
