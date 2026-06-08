# felt.bet TikTok Carousel v5 Iteration Notes

## Findings First: What Was Wrong With `v4`

- The overall story was good, but the layout rhythm repeated too often. Slides `1`, `2`, `3`, and `5` all leaned on a similar left-copy / right-device pattern.
- Slide `2` still felt too clipped to prove the join / host flow quickly. The screenshot read more like a crop than a clear system.
- Slide `3` had the right idea, but the strongest operational proof was trapped inside a narrow phone crop instead of getting hero treatment.
- Slide `4` had real product value, but the proof hierarchy was split across too many small competing crops.
- Slide `5` reused the home surface without enough new payoff, so the close felt calmer than `v4` but not stronger.
- Some support crops still felt decorative rather than evidentiary, and some of the dark staging felt flatter than premium.

## What I Changed And Why

- Rebuilt the composition in `composition/felt_tiktok_carousel.html` instead of lightly polishing the old layout. The new deck uses materially more varied pacing across the five slides.
- Slide `1` now uses a wide desktop home capture as the dominant proof, with a small mobile support crop that adds real specificity instead of filler.
- Slide `2` now uses fresh `v5` lobby captures and a reversed layout so the join / host flow feels faster and more distinct from slide `1`.
- Slide `3` now gives the new live guided table desktop capture almost the whole frame. This is the cleanest proof upgrade in the set.
- Slide `4` now uses a fresh training / session review desktop capture as the hero and keeps only one support crop: the clearest truthful coaching detail.
- Slide `5` now closes on a cleaner return surface with a calmer CTA and no redundant support crop, so the final slide feels more credible and less busy.
- Tightened the visual system toward sharper cream-on-dark proof, more disciplined gold use, and stronger separation between headline glance and screenshot glance.

## Screenshots Captured

Fresh captures saved for `v5`:

- `captures/home/felt_home_desktop_1440x1400_v5.png`
- `captures/home/felt_home_desktop_clean_1440x1400_v5.png`
- `captures/home/felt_home_mobile_430x932_v5.png`
- `captures/home/felt_home_mobile_clean_430x932_v5.png`
- `captures/lobby/felt_lobby_desktop_1440x1200_v5.png`
- `captures/lobby/felt_lobby_mobile_430x932_v5.png`
- `captures/training/felt_training_desktop_1440x1400_v5.png`
- `captures/training/felt_training_mobile_430x932_v5.png`
- `captures/guided/felt_guided_setup_desktop_1440x1400_v5.png`
- `captures/guided/felt_guided_live_desktop_1440x1400_v5.png`

Final slide mapping:

- `Slide 1`: `captures/home/felt_home_desktop_clean_1440x1400_v5.png` + `captures/home/felt_home_mobile_clean_430x932_v5.png`
- `Slide 2`: `captures/lobby/felt_lobby_mobile_430x932_v5.png` + `captures/lobby/felt_lobby_desktop_1440x1200_v5.png`
- `Slide 3`: `captures/guided/felt_guided_live_desktop_1440x1400_v5.png`
- `Slide 4`: `captures/training/felt_training_desktop_1440x1400_v5.png` + `captures/guided/felt_guided_table_feedback.png`
- `Slide 5`: `captures/home/felt_home_mobile_clean_430x932_v5.png`

Captured but not used in the final export:

- `captures/guided/felt_guided_setup_desktop_1440x1400_v5.png`
- `captures/training/felt_training_mobile_430x932_v5.png`

Those states were truthful and useful for decision-making, but they weakened first-glance clarity once placed in the final deck.

## Research Conclusions Actually Applied

- Used the documented `friction -> simplification -> operational proof -> mastery -> return` sequence directly.
- Kept copy secondary to proof selection. Screenshots were chosen first, then the headlines were constrained to what the UI could prove quickly.
- Used one dominant proof asset per slide and deleted weak support proof where it was not earning its space.
- Strengthened the slide `1` to slide `2` handoff by opening with a structural pain statement, then paying it off immediately with the code / lobby flow.
- Leaned on mastery and social return logic rather than gambling-coded excitement, money language, or fake urgency.
- Preserved the premium dark-mode stage while letting the real cream product surfaces do more of the persuasion work.

## Remaining Limitations

- I did not have a clean public friend-group table creation success state with real populated private-table continuity to capture.
- The strongest newly captured live table proof is still a guided solo AI state, not a true active friend table.
- The public coaching flow was less stable to recapture interactively in this session, so I intentionally kept the earlier truthful coaching detail crop because it was still the clearest evidence for slide `4`.

## Export And QA Confirmation

- Render path used: `composition/render_felt_tiktok_carousel.ps1`
- QA status: all five slides returned `QA PASS`
- Visual QA screenshots generated in `qa/screenshots/`

Exact `1080 x 1920` confirmation:

- `felt_tiktok_slide_1_v5.png` -> `1080 x 1920`
- `felt_tiktok_slide_2_v5.png` -> `1080 x 1920`
- `felt_tiktok_slide_3_v5.png` -> `1080 x 1920`
- `felt_tiktok_slide_4_v5.png` -> `1080 x 1920`
- `felt_tiktok_slide_5_v5.png` -> `1080 x 1920`
