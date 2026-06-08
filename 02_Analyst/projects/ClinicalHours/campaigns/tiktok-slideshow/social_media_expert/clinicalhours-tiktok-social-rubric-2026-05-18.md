---
title: ClinicalHours TikTok Social Rubric - 2026-05-18
description: Human-readable scoring logic for ClinicalHours TikTok slides and decks
last_updated: 2026-05-29
tags: [clinicalhours, tiktok, rubric, qa, social]
---

# ClinicalHours TikTok Social Rubric - 2026-05-18

## Purpose

This rubric turns the new ClinicalHours slideshow system into a grading layer future agents can use to:

- score individual slides
- group passed slides into one valid deck
- reject slides that overclaim, mix lanes, or weaken trust

## Required Context

Read these before generating or grading:

- `02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18.md`
- `02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18.md`
- `02_Analyst/projects/ClinicalHours/Strategy/ClinicalHours-Product-Map.md`
- `02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07.md`
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist.md`

## User Intent Gate

When working directly with Shivam on a new ClinicalHours slide request:

- ask what content or topic the slides should cover before choosing a lane
- if that answer is still ambiguous, ask one short follow-up about audience or CTA

Only skip this when the task is automated or the answer is already explicit in the request.

## Hard Fail Rules

Reject immediately if any slide:

- fabricates UI states
- uses generated support imagery as claim-bearing proof
- shows patient-identifiable data
- uses fake partner logos or fake adoption metrics
- relies on the homepage `0+` placeholder stats as proof
- claims guaranteed admissions, guaranteed clinical hours, or guaranteed staffing outcomes
- claims certification or compliance status not visibly or textually supported
- makes broader validated claims than the chosen evidence tier allows

## Lane Declaration

Every slide and deck must declare one lane:

- `clinic_ops_primary`
- `student_discovery_secondary`
- `two_sided_network_explainer`

If the slide visually or verbally mixes lanes with no clear reason, it should score down.

Every deck should also declare:

- one canonical `evidence_tier`: `validated_pilot`, `product_surface`, or `market_hypothesis`
- one `proof_access`: `public_site`, `authenticated_preview`, or `mixed_public_and_authenticated_preview`

Visible role labels may vary, but the stored machine role should stay canonical.

## Slide Role Templates

### `clinic_ops_primary`

1. `friction`
2. `unification`
3. `workflow_proof`
4. `control`
5. `activation`

### `student_discovery_secondary`

1. `friction`
2. `discovery`
3. `simplification`
4. `documentation_direction`
5. `activation`

## Slide Scoring Scale

- `1` = fail
- `2` = weak
- `3` = needs revision
- `4` = pass
- `5` = strong pass

## Slide Rubric

### A. Truth And Compliance

Pass signals:

- claim matches declared evidence tier
- screenshot is truthful
- no PHI
- no fake or unsourced quantitative proof
- no admissions bait
- no medical-compliance overclaim

### B. Message Clarity

Pass signals:

- one dominant idea
- lane is obvious
- meaning is clear in about `2 seconds`
- subtext supports the headline instead of rescuing it

### C. Product-Led Proof

Pass signals:

- hero asset visibly proves the claim
- support crop adds real explanatory value
- generated support imagery, if any, stays clearly secondary to real proof
- screenshot does more work than styling

### D. Visual Restraint

Pass signals:

- calm healthcare-infrastructure tone
- clinical blue and green are purposeful
- red is used only for friction or warning
- eye path from headline to proof is strong

### E. Technical Export

Pass signals:

- `1080 x 1920`
- sharp text
- no clipping
- safe-zone compliance
- no essential-text overlap with proof

## Slide Approval Rule

Approve only if:

- all hard-fail rules pass
- weighted score is at least `4.2`
- every category is at least `4`
- the slide matches its lane and role

Revise if:

- weighted score is between `3.0` and `4.19`
- no hard fail triggered

Reject if:

- any hard fail triggers
- weighted score is below `3.0`
- role or lane mismatch is severe

## Deck Assembly Rules

- Use exactly `5` slides.
- Use one lane only unless the assignment explicitly requests a two-sided explainer.
- Use only slide-approved assets.
- Prefer one hero proof asset per slide.
- Maximum `2` support proof crops per slide.
- Do not repeat the same hero state on adjacent slides.
- Final slide may contain the strongest CTA, but it must still feel credible.

## Deck Rubric

### A. Role Coverage And Order

Pass signals:

- all required roles are present
- order is correct for the declared lane
- each slide belongs in its slot

### B. Narrative Flow

Pass signals for `clinic_ops_primary`:

- slide `1` names the manual pain
- slide `2` shows the cleaner system
- slide `3` proves one workflow
- slide `4` proves control or trust
- slide `5` offers a believable next step

### C. Visual Variety

Pass signals:

- deck feels like one system
- slides are not near-duplicates
- layout rhythm changes enough to preserve attention

### D. Proof Progression

Pass signals:

- proof gets more specific as the deck progresses
- the viewer feels they are going deeper into the product
- no slide exists only for decoration

### E. CTA Credibility

Pass signals:

- final slide closes calmly
- CTA matches the lane
- no desperation or fake urgency

## Deck Approval Rule

Approve only if:

- all five slides are already slide-approved
- roles are present in order
- deck weighted score is at least `4.3`
- every deck category is at least `4`

## What Agents Should Store

- `asset_id` or `deck_id`
- lane
- intended role
- source captures
- evidence tier
- copy used
- hard-gate results
- category scores
- weighted score
- status: `approved`, `revise`, or `rejected`
- revision notes
