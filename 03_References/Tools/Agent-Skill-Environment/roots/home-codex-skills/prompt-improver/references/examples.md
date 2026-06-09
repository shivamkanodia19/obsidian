# Examples of Prompt Improvement

These examples reflect the newer policy:
- do not assume every short prompt is vague
- research only when it changes the next action
- ask fewer questions
- verify freshness when the task depends on current information

## 1. Clear Prompt, Execute Immediately

**Prompt:**
```text
Refactor `getUserById` in `src/api/users.ts` to use async/await instead of chained promises. Keep the return type unchanged and update tests if needed.
```

**Decision:**
- clear enough to execute
- no research
- no clarification questions

**Why:**
- target is named
- action is named
- constraint is named
- verification path is implied

## 2. Low Ambiguity, One Safe Assumption

**Prompt:**
```text
rename this variable to something clearer
```

**Context:**
- the user was just discussing one specific file and highlighted a single variable

**Decision:**
- no research
- no clarification question
- proceed using the active file context

**After execution:**
- briefly note the assumed variable target if useful

## 3. One Question, No Broad Research

**Prompt:**
```text
update the docs for this
```

**Context:**
- the code change is known from the conversation
- unknown: whether the docs should be user-facing or developer-facing

**Decision:**
- ask one question
- do not start broad repo exploration first

**Good question:**
- `Which docs should I update?`
  - `User docs` - public behavior and usage only
  - `Dev docs` - implementation notes and maintenance details
  - `Both` - update both surfaces together

## 4. Targeted Research Before Asking

**Prompt:**
```text
fix the bug
```

**Context:**
- no active bug target in conversation

**Decision:**
- ask one grounding question immediately if there is no anchor at all
- only inspect likely bug signals first when the conversation or current work already points to a likely area

**Useful research:**
- failing tests
- recent error logs mentioned in repo or conversation
- recent commits
- likely touched files

**Good question after research:**
- `Which bug should I fix?`
  - `Token validation failure in auth.ts` - matches failing auth tests
  - `Login redirect regression` - touched in a recent commit
  - `Session timeout issue` - recent error path in session handling

## 5. Freshness-Sensitive Prompt

**Prompt:**
```text
use the latest research for the latest models
```

**Decision:**
- current-source verification is required
- use primary sources first
- do not answer from memory

**Useful sources:**
- official provider model pages
- official prompting guides
- recent papers for broader empirical claims

## 6. Repo Pattern Choice

**Prompt:**
```text
add validation here
```

**Context:**
- location is known from active file
- unknown: whether validation belongs inline, in middleware, or in a shared helper

**Decision:**
- inspect nearby patterns
- ask one grounded scope/placement question only if the repo supports multiple real patterns

**Bad approach:**
- asking generic questions like `what kind of validation do you want?` before checking the codebase

**Better approach:**
- inspect similar endpoints first
- then ask:
  - `Where should validation live?`
    - `Inline in this handler` - matches most files in this module
    - `Shared helper` - reuse across multiple entry points
    - `Middleware layer` - centralize request validation

## 7. Long-Context Prompt

**Prompt:**
```text
review this large set of notes and tell me what I should do next
```

**Decision:**
- if the notes are already present, do not ask generic questions first
- extract objective, constraints, and candidate next steps from the context
- ask at most one follow-up if success criteria are still missing

## 8. Model-Specific Prompt Improvement

**Prompt:**
```text
write me a better prompt for this agent
```

**Decision:**
- determine what the agent must do
- rewrite around:
  - objective
  - constraints
  - tool policy
  - output contract
  - verification

**Do not default to:**
- making the prompt longer
- inserting exposed chain-of-thought boilerplate
- adding examples unless they improve format, tone, or edge-case handling
