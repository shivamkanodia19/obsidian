---
name: prompt-improver
description: This skill improves underspecified prompts by deciding whether to execute directly, make a safe assumption, do minimal targeted research, or ask a small number of grounded clarification questions.
---

# Prompt Improver Skill

## Purpose

Turn ambiguous prompts into executable requests with the least friction possible.

This skill is not a license to over-question or over-research. Its job is to:
- detect whether a prompt is actually underspecified
- recover missing context from the conversation or repo when helpful
- ask only the minimum clarifying questions needed
- proceed with execution once ambiguity is low enough

## What Changed

Modern frontier models usually do better with:
- direct, outcome-first instructions
- explicit constraints and success criteria
- structured output contracts over prose-only formatting requests
- strong tool/context design instead of "clever prompt wording"

This skill should therefore optimize for:
- **clarity over cleverness**
- **minimal blocking**
- **grounded options**
- **current-source verification when freshness matters**
- **ask Shivam when ambiguity is meaningful instead of silently guessing**

## When This Skill Is Invoked

**Automatic invocation:**
- A `UserPromptSubmit` hook runs on every prompt
- The hook asks the model to evaluate whether enrichment is needed
- This skill guides what to do next

**Manual invocation:**
- Improve a vague request before execution
- Tighten a prompt-writing workflow
- Build grounded clarification questions for a repo or research task

## Decision Policy

Do this first on every prompt:

### 1. Triage the prompt

Classify the request into one of four buckets:

1. **Clear enough to execute**
   - Target is identifiable
   - Desired outcome is understandable
   - Risk of a wrong assumption is low
   - Action: execute normally

2. **Low ambiguity**
   - One small detail is missing
   - A reasonable assumption is available
   - Consequences of guessing are limited
   - Action: prefer execution with a stated assumption, or ask one short question if the assumption is risky

3. **Meaningful ambiguity**
   - Missing target, scope, approach, or acceptance criteria would materially change the work
   - Repo state, docs, or existing patterns are needed to ground options
   - Action: do minimal targeted research, then ask 1-3 concrete questions

4. **Freshness / high-stakes ambiguity**
   - The request depends on current docs, prices, laws, model capabilities, schedules, or other unstable facts
   - Or the task is high-stakes enough that outdated knowledge is risky
   - Action: verify with current primary sources before asking or executing

Workspace preference:
- if a prompt is materially ambiguous or has multiple non-obvious paths, prefer asking a grounded clarification question over silently choosing a path for Shivam

### 2. Build the missing contract

When a prompt needs improvement, recover or clarify these in order:
- **Objective**: What is the user actually trying to achieve?
- **Target**: Which file, system, dataset, API, model, or artifact is involved?
- **Constraints**: What must or must not change?
- **Tools / data**: What context or tools are relevant?
- **Output contract**: What should the final answer or artifact look like?
- **Verification**: How will success be checked?

Do not ask about items the conversation or repo already answers.

## Core Workflow

### Phase 1: Check Existing Context

Before doing any new work:
- review recent conversation state
- reuse prior decisions, file references, and constraints
- avoid asking for information the user already gave

If the conversation already resolves the ambiguity, skip research and questions.

### Phase 2: Research Only When Needed

Research is **conditional**, not mandatory.

Research only when it will materially improve the next action:
- identify the right target
- ground answer choices in real repo patterns
- verify unstable or current facts
- reduce the chance of asking a lazy or generic question

Stop researching as soon as you can either:
- execute safely, or
- ask grounded questions with concrete options

For completely targetless prompts like `fix the bug` or `update this`, use a **small research budget**:
- start with the active conversation context
- then do at most 2-3 cheap narrowing checks
- if those checks do not surface 1-3 strong candidates, stop and ask a question

Do not do broad repo wandering, exhaustive file listing, or large-scale grep sweeps just to avoid asking a question.

If there is **no anchor at all** from the prompt or conversation:
- no file
- no subsystem
- no current error
- no active artifact
- no recent target already in context

then prefer asking **one immediate grounding question** before repo exploration.

Research-first is best when you already have at least one concrete lead.

### Phase 3: Generate Minimal Grounded Questions

Ask questions only when they unblock meaningful decisions.

**Default count:**
- `0 questions`: prompt is clear enough, or a safe assumption exists
- `1 question`: one decisive unknown remains
- `2-3 questions`: moderate ambiguity with multiple independent decisions
- `4 questions max`: only for truly coupled, high-impact decisions

Never ask a shotgun list of generic questions.

Each question should:
- resolve exactly one decision point
- be grounded in conversation, repo findings, docs, or current-source research
- offer 2-4 concrete options
- explain trade-offs briefly

### Phase 4: Execute Once Unblocked

Once ambiguity is low enough:
- proceed with the user's request
- use the clarified contract, not the original vague phrasing
- keep the final work outcome-focused

If you made a reasonable assumption instead of asking, state it briefly after doing the work.

## Research Guidance

Prefer this order:

1. **Conversation history**
2. **Local repo and docs**
3. **Primary external sources** when freshness or authority matters
4. **Secondary sources** only if primary sources are unavailable or insufficient

For repo work, common useful checks are:
- related files and nearby implementations
- tests and failing checks
- project docs and config
- recent commits when behavior changed recently

For current-information tasks, prefer:
- official documentation
- official release notes
- primary product pages
- canonical API docs

Do not browse the web just because a prompt is short.

For detailed tactics, see [references/research-strategies.md](references/research-strategies.md).

## Clarification Guidance

Good clarification questions are:
- short
- specific
- grounded
- decision-oriented

Bad clarification questions are:
- generic
- repetitive
- answerable from existing context
- broader than the actual blocker

For templates and patterns, see [references/question-patterns.md](references/question-patterns.md).

## Prompt Improvement Principles

When mentally rewriting or tightening a prompt, prefer:
- **Outcome-first wording**: start from the result needed
- **Direct instructions**: avoid decorative phrasing
- **Explicit constraints**: name non-negotiables
- **Structured outputs**: use schema / JSON / XML / tables when appropriate
- **Few-shot only when useful**: best for format, tone, and edge cases
- **Tool-aware design**: rely on tool descriptions and concrete context, not boilerplate repetition

Avoid assuming that longer prompts are better.

## Examples

### Example 1: Low Ambiguity, No Research Needed

**Prompt:** `rename this variable to something clearer`

**Context:** User is already discussing a specific file and highlighted a variable moments ago.

**Decision:**
- no research
- no clarifying questions
- execute directly using existing context

### Example 2: One Question, No Broad Research

**Prompt:** `update the docs for this`

**Context:** The code change is already clear, but the intended audience is not.

**Decision:**
- ask one short question such as whether docs should target users or developers
- do not launch broad repo exploration first

### Example 3: Targeted Research Before Asking

**Prompt:** `fix the bug`

**Context:** No active bug target in conversation.

**Decision:**
- inspect failing tests / recent errors / likely target files
- then ask one grounded question with concrete options

### Example 4: Freshness-Sensitive Prompt

**Prompt:** `use the latest research for the latest models`

**Decision:**
- verify current models and current provider guidance from primary sources
- then synthesize the prompt or answer using current evidence

For broader scenarios, see [references/examples.md](references/examples.md).

## Key Principles

1. **Short does not mean vague**
2. **Research is conditional, not automatic**
3. **Ask fewer questions**
4. **Ground every option**
5. **Prefer execution once risk is low enough**
6. **Use current primary sources when freshness matters**
7. **Optimize for outcome, constraints, tools, schema, and verification**
8. **Respect Shivam's standing preference for clarification when ambiguity is meaningful**

## Progressive Disclosure

This file contains the operating policy. Load references only when needed:

- **Research tactics**: [references/research-strategies.md](references/research-strategies.md)
- **Question templates**: [references/question-patterns.md](references/question-patterns.md)
- **Worked examples**: [references/examples.md](references/examples.md)
