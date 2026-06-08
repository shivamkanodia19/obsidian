---
title: Run Log Template
description: Copy-ready template for concise task-level execution traces
last_updated: 2026-05-10
type: template
---

# Run Log Template

Use this after a meaningful agent run when you want future sessions to understand what happened without reading the whole chat.

## Copy-Ready Frontmatter

```yaml
---
title: [Run log title]
description: [One-line summary of what was accomplished]
project: [project slug or cross-functional]
status: completed
task: [[../tasks/[task-file-name]]]
task_type: reasoning
route: standard
review_mode: self-review
date: YYYY-MM-DD
artifacts:
  - [[02_Analyst/...]]
  - [[05_Outputs/...]]
open_risks:
  - [Remaining risk or unresolved issue]
last_updated: YYYY-MM-DD
tags: [run-log, reasoning]
---
```

## Copy-Ready Body

```markdown
# [Run Log Title]

## Objective

[What this run was trying to do.]

## Context Loaded

### Initial

- [[02_Analyst/...]]
- [[01_Source/...]]

### Pulled On Demand

- [[03_References/...]]
- [[05_Outputs/...]]

## Route Used

- Task class: `quick-turn | standard | high-stakes | deep-research | ops-automation`
- Agent pattern: `single pass | reviewer-loop | multi-agent consensus | router-manager`

## Execution Summary

- [Step 1]
- [Step 2]
- [Step 3]

## Review Findings

- [Most important flaw found]
- [How it was resolved]

## Artifacts Produced

- [[02_Analyst/...]]
- [[05_Outputs/...]]

## Remaining Risks

- [What still needs validation, review, or user judgment]

## Next Best Action

- [The cleanest next move from here]
```

## Notes

- Keep this short and decision-focused.
- If the run was purely operational and produced no durable artifact, it usually does not need a full run log.
