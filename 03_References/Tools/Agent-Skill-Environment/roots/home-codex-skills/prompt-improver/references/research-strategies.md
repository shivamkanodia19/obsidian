# Research Strategies for Context Gathering

This reference explains how to gather only the context that is actually needed to improve a prompt.

The main change in this version is simple:
- **do not research by default**
- **research only when it changes the next action**

## Table of Contents

- [Triage Before Research](#triage-before-research)
- [When Research Is Worth It](#when-research-is-worth-it)
- [Research Order](#research-order)
- [Repo Research Patterns](#repo-research-patterns)
- [Current-Source Research](#current-source-research)
- [Stop Conditions](#stop-conditions)

## Triage Before Research

Before opening files or searching the web, identify the kind of gap:

- **Target gap**: Which file, API, component, model, or artifact?
- **Scope gap**: How much should change?
- **Approach gap**: Which of several materially different paths?
- **Constraint gap**: What must remain unchanged?
- **Freshness gap**: Does the answer depend on current information?

If none of those gaps matter enough to block execution, do not research.

## When Research Is Worth It

Research is usually worth doing when:
- the user’s target is unclear and the repo can narrow it down
- you need concrete options before asking a question
- current docs or releases may have changed recently
- the request is high-stakes and stale knowledge is risky
- existing patterns in the codebase should influence the recommendation

Research is usually not worth doing when:
- the conversation already answers the question
- only one low-risk assumption is missing
- the prompt is short but still executable
- you are searching for context you do not actually need
- there is no anchor at all and the cheapest next step is one grounding question

## Research Order

Use this order unless the task clearly requires something else:

1. **Conversation history**
2. **Local files and project docs**
3. **Tests / recent failures / recent changes**
4. **Primary external sources** for unstable or authoritative facts
5. **Secondary external sources** only if needed

### Conversation history

Check first for:
- named files or functions
- prior decisions
- already-declared preferences
- prior errors or outputs
- scope limits the user already stated

### Local repo

Check local context when the task is implementation- or repo-dependent:
- related files
- similar implementations
- tests
- project docs
- config and build scripts

### External sources

Use external research when:
- the user asked for the latest info
- the topic is unstable
- accuracy depends on current vendor docs, release notes, laws, or prices

Prefer official docs, official product pages, release notes, standards bodies, or primary papers.

## Repo Research Patterns

### Pattern 1: Narrow the target

Use when the request names an action but not the target.

Examples:
- `fix the bug`
- `update the tests`
- `refactor this`

Useful checks:
- current working files from the conversation
- failing tests
- recent modified files
- likely pattern matches in the repo

Apply a small budget here:
- prefer 2-3 quick checks, not an open-ended search
- stop once you have 1-3 plausible candidates
- if you still do not have candidates, ask immediately

Prerequisite:
- only do this when you have at least one anchor such as a current file, subsystem, recent error, or active topic
- if you do not have an anchor, ask a grounding question first

Avoid:
- full repo enumeration
- giant unfiltered file listings
- broad keyword searches that generate hundreds of hits without narrowing the decision

### Pattern 2: Ground answer choices

Use when you will probably need to ask a question, but the options should come from the repo instead of your imagination.

Examples:
- auth strategy already used elsewhere
- naming conventions
- where similar validation or logging lives
- which config file usually owns a behavior

### Pattern 3: Verify constraints

Use when the user’s request could conflict with existing rules.

Examples:
- tests must stay intact
- API format is externally consumed
- project uses a specific framework pattern
- a migration must preserve backward compatibility

### Pattern 4: Check recent change history

Use when behavior may have shifted recently.

Useful for:
- regressions
- bugs after recent merges
- duplicate work avoidance
- understanding why a pattern exists

## Current-Source Research

For latest-model or latest-research tasks, research should be:
- **primary-source first**
- **date-aware**
- **cross-checked when possible**

Good primary sources:
- official API docs
- official model pages
- official release posts
- research papers
- standards or government sources when relevant

For technical model guidance, prefer:
- official vendor docs first
- papers for broader empirical claims

## Stop Conditions

Stop researching when you can do one of these confidently:

1. execute directly
2. make a safe assumption
3. ask 1-3 grounded clarification questions

Also stop if your first 2-3 narrowing checks did not materially reduce ambiguity. At that point, more searching is usually a sign that a user question is cheaper than more exploration.

Do not keep researching just to make the prompt feel more sophisticated.

## Practical Checklist

Before moving on from research, verify:

- [ ] I know whether the prompt is actually blocked
- [ ] I checked conversation state first
- [ ] I used local context before external research when appropriate
- [ ] Any web research used primary or authoritative sources
- [ ] I have enough context to execute or ask specific questions
- [ ] I am not researching beyond the real blocker
