---
title: ClinicalHours Visual Iteration Loop v1 - 2026-05-31
description: Required generator and fresh-context judge loop for ClinicalHours visuals, with Codex tool routing and Zernio publishing gates
last_updated: 2026-05-31
---

# ClinicalHours Visual Iteration Loop v1

## Why This Exists

The current ClinicalHours visual system already protects truth, proof discipline, and layout quality.

What it does not yet force strongly enough is repeated improvement.

This note upgrades the workflow from:

- build
- render
- check
- maybe ship

to:

- build
- render
- cold-judge
- repair
- re-judge
- repeat until the work is actually good or the branch is explicitly retired

## External Context Reviewed

### Zernio API

Zernio is useful here as a downstream publishing layer, not as a design engine.

What matters for this workflow:

- the base REST API lives at `https://zernio.com/api/v1`
- it supports profiles, connected accounts, drafts, scheduled posts, and immediate publishing
- media upload uses an upload-link flow
- the Zernio MCP docs describe `280+` tools, including post creation, upload-link generation, media status checks, analytics, inbox, and ads

Use Zernio only after a visual branch has already passed the ClinicalHours review loop.

### Codex Design And Visual Tooling Available Here

Current high-value design and visual surfaces in this Codex environment:

- `Figma` MCP for decks, diagrams, visual exploration, design editing, and screenshots
- `Browser` / browser-use tools for local preview, truthful browser capture, and page inspection
- `Chrome` and `Computer Use` for authenticated or profile-bound browser flows when a normal local browser pass is not enough
- local image inspection through `view_image`
- `image_gen` for editing or generating support imagery

Use them with a strict split:

- real ClinicalHours proof: browser capture and derived crops
- layout exploration and visual polish: Figma or local composition
- non-claim support imagery: `image_gen` or other image tools only in a secondary role

## Required Loop

### 1. Lock Strategy And Lane First

Before generating anything, declare:

- deck topic
- lane
- evidence tier
- proof access
- target branch or whether this is a new branch

No build starts before the lane is explicit.

### 2. Lock Proof Before Styling

Pick the hero proof asset for each slide before refining the copy or adding support imagery.

If the screenshot cannot support the claim in about `2` seconds:

- tighten the crop
- recapture a better state
- or weaken the claim

Do not style your way around weak proof.

### 3. Build The Candidate

Use the existing ClinicalHours composition system unless there is a strong reason to move the branch into Figma-first exploration.

Builder responsibilities:

- preserve proof truth
- keep one dominant message per slide
- keep one dominant hero proof asset per slide
- avoid branch drift into mixed lanes or broader claims

### 4. Render And Emit Review Artifacts

Every candidate render must produce:

- exported slide PNGs
- QA screenshots when requested
- copy-audit result
- a machine-readable review bundle

The review bundle is the handoff packet for fresh-context judges.

### 5. Run Judge A From A Fresh Context

Judge A should start from a fresh context whenever possible.

Judge A receives only:

- the declared branch topic and lane
- required strategy and rubric files
- the latest review bundle
- the exported slide PNGs
- QA screenshots

Judge A should not see:

- builder chain-of-thought
- earlier judge notes
- repair plans from previous rounds

Judge A writes an independent verdict first.

### 6. Run Judge B From A Separate Fresh Context

Judge B follows the same rules as Judge A.

Judge B should not read Judge A before writing the initial verdict.

This second pass is not redundancy theater.

Its job is to catch:

- generic proof outranking specific proof
- branch drift
- emotionally weak first frames
- CTA mismatch
- slides that are technically real but semantically wrong

### 7. Synthesize Only After Independent Judging

Only after both judges submit their first-pass findings may the builder or synthesizer compare the results.

Cluster findings into:

- hard fail
- must-fix
- optional improvement
- retire-and-reframe

### 8. Repair The Candidate

Repair priority order:

1. truth and evidence tier
2. topic-to-proof fit
3. screenshot readability
4. sequence logic
5. visual polish

If the judges disagree, prefer the narrower and more truthful reading unless there is stronger visible proof.

### 9. Repeat Until Pass Or Explicit Retirement

Do not ship because the deck became "good enough for now."

Keep iterating until one of these is true:

- the branch passes the approval gate
- the branch is retired because the topic cannot be supported truthfully with the current proof inventory
- the branch is reframed into a narrower, more supportable story

## Fresh-Context Judge Rules

Each fresh-context judge must:

- score every slide against the ClinicalHours rubric
- score the deck as a whole
- identify the single biggest persuasive weakness
- identify the single biggest truth-risk weakness
- say whether the branch should `keep`, `revise`, or `retire`

Each judge should explicitly answer:

1. What is this slide promising?
2. What visible asset is meant to prove it?
3. Does the biggest readable text inside that asset help or hurt the promise?
4. Would a skeptical viewer understand the proof quickly?
5. Is the slide doing a distinct job in the five-slide sequence?

## Approval Gate

No ClinicalHours visual branch ships until all of these are true:

- copy audit passes
- render QA passes
- no hard-fail rubric rule is triggered
- every slide clears the current slide threshold
- the deck clears the current deck threshold
- at least `2` fresh-context judges independently mark the branch `pass` or `strong_pass`
- no unresolved `must-fix` item remains open

## Plateau Rule

If two consecutive repair rounds fail to improve the core issue materially:

- do not keep polishing the same branch
- either tighten the topic
- choose stronger proof
- or retire the branch

The failure mode to avoid is endless cosmetic iteration on weak strategic proof.

## Image-Specific Rule

For any generated still, support image, or edited image:

- run a separate fresh-context image review before it becomes part of a slide
- reject it if it introduces fake UI cues, anatomy problems, fake text, visual artifacts, or claim-bearing ambiguity
- keep generated imagery subordinate to real product proof

If an image is meant to persuade on a product claim by itself, it should usually be rejected.

## Recommended Tool Routing

### Truthful Product Proof

Use:

- `Browser` or Playwright-style browser tooling
- `Chrome` or `Computer Use` for authenticated or sticky-profile states
- local derived crops under `captures/`

Do not use Figma or image generation to invent product proof.

### Layout Exploration

Use:

- local HTML composition for reproducible branches
- Figma for deliberate alternative layouts, moodboards, or faster visual exploration before porting the winning direction back into the reproducible system

### Support Imagery

Use:

- `image_gen`
- approved external image tooling

Only after proof and copy are already locked.

### Visual Review

Use:

- exported PNGs
- QA screenshots
- `view_image`
- Figma screenshots when a design-first route is being explored

## Zernio Publishing Gate

Once a branch passes the full review loop:

1. Create the platform-specific copy variants only after the creative is locked.
2. Use Zernio draft or scheduled-post flows instead of publishing immediately by default.
3. Upload the final approved media through Zernio's upload-link flow.
4. Keep post metadata tied to the winning branch suffix so later analytics can be traced back to the exact visual system.

Do not let Zernio scheduling pressure shorten the review loop.

## Required Durable Artifacts

For any durable branch or major repair pass, save:

- updated iteration note
- updated spec if the branch is reproducible
- latest review bundle
- judge findings or a summarized verdict note
- updated indexes if the branch becomes canonical, revised, or retired

## Default Judge Prompt Stub

```text
You are a fresh-context visual judge for ClinicalHours.

You are not the builder.
You have not seen prior judge notes.
You should evaluate the latest branch only from the exported visuals, QA artifacts, rubric, and required strategy files.

Score each slide and the deck.
Call out hard fails, topic-to-proof mismatches, weak screenshot text, and branch-level problems.
Do not suggest decorative fixes before proving that the current proof and sequence are sound.
Return one of: pass, revise, retire.
```
