# felt.bet TikTok Carousel v4 Iteration Notes

## Outcome

Created a new `v4` export set from the existing local HTML composition:

- `felt_tiktok_slide_1_v4.png`
- `felt_tiktok_slide_2_v4.png`
- `felt_tiktok_slide_3_v4.png`
- `felt_tiktok_slide_4_v4.png`
- `felt_tiktok_slide_5_v4.png`

All five exports were verified locally on `2026-05-15` as exactly `1080 x 1920`.

## What Changed

- tightened slide 2 hero cropping so the join/host flow reads faster
- enlarged slide 1 support proof so it feels less decorative and more legible
- enlarged slide 5 support panel and sharpened the close with a cleaner fine-print line
- replaced loose implicit layout discipline with explicit `data-proof` annotations on screenshot assets
- extended the local QA so it now catches proof-asset overlap against essential text
- upgraded the render script so QA warnings fail the export instead of just printing to the console

## Why These Changes Matter

The earlier versions had two recurring risks:

- text and proof could drift too close together during edits
- support crops could shrink into decorative noise

This pass makes the system more reliable for future iterations, not just prettier for one export. The carousel now has stronger guardrails against the exact issues that created overlap and crop problems before.

## Research Applied In This Pass

- TikTok’s image/carousel guidance favors fast visual storytelling, so each slide keeps one dominant promise.
- TikTok’s safe-area guidance informed the stricter local QA boundaries for essential text.
- The internal Felt retention note was used to keep the sequence centered on activation, visible state, mastery, and return instead of casino-style urgency.

## Screenshot Mapping

- `Slide 1`: `felt_home_mobile_390x844.png` + `felt_home_desktop_full.png`
- `Slide 2`: `felt_lobby_mobile_390x844.png` + `felt_lobby_desktop_full.png`
- `Slide 3`: `felt_guided_table_mobile_390x844.png` + `felt_guided_table_desktop.png`
- `Slide 4`: `felt_guided_table_mobile_feedback_390x844.png` + `felt_training_mobile_430x932.png` + `felt_guided_table_feedback.png`
- `Slide 5`: `felt_home_mobile_390x844.png` + `felt_guided_live_desktop.png`

## Files Updated

- `felt_tiktok_carousel.html`
- `render_felt_tiktok_carousel.ps1`
- `felt_tiktok_skill_mcp_guardrails_2026-05-15.md`
- `felt-tiktok-slideshow-retention-strategy-2026-05-15.md`

## Dimensions Confirmation

- `felt_tiktok_slide_1_v4.png` -> `1080 x 1920`
- `felt_tiktok_slide_2_v4.png` -> `1080 x 1920`
- `felt_tiktok_slide_3_v4.png` -> `1080 x 1920`
- `felt_tiktok_slide_4_v4.png` -> `1080 x 1920`
- `felt_tiktok_slide_5_v4.png` -> `1080 x 1920`
