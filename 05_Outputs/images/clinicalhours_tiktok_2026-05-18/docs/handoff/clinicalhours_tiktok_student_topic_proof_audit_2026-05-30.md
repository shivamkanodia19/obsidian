---
title: ClinicalHours TikTok Student Topic-Proof Audit - 2026-05-30
description: Ranked findings across the current student-facing ClinicalHours decks, plus keep/revise/retire decisions and the chosen repair path
last_updated: 2026-05-30
---

# ClinicalHours TikTok Student Topic-Proof Audit - 2026-05-30

## Main findings

1. `v6realleads` has the weakest topic-to-proof fit. Its trust story is real, but slide `1` and slide `4` lean on text-heavy story proof and generic support panels instead of one fast visual reason to believe the claim.
2. The recurring failure mode is not fake proof. It is generic proof outranking specific proof. The biggest offenders are the broad dashboard hero, the welcome panel, and the full auth page when the topic is narrower than `account exists`.
3. `v5firstpath` had the best student sequence to save. Its weak spots were fixable with proof hierarchy changes rather than a new topic: slide `3` needed the clinic card to be the hero, and slide `4` needed the `Log Your First Hours` state to be the hero.
4. `v6guestfirst` is still viable, but the full auth page visually weights `Continue with Google` and the sign-in form more than `Browse as guest`, so the branch needs tighter guest-action proof whenever it is extended.
5. Older baselines are still useful, but they are not exempt from proof mismatch. `v3bright7` and `v4memory` both open with map-led proof that is truthful yet only indirectly proves the pain they name.

## Re-ranked branches

1. `v5firstpath` - `keep`
   Reason: strongest five-slide student sequence after the `2026-05-30` proof-hierarchy repair.
2. `v6guestfirst` - `keep`
   Reason: clean topic, credible CTA, but still wants tighter guest-action proof and less full-auth repetition.
3. `v4memory` - `revise`
   Reason: strong follow-through lane, but slide `1` still proves discovery better than lost context.
4. `v3bright7` - `revise`
   Reason: polished baseline, but broader and less issue-specific than the best newer branches.
5. `v4impact` - `revise`
   Reason: good later-stage topic, but some record/clinic continuity claims are still inferred rather than directly shown.
6. `v6realleads` - `retire`
   Reason: the truthful proof inventory is not yet specific enough to sustain the sharper trust claim across all five slides.

## Slide-by-slide issue list

### `v3bright7`

- Slide `1`: map proof shows available search, not the feeling that the search is random.
- Slide `4`: `Search, save, track, log.` is broader than the proof collage really supports.

### `v4memory`

- Slide `1`: `Found clinics. Lost track?` still starts on map/search proof instead of visible memory loss or saved-context proof.
- Slide `4`: truthful and useful, but the empty-state-adjacent support crop keeps the promise at setup and follow-through, not a mature saved workflow.

### `v4impact`

- Slide `1`: account records support later recall, but they do not fully prove the sharper `hours alone do not show impact` framing.
- Slide `3`: the clinic card plus welcome panel implies continuity, but it does not visibly prove a clinic being tied back to a later record.

### `v5firstpath`

- Slide `3`: repaired on `2026-05-30`; the featured clinic card now carries the preview claim and the broad dashboard shell is only support.
- Slide `4`: repaired on `2026-05-30`; the journal `Log Your First Hours` state now carries the first-log claim and the return-point/dashboard proof is secondary.

### `v6realleads`

- Slide `1`: the `How It Started` proof is truthful, but the key outdated-list language is too text-heavy and slow for a first-frame trust hook.
- Slide `4`: the collage repeats the story proof and mixes in generic dashboard/auth support, so `Know why it feels more credible.` outruns what the slide visibly proves.

### `v6guestfirst`

- Slide `2`: full auth proof is current and truthful, but it still lets form boilerplate compete with the guest-first promise.
- Slide `4`: account usefulness is real, but the proof is still generic enough that the claim must stay narrow.
- Slide `5`: the CTA is credible, but the same auth-heavy proof pattern should be tightened if the branch is extended again.

## Chosen repair path

- Revised branch: `v5firstpath`
- Why: it had the best lane discipline, the clearest student progression, and the smallest set of proof changes needed to become stronger end to end.
- What changed:
  - slide `3` now uses `captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png` as the hero proof
  - slide `4` now uses `captures/derived/clinicalhours_journal_cta_focus_v2.png` as the hero proof
  - the copy on both slides was narrowed to what the screenshot text visibly supports
- What stayed limited:
  - slide `4` still uses a first-run journal surface, so the branch can promise first-log direction and return-point clarity, not a completed saved workflow
  - the fresh public auth capture from `2026-05-30` confirms the guest-first state is real, but the full auth page still visually favors sign-in over guest browsing, so the tighter derived guest-action crop remains the safer CTA proof
