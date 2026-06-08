---
title: Task Routing Policy
project: references
strategic: true
status: active
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-10
tags: [references, routing, agents, tasks, orchestration]
---

# Task Routing Policy

This framework routes agent work across research, writing, reasoning, outreach, decision support, and operations. The goal is to improve quality through orchestration, not just bigger prompts.

## Routing Principles

1. Start with a task card before loading deep context.
2. Use the smallest viable context first, then pull more only if needed.
3. Spend more reasoning budget on planning, synthesis, and ambiguity.
4. Spend less reasoning budget on cleanup, formatting, and mechanical transforms.
5. Escalate review intensity when the output is external-facing, high-stakes, or hard to verify.

## Required Inputs Before Routing

- Goal
- Audience
- Constraints
- Definition of done
- Failure conditions

If one of those is missing, the task is under-specified and should be clarified or narrowed before execution.

## Task Classes

| Task Class | Best For | Initial Context | Default Pattern | Review Requirement |
|---|---|---|---|---|
| `quick-turn` | Small rewrites, summaries, formatting, shallow lookups | 1-2 core files or one prompt | Single pass | Self-check only |
| `standard` | Most writing, reasoning, outreach, and project-note work | Index + 1-3 relevant files | Producer then self-review | Recommended |
| `high-stakes` | Financial, academic, career, or external-facing recommendations | Index + task card + source files + references | Producer + skeptic + integrator | Required |
| `deep-research` | Multi-source synthesis, landscape mapping, evidence-heavy work | Task card + minimal seed context, then staged pull | Researcher + reviewer or parallel specialists | Required |
| `ops-automation` | SOPs, workflow design, tool routing, repeatable procedures | Existing process docs + current constraints | Planner + executor + verification pass | Required if the workflow will be reused |

## Model And Effort Guidance

- Use the strongest available reasoning setup for planning, ambiguity resolution, and final synthesis.
- Use a lighter setup for repetitive extraction, formatting, or narrow follow-through steps.
- If only one model is available, simulate routing by varying depth, review intensity, and context size instead of changing tools.

## Context Rules By Class

- `quick-turn`: do not preload project history unless the wording depends on it
- `standard`: load the relevant index first, then only the files closest to the ask
- `high-stakes`: load source-of-truth files plus the best reusable framework before producing claims
- `deep-research`: stage context in waves and write intermediate findings before synthesis
- `ops-automation`: prefer existing procedures over inventing a new system from scratch

## Output Rules

- Every routed task should produce one of:
  - a durable Analyst note
  - a finished Output artifact
  - a structured run log
  - an explicit no-artifact decision

## Escalation Triggers

Escalate from `standard` to `high-stakes` or `deep-research` when:

- The output will be sent externally
- The recommendation could change money, grades, applications, or strategy
- Claims require evidence and source discipline
- The task crosses multiple projects or conflicting prior notes
- The first pass reveals ambiguity that could change the answer materially

## Related Frameworks

- [[Codex-Adversarial-Multi-Agent-Workflow]]
- [[reviewer-loop-policy]]
