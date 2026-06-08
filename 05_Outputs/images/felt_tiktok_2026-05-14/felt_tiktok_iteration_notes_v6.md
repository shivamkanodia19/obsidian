# felt.bet TikTok Carousel v6 Iteration Notes

## Findings First: What Still Needed Work After `v5`

- Slide `2` still overclaimed versus the proof. The crop showed `host` and `join`, but not `whole crew in`, `share`, or `rejoin` strongly enough.
- Slide `4` proved `training` better than `review`. The hero was clean, but the review logic and coaching detail were still too distant.
- Slide `5` had the weakest proof-to-claim match. The home mobile surface was truthful, but it did not really prove `home base` or social continuity.
- The deck rhythm was improved in `v5`, but slides `1`, `3`, `4`, and `5` still repeated a similar top-left-copy / lower-proof cadence.

## What I Changed And Why

- Tightened slide `2` into a more truthful claim: `Host it. Join by code.` The layout now gives the desktop lobby state the hero role so the `start a new table` and `paste invite code` paths read faster, with the mobile lobby capture acting as support instead of carrying the whole slide.
- Tightened slide `3` copy from a social-feeling claim to a direct operational one: `Stacks. Board. Next move.` That better matches the guided live table proof the product can currently show.
- Rebuilt slide `4` around fresher review proof. The hero now uses a new Playwright capture of the training surface with populated `Session Review` metrics, and the coaching inset was enlarged so the `see the leak` idea is more legible.
- Reframed slide `5` away from the weaker `home base` claim toward a more truthful two-speed return loop: `Table night or quick reps.` That better matches the actual home surface, which clearly shows `Play with friends` plus `Practice vs AI`.
- Preserved the local HTML + PowerShell export path so the slide deck still benefits from the existing safe-zone and overlap QA checks.
- Added a reusable prompt-system playbook for future image/prompt refinement work:
  - `docs/playbooks/felt_tiktok_codex_image_prompt_system_v6_2026-05-16.md`

## Screenshots Captured

Fresh `v6` source captures saved with Playwright:

- `captures/home/felt_home_desktop_1440x1200_v6.png`
- `captures/home/felt_home_mobile_430x932_v6.png`
- `captures/lobby/felt_lobby_desktop_1440x1200_v6.png`
- `captures/lobby/felt_lobby_mobile_430x932_v6.png`
- `captures/training/felt_training_desktop_review_1440x1200_v6.png`
- `captures/guided/felt_guided_coach_desktop_1440x1200_v6.png`

## Final Slide Mapping

- `Slide 1`: `captures/home/felt_home_desktop_clean_1440x1400_v5.png` + `captures/home/felt_home_mobile_clean_430x932_v5.png`
- `Slide 2`: `captures/lobby/felt_lobby_desktop_1440x1200_v6.png` + `captures/lobby/felt_lobby_mobile_430x932_v6.png`
- `Slide 3`: `captures/guided/felt_guided_live_desktop_1440x1400_v5.png`
- `Slide 4`: `captures/training/felt_training_desktop_review_1440x1200_v6.png` + `captures/guided/felt_guided_table_feedback.png`
- `Slide 5`: `captures/home/felt_home_mobile_clean_430x932_v5.png`

## Remaining Limitations

- I still did not get a clean public `rejoin` or active friend-table continuity state. Slide `2` is now more truthful, but it still proves host/join better than true return-to-room behavior.
- The strongest live table proof is still a guided solo AI table, not a real populated private friend table.
- Slide `5` now closes on a more truthful `friends or reps` return loop, but it is still not a literal social continuity state.

## Export And QA Confirmation

- Render path used: `composition/render_felt_tiktok_carousel.ps1`
- Command used:

```powershell
.\render_felt_tiktok_carousel.ps1 -VersionSuffix v6 -RunQa -GenerateQaShots
```

- QA status: all five slides returned `QA PASS`
- Visual QA screenshots generated in `qa/screenshots/`

Exact `1080 x 1920` confirmation:

- `felt_tiktok_slide_1_v6.png` -> `1080 x 1920`
- `felt_tiktok_slide_2_v6.png` -> `1080 x 1920`
- `felt_tiktok_slide_3_v6.png` -> `1080 x 1920`
- `felt_tiktok_slide_4_v6.png` -> `1080 x 1920`
- `felt_tiktok_slide_5_v6.png` -> `1080 x 1920`
