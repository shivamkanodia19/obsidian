---
title: ClinicalHours TikTok Student Marketing Sequence And Copy Audit - 2026-05-19
description: Durable method for structuring the bright student deck and rejecting AI-sounding copy or weak screenshot text
last_updated: 2026-06-02
---

# ClinicalHours TikTok Student Marketing Sequence And Copy Audit - 2026-05-19

## Why this exists

The earlier bright student deck could pass layout QA while still shipping:

- internal strategy language in visible copy
- generic onboarding filler inside screenshots
- raw proof assets whose readable text undercut the slide claim

This note is the fix. Future agents should use it whenever they extend `v3bright` or build another student-facing branch.

Before building a new student-facing deck directly for Shivam, ask what content or topic the slides should cover.

## Canonical bright student sequence

Use this sequence for the current `student_discovery_secondary` lane:

1. Slide `1`: hook plus problem
2. Slide `2`: solution through map discovery
3. Slide `3`: preview of a real clinic
4. Slide `4`: account proof and follow-through
5. Slide `5`: low-friction CTA

Machine-role mapping for stored specs:

- `hook plus problem` -> `friction`
- `solution through map discovery` -> `discovery`
- `preview of a real clinic` -> `simplification`
- `account proof and follow-through` -> `documentation_direction`
- `low-friction CTA` -> `activation`

Current `v3bright7` mapping:

- Slide `1`: `Finding clinical hours still feels random.`
- Slide `2`: `9,512 openings. One map.`
- Slide `3`: `See the clinic before you click.`
- Slide `4`: `Search, save, track, log.`
- Slide `5`: `Browse first. Sign in later.`

## Issue-specific student exception: `v4impact`

Use a different sequence when the student problem is not discovery but later recall and impact articulation.

- Start from authenticated journal, reflections, and account-record proof.
- Favor product language the UI already uses, such as `log clinical hours`, `write reflections`, and `track your progress`.
- Keep the promise narrow: better capture now, easier retrieval later.
- Do not turn this branch into admissions-outcome copy, quantified impact claims, or `AMCAS-ready` language.

## Overlay copy rules

- Every visible line must sound like something a student could say or immediately understand.
- Headlines should stay within `4` to `8` words.
- Subtext should be one short sentence.
- Use concrete UI nouns whenever possible:
  - `map`
  - `clinic`
  - `browse`
  - `save`
  - `track`
  - `hours`
- Do not explain why the slide works.
- Do not expose the strategy taxonomy to the audience unless the assignment explicitly asks for it.

## Screenshot text rules

- The biggest readable text inside the crop must support the claim, not distract from it.
- Empty-state text cannot be the hero proof unless the slide is explicitly about first-run setup.
- Generic homepage slogans should not dominate a pain slide.
- Auth form boilerplate should not dominate a guest-first CTA slide.
- Crop to one proof action, not one entire screen.
- Reject crops that center on dark empty space while the useful control or label sits tiny in a corner.
- Reject crops that chop off the very metric, CTA, or journal label that the slide copy depends on.
- For clinic-preview slides, prefer the featured clinic card as the hero over a broader dashboard shell when the claim is about deciding whether one clinic is worth the click.
- For first-log slides, prefer the visible `Log Your First Hours` journal CTA as the hero over a generic `Welcome back` account crop when the promise is about where the first shift goes next.

## Visual variation rule

For student-facing branches, do not automatically reuse the last successful bright shell.

- Compare against the latest nearby branches before choosing colors or layout.
- If the new work still uses the same pastel gradient, rounded proof-card stack, and progress chrome, treat that as a design warning and justify it before shipping.
- Pick a visual system that fits the issue: search can feel brighter and broader; impact capture can feel more editorial and reflective.
- Variation should stay calm and relevant. Do not swap into loud novelty styling that weakens trust or mobile readability.

## Hard-fail structure patterns

- Bottom keyword pills should not be the default slide-finishing pattern. If a branch uses the same bottom chip row on most slides, treat that as visual sameness and redesign it.
- Avoid visible strategy-note cards such as `WHY IT LANDS`, `WHY IT EXISTS`, `AFTER THE PREVIEW`, or `AFTER THE FIRST SHIFT`. Those are builder labels, not audience copy.
- Avoid stacked horizontal dashboard or auth strips when none of them is clearly the hero proof. They usually signal that the crop should be tighter or that the slide claim is too broad.
- Avoid repeating the same copy-left, proof-bottom shell across most of the deck. A stronger student branch should vary slide roles while keeping the sequence clear.

## Hard-fail phrases

Reject any visible slide copy containing:

- `why this works`
- `better story`
- `calm close`
- `best student proof`
- `real search flow`
- `visual payoff`
- `cold traffic`
- `in-feed`
- `abstract promise`

Treat these as warning patterns even if phrased slightly differently:

- `prove this is`
- `preview-style proof`
- `better close`
- `feels bigger and easier`
- `should feel like`
- `why it lands`
- `why it exists`
- `after the preview`
- `after the first shift`

## Hard-fail raw assets

Do not use these as uncropped hero assets in the bright student lane:

- `captures/home/clinicalhours_home_mobile_430x932_live.png`
- `captures/auth/clinicalhours_dashboard_overview_auth_live_v3.png`
- `captures/auth/clinicalhours_journal_section_auth_live_v3.png`
- `captures/auth/clinicalhours_auth_signin_card_auth_live_v3.png`

Reason:

- their dominant visible text is generic, empty-state, or off-message for the bright student sequence

Prefer these safer proof assets:

- `captures/derived/clinicalhours_map_tall_controls_focus_v1.png`
- `captures/derived/clinicalhours_map_focus_v1.png`
- `captures/auth/clinicalhours_dashboard_hero_auth_live_v2.png`
- `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png`
- `captures/derived/clinicalhours_dashboard_records_band_v1.png`
- `captures/derived/clinicalhours_dashboard_experiences_card_v1.png`
- `captures/derived/clinicalhours_dashboard_preview_landscape_v1.png`
- `captures/derived/clinicalhours_dashboard_reflections_focus_v1.png`
- `captures/derived/clinicalhours_journal_toolbar_tile_v2.png`
- `captures/derived/clinicalhours_journal_controls_band_v1.png`
- `captures/derived/clinicalhours_journal_prompt_focus_v1.png`
- `captures/derived/clinicalhours_journal_header_band_v1.png`
- `captures/derived/clinicalhours_journal_cta_focus_v2.png`
- `captures/derived/clinicalhours_auth_guest_actions_v1.png`
- `captures/derived/clinicalhours_auth_actions_focus_v2.png`

## Required build path

1. Pick the proof assets first.
2. Write audience-facing copy against those assets.
3. Rebuild crops with `composition/build_clinicalhours_tiktok_crop_derivatives.ps1` if the screenshot text is weak.
4. Render with `composition/render_clinicalhours_tiktok_carousel.ps1`.
5. Treat the render as incomplete unless both of these pass:
   - copy and asset audit
   - layout QA plus human review

Canonical render command:

```powershell
powershell -ExecutionPolicy Bypass -File ".\05_Outputs\images\clinicalhours_tiktok_2026-05-18\composition\render_clinicalhours_tiktok_carousel.ps1" -HtmlFile "clinicalhours_tiktok_student_auth_v3bright.html" -VersionSuffix v3bright7 -RunQa -GenerateQaShots
```

## System hook

The render script now calls:

- `composition/audit_clinicalhours_tiktok_copy.ps1`

That audit currently blocks:

- known internal-strategy phrases
- known weak raw proof assets

If a future agent finds a new class of generic or AI-sounding copy, add it to the audit script and document the change here in the same pass.
