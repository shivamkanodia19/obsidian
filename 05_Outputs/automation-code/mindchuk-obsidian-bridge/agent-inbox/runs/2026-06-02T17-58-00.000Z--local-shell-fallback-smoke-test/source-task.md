---
title: "Local Shell Fallback Smoke Test"
status: "pending"
source: "local-test"
mindchuk_kind: "agent_command"
source_message_id: "local-shell-fallback-smoke-test"
sent_at: "2026-06-02T17:58:00.000Z"
tags:
  - "AGENT"
---

## Prompt
Run exactly one shell command to print the current working directory. Then write `success-note.md` in the run directory. The success note must include:

- the line `PASS`
- the printed working directory
- one sentence confirming the fallback pipeline works

Do not modify any files outside the run directory.
