# ClinicalHours TikTok Iteration Notes - v2auth

Date: `2026-05-18`

## What changed

- Built an authenticated student-product deck in `composition/clinicalhours_tiktok_student_auth_v2.html`.
- Replaced weaker `v2` proof assets with sharper `v3` element captures from the live authenticated product.
- Re-rendered the deck after each crop/layout adjustment until all slides passed QA and the human review no longer showed clipped proof text.

## Capture improvements

- `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
- `captures/auth/clinicalhours_dashboard_overview_auth_live_v3.png`
- `captures/auth/clinicalhours_journal_section_auth_live_v3.png`
- `captures/auth/clinicalhours_auth_signin_card_auth_live_v3.png`

These `v3` captures were taken with Playwright after enlarging the UI and capturing the real element instead of relying on thin or loosely cropped first-pass screenshots.

## Layout decisions

- Slide 2 now uses the full featured-clinic card as a contained proof strip to avoid left-edge clipping.
- Slide 4 now uses a taller overview capture with a top-focused crop so the metric row and workflow modules read more clearly.
- Slide 5 now uses a higher-resolution sign-in card capture for cleaner export at TikTok size.

## Verification

Rendered with:

```powershell
powershell -ExecutionPolicy Bypass -File ".\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_auth_v2.html" -VersionSuffix v2auth -RunQa -GenerateQaShots
```

Result:

- all 5 slides passed QA
- all 5 exports are `1080 x 1920`
