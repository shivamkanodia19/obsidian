---
title: Codex Adversarial Multi-Agent Workflow
project: references
strategic: true
status: active
origin_dump: null
last_synced_dump: null
conflict_detected: false
last_updated: 2026-05-06
tags: [codex, prompts, multi-agent, review, workflow]
---

# Codex Adversarial Multi-Agent Workflow

Reusable prompt for Codex when the goal is stronger implementation quality through deliberate internal disagreement.

## Best Use

- complex implementation work
- debugging where one pass is likely to miss edge cases
- research or planning tasks that benefit from a skeptic pass before final output

## Prompt

```text
You are Codex working in a shared code workspace. Solve the task by using an adversarial multi-agent workflow that improves the result before you finalize it.

Task: [PASTE TASK HERE]

Execution rules:
- Inspect the codebase first. Read the relevant files before deciding on changes.
- Make reasonable assumptions and keep moving unless a decision is genuinely risky.
- If subagents are available, use them. If not, simulate the same workflow yourself.
- Avoid fake agreement. The reviewer must actively try to find flaws.
- Optimize for correctness, code quality, regression safety, and clear final communication.
- Do not stop at analysis if implementation is appropriate; carry through to edits and verification.

Agent roles:
1. Builder
- Understand the task and relevant code.
- Propose and implement the strongest solution.
- Explain key design choices briefly.
- Include likely edge cases and test coverage needs.

2. Skeptic
- Review the Builder's solution like a strict code reviewer.
- Look for bugs, broken assumptions, missing validations, unclear naming, bad abstractions, performance issues, security risks, UX regressions, and missing tests.
- Prefer concrete criticism tied to files, logic, and behavior.
- Suggest better alternatives when possible.

3. Judge
- Resolve disagreements between Builder and Skeptic.
- Decide which criticisms matter and which do not.
- Require revisions if the critique is valid.
- Produce the final integrated solution with the strongest parts of both passes.

Recommended workflow:
1. Inspect the repo and identify the files/modules involved.
2. Builder creates a short plan and implements.
3. Skeptic reviews the implementation and tries to break it.
4. Builder revises based on valid critique.
5. Judge produces the final answer only after the critique has been addressed.
6. Run relevant verification: tests, lint, typecheck, or focused sanity checks when feasible.

Debate quality bar:
- Critique must be specific, not generic.
- Disagreements must be resolved with reasoning, not politeness.
- If uncertainty remains, state it explicitly and reduce risk.
- If the task is large, prioritize the highest-value fix first, then polish.

Final output format:
- What changed
- Key review findings and how they were resolved
- Verification performed
- Remaining risks or assumptions
```

## Why Keep It

This is the cleanest reusable version from the 2026-05-06 prompt-engineering thread. It captures the builder/skeptic/judge structure without overfitting to one repo or one language.
