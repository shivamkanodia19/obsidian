---
title: ClinicalHours TikTok Skill MCP Guardrails - 2026-05-18
description: Workflow guardrails for future agents using tools and local rendering to build ClinicalHours TikTok slides
last_updated: 2026-05-29
---

# ClinicalHours TikTok Skill / MCP Guardrails - 2026-05-18

## Purpose

This is the operating spec future agents should follow so the ClinicalHours system does not ship:

- fake medical-adjacent UI
- mixed-audience slides
- proof assets too small to matter
- unsafe edge text
- placeholder metrics as evidence

Read with:

- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_iteration_loop_v1_2026-05-31]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist]]

## Non-Negotiables

- If Shivam is asking for a new ClinicalHours deck directly, ask what content or topic he wants on the slides before choosing a lane or writing copy.
- Final PNGs must be exactly `1080 x 1920`.
- All essential text must remain inside the safe area encoded in `clinicalhours_tiktok_carousel.html`.
- Every slide needs one dominant message and one dominant proof asset.
- Use real ClinicalHours captures only for proof slides.
- Never show PHI or fake partner/adoption proof.
- Do not use the homepage `0+` stat block as hero proof.
- If a screenshot crop is too small to explain the point in under 2 seconds, replace or enlarge it.
- Do not ship internal strategy language in visible deck copy.
- Do not ship raw proof assets whose dominant readable text is empty-state filler or generic onboarding copy.
- Do not invent hybrid evidence-tier strings. Keep claim strength in `evidence_tier` and visibility in `proof_access`.
- Do not ship a branch on the first clean render. Every serious branch must go through at least one fresh-context judge loop.
- Fresh-context judges must not see the builder's reasoning or earlier judge notes before submitting their first verdict.

## Role Assignments By Skill

### `content-strategy`

Owns:

- lane selection
- emotional job of each slide
- sequence logic
- headline brevity

Must enforce:

- one lane per deck by default
- one promise per slide
- fast payoff after the first tension slide

### `content-research-writer`

Owns:

- evidence tier discipline
- claim weakening when proof is thin
- compliance phrasing

Must enforce:

- internal validated claims stay distinct from public-surface claims
- any unsupported number is removed or labeled
- no overclaiming on HIPAA, adoption, or outcomes

### `canvas-design`

Owns:

- composition
- focal hierarchy
- visual restraint
- screenshot legibility

Must enforce:

- one hero screenshot per slide
- support crops only when they add proof
- text cannot sit on busy UI
- blue and green are purposeful, not decorative clutter

### `audit`

Owns:

- final structural QA
- detection of collisions, unsafe text, wrong dimensions, and weak lane discipline

## Role Assignments By Tool / Workflow

### Codex MCP setup

- In this environment, Codex reads MCP servers from `C:\Users\shiva\.codex\config.toml`.
- Keep Playwright and the Replicate-support `rube` server registered there for this workflow.
- After changing the MCP registry, start a fresh Codex session before expecting the new server tools to be callable.

### Playwright browser tools

Before saving any source screenshot:

- capture the full truthful state first
- save the uncropped original
- only then create derived crops in composition
- reject any state with private data, broken UI, or placeholder proof
- keep every claim-bearing screenshot or crop traceable to `captures/`

### Replicate MCP (`rube`)

- Playwright owns truthful proof capture.
- Replicate MCP owns secondary support imagery that strengthens emotion and framing without inventing evidence.
- Use Replicate only after the proof inventory is locked.
- Never let generated support imagery replace a real ClinicalHours UI asset on a claim slide.
- Reject any generated image that resembles fabricated product UI, fake metrics, fake map density, or an unshipped workflow state.

### Figma MCP

- Use Figma for layout exploration, alternate visual systems, deck mockups, and presentation polish.
- Do not use Figma mockups as claim-bearing ClinicalHours proof.
- If a Figma route wins strategically, port the result back into the reproducible ClinicalHours composition system or clearly label it as exploratory.

### Local HTML composition

Canonical source:

- `05_Outputs/images/clinicalhours_tiktok_2026-05-18/composition/clinicalhours_tiktok_carousel.html`

Rules:

- proof assets must use `data-proof="true"`
- essential text must use `data-essential="true"` and `data-text="true"`
- run QA after any proof-asset change
- if a screenshot needs tighter readable text, create a derived crop instead of defending the raw asset with copy

### Local render script

Canonical export command:

```powershell
.\render_clinicalhours_tiktok_carousel.ps1 -VersionSuffix v1 -RunQa -GenerateQaShots
```

The render script now also writes a JSON review bundle to `qa/review_bundles/` for fresh-context agent review.

### Fresh-context visual review

Every serious branch should be reviewed by at least `2` independent fresh-context judges.

Judge inputs:

- latest exported PNGs
- QA screenshots
- review bundle
- rubric
- required strategy files

Judge rules:

- no prior builder reasoning
- no prior judge notes before the initial verdict
- score slide-level proof fit, screenshot readability, lane discipline, and CTA credibility
- return `pass`, `revise`, or `retire`

## What QA Should Catch Automatically

- text overflow
- safe-zone violations
- text-on-text overlap
- proof overlap with essential text
- wrong dimensions
- banned internal-strategy phrases from `composition/audit_clinicalhours_tiktok_copy.ps1`
- banned raw proof assets whose screenshot text is known to undercut the claim

## What Still Requires Human Review

- whether the lane is clear
- whether the evidence tier is respected
- whether the screenshot is the right proof, not just a real one
- whether the dominant screenshot text helps or hurts the headline
- whether the sequence is emotionally coherent
- whether the CTA feels credible

Fresh-context judge agents should cover the same questions before a human makes a final shipping decision.

## Default Handoff Prompt

`If Shivam is asking for a new ClinicalHours deck directly, first ask what content or topic he wants on the slides. If needed, ask one short follow-up about audience or CTA. Then work from the existing clinicalhours_tiktok_carousel.html and current live captures. Keep real ClinicalHours screenshots as the hero. Before export, run the local render script with QA enabled and fix every warning. Do not ship any slide with cropped-off text, proof assets touching essential text, placeholder metrics used as proof, repeated metric conflicts, or claims stronger than the visible evidence supports.`
