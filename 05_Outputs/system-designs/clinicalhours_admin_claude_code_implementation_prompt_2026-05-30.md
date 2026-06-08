---
title: ClinicalHours Admin Claude Code Implementation Prompt
project: clinicalhours
status: handoff-ready
last_updated: 2026-05-30
tags: [clinicalhours, admin, claude-code, implementation-prompt]
---

# ClinicalHours Admin Claude Code Implementation Prompt

Use the prompt below as the implementation brief for Claude Code inside the ClinicalHours application repository.

## Prompt

```text
You are implementing the next major version of the ClinicalHours admin.

Context:

- Product: ClinicalHours
- Current route: `/admin`
- Observed stack from the live app: React + Vite-style bundle + Supabase + Supabase Edge Functions
- There is already a live admin with these major surfaces:
  - top-level tabs: Dashboard, Users, Hospitals, Automation, Supply, Settings
  - Dashboard already includes KPIs, Live Activity Stream, Guest Session Analytics, Funnel Analysis, High-Intent Abandoners, Zero-Save Opportunities, and a placeholder Search Gap Analysis card
  - Users already includes authenticated users + guest users, funnel-stage filtering, user detail, and profile inspection
  - Hospitals already includes Hospital Pages, Hospital Accounts, Pending Approvals, and Notifications
  - Automation already includes cohort-like operator tools such as High-Intent Abandoners, Dormant Signups, High-Intent Guests, Hospitals Awaiting Review, and Stale Opportunities
  - Supply already includes clinic admin console launching
  - Settings already includes mass email, CSV import, data quality jobs, maintenance, logos, and premium monitoring
  - There is already an Admin Assistant entry point

High-level goal:

Turn the admin into a business operating system for ClinicalHours that can run:

- clinic acquisition
- student growth and conversion
- clinic onboarding and support
- marketplace supply quality
- revenue monitoring
- internal operations

This is a constrained, auditable, domain-specific agentic admin OS. It is not a generic multi-agent playground.

Core design principles:

1. Preserve existing working admin capabilities unless they are clearly redundant.
2. Reuse and refactor current admin modules instead of replacing everything from scratch.
3. Agents may think broadly but must act narrowly.
4. All risky actions require explicit approval.
5. Data trust is a first-class product area.
6. The admin home should be a control tower, not a flat dashboard.
7. Add feature flags and safe rollout guards for all agentic and messaging functionality.

Target information architecture:

- Control Tower
- Growth
- Clinic Pipeline
- Clinic Ops
- Supply
- Messaging
- Revenue
- Data Trust
- Settings
- Agent Inbox

Map existing features into this IA instead of deleting them:

- Dashboard -> Control Tower
- Users -> mostly Growth
- Hospitals -> split into Clinic Pipeline and Clinic Ops
- Automation -> evolve into Agent Inbox + workflow launchers
- Supply -> retain and deepen
- Settings -> retain internal tools with stronger safeguards

System architecture to implement:

1. System of record
   - students
   - guest sessions
   - hospitals / hospital pages
   - clinic leads and contacts
   - opportunities
   - campaigns and sequences
   - approvals
   - premium / revenue state
   - data quality incidents

2. System of execution
   - lead research
   - contact enrichment
   - outreach drafting
   - campaign launches
   - hospital approval review
   - clinic onboarding
   - stale opportunity cleanup
   - funnel interventions

3. System of intelligence
   - anomaly detection
   - next-best-action suggestions
   - draft generation
   - cohort generation
   - priority scoring
   - run summaries

Business loops to support:

1. Clinic acquisition loop
   - discover clinic
   - enrich contact and clinic context
   - score fit and urgency
   - draft outreach
   - require human approval before send
   - track reply / meeting / pilot / live clinic

2. Student conversion loop
   - detect drop-off cohorts
   - explain where they stalled
   - generate recommended intervention
   - require human approval for sends
   - measure lift

3. Clinic onboarding loop
   - track pending approvals
   - identify onboarding blockers
   - assign follow-up actions

4. Supply quality loop
   - detect stale / duplicate / low-signal / incomplete opportunities
   - auto-run safe repairs
   - require approval for archive / destructive actions

5. Revenue loop
   - monitor premium and clinic commercial state
   - flag churn / renewal / inactivity risks

Agent roster to implement:

- Router / Chief of Staff Agent
- Funnel Analyst Agent
- Clinic Lead Research Agent
- Outreach Drafter Agent
- Sequence Manager Agent
- Clinic Onboarding Agent
- Supply Quality Agent
- Revenue Monitor Agent
- Data Trust Agent

Important:
- Do not implement these as vague chat-only personas.
- Implement them as structured workflows over explicit data models, task queues, and approval gates.
- Use agent disagreement selectively only where judgment matters. Example: proposer + reviewer + human approver for clinic outreach or archive recommendations.

Required new backend concepts:

- clinic leads
- lead contacts
- pipeline stage history
- campaigns
- campaign audiences
- campaign messages
- message sequences
- sequence steps
- agent tasks
- agent runs
- agent recommendations
- approval tasks
- metric definitions
- metric snapshots
- data quality incidents
- playbooks

Implement concrete database changes:

- add migrations for the new tables
- add indexes for common filtering and queue operations
- add RLS policies and role-aware access rules
- add audit fields for all approval- and agent-driven records

Implement concrete backend APIs / functions:

- agent router
- lead enrichment
- outreach draft generation
- cohort builder
- sequence queueing
- send-approved-campaign
- approve-agent-action
- metric snapshot recompute
- data trust audit

Existing functions in the app may already exist for:

- mass email
- CSV import
- data quality jobs
- hospital review

Inspect and reuse them where possible, but fix any dangerous coupling.

Critical safety requirement:

No agent-generated or cohort-generated email may send automatically without an explicit approval state.

Model outbound message states:

- draft
- needs_review
- approved
- queued
- sent
- failed
- cancelled

Each message must preserve:

- author source (human or agent)
- reasoning / template provenance
- target audience definition
- approval chain
- final send result

Build these product surfaces:

1. Control Tower
   - KPI strip
   - Needs Attention queue
   - agent recommendations
   - data trust status
   - open approvals
   - stale opportunity count
   - outreach queue
   - conversion alerts

2. Growth
   - funnel by time range
   - cohort explorer
   - high-intent abandoners
   - dormant signups
   - high-intent guests
   - search gap analysis
   - campaign performance

3. Clinic Pipeline
   - lead table / board
   - lead detail
   - contact detail
   - research notes
   - fit and urgency scores
   - outreach sequence state
   - stage movement history
   - next actions

4. Clinic Ops
   - pending approvals
   - onboarding blockers
   - active clinic health
   - launch into clinic admin consoles

5. Supply
   - stale opportunities
   - low-engagement opportunities
   - duplicate detection
   - incomplete opportunity queues
   - repair previews
   - archive recommendations

6. Messaging
   - audience builder
   - templates
   - draft review
   - approval queue
   - send history
   - experiment / sequence performance

7. Revenue
   - premium summary
   - subscription health
   - pilot / live clinic commercial pipeline
   - churn and renewal flags

8. Data Trust
   - metric definitions
   - freshness timestamps
   - source-of-truth mapping
   - anomaly log
   - failed jobs
   - audit log

9. Agent Inbox
   - queued recommendations
   - blocked tasks
   - drafts awaiting approval
   - failed agent runs
   - recent run history

Implementation constraints:

- Inspect the codebase first and understand existing admin components before changing structure.
- Preserve working behaviors from the current admin and refactor them into the new IA.
- Use feature flags for unfinished or risky areas.
- Keep all destructive and send-capable actions behind confirmation and approval flows.
- If the existing live admin has current data jobs or email tools, keep them available during migration.
- Prefer incremental integration over hard replacement.

Expected developer workflow:

1. Audit the existing admin routes, components, data hooks, Supabase tables, and edge functions.
2. Produce a short implementation plan in the repo.
3. Add schema migrations and backend primitives first.
4. Refactor the admin IA and routing.
5. Build new domain models and queue views.
6. Integrate agent task orchestration and approvals.
7. Add tests.
8. Run the test suite and fix failures.
9. Update internal docs / README for the admin architecture.

Testing requirements:

- unit tests for scoring, state transitions, and permission checks
- integration tests for approval flows
- integration tests for message state machine
- integration tests for lead pipeline transitions
- smoke tests for the admin route and key tabs

Acceptance criteria:

- A founder can open `/admin` and immediately see what changed, what needs action, and what agents recommend.
- Clinic acquisition can be run from the admin through a lead pipeline.
- Student conversion campaigns can be drafted and approved from the admin.
- Hospital approvals, opportunity cleanup, and messaging all have explicit review controls.
- Every risky action is auditable.
- Data trust is visible enough that operators know whether to trust the dashboard.
- Existing core admin utilities still work.

If codebase reality differs from this prompt:

- trust the codebase over this prompt for implementation details
- preserve current production-safe behaviors
- adapt the design without losing the business intent

Do not stop at mockups or planning. Implement the full system end-to-end in the repository, including migrations, backend, UI, tests, and documentation.
```

## Notes For The Implementer

- The current live admin already has useful operator cohorts. Reuse them rather than rebuilding them from zero.
- The current admin already has risky internal tools in `Settings`. Add stricter approval and audit semantics there.
- Treat messaging with special caution.
- If current send flows are coupled too broadly, split them before building agent-generated targeting on top.
