---
title: ClinicalHours TikTok System Handoff - 2026-05-19
description: Durable handoff describing the current canonical deck variants, read order, and replication risks
last_updated: 2026-06-02
---

# ClinicalHours TikTok System Handoff - 2026-05-19

## What Is Canonical Right Now

The slideshow system now has multiple durable output paths, but they still serve different jobs.

- `v1` is the canonical `clinic_ops_primary` path. It has the strongest traceability because it has iteration notes, QA screenshots, exports, and a machine-readable deck spec in `pipeline/specs/`.
- `v4onboard` is the issue-specific clinic-ops path for onboarding visibility loss. It keeps the light-only clinic-ops shell and has exports, QA screenshots, iteration notes, and a matching deck spec.
- `v4expiry` is the issue-specific clinic-ops path for quiet expirations and renewal visibility. It keeps the same light-only clinic-ops shell and has exports, QA screenshots, iteration notes, and a matching deck spec.
- `v8conciseops` is a recorded concise clinic-ops experiment, but it is not the preferred future baseline. Keep it as a cautionary branch showing what happens when the copy gets shorter without enough slide-role variation or screenshot simplification.
- `v9impactops` is the current concise clinic-ops correction branch. It keeps the shorter-copy goal, but replaces the weaker `v8conciseops` proof framing with clearer queue, review, output, and trust states plus stronger slide-role variation.
- `v2auth` is the clearest documented authenticated student-product path. It has exports, QA screenshots, an alternate HTML composition, and iteration notes tied to upgraded `auth` captures.
- `v3bright` is now the current bright student-facing path. Its latest canonical export set is `v3bright7`, and it now has an HTML composition, QA screenshots, a dedicated iteration note, a machine-readable deck spec, a companion visual-strategy note, and a pre-render copy audit.
- `v4impact` is the issue-specific student path for later-stage impact articulation. It uses authenticated journal, reflection, and account surfaces, and has exports, QA screenshots, iteration notes, and a matching deck spec.
- `v4memory` is the issue-specific student path for losing track after discovery. It uses a quieter paper-and-organizer direction, centers save-and-track follow-through, and has exports, QA screenshots, iteration notes, and a matching deck spec.
- `v5firstpath` is the issue-specific student path for the first practical path from first click through first logged shift. Its `2026-05-30` repair tightened topic-to-proof fit by making the featured clinic card and the visible first-log CTA the dominant proof moments.
- `v6realleads` is the issue-specific student trust path for stale lists, word of mouth, and whether a clinic is worth the click. It has durable artifacts, but the current branch still has the weakest topic-to-proof fit and should be revised or retired before reuse.
- `v6guestfirst` is the issue-specific student activation path for browsing before signup. It has durable artifacts and a narrow topic, but still benefits from tighter guest-action proof and less full-auth repetition.
- `v7semesterstart` is the strongest current student-facing reference for visual variety, proof continuity, and logical `search -> check -> save -> browse first` sequencing. It should be treated as the best current quality benchmark for student decks, but not as the next universal template.

## Recommended Starting Point

Start from `v1` unless the assignment explicitly needs student-facing storytelling.

Why:

- the clinic-ops lane still has the strongest truthful public proof
- the capture-to-copy mapping is clearest there
- the pipeline artifacts already describe that deck path

If the assignment wants fewer words and more impact, use `v7semesterstart` as the quality benchmark for slide-role variation, proof continuity, and pacing, then adapt that discipline to the correct lane.

If the assignment is concise clinic-ops specifically, inspect `v9impactops` before you invent a new shell. It is the current clinic-ops example of that benchmark being applied well enough to reuse.

Do not use `v8conciseops` as the baseline shell for concise work. Only inspect it as a cautionary example of failure modes to avoid: visually repetitive slides, screenshot-led copy that still feels too wordy, and proof crops that do not become clearer just because the headlines are shorter.

Choose `v2auth` or `v3bright` only when the ask is clearly about student discovery, authenticated workflow, or a brighter consumer-marketing tone.

Choose `v4impact` when the student problem is not finding experiences, but remembering, documenting, and later explaining what mattered.

Choose `v4memory` when the student problem is not discovery scarcity or later reflection, but losing the thread after finding clinics worth keeping.

Choose `v5firstpath` when the student problem is the first practical route from first click through first log.

Choose `v6guestfirst` when the student problem is signup resistance before the search has proved its value.

Use `v6realleads` only after a fresh topic-to-proof review. Its trust topic is promising, but the current branch is not yet the safe default.

## Interactive Rule

When working directly with Shivam on a new ClinicalHours slide request, ask what content or topic he wants on the slides before you choose a lane or start writing copy.

If needed, ask one short follow-up about audience or CTA.

If the work is automated or the request is already specific, use the normal defaulting rules.

## Minimal Read Order For A Future Agent

1. [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/_index|Campaign hub]]
2. [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18]]
3. [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18]]
4. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]
5. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_iteration_loop_v1_2026-05-31]]
6. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/_index|QA docs hub]]
7. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_student_visual_audit_and_variation_rules_2026-06-02]]
8. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v3bright7]]
9. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v4impact]]
10. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v4memory]]
11. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v5firstpath]]
12. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v6guestfirst]]
13. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v7semesterstart]]
14. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v9impactops]]
15. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_student_topic_proof_audit_2026-05-30]]
16. The folder index for the variant you are actually extending: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/composition/_index|composition]], [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/exports/_index|exports]], and [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/qa/_index|qa]]

## What To Trust

- Trust enterprise element-level recaptures over rough viewport crops when a clinic-ops slide makes a product claim.
- Trust the student homepage hero, map, and auth states more than the lower homepage stat cards.
- Trust the pipeline specs for the `v1` clinic-ops deck, the `v3bright7` bright student deck, the `v4impact` student impact-story branch, and the `v4memory` student search-memory branch.
- Trust the copy-audit script to catch known internal-strategy phrases and banned raw bright-lane assets before export.
- Trust the social rubric, QA checklist, and fresh-context judge loop as the acceptance gate before shipping.

## What Not To Assume

- Do not assume the newest export version is the most reproducible one.
- Do not assume the public enterprise page equals validated customer outcomes. Public surface and validated pilot evidence are different tiers.
- Do not assume older `v3bright` exports are the current bright canonical branch; use `v3bright7` plus its iteration note and deck spec.
- Do not assume `v3bright7` is the right student default for later-stage articulation asks; use `v4impact` when the problem is capturing or retrieving impact details after the experience.
- Do not assume `v3bright7` is the right student default for save-and-track follow-through asks; use `v4memory` when the problem is losing track after discovery.
- Do not assume the broader dashboard hero is the right preview proof just because it is visually larger; if the slide topic is about one clinic being worth the click, the featured clinic card should usually be the hero.
- Do not assume the welcome panel is the right first-log proof just because it mentions `Log Hours`; if the topic is about where the first shift goes next, the visible `Log Your First Hours` journal CTA should usually carry the slide.
- Do not assume the latest successful student palette or shell should be copied into the next student branch. Compare recent exports first and choose a distinct identity when the issue is new.
- Do not assume `v7semesterstart` should become the default student template. Its value is the variety across slide roles and the stronger proof chain, not the exact cream-blue shell or card arrangement.
- Do not assume `v8conciseops` is the right concise branch to extend. It passed mechanical QA, but it is not the preferred creative standard because the slides feel too visually similar and the screenshot text remains too wordy or unclear.
- Do not assume `v9impactops` is a universal new default. Its value is that it fixes the concise clinic-ops branch without turning into a template for unrelated lanes or topics.
- Do not assume placeholder homepage metrics can be rehabilitated with better cropping. They should stay out of proof slides.

## Required Documentation When Adding A New Variant

If a future agent creates another named branch, the work is not fully handed off until all of these exist:

- updated `composition/_index.md`
- updated `exports/_index.md`
- updated `qa/_index.md` if new QA screenshots were generated
- a short iteration note or handoff note explaining proof mapping and what changed
- a pipeline spec if the new variant is meant to be reproducible at the same level as `v1`
- a review bundle and cold-judge pass before calling the branch ready to ship

## Current Residual Gaps

- `v2auth` still has no machine-readable deck spec, so it remains less reproducible than `v1` and `v3bright7`.
- The strongest truthful proof still lives on the clinic-ops enterprise page, so the bright student lane should keep tighter copy and narrower claims.
- Earlier `v3bright` export suffixes remain useful history, but future agents should treat `v3bright7` as the active bright default.
- `v4impact` is reproducible, but it still depends on mixed public and authenticated preview surfaces, so its copy should stay narrower than any claim about finished applications or outcomes.
- `v4memory` is reproducible, but its save-and-track story still relies on dashboard records, journal controls, and an empty-state prompt support crop, so its copy should stay at `save`, `track`, and `log`, not a filled student workflow or admissions output claim.
- `v5firstpath` is now stronger after the `2026-05-30` repair, but its first-log proof still depends on a first-run journal state, so it should promise direction and follow-through, not a completed saved workflow.
- `v6guestfirst` remains useful, but full public auth screens still visually favor sign-in over guest browsing; use tighter guest-action crops whenever possible.
- `v6realleads` remains the weakest current student branch for topic-to-proof fit and should not be reused without a fresh audit or a more specific proof set.
- `v8conciseops` should stay documented as a concise clinic-ops experiment, but future agents should not treat it as the default concise benchmark. The better target is `v7semesterstart`-level variation and impact with even fewer words.
- `v9impactops` is now the better concise clinic-ops branch to inspect, but slide `4` still depends on a text-heavier outputs proof than ideal. If a cleaner enterprise output or audit capture is created later, that slide should be refreshed first.
