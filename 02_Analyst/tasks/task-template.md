---
title: Task Template
description: Copy-ready template for scoped agent tasks with clear constraints and a definition of done
last_updated: 2026-05-10
type: template
---

# Task Template

Use this when you want an agent to do meaningful work without relying on a vague prompt. The goal is to make the task small enough to route well and explicit enough to review well.

## Copy-Ready Frontmatter

```yaml
---
title: [Task title]
description: [One-sentence goal]
project: [project slug or cross-functional]
strategic: false
status: proposed
origin_dump: null
last_synced_dump: null
references:
  - "[[03_References/...]]"
task_type: reasoning
priority: medium
definition_of_done:
  - [Required outcome 1]
  - [Required outcome 2]
failure_conditions:
  - [What would make the output unusable]
context_sources:
  - "[[02_Analyst/...]]"
  - "[[01_Source/...]]"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
tags: [task, reasoning]
run_log: [[../run-logs/agent-run-YYYY-MM-DD-short-topic]]
---
```

## Copy-Ready Body

```markdown
# [Task Title]

**Status:** proposed  
**Owner:** agent  
**Task Type:** reasoning

## Objective

[What the agent is trying to accomplish and why it matters.]

## Audience

[Who will use the result: you, a collaborator, a clinic, a professor, a recruiter, etc.]

## Current State

[What already exists, what is missing, and what prior notes this task should respect.]

## Constraints

- [Time, tone, domain, accuracy, tool, or source constraints]
- [What the agent may not assume]
- [What the agent must preserve]

## Required Output

- [Exact deliverable shape: memo, shortlist, draft, analysis note, revision, rubric, plan]
- [Where it should be saved]

## Minimum Context To Load First

- [[02_Analyst/...]]
- [[01_Source/...]]

## On-Demand Context

- [[03_References/...]]
- [[05_Outputs/...]]

## Review Plan

- Review mode: `none | self-review | reviewer-loop | multi-agent`
- Key failure check: [What the reviewer should try to break]

## Definition Of Done

- [Observable completion condition 1]
- [Observable completion condition 2]
- [Observable completion condition 3]

## Failure Conditions

- [A false claim would invalidate the result]
- [Missing citation, missing decision, weak reasoning, wrong format, etc.]

## Inputs / Links

- [[02_Analyst/...]]
- [[01_Source/...]]
- [[03_References/...]]

## Next Actions

- [Immediate next step if the task is not yet complete]

## Completion Notes

- [Filled in after execution]

## History

- [YYYY-MM-DD] Task created
```

## Suggested Defaults By Task Type

- `reasoning` - decision memo, tradeoff analysis, recommendation
- `writing` - draft, rewrite, tone polish, executive summary
- `research` - sourced synthesis, comparison table, evidence-backed findings
- `analysis` - structured evaluation, criteria scoring, interpretation
- `outreach` - email copy, targeting logic, follow-up sequence
- `operations` - workflow, SOP, checklist, automation handoff
- `mixed` - multi-step work that spans more than one of the above

## Notes

- Keep the initial context small. Start with the minimum files needed to orient the run.
- If the task affects a major project or external-facing output, link the final run in [[../run-logs/_index]].

## Companion Project Index Frontmatter

If the task belongs cleanly to one topic, prefer the nearest `_index.md` frontmatter over a separate task file:

```yaml
agent_context: true
current_focus:
  - [What matters now]
active_tasks:
  - [What the next agent should advance]
prompt_context:
  - "[[02_Analyst/...]]"
definition_of_done:
  - [Observable completion condition]
blocked_by:
  - [Main current constraint]
```
