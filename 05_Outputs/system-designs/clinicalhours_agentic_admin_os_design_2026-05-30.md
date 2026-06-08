---
title: ClinicalHours Agentic Admin OS Design
project: clinicalhours
status: strategy-ready
last_updated: 2026-05-30
tags: [clinicalhours, admin, agentic-os, system-design, automation]
---

# ClinicalHours Agentic Admin OS Design

## Objective

Turn the ClinicalHours admin into a business operating system that can run:

- clinic acquisition
- student growth and conversion
- clinic onboarding and support
- marketplace supply quality
- revenue monitoring
- internal operations

This should not be a generic "multi-agent society." It should be a constrained, auditable, business-specific agentic system.

## Why This Is The Right Frame

The broad "agentic OS" idea and the ClinicalHours admin goal share the same core pattern:

- specialized agents with clear roles
- shared memory and shared business state
- task routing and handoffs
- review and challenge loops where judgment matters
- action controls and audit logs

ClinicalHours does **not** need open-ended agent collaboration for everything. It needs a focused operating system for recurring business loops.

## Live Admin Baseline (Observed 2026-05-29 / 2026-05-30)

The shipped admin already includes:

- top-level tabs: `Dashboard`, `Users`, `Hospitals`, `Automation`, `Supply`, `Settings`
- `Dashboard` modules for KPIs, live activity, guest session analytics, funnel analysis, high-intent abandoners, zero-save opportunities, and placeholder search-gap analysis
- `Users` tab for authenticated users + guest sessions, funnel-stage filtering, user detail, and deeper profile inspection
- `Hospitals` tab for hospital pages, hospital accounts, pending approvals, and notification logs
- `Automation` tab for ready-to-act cohorts such as high-intent abandoners, dormant signups, high-intent guests, pending approvals aging, and stale opportunities
- `Supply` tab for launching clinic admin consoles
- `Settings` tab for mass email, CSV import, data quality, maintenance, logos, and premium monitoring
- floating `Admin Assistant`

This means the admin is already moving toward an operating console. The next step is to unify it around shared workflows, memory, permissions, and agent execution.

## Design Principles

1. Agents think broad, act narrow.
2. Every risky action must have an approval boundary.
3. The admin is a command center, not a metrics gallery.
4. Data trust is a first-class feature, not an afterthought.
5. Reuse existing admin surfaces wherever possible before inventing new ones.
6. Default to queues, playbooks, and cohorts over abstract AI magic.
7. Multi-agent debate should be used selectively for high-judgment tasks.

## The Three-Layer Model

### 1. System Of Record

The source of truth for:

- students
- guest sessions
- hospitals and hospital pages
- clinic leads and contacts
- opportunities
- campaigns and sequences
- approvals
- premium and revenue state
- data quality incidents

### 2. System Of Execution

The place where humans and agents operate:

- lead research
- contact enrichment
- outreach drafting
- campaign launches
- approval review
- clinic onboarding
- stale opportunity cleanup
- funnel interventions

### 3. System Of Intelligence

The layer that notices, prioritizes, recommends, drafts, and monitors:

- anomaly detection
- next-best-action suggestions
- lead scoring
- cohort generation
- draft generation
- follow-up scheduling
- metrics interpretation

## The Core Business Loops

### Clinic Acquisition Loop

1. Discover clinic
2. Enrich contact and context
3. Score fit and urgency
4. Draft outreach
5. Human approve send
6. Track reply and stage movement
7. Convert to meeting, pilot, live clinic, renewal

### Student Conversion Loop

1. Detect drop-off cohort
2. Diagnose where they stalled
3. Draft intervention
4. Human approve targeted send
5. Measure lift
6. Improve playbook

### Clinic Onboarding Loop

1. Detect pending approval or setup friction
2. Identify blocker
3. Recommend follow-up
4. Assign owner or agent
5. Track to activated clinic

### Supply Quality Loop

1. Detect stale, duplicate, missing, low-signal, or low-engagement opportunities
2. Queue repair or archive decisions
3. Execute safe fixes automatically
4. Route risky changes for approval

### Revenue Loop

1. Monitor premium and clinic revenue states
2. Flag churn or inactivity risk
3. Suggest retention or expansion actions
4. Track conversion and renewal health

## Target Information Architecture

The existing tabs should evolve into a clearer operating structure:

- `Control Tower`
- `Growth`
- `Clinic Pipeline`
- `Clinic Ops`
- `Supply`
- `Messaging`
- `Revenue`
- `Data Trust`
- `Settings`
- `Agent Inbox`

### Mapping From Current Admin

- current `Dashboard` -> `Control Tower`
- current `Users` -> mostly `Growth`
- current `Hospitals` -> split between `Clinic Pipeline` and `Clinic Ops`
- current `Automation` -> becomes both `Agent Inbox` and workflow launchers inside `Growth`, `Clinic Pipeline`, and `Supply`
- current `Supply` -> stays `Clinic Ops` launcher + `Supply`
- current `Settings` -> remains `Settings`, but internal tools get stricter safeguards

## Screen-Level Product Spec

### Control Tower

Purpose: answer "what changed, what needs action, what should we do next?"

Must include:

- daily and weekly business KPI strip
- `Needs Attention` queue
- agent recommendations panel
- data trust status
- high-risk anomalies
- pending approvals count
- open outreach tasks count
- stale opportunities count
- recent conversions and failures

### Growth

Purpose: run student acquisition, activation, and retention.

Must include:

- funnel by time range
- cohort explorer
- high-intent abandoners
- dormant signups
- high-intent guest sessions
- search gap analysis
- campaign performance
- reactivation playbooks

### Clinic Pipeline

Purpose: run clinic lead generation and outbound sales.

Must include:

- lead pipeline board
- lead and contact records
- fit and urgency scoring
- research notes
- email sequence state
- meeting / pilot / live clinic progression
- owner assignment
- next action date

### Clinic Ops

Purpose: run active clinic and hospital workflows.

Must include:

- pending approvals
- activated clinics
- clinic onboarding blockers
- jump-in links to clinic admin consoles
- clinic-level email, activity, positions, applicants, and settings

### Supply

Purpose: maintain opportunity quality and marketplace health.

Must include:

- stale opportunities
- low-engagement opportunities
- duplicate detection
- missing metadata queues
- geo / links / logo / state repair jobs
- archive recommendations

### Messaging

Purpose: centralize all controlled outbound sending.

Must include:

- audience builder
- campaign drafts
- sequence templates
- approval queue
- send history
- deliverability status
- experiment tracking

### Revenue

Purpose: monitor premium and clinic commercial health.

Must include:

- premium members
- subscription status
- premium page visitors
- clinic pilot pipeline
- active clinic subscriptions
- churn / renewal flags

### Data Trust

Purpose: make the admin trustworthy enough to run the business from.

Must include:

- metric definitions
- freshness timestamps
- source-of-truth ownership
- anomaly log
- ingestion failures
- audit log for agent and human actions

### Agent Inbox

Purpose: show what agents noticed, suggested, drafted, or need approved.

Must include:

- recommended actions
- queued drafts
- blocked workflows
- approval tasks
- failed runs
- agent run logs

## Agent Roster

The goal is not to create dozens of agents. Start with a compact stack.

### 1. Router / Chief Of Staff Agent

Role:

- reads state across the admin
- prioritizes work
- routes tasks to specialized agents
- assembles daily recommendations

Reads:

- KPI snapshots
- pending queues
- approvals
- active campaigns
- lead pipeline state

Writes:

- `agent_tasks`
- recommendation cards
- priority scores

Cannot:

- send, approve, delete, or archive anything directly

### 2. Funnel Analyst Agent

Role:

- interprets user behavior and conversion drop-offs
- generates cohorts
- suggests interventions

Reads:

- tracking events
- guest sessions
- signups
- saved opportunities
- applications

Writes:

- cohort definitions
- anomaly alerts
- experiment suggestions

### 3. Clinic Lead Research Agent

Role:

- discovers clinic leads
- enriches clinic records
- identifies pain signals and likely buyer roles

Reads:

- current lead database
- clinic pages
- external enrichment results

Writes:

- lead records
- contact candidates
- research notes
- fit / urgency scores

### 4. Outreach Drafter Agent

Role:

- drafts outbound clinic emails and student activation messages

Reads:

- contact record
- clinic intelligence
- sequence templates
- campaign goals

Writes:

- draft subject/body
- personalization reasoning
- send recommendation

Cannot:

- send directly

### 5. Sequence Manager Agent

Role:

- watches campaign state
- decides what should be queued next

Reads:

- sequence steps
- sends
- opens / replies / status fields

Writes:

- next-step tasks
- follow-up drafts
- sequence health flags

### 6. Clinic Onboarding Agent

Role:

- tracks pending hospital approvals and post-approval setup
- identifies blockers

Reads:

- hospital accounts
- hospital pages
- clinic setup status
- applicant / position readiness

Writes:

- follow-up tasks
- blocker labels
- health status

### 7. Supply Quality Agent

Role:

- detects stale, duplicate, broken, or underperforming supply

Reads:

- opportunities
- usage / save / apply signals
- quality flags

Writes:

- repair queues
- archive recommendations
- cleanup tasks

### 8. Revenue Monitor Agent

Role:

- tracks premium, pilot, and subscription health

Reads:

- premium records
- clinic subscription records
- usage signals

Writes:

- churn-risk flags
- renewal follow-up tasks
- revenue snapshots

### 9. Data Trust Agent

Role:

- monitors freshness, metric consistency, and broken pipelines

Reads:

- metric computations
- event counts
- import and function logs

Writes:

- incident records
- trust badges
- anomaly explanations

## Where Agent Disagreement Helps

Selective multi-agent challenge is valuable in these cases:

- clinic fit scoring
- whether to contact a lead now or later
- whether an outreach draft is strong enough to send
- whether a funnel anomaly is product-related or a tracking issue
- whether an opportunity should be repaired or archived

Recommended pattern:

- `proposer agent`
- `reviewer / challenger agent`
- `human approver` for risky actions

Do **not** add internal debate to routine low-risk operations.

## Human-In-The-Loop Policy

### Safe To Auto-Run

- cohort generation
- anomaly detection
- scoring
- draft creation
- summary generation
- queue prioritization
- non-destructive repair previews

### Requires Human Approval

- any outbound clinic email
- any outbound student campaign email
- hospital approval or rejection
- archiving or pausing a hospital page
- archiving a live opportunity
- mass imports
- destructive maintenance jobs

### Forbidden Without Explicit Override

- deleting records based on agent judgment alone
- changing pricing
- sending mass email automatically
- modifying clinic-facing copy in production without review

## Data Model Additions

The current admin uses existing platform tables, but an agentic admin needs several new business tables.

### New Tables

- `clinic_leads`
- `clinic_lead_contacts`
- `lead_pipeline_events`
- `campaigns`
- `campaign_audiences`
- `campaign_messages`
- `message_sequences`
- `sequence_steps`
- `agent_tasks`
- `agent_runs`
- `agent_recommendations`
- `approval_tasks`
- `metric_definitions`
- `metric_snapshots`
- `data_quality_incidents`
- `playbooks`

### Example Minimal Fields

`clinic_leads`
- `id`
- `clinic_name`
- `website`
- `location`
- `segment`
- `fit_score`
- `urgency_score`
- `pipeline_stage`
- `owner_user_id`
- `next_action_at`
- `source`
- `notes`

`clinic_lead_contacts`
- `id`
- `lead_id`
- `name`
- `title`
- `email`
- `phone`
- `confidence`
- `primary_contact`

`agent_tasks`
- `id`
- `task_type`
- `status`
- `priority`
- `entity_type`
- `entity_id`
- `assigned_agent`
- `input_payload`
- `output_payload`
- `needs_approval`
- `approved_by`
- `created_at`
- `completed_at`

`approval_tasks`
- `id`
- `approval_type`
- `entity_type`
- `entity_id`
- `proposed_action`
- `reasoning`
- `status`
- `reviewed_by`
- `reviewed_at`

## API / Function Layer

The admin already uses Supabase functions. Extend that pattern.

Recommended new functions:

- `agent-router`
- `lead-enrich`
- `draft-outreach`
- `queue-sequence-step`
- `send-approved-campaign`
- `approve-agent-action`
- `build-cohort`
- `compute-metric-snapshots`
- `data-trust-audit`

All send-capable or destructive functions should require:

- authenticated admin session
- role check
- approval task validation
- audit log write

## Messaging Model

One of the highest-risk areas is outbound communication, so the messaging model should be explicit.

States:

- `draft`
- `needs_review`
- `approved`
- `queued`
- `sent`
- `failed`
- `cancelled`

Every message should store:

- template used
- agent / human author
- audience definition
- approval chain
- send result

## Observability And Trust

The admin should surface:

- metric freshness
- last successful recompute
- broken function or job alerts
- inconsistent counts between surfaces
- failed agent runs
- failed sends
- audit trail of who approved what

Without this layer, the admin cannot become the operating system for the business.

## Phased Rollout

### Phase 0: Trust And Foundation

- unify metric definitions
- add freshness timestamps
- add audit logging
- add core task / approval tables

### Phase 1: Control Tower

- rebuild `/admin` landing page into queue + KPI + agent recommendation surface
- preserve existing working widgets where useful

### Phase 2: Lead OS

- add clinic lead model
- add pipeline UI
- add enrichment and scoring workflows

### Phase 3: Messaging And Approvals

- build campaign drafts, approvals, and send history
- reuse existing mass-email infrastructure carefully

### Phase 4: Agent Execution

- add router, drafter, analyst, and trust agents
- add `Agent Inbox`

### Phase 5: Commercial And Clinic Ops

- add pilot / active clinic / renewal views
- deepen clinic onboarding and supply-health flows

## Success Criteria

The agentic admin is working when:

- the founder can see the business state and next actions in under 60 seconds
- clinic acquisition is run from a lead pipeline inside admin
- student conversion campaigns are launched from admin with approval controls
- every risky action is reviewable and auditable
- metrics are trusted enough for decisions
- agent recommendations reduce manual operator work instead of increasing it

## Anti-Patterns To Avoid

- agent chat without business state
- autonomous sending without approvals
- burying decisions in prompts instead of data structures
- mixing experimental AI behavior with destructive tools
- building a generic AI shell before the lead, campaign, and approval models exist

## Bottom Line

ClinicalHours should become a **focused agentic admin OS**:

- not a generic dashboard
- not a generic AI playground
- a domain-specific control system for growth, lead generation, clinic ops, and business execution

That is the right descendant of the earlier "agentic OS" idea.
