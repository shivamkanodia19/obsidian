---
title: Reviewer Loop Policy
project: references
strategic: true
status: active
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-10
tags: [references, review, agents, quality, workflow]
---

# Reviewer Loop Policy

This framework makes review loops explicit for non-development work. The purpose is to reduce weak reasoning, unsupported claims, and polished-but-fragile outputs.

## When A Reviewer Loop Is Required

- External-facing writing
- Strategy or decision recommendations
- Research synthesis with factual claims
- Work that may influence money, applications, grades, or operations
- Any task routed as `high-stakes`, `deep-research`, or reusable `ops-automation`

## Default Roles

### 1. Producer

- Creates the first complete version
- Works from the task card and the minimum necessary context

### 2. Skeptic

- Tries to break the output
- Looks for weak logic, unsupported claims, missing sources, hidden assumptions, and scope drift

### 3. Integrator

- Resolves valid criticism
- Produces the final version or flags what still needs user judgment

## Domain-Specific Review Focus

- `research`: evidence quality, source fit, overclaiming, missing caveats
- `writing`: audience fit, clarity, tone, unsupported assertions, structure
- `reasoning`: assumption quality, tradeoffs, logical jumps, untested premises
- `outreach`: credibility, specificity, personalization, friction, CTA quality
- `operations`: reuse safety, handoff clarity, failure points, missing checks

## Minimum Review Questions

Every reviewer loop should answer:

1. What is the strongest reason this output could be wrong?
2. What claim is least supported by the loaded context?
3. What did the producer assume without proving?
4. What would confuse or mislead the final reader?
5. What is the smallest revision that meaningfully improves reliability?

## Output Standard

The loop is only complete when the final artifact includes:

- A clear recommendation or deliverable
- The key risk or caveat
- A record of what changed after review

If the work is substantial, capture the review result in [[02_Analyst/run-logs/_index]].

## Relationship To Multi-Agent Work

- Use this as the default quality loop for non-trivial tasks.
- Use [[Codex-Adversarial-Multi-Agent-Workflow]] when the work benefits from stronger disagreement or parallel specialized roles.
