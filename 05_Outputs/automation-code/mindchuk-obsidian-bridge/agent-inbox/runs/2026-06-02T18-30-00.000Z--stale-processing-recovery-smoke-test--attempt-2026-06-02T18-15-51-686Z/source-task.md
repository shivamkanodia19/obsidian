---
title: "Stale Processing Recovery Smoke Test"
status: "pending"
source: "local-test"
mindchuk_kind: "agent_command"
source_message_id: "stale-processing-recovery-smoke-test"
sent_at: "2026-06-02T18:30:00.000Z"
tags:
  - "AGENT"
run_id: "stale-processing-recovery-smoke-test"
runner_started_at: "2026-06-02T12:00:00.000Z"
runner_mode: "codex-refine-then-execute"
runner_recovered_at: "2026-06-02T18:15:51.680Z"
---

## Prompt
Run exactly one shell command to print the current working directory. Then write `success-note.md` in the run directory. The note must include:

- the line `PASS`
- one sentence saying the stale processing task was recovered successfully
- the printed working directory

Do not modify any files outside the run directory.

## Runner
- status: pending
- started_at: 
- completed_at: 
- exit_code: 
- run_id: 
- run_dir: 
- result_summary: Recovered after a previous runner interruption.
