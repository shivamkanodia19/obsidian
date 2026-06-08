---
title: ClinicalHours TikTok Iteration Notes v5firstpath - 2026-05-28
description: Issue-specific notes for the student first-path branch after the topic-to-proof alignment repair
last_updated: 2026-05-30
---

# ClinicalHours TikTok Iteration Notes v5firstpath

## Topic-to-proof repair on 2026-05-30

- Audited the current student branches against `v3bright7`, `v4memory`, and `v4impact` for topic-to-proof fit rather than just truth and layout.
- Confirmed `v5firstpath` was the highest-upside branch to repair because its sequence was already the strongest, but slide `3` and slide `4` still let generic dashboard proof outrank the specific student topic.
- Rechecked the live public auth page with Playwright on `2026-05-30` and saved `captures/auth/clinicalhours_auth_live_2026-05-30.png` to confirm the guest-first public state is still visible.
- Rebuilt slide `3` so the featured clinic card is the dominant preview proof and the broader dashboard shell is only support.
- Rebuilt slide `4` so the visible `Log Your First Hours` journal CTA is the hero proof and the return-point/dashboard proof is now secondary.
- Narrowed the copy to what the screenshot text visibly supports instead of asking the viewer to infer a stronger workflow than the crops prove.

## Refresh on 2026-05-29

- Re-rendered the branch after updating the durable Playwright and Replicate workflow guidance in the vault.
- Added a non-claim path/progress support layer to the composition so the student story reads more intentionally from first click through first log without replacing any truthful proof asset.
- Confirmed the live Codex MCP registry now includes Playwright and `rube` in `C:\Users\shiva\.codex\config.toml`.
- Replicate MCP did not hot-load into this already running Codex session, so this refresh keeps the current truthful product proof and local support framing. The next fresh Codex session should be able to pick up the newly registered server.

## Final output

- composition source: `composition/clinicalhours_tiktok_student_first_path.html`
- export suffix: `v5firstpath`
- render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_first_path.html" -VersionSuffix v5firstpath -RunQa -GenerateQaShots
```

- result:
  - `COPY AUDIT PASS`
  - `5/5` slides passed layout QA
  - all exports verified at `1080 x 1920`
  - browser QA pass through Playwright localhost preview, with only a favicon 404 outside the slide system
  - topic-to-proof repair re-render completed on `2026-05-30`

## Issue framing

- The student problem here is not only discovery scarcity and not later admissions-story recall.
- The student problem is that the first student workflow still feels scattered:
  - no obvious first click
  - too many tabs after the search begins
  - no obvious home for the first logged shift
- The truthful claim is narrower than a full application or admissions workflow:
  - one clearer start
  - one map
  - one clinic preview before the next click
  - one account flow that makes the first log easier to start and easier to find later
- The branch stays inside `product_surface` with `mixed_public_and_authenticated_preview`.

## Final proof mapping

- Slide `1`:
  - `captures/derived/clinicalhours_home_mobile_start_focus_v1.png`
- Slide `2`:
  - `captures/derived/clinicalhours_map_focus_v1.png`
- Slide `3`:
  - `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
  - `captures/auth/clinicalhours_dashboard_hero_auth_live_v2.png`
- Slide `4`:
  - `captures/derived/clinicalhours_journal_cta_focus_v2.png`
  - `captures/derived/clinicalhours_journal_toolbar_tile_v2.png`
  - `captures/derived/clinicalhours_dashboard_welcome_panel_v1.png`
- Slide `5`:
  - `captures/derived/clinicalhours_auth_guest_actions_v1.png`

## What changed from nearby branches

- This branch starts earlier than `v4memory` and `v4impact`.
- It is about the first practical student path:
  - where to click first
  - how to narrow the search
  - how to keep one clinic in view
  - where the first hours log should go
- It keeps the brighter student lane but shifts the palette and type pairing so it does not read like a direct `v3bright7` copy.
- It stays separate from `v4memory` by focusing on the first-run path instead of the memory problem after discovery.
- It stays separate from `v4impact` by avoiding reflections, impact language, and later-story framing.
- After the `2026-05-30` repair, it also makes the proof progression more specific:
  - slide `3` now centers the clinic card instead of a generic dashboard shell
  - slide `4` now centers the first-log CTA instead of a generic welcome state

## Proof limits to preserve

- Keep the promise at `start`, `browse`, `preview`, `log hours`, and `find the record later`.
- Do not imply guaranteed placements, guaranteed hours, or guaranteed admissions outcomes.
- Do not imply authenticated dashboard states are the same as the guest flow.
- Do not imply AMCAS-ready export, application standardization, or a filled application pipeline unless a visible screenshot proves it.
- Slide `4` now uses the journal CTA as the hero proof, but it still depends on a first-run empty-state-adjacent student surface, so the copy should stay at first-run setup and follow-through, not a finished logged workflow.
- The fresh `2026-05-30` auth recheck confirmed the public guest-first state is still real, but the full page still gives `Continue with Google` and the sign-in form more visual weight than `Browse as guest`, so the tighter derived guest-action crop remains the safer CTA proof for this branch.
