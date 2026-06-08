---
title: ClinicalHours Experiment Log Framing - 2026-05-07
project: clinicalhours
strategic: true
status: stable
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-08
tags: [clinicalhours, accelerator, experiment-log, pilot, ai]
---

# ClinicalHours Experiment Log Framing - 2026-05-07

Status: backfilled memo from the May 7 experiment-log answer refinement cluster.

## Core Decision

The strongest conclusion from the pilot evidence was not "major pivot." It was "change product features or workflow."

That means:

- keep the broader ClinicalHours direction toward clinic operations automation
- change near-term feature priorities based on what the pilot clinic actually surfaced
- avoid claiming market-wide proof from one clinic and a small stakeholder set

## What The Pilot Actually Validated

The most defensible pain points were:

- evaluation follow-up workflows
- onboarding workflows with deadlines, reminders, and status tracking
- administrative communication
- fragmented staff coordination across email, Google Drive, Notes, and other ad hoc tools

The durable product insight was that small clinics appear to need support beyond volunteer coordination alone. The safer claim is not "we proved the whole workforce-automation thesis." It is "our pilot clinic validated broader administrative pain, and the strongest next product tests sit above the original volunteer-management wedge."

## Best Experiment-Log Framing

### Hypothesis

The cleanest hypothesis was:

"Small clinics need and will adopt automation beyond volunteer coordination, especially for onboarding, evaluation follow-up, and routine administrative workflows."

### Hypothesis Type

The best classification was:

- primary: `Problem importance`
- secondary overlap: `Value proposition`

### Decision Category

Best option:

- `Change product features or workflow`

Second-best but weaker:

- `Continue with current direction`

Why: the evidence was strong enough to re-prioritize features, but not strong enough to justify a stronger "pivot" label.

## AI-Use Framing To Preserve

The conservative, defensible AI claim set was:

- AI helped summarize and analyze interview notes or transcripts
- AI helped synthesize product requirements and draft implementation prompts
- AI helped improve decision-making around what to build next

The important guardrail was to avoid implying that AI had already built or autonomously operated the product. In this cycle, AI mainly supported interpretation, framing, and scoped planning.

## Responsible-AI Answer

The strongest responsible-use framing was:

- keep a human in the loop for any higher-stakes workflow
- be especially conservative around AI-generated emails, evaluation handling, onboarding data, and message organization
- limit unnecessary sensitive-data exposure
- avoid full automation until output quality and context handling are reliable

## Highest-Priority Next Step

The strongest next action was to build and test a narrow `evaluation automation MVP` with the pilot clinic.

The best concrete version of that test:

- identify participating volunteers after a clinic session
- send the right evaluation forms automatically
- store responses in the correct profiles
- let staff review results without juggling manual Drive and email follow-up

Pricing can still be explored, but it should be treated as a secondary parallel workstream rather than the single highest-priority next step in the experiment log.

## What To Avoid

- overclaiming from one pilot clinic
- calling the result a major pivot
- bundling pricing and feature-building as equal priorities in a single field
- describing AI as having built features it only helped analyze or scope

## Why This Note Matters

The May 7 session cluster was repetitive on the surface because it answered one accelerator field after another. The durable output was not the exact wording of each individual answer. It was the tighter strategic framing:

- evidence supports feature reprioritization, not a full repositioning claim
- the clearest validated workflow is evaluation automation
- broader workforce-automation language should stay evidence-bound
- AI-use claims should remain conservative and operationally specific
