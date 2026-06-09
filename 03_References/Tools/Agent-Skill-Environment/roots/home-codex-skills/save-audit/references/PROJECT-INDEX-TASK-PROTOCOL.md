# Project Index Task Protocol

Use project or topic `_index.md` frontmatter as the default prompt brief when that index declares:

```yaml
agent_context: true
```

Required scalar fields:

- `project`
- `scope`
- `status`

Required list fields:

- `current_focus`
- `active_tasks`
- `prompt_context`
- `definition_of_done`

Optional but useful:

- `blocked_by`
- `task_cards`
- `surface_in_root`

Rules:

1. Keep each list short. Usually 1-3 items is enough.
2. Prefer one-topic task context in the nearest `_index.md` instead of creating a separate task file by default.
3. Create a standalone task card only when the task is cross-project, high-stakes, reusable, or needs a reviewer-loop trail.
4. Treat stale task frontmatter as routing drift. If the index says one thing and the canonical note says another, update the index first.
5. `prompt_context` should point to the smallest useful set of canonical notes, not every related file.
6. Use `surface_in_root: true` only on primary hubs that should appear in the root Analyst router.
