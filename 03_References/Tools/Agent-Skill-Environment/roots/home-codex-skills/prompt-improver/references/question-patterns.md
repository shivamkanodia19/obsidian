# Question Patterns for Effective Clarification

This reference covers how to ask clarifying questions without turning prompt improvement into unnecessary ceremony.

## Table of Contents

- [Ask or Assume](#ask-or-assume)
- [Question Construction Principles](#question-construction-principles)
- [Question Count Guidelines](#question-count-guidelines)
- [Question Templates by Category](#question-templates-by-category)
- [Option Generation Best Practices](#option-generation-best-practices)
- [Common Pitfalls](#common-pitfalls)

## Ask or Assume

Before writing a question, decide whether you even need one.

### Prefer an assumption when:
- one choice is clearly the default
- the consequence of being wrong is low
- the user can easily correct course later
- the repo or conversation strongly implies the answer

### Prefer a question when:
- the choice materially changes scope or output
- there are multiple plausible targets
- the user’s preference is the main unknown
- guessing would waste significant time or create rework

If you do ask, keep it to the smallest decisive question.

## Question Construction Principles

### Core principles

1. **Ground every option**
   - Use conversation history, repo findings, docs, or current research
   - Do not invent abstract choices if concrete ones are available

2. **Ask one decision at a time**
   - Keep each question focused on a single blocker

3. **Make options executable**
   - Each option should imply a real next step

4. **Explain the trade-off briefly**
   - One sentence is usually enough

5. **Avoid fake optionality**
   - Do not present multiple options when only one is realistic

## Question Count Guidelines

Use as few questions as possible.

- **0 questions**: execute directly
- **1 question**: default when only one decisive unknown remains
- **2-3 questions**: moderate ambiguity with independent decisions
- **4 max**: only when several high-impact decisions are genuinely coupled

Do not default to 5-6 questions.

## Question Templates by Category

### 1. Target selection

**When:** The action is clear, but the target is not.

Examples:
- Which file should be updated?
- Which model family should this target?
- Which bug are you referring to?

Good option shape:
- concrete file or component names
- concrete model names
- concrete bug candidates from recent findings

### 2. Scope selection

**When:** The target is known, but how far to go is unclear.

Examples:
- Should this be a narrow fix or a broader cleanup?
- Do you want docs only, code plus docs, or code plus docs plus tests?

Good option shape:
- minimal scope
- balanced scope
- full scope

### 3. Output contract

**When:** The work is clear, but the final deliverable is not.

Examples:
- Should the result be a patch, summary, plan, or draft?
- Do you want plain text, Markdown, JSON, or a table?

Good option shape:
- formats with real downstream implications
- audience-specific deliverables

### 4. Preference / policy choice

**When:** The main unknown is user preference rather than technical uncertainty.

Examples:
- concise vs detailed
- safe refactor vs aggressive cleanup
- internal-only vs user-facing docs

### 5. Freshness-sensitive choice

**When:** The answer depends on which current source or current target to optimize for.

Examples:
- latest stable vs latest preview model
- official docs only vs docs plus recent papers

## Option Generation Best Practices

Good options should be:
- concrete
- mutually exclusive when possible
- easy to compare
- directly tied to the next action

Good:
- `GPT-5.5`
- `GPT-5.4-mini`
- `Claude Opus 4.7`

Bad:
- `Use a different model`
- `Try another approach`
- `More advanced option`

If an "Other" path is plausible, rely on the UI's free-form escape hatch instead of making your listed options vague.

## Common Pitfalls

Avoid:
- asking questions answerable from the repo or conversation
- asking for preferences too early when execution can begin safely
- giving generic labels with no trade-offs
- packing multiple decisions into one question
- over-asking because the prompt is short

## Quick Checklist

Before asking:

- [ ] Is a question actually necessary?
- [ ] Is this the smallest decisive question?
- [ ] Are the options grounded in real context?
- [ ] Will the answer clearly change the next action?
- [ ] Am I keeping the total question count minimal?
