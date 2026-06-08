---
title: ClinicalHours Next Wedge Priority - 2026-05-10
description: Decide which ClinicalHours workflow wedge should be prioritized next and how to frame it without overclaiming
project: clinicalhours
strategic: true
status: complete
origin_dump: null
last_synced_dump: null
references:
  - "[[02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07]]"
  - "[[02_Analyst/projects/ClinicalHours/Strategy/niche-refinement]]"
  - "[[02_Analyst/projects/ClinicalHours/Outreach/DFW-Strategy]]"
  - "[[03_References/Frameworks/task-routing-policy]]"
  - "[[03_References/Frameworks/reviewer-loop-policy]]"
task_type: reasoning
priority: high
definition_of_done:
  - A durable decision memo recommends the next workflow wedge and the sequencing logic behind it
  - The memo stays evidence-bound to current pilot knowledge and avoids market-wide overclaiming
  - A run log records what context was loaded, what review loop was used, and what remains uncertain
failure_conditions:
  - The recommendation claims more validation than the current pilot supports
  - The output collapses product strategy, outreach messaging, and pricing into one vague direction
  - The memo does not identify the main risk or next validation step
context_sources:
  - "[[02_Analyst/projects/ClinicalHours/_index]]"
  - "[[02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07]]"
  - "[[02_Analyst/projects/ClinicalHours/Strategy/niche-refinement]]"
  - "[[02_Analyst/projects/ClinicalHours/Outreach/DFW-Strategy]]"
created: 2026-05-10
last_updated: 2026-05-10
tags: [task, clinicalhours, strategy, decision]
run_log: [[02_Analyst/run-logs/agent-run-2026-05-10-clinicalhours-next-wedge-priority]]
---

# ClinicalHours Next Wedge Priority - 2026-05-10

**Status:** complete  
**Owner:** agent  
**Task Type:** reasoning

## Objective

Decide what ClinicalHours should build and claim next, using only what the current pilot and existing strategy notes actually support.

## Audience

Shivam and future agents working on ClinicalHours strategy, outreach, and pilot execution.

## Current State

ClinicalHours has already moved beyond a pure volunteer-coordination framing in practice, but the current evidence still comes from a narrow pilot context. The vault already suggests that evaluation workflows, onboarding reminders, and administrative coordination are stronger near-term wedges than a broad "clinic ops platform" claim. What is missing is one short decision memo that turns that insight into a practical next-step sequence.

## Constraints

- Stay evidence-bound to the current pilot and existing Analyst notes.
- Do not describe broad workflow automation as already proven market-wide.
- Preserve the current small-clinic orientation rather than jumping straight to a large-clinic or hospital story.
- Keep pricing as a parallel business-model thread, not the main product-validation claim.

## Required Output

- A decision memo saved to `02_Analyst/projects/ClinicalHours/Strategy/next-wedge-priority-2026-05-10.md`
- A concise execution trace saved to `02_Analyst/run-logs/agent-run-2026-05-10-clinicalhours-next-wedge-priority.md`

## Minimum Context To Load First

- [[02_Analyst/projects/ClinicalHours/_index]]
- [[02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07]]

## On-Demand Context

- [[02_Analyst/projects/ClinicalHours/Strategy/niche-refinement]]
- [[02_Analyst/projects/ClinicalHours/Outreach/DFW-Strategy]]
- [[03_References/Frameworks/task-routing-policy]]
- [[03_References/Frameworks/reviewer-loop-policy]]

## Review Plan

- Review mode: `reviewer-loop`
- Key failure check: the reviewer should try to find where the memo overstates evidence or confuses near-term sequencing with long-term vision

## Definition Of Done

- The next wedge recommendation is explicit
- The sequence after that recommendation is explicit
- The main caveat is explicit

## Failure Conditions

- The memo reads like generic startup advice rather than a context-bound decision
- The memo makes unsupported market claims
- The next experiment is not concrete enough to run

## Inputs / Links

- [[02_Analyst/projects/ClinicalHours/_index]]
- [[02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07]]
- [[02_Analyst/projects/ClinicalHours/Strategy/niche-refinement]]
- [[02_Analyst/projects/ClinicalHours/Outreach/DFW-Strategy]]

## Next Actions

- Use the decision memo to scope the next MVP test and the success signals that should decide whether the wedge expands

## Completion Notes

- Output memo drafted and sent through reviewer loop on 2026-05-10
- Reviewer pass tightened the evidence boundary so the memo now distinguishes pilot validation from broader market validation

## History

- [2026-05-10] Task created to exercise the new vault task system on a real ClinicalHours strategy decision
