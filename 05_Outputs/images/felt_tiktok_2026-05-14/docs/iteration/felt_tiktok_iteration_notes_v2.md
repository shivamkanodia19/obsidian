# felt.bet TikTok Carousel v2 Iteration Notes

## Outcome

Created a stronger `v2` set from the existing local HTML build and real felt.bet screenshots:

- `felt_tiktok_slide_1_v2.png`
- `felt_tiktok_slide_2_v2.png`
- `felt_tiktok_slide_3_v2.png`
- `felt_tiktok_slide_4_v2.png`
- `felt_tiktok_slide_5_v2.png`

All five exports were verified locally on `2026-05-14` as exactly `1080 x 1920`.

## What I Changed And Why

### Deck-level changes

- Removed the failed create-table state from hero treatment. The prior deck gave too much weight to a red error banner, which weakened trust and made the product feel unstable.
- Rebuilt the sequence around clearer emotional pacing: `tension -> relief -> control -> mastery -> invitation`.
- Shifted the system from "headline poster plus decorative screenshots" to "one hero crop, one proof accent, one fast message."
- Reduced muddy ambient gold. Gold now acts as a signal color for brand, labels, and CTA moments, while felt-green carries product depth and action.
- Added a local single-slide export mode to `felt_tiktok_carousel.html` so each PNG could be re-rendered cleanly from the same composition source.

### Slide-by-slide changes

- `Slide 1`: Reframed the opener around tension and curiosity. The hero is now a large real felt.bet welcome flow with a smaller lobby phone as proof, instead of a cluttered three-device stack with an error-state panel.
- `Slide 2`: Turned the second frame into the clean payoff. The centered mobile crop now emphasizes hosting and joining with one code, with small supporting crops that make the setup feel tangible in under two seconds.
- `Slide 3`: Rebuilt the operational proof slide around a live table-state desktop view instead of the dimmed host-panel/error composition. The goal was to show organization and visibility, not "create table" friction.
- `Slide 4`: Made coaching the differentiator. The main frame now prioritizes the live feedback moment, with training UI as support rather than competition.
- `Slide 5`: Reworked the close to feel premium and product-led. The CTA is now a restrained dark card with a gold edge, while the main phone crop shows `Play with friends`, `Join with a code`, and training adjacency more clearly.

## Design Philosophy Used

### Quiet Signal

This version leans into a premium dark field where the product is the brightest object in the frame. The background is not meant to entertain on its own; it exists to create pressure and quiet so the real felt.bet UI feels illuminated, deliberate, and worth focusing on. The deck should stop scroll through contrast and composure, not through noise.

Warm gold is treated as signal, not wallpaper. It should mark brand, sequence, and action, but never flood the frame. Felt-green carries the sense of product competence, table depth, and continuity from slide to slide. The visual rhythm works best when gold creates the first spark of attention and green holds the eye inside the UI.

Each slide is built around one dominant proof crop and one supporting proof accent. That keeps the message legible in under two seconds and prevents the carousel from feeling like a template with interchangeable screenshots. The sequence should feel progressively more specific: from abstract pain, to simple setup, to visible control, to coaching value, to a calm invitation.

The craftsmanship goal was restraint. Real felt.bet screenshots remain the hero, but their crops, scale, overlap, and glow are tuned so the work feels intentional rather than raw. The deck should read like a polished product story, not a casino ad, not a generic growth template, and not a mockup disconnected from the actual UI.

## Research Findings Actually Applied

- `TikTok hook speed`: TikTok's current performance guidance emphasizes the hook in the first `6` seconds and the proposition in the first `3`. I translated that into shorter headlines, fewer support lines, and a faster reveal on slide 2.
- `Narrative pacing beats feature dumping`: TikTok's carousel/image guidance rewards a clear sequence more than five unrelated product claims. I used a beginning-middle-end progression across the five slides instead of repeating the same layout rhythm.
- `One CTA across the set`: TikTok carousel guidance uses a single CTA across the creative. That is why slide 5 resolves the whole story with one restrained product card instead of turning each slide into its own mini-ad.
- `Warm vs cool attention`: Current color-attention research suggests warm hues are better for first-hit arousal while cooler hues support longer concentration. I used that to push more gold into slides 1 and 5, and more green into slides 2 and 4.
- `Hierarchy through limited accents`: Nielsen Norman Group's visual-hierarchy guidance supports using bright accents sparingly and giving each frame one clear winner. That is why the deck avoids broad gold fills and reduces screenshot clutter.
- `Dark-mode readability`: Accessibility and dark-theme guidance support stronger luminance contrast than designers often expect on dark surfaces. I increased headline-to-background contrast and avoided thin low-contrast support copy.

## Color Psychology Rationale

- `Espresso black`: provides seriousness, premium restraint, and a clean stage for the light UI surfaces.
- `Felt green`: signals depth, calm control, and product continuity. It also keeps the product feeling like a real tool rather than a hypey ad.
- `Warm gold`: acts as the attention pin. It is strongest on the opener, micro-labels, and the close so the sequence starts with a spark and ends with a confident invitation.
- `Cream UI surfaces`: preserve the truth of the real felt.bet product and create immediate contrast against the dark composition shell.

Approximate visual split used in the final deck:

- `80%` espresso-black / dark neutrals
- `15%` felt-green atmosphere and product accents
- `5%` warm-gold signal moments

## Screenshot-to-Slide Mapping

- `Slide 1`: `felt_home_desktop_full.png` + `felt_lobby_mobile_390x844.png`
- `Slide 2`: `felt_lobby_mobile_390x844.png` used as hero plus two supporting crops
- `Slide 3`: `felt_guided_table_desktop.png` used as hero plus supporting detail crop
- `Slide 4`: `felt_guided_table_mobile_feedback_390x844.png` + `felt_guided_table_feedback.png` + `felt_training_mobile_430x932.png`
- `Slide 5`: `felt_home_mobile_390x844.png` + `felt_guided_live_desktop.png`

## Remaining Limitations

- The real felt.bet table/training UI naturally contains cards, pots, and action controls. I de-emphasized those areas through crop choice and bottom fade treatment, but they are still present because the brief required real product truth.
- The inaccessible completed hosted-table creation flow is still unavailable, so the deck uses the strongest truthful states that were captured in-session rather than a fresh "completed host setup" state.
- If this runs as a paid TikTok carousel ad rather than an organic slideshow, TikTok's current specs indicate music is required at the ad level. That is outside the PNG export scope but should be handled in ad assembly.

## Dimensions Confirmation

Verified locally with PowerShell image metadata:

- `felt_tiktok_slide_1_v2.png` -> `1080 x 1920`
- `felt_tiktok_slide_2_v2.png` -> `1080 x 1920`
- `felt_tiktok_slide_3_v2.png` -> `1080 x 1920`
- `felt_tiktok_slide_4_v2.png` -> `1080 x 1920`
- `felt_tiktok_slide_5_v2.png` -> `1080 x 1920`

## Sources Used

- TikTok creative best practices for performance ads: <https://ads.tiktok.com/help/article/creative-best-practices>
- TikTok specifications for carousel ads: <https://ads.tiktok.com/help/article/specifications-for-carousel-ads>
- TikTok image ads / carousel ads playbook: <https://ads.tiktok.com/business/library/Image_Ads_Carousel_Ads_Playbook.pdf>
- TikTok image ads visual marketing guide: <https://ads.tiktok.com/business/en-US/blog/tiktok-image-ads-visual-marketing-guide>
- Nielsen Norman Group visual design principles: <https://media.nngroup.com/media/articles/attachments/Principles_Visual_Design-A4.pdf>
- University of Nottingham Ningbo China color-attention research: <https://research.nottingham.edu.cn/en/publications/impact-of-color-hues-on-arousal-concentration-and-visual-attentio/>
- W3C contrast minimum guidance: <https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html>
