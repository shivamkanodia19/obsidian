---
title: ClinicalHours TikTok Replication Playbook - 2026-05-19
description: Top-level replication contract for rebuilding, extending, or auditing the ClinicalHours TikTok slideshow system
last_updated: 2026-06-02
---

# ClinicalHours TikTok Replication Playbook - 2026-05-19

## Purpose

This is the durable operating contract for future agents who need to reproduce the ClinicalHours TikTok slideshow system without guessing which files are canonical.

Use it when the task is any of:

- rebuild an existing deck version
- extend a lane with better proof or copy
- add a new export variant
- audit whether the current docs still match the working assets

## Folder Responsibilities

- `02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/` owns strategy, lane logic, retention framing, and rubric references.
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/` owns truthful source proof.
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/composition/` owns the HTML sources and render script.
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/exports/` owns shipped PNG sets.
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/qa/` owns screenshot evidence from layout QA.
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/` owns the human-readable operating contract, handoff, and approval rules.
- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/pipeline/` owns machine-readable config and deck specs for the reproducible deck branches.

## Required Read Order

1. [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18]]
2. [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18]]
3. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19]]
4. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist]]
5. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_skill_mcp_guardrails_2026-05-18]]
6. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_iteration_loop_v1_2026-05-31]]
7. [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_student_visual_audit_and_variation_rules_2026-06-02]]

## Variant Matrix

### `v1`

- lane: `clinic_ops_primary`
- strongest use: default reproducible deck
- composition: `composition/clinicalhours_tiktok_carousel.html`
- export path: `exports/v1/`
- documentation strength: strongest
- machine-readable spec: yes

### `v2auth`

- lane: student-facing authenticated workflow
- strongest use: student-product proof with logged-in surfaces
- composition: `composition/clinicalhours_tiktok_student_auth_v2.html`
- export path: `exports/v2auth/`
- documentation strength: medium
- machine-readable spec: no

### `v4onboard`

- lane: `clinic_ops_primary`
- strongest use: issue-specific onboarding-visibility story
- composition: `composition/clinicalhours_tiktok_clinic_onboarding_visibility.html`
- export path: `exports/v4onboard/`
- documentation strength: durable
- machine-readable spec: yes

### `v4expiry`

- lane: `clinic_ops_primary`
- strongest use: issue-specific expiring-clearances and renewal-visibility story
- composition: `composition/clinicalhours_tiktok_clinic_expiring_clearances.html`
- export path: `exports/v4expiry/`
- documentation strength: durable
- machine-readable spec: yes

### `v8conciseops`

- lane: `clinic_ops_primary`
- strongest use: cautionary concise clinic-ops branch that documents what to avoid when a request asks for shorter copy
- composition: `composition/clinicalhours_tiktok_clinic_ops_concise.html`
- export path: `exports/v8conciseops/`
- documentation strength: durable
- machine-readable spec: yes

### `v9impactops`

- lane: `clinic_ops_primary`
- strongest use: current concise clinic-ops branch for shorter copy with stronger slide-role variation and clearer proof
- composition: `composition/clinicalhours_tiktok_clinic_ops_impact.html`
- export path: `exports/v9impactops/`
- documentation strength: durable
- machine-readable spec: yes

### `v3bright`

- lane: student-facing, brighter marketing treatment
- strongest use: bright student-facing discovery and activation storytelling
- composition: `composition/clinicalhours_tiktok_student_auth_v3bright.html`
- export path: latest canonical set in `exports/v3bright7/`
- documentation strength: durable
- machine-readable spec: yes

### `v4impact`

- lane: `student_discovery_secondary`
- strongest use: issue-specific student story about logging reflections and retrieving details later to show impact
- composition: `composition/clinicalhours_tiktok_student_impact_story.html`
- export path: `exports/v4impact/`
- documentation strength: durable
- machine-readable spec: yes

### `v4memory`

- lane: `student_discovery_secondary`
- strongest use: issue-specific student story about losing track of where you saw a shift and finding it again quickly
- composition: `composition/clinicalhours_tiktok_student_search_memory.html`
- export path: `exports/v4memory/`
- documentation strength: durable
- machine-readable spec: yes

### `v5firstpath`

- lane: `student_discovery_secondary`
- strongest use: issue-specific student story about the first practical path from first click through first logged shift
- composition: `composition/clinicalhours_tiktok_student_first_path.html`
- export path: `exports/v5firstpath/`
- documentation strength: durable
- machine-readable spec: yes

### `v6realleads`

- lane: `student_discovery_secondary`
- strongest use: issue-specific student trust story around stale lists, word of mouth, and proving a clinic is worth the click
- composition: `composition/clinicalhours_tiktok_student_real_leads.html`
- export path: `exports/v6realleads/`
- documentation strength: durable
- machine-readable spec: yes

### `v6guestfirst`

- lane: `student_discovery_secondary`
- strongest use: issue-specific student activation story around browsing before signup and delaying account creation until it helps
- composition: `composition/clinicalhours_tiktok_student_guest_first.html`
- export path: `exports/v6guestfirst/`
- documentation strength: durable
- machine-readable spec: yes

## Default Replication Workflow

### 0. Ask for the deck topic when interactive

When working directly with Shivam on a new ClinicalHours slide request:

- ask what content or topic the slides should cover
- if needed, ask one short follow-up about audience or CTA

If the assignment is automated or already explicit, continue without this step.

### 1. Declare the lane and target variant

Before touching proof or copy, write down:

- lane
- evidence tier
- proof access
- whether you are extending `v1`, `v2auth`, `v3bright`, or creating a new branch

If the assignment is ambiguous, use `v1` and `clinic_ops_primary`.

If the assignment wants fewer words and more impact, borrow `v7semesterstart` as the quality benchmark for variation, sequencing, and proof clarity before you choose the final shell.

If the assignment is concise clinic-ops specifically, prefer `v9impactops` over `v8conciseops`.

### 2. Lock the proof inventory first

- Start from the current captures index: [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/_index|captures]]
- Prefer enterprise element recaptures for clinic-ops proof.
- Avoid the student homepage lower stat cards because the public captures show placeholder `0+` metrics.
- If a screenshot does not prove the claim in under `2` seconds, either enlarge it or choose a different proof asset.
- Treat crop quality as part of proof quality. Reject crops that clip key labels, bury the relevant action in empty space, or turn the screenshot into a decorative dark rectangle.

### 2.5. Decide whether support imagery is needed

- Only make this decision after the proof inventory is locked.
- If a slide needs more atmosphere, pacing, or visual rhythm, use Replicate MCP support imagery only in a secondary role.
- Do not let generated support art replace captured ClinicalHours proof or imply a stronger workflow state than the visible product evidence supports.

### 3. Pick the right composition source

- Use `clinicalhours_tiktok_carousel.html` for the reproducible clinic-ops path.
- Use `clinicalhours_tiktok_clinic_onboarding_visibility.html` when the story is specifically about onboarding visibility loss.
- Use `clinicalhours_tiktok_clinic_expiring_clearances.html` when the story is specifically about quiet expirations, renewal follow-up, and status visibility.
- Use `clinicalhours_tiktok_clinic_ops_impact.html` when the story is concise clinic-ops with fewer words, stronger screenshot readability, and more distinct slide roles than `v8conciseops`.
- Use `clinicalhours_tiktok_clinic_ops_concise.html` only when you are explicitly auditing or extending the `v8conciseops` experiment. Do not treat it as the default concise starting point for future work.
- Use `clinicalhours_tiktok_student_auth_v2.html` when the story depends on authenticated student-product proof.
- Use `clinicalhours_tiktok_student_auth_v3bright.html` when the brighter student-facing visual direction is intentional, and pair it with `clinicalhours_tiktok_iteration_notes_v3bright7.md`.
- Use `clinicalhours_tiktok_student_impact_story.html` when the student problem is later-stage articulation, reflections, and retrieving details that show impact.
- Use `clinicalhours_tiktok_student_real_leads.html` when the student problem is trust in whether the listing is real, current, and worth the click.
- Use `clinicalhours_tiktok_student_guest_first.html` when the student problem is signup resistance before the search has proven its value.

### 3.5. Choose a visual identity on purpose

- Before styling a new student branch, review the most recent student exports in `exports/` and note what palette, framing, and shell they already use.
- If the task is a new durable issue branch, do not copy the current student shell by default.
- Keep the colors relevant and not distracting, but make the branch visually distinct enough that it does not read like the same slideshow with swapped copy.
- Record that design choice in the iteration note so the next agent knows whether the look was intentional or inherited.
- Before reusing a student-facing shell, compare it against the latest nearby export branches. Do not default to the same palette, typography stack, proof-card shapes, and progress UI unless the assignment explicitly calls for a direct continuation.
- For student-facing work, read the visual audit note and inspect `v7semesterstart` before styling. Use it as the benchmark for slide-to-slide variety and proof continuity, not as the default shell to clone.
- For concise or automated asks in any lane, use `v7semesterstart` as the benchmark for visual variety, proof readability, and sequencing discipline. Then reduce the copy further than `v7semesterstart` instead of inheriting `v8conciseops`-style repetition.
- If three or more slides share the same proof framing, card rhythm, and caption density, stop and redesign at least one slide role before rendering again.
- Keep the old bottom `chip-stack` / `chip` pattern off by default. Reintroduce it only if the labels are genuinely informative proof rather than decorative keywords.

### 4. Write copy after proof selection

Keep each slide inside one lane, one role, and one dominant claim.

If the proof asset is weaker than the copy, weaken the copy.

Do not invent hybrid evidence-tier strings to explain mixed screenshot visibility. Keep:

- claim strength in `evidence_tier`
- screenshot visibility in `proof_access`

For the bright student lane, also read:

- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19]]

### 5. Run the copy and screenshot-text gate

- Reject any visible line that sounds like creator commentary instead of audience copy.
- Reject any hero screenshot whose most readable text is empty-state filler, generic onboarding language, or off-lane boilerplate.
- If the screenshot is real but the readable text is weak, crop it tighter or swap the asset before render.
- Reject any slide whose screenshot still asks the viewer to read paragraph-level product text to understand the point.
- Reject any concise deck whose slides feel like the same layout repeated with different screenshots.
- The shared render script now runs `composition/audit_clinicalhours_tiktok_copy.ps1` automatically. Treat an audit failure as a content failure, not a formatting failure.

### 6. Render and review

Canonical render entrypoint:

```powershell
.\render_clinicalhours_tiktok_carousel.ps1 -VersionSuffix <suffix> -RunQa -GenerateQaShots
```

If an alternate HTML file is the source, pass `-HtmlFile` explicitly.

### 6.5. Use the review bundle

The render script now emits a review bundle JSON under `qa/review_bundles/`.

Treat that bundle as the approved handoff packet for fresh-context judges.

### 7. Apply all QA layers

- Machine QA: copy audit, safe zones, overlap, overflow, dimensions
- Fresh-context judge QA: independent agent review from a clean context using only the review bundle, required strategy files, exports, and QA screenshots
- Human QA: truthfulness, lane clarity, proof strength, screenshot-text quality, crop quality, pacing, CTA credibility

Do not treat the fresh-context judge layer as optional when a branch is being materially changed or promoted.

Human QA should explicitly fail when:

- the crop cuts off the proof that the headline depends on
- a screenshot is centered on empty-state dead space instead of the useful control or label
- the visible product text is too small to read in a phone feed
- the new branch looks like a palette-swapped copy of a previous slideshow
- fresh-context judges keep finding the same semantic weakness across rounds

No variant is fully replicated until all three layers pass.

### 7.5. Repeat until pass or retire

- Do not ship on the first clean render.
- Run at least `2` independent fresh-context judges before approval.
- If the branch does not improve materially across `2` consecutive repair rounds, reframe it or retire it instead of polishing weak proof.

### 8. Update the docs in the same pass

If you create or materially change a variant, update:

- the relevant `_index.md` files
- a handoff or iteration note explaining what changed
- the pipeline spec if the deck is meant to be reproducible without manual reconstruction

## Decision Rules

- Choose truth over polish.
- Choose the stronger proof asset over the cleverer copy.
- Choose captured proof over generated support whenever the two are in tension.
- Choose the narrower claim when evidence tiers are mixed.
- Choose a new machine-readable spec only when the variant is becoming a durable branch, not a throwaway exploration.
- Choose a fresh but restrained visual system for new durable branches instead of reusing the last successful student palette by habit.
- Choose a visual system that fits the issue, not just the last deck that rendered successfully.

## Replication Completion Checklist

- The lane is declared.
- The evidence tier is explicit.
- The proof assets are traceable to captures in this tree.
- The composition file is identified.
- The export suffix is documented.
- QA screenshots exist if a render was run.
- The handoff or iteration docs explain what is canonical after the change.

## Known Structural Limits

- `v2auth` still does not have a pipeline deck spec.
- `v3bright7` is now durable, but its proof tier still depends on a mix of public student surfaces and authenticated preview captures.
- `v4impact` is now durable, but its proof still depends on authenticated preview surfaces and empty-state student records, so the copy must stay narrower than finished-outcome claims.
- The strongest truthful clinic proof still lives on the enterprise page, so both `v4onboard` and `v4expiry` still reuse overlapping proof surfaces and must differentiate through narrower copy, proof emphasis, and issue framing.
