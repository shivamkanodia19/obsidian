---
title: ClinicalHours Admin Dashboard Revamp Brief for Claude Code
project: clinicalhours
strategic: true
status: draft
last_updated: 2026-05-28
tags: [clinicalhours, admin-dashboard, analytics, ai-insights, automation, claude-code]
---

# ClinicalHours Admin Dashboard Revamp Brief for Claude Code

## Objective

Revamp `https://clinicalhours.org/admin` so it becomes a trustworthy operating console for ClinicalHours, not just a dark grid of counters.

The new admin page should answer five questions quickly:

1. What changed?
2. What needs action right now?
3. Where is the funnel breaking?
4. What data can we trust?
5. What should we do next?

## What I Reviewed

- The attached admin screenshot from `2026-05-28`
- Local ClinicalHours strategy notes, wedge notes, product captures, and market research
- Playwright access attempt on `2026-05-28`

Important note:

- The first credential pair failed, but the corrected direct ClinicalHours login for `codextest@gmail.com` succeeded on `2026-05-28`.
- I then inspected the admin page in authenticated read-only mode without taking state-changing actions inside admin.
- Google OAuth still hit a verification challenge, but it was no longer needed once the direct site login worked.

## Verified Live Admin Observations

These observations come from the authenticated read-only admin session on `2026-05-28`.

### Current overview modules

The `Overview` tab currently includes:

- top KPI cards
- a `Live Activity Stream`
- a `Guest Session Analytics` panel

### Overview metrics currently visible

- `17` landing visitors today
- `3` guest sessions started today
- `0` new signups today
- `368` total students
- `4` approved hospitals
- `0` pending hospitals
- `1` rejected hospitals
- `9,516` opportunities
- `0` applications
- `79` clinical hours logged
- `1,737` active users (30d)

### Existing useful modules already on the page

- `Live Activity Stream`
  This already logs page views and logins with page paths like `/admin`, `/dashboard`, `/auth`, and `/opportunities`.

- `Guest Session Analytics`
  This already shows:
  - total sessions
  - today
  - this week
  - sessions by day
  - peak hours

This matters because the redesign should build on these modules instead of throwing them away.

### What other tabs currently contain

- `Students`
  A `User Directory` view with columns like user, contact, education, location, status, joined, and actions.

- `Hospitals`
  Hospital pages, hospital accounts, notifications, and a `Create Hospital Page` flow.

- `Clinic admin`
  A launcher into clinic admin consoles, with explicit note that super-admins can access every clinic dashboard.

- `Pending`
  Pending hospital approval review plus review history.

- `Tools`
  Email, import, data quality, maintenance, and a mass-email tool.

- `Logos`
  Logo coverage and batch logo fetch tooling.

- `Guests`
  A deeper guest analytics area with conversion behavior and session explorer.

- `Premium`
  Live premium counts, premium source breakdown, and premium activity.

- `Activity`
  A broader event feed with filters and event-type totals.

## Accuracy Problems Already Visible

The current admin page is not only a UX problem. It is already showing likely metric-definition or data-source inconsistency.

### Clear examples

1. `Students` tab shows `0 total users`, while `Overview` shows `368 Total Students`.
2. `Guests` tab shows `0 Total Sessions`, `0 Converted Sessions`, and `0 Sessions Today`, while:
   - `Overview` shows `3` guest sessions today
   - `Overview` guest analytics shows `306` total sessions
   - `Activity` shows `225` guest sessions
3. `Overview` shows `1,737 Active Users (30d)`, while `Activity` shows `43 Active Users`.
4. `Hospitals` tab shows `2 hospital pages`, while `Overview` highlights `4 approved hospitals` and `1 rejected hospital`.

Some of these may be legitimate entity differences, but the page does not explain them. That makes the admin surface harder to trust than it should be.

This is the strongest argument for:

- a metric dictionary
- a semantic metric layer
- freshness badges
- definition tooltips
- a visible source-of-truth / data-trust model

## High-Level Diagnosis

The current admin page looks like an internal platform admin surface, not a clinic coordinator console.

That means the page should primarily help the ClinicalHours team run:

- student growth
- guest-to-signup conversion
- hospital and opportunity supply
- pending approvals and moderation
- marketplace health
- data quality
- future clinic workflow operations

Right now the page appears to mix all of those concerns into one flat card grid.

### What is working

- There is already a central admin entry point.
- Core counts exist for growth and supply.
- Important admin domains already exist as tabs: `Students`, `Hospitals`, `Clinic admin`, `Pending`, `Guests`, `Premium`, `Activity`.

### What is not working

1. The page looks like a menu of counters, not a decision surface.
2. Daily metrics and lifetime metrics are mixed together without strong context.
3. Everything appears to have equal visual weight, so urgency is unclear.
4. There is no obvious action queue.
5. There is no obvious funnel view.
6. There is no obvious data freshness / trust status.
7. There is no distinction between platform admin work and clinic workflow work.
8. Tabs like `Tools`, `Logos`, and `Premium` sit beside much more important operational areas, which flattens hierarchy.
9. The admin tabs overflow horizontally even on desktop, which is a sign that the top-level IA is carrying too many peers.
10. The page already has better modules lower down (`Live Activity Stream`, `Guest Session Analytics`), but they are visually subordinate to the raw counter wall instead of driving the page narrative.

## Most Important Product Insight

There are really two different admin jobs here:

1. **Platform admin**
   This is the view implied by the screenshot: growth, approvals, supply, users, guests, premium, and moderation.

2. **Clinic workflow ops**
   This is the stronger validated ClinicalHours wedge from the local strategy notes: evaluation follow-up, onboarding reminders, status tracking, expiring items, and reducing email/forms/Drive chaos.

These should not share the same default landing surface.

The homepage of `/admin` should become the **platform operating console**.

The deeper `Clinic admin` area should become a **clinic workflow operations view**.

## Core Recommendation

Replace the current flat card grid with a role-aware admin console built around:

- overview
- queue
- funnel
- supply-demand balance
- data trust
- automation

## Recommended Information Architecture

### Primary navigation

Replace the current flat tab row with grouped admin domains:

- `Overview`
- `Growth`
- `Supply`
- `Operations`
- `Clinic Ops`
- `Data Trust`
- `Automation`
- `Settings`

### Where current tabs should go

- `Students`, `Guests`, `Premium` -> `Growth`
- `Hospitals`, `Pending` -> `Supply`
- `Clinic admin` -> `Clinic Ops`
- `Activity` -> `Operations` or `Data Trust` depending on whether it means user activity or admin audit activity
- `Tools`, `Logos` -> `Settings` or a compact utility menu, not top-tier nav

## Recommended Above-the-Fold Layout

The first screen should fit on one screen without requiring a long scroll for the main story.

### Row 0: controls

- date range
- compare period
- segment filter
- region filter
- last refreshed timestamp
- data trust badge

### Row 1: top KPI strip

Use one consistent time window for this strip, like `Today`, `Last 7 days`, or `Last 30 days`.

Suggested KPIs:

- active students
- guest to signup conversion
- approved active hospitals
- live opportunities
- pending review items
- stale or broken opportunities

### Row 2: action and insight layer

Left side:

- `Needs Attention` queue

Right side:

- `AI Insights` panel with evidence-backed summaries

### Row 3: operating story

- `Growth Funnel`
- `Supply vs Demand by Region`
- `Pending Approvals Aging`

### Row 4: trust and automation

- `Data Trust`
- `Automation Recommendations`
- `Recent Admin / System Activity`

## What Should Be in the `Needs Attention` Queue

This queue is more important than most raw counters.

It should rank items by urgency and impact:

- pending hospital approvals older than 24 or 72 hours
- hospitals or listings missing required metadata
- stale opportunities not refreshed in X days
- broken application links
- duplicate hospitals or duplicate listings
- abnormal signup drop
- high-traffic pages with low signup conversion
- clinic workflows with expiring clearances or overdue evaluation follow-up

Each queue item should have:

- title
- reason it matters
- exact evidence
- age
- impact estimate
- one next action

## Recommended KPI Changes

### Metrics to demote

These are useful but should not dominate the first screen as isolated counters:

- lifetime `Total Students`
- raw `Approved Hospitals`
- raw `Rejected Hospitals`
- utility counts without trend context

### Metrics to promote

- visitor -> guest -> signup conversion
- signup -> activated student conversion
- opportunities viewed -> saved -> applied
- pending hospitals by age
- live opportunities by freshness
- supply-demand coverage by region
- premium conversion rate
- admin SLA metrics like median approval time

## Concrete UI/UX Changes

1. Use one clear time scope at a time.
   The screenshot mixes `today` metrics with lifetime totals. That makes interpretation slower and easier to misread.

2. Put the most important information top-left and above the fold.
   The page currently reads like an evenly weighted list.

3. Stop treating every counter like the same kind of insight.
   Split counters into `Growth`, `Supply`, `Operations`, and `Trust`.

4. Replace some cards with trend modules.
   A raw count is weaker than count + direction + comparison.

5. Show why a number matters.
   Every important card should have a subtitle like `vs yesterday`, `vs last 7 days`, `from guest sessions`, or `awaiting approval`.

6. Add drilldowns from each KPI.
   Clicking a metric should open the list of entities behind it, not just feel decorative.

7. Reduce the number of first-class nav items.
   Move low-frequency utilities into a secondary menu.

8. Add freshness and trust badges directly on the page.
   If the admin cannot trust the data, the page fails even if it looks good.

## Separate View: `Clinic Ops`

The local ClinicalHours strategy notes point to a stronger clinic workflow wedge than the screenshot currently shows.

The `Clinic Ops` area should be built for:

- evaluation follow-up automation
- onboarding reminders
- status tracking
- expiring credentials / clearances
- missing forms
- audit readiness

Suggested modules:

- volunteers waiting on evaluation
- onboarding completion by step
- expiring items in 7 / 30 days
- reminders sent vs completed
- overdue follow-up by clinic
- record-level timeline for each person or clinic workflow

This area should feel like workflow triage, not business analytics.

## AI Insights Strategy

AI-generated insights are a good idea here, but only if they are evidence-backed and visibly constrained.

### Rule: AI insights must be descriptive before they are prescriptive

Every AI insight should have this structure:

- `Observation`
- `Evidence`
- `Why it matters`
- `Suggested next action`
- `Confidence`

### Every insight card should include

- exact metric names
- exact time window
- current value
- comparison value
- percent or absolute delta
- sample size where relevant
- freshness timestamp
- confidence level
- link to underlying drilldown

### Example insight formats

- `Guest to signup conversion fell 38% week over week. Most of the drop came after guest browsing began, not at landing. Evidence: 412 guest sessions, 19 signups this week vs 31 last week. Confidence: high.`
- `Dallas student demand is outpacing approved supply. Saves and opportunity views are rising faster than active local listings. Confidence: medium.`
- `Two pending hospital approvals would close 16% of the current Texas supply gap if approved. Confidence: high.`

### Hard guardrails for accuracy

Never show an AI insight if:

- the underlying metrics failed validation
- data freshness is stale beyond threshold
- sample size is below the minimum threshold
- the comparison window is inconsistent
- the event definition changed recently and the metric is unstable

### Confidence rubric

- `High`: governed metric, fresh data, sample size above threshold, clear comparison
- `Medium`: governed metric, acceptable freshness, weaker sample or noisier trend
- `Low`: exploratory only, should not drive automated action

## Automation Opportunities

The admin page should not auto-send or auto-change critical things silently.

It should first become an **automation recommendation center** with explicit approval.

### Good first automation categories

1. **Marketing / growth recommendations**
   - suggest high-intent guest cohorts for follow-up
   - suggest regions with strong demand but weak supply
   - suggest pages with high views and weak signup conversion
   - suggest student onboarding prompts when activation stalls

2. **Supply operations**
   - prioritize pending hospitals by likely impact
   - flag stale listings
   - flag broken application URLs
   - suggest duplicate merge candidates

3. **Clinic ops**
   - recommend reminder batches for overdue onboarding steps
   - surface people or clinics needing evaluation follow-up
   - flag expiring items before they become problems

4. **Data quality**
   - flag new unexpected events
   - flag metric drops caused by broken instrumentation
   - flag entities with missing required fields

### Example automations worth building

- `Recommend follow-up cohort`: guests who viewed 3+ opportunities but did not sign up
- `Recommend supply push`: metro areas with high demand / low approved supply
- `Recommend cleanup`: listings with broken outbound links or old timestamps
- `Recommend clinic follow-up`: records stuck in onboarding for 7+ days

### Approval rule

Any recommendation that sends messages, changes records, or affects external systems should require:

- human approval
- visible evidence
- audit logging

## Accuracy and Data Trust Strategy

This is the most important part if AI insights are going to matter.

### Use a five-layer trust model

1. **Tracking plan**
   Define the events and properties that matter.

2. **Validation**
   Reject or flag malformed or unexpected events.

3. **Metric layer**
   Centralize metric definitions so every dashboard and insight uses the same logic.

4. **Insight layer**
   Generate AI summaries only from governed metrics, never from arbitrary raw strings.

5. **Action layer**
   Only allow automation when the insight is trusted and the action risk is acceptable.

### Suggested critical events for ClinicalHours admin analytics

- `landing_viewed`
- `guest_session_started`
- `sign_up_started`
- `sign_up_completed`
- `student_activated`
- `opportunity_viewed`
- `opportunity_saved`
- `application_started`
- `application_submitted`
- `hospital_submitted`
- `hospital_approved`
- `hospital_rejected`
- `opportunity_marked_stale`
- `hours_logged`
- `evaluation_requested`
- `evaluation_completed`
- `onboarding_step_completed`
- `premium_started`
- `premium_converted`
- `admin_action_taken`

### Suggested validation rules

- required IDs present
- event timestamps valid
- region / state fields valid
- approval status values limited to accepted enums
- numeric counters non-negative
- broken links flagged
- stale listings flagged

### Suggested semantic metrics

- guest to signup conversion
- signup to activation conversion
- approval SLA
- opportunity freshness rate
- supply-demand imbalance score
- evaluation completion rate
- onboarding completion rate
- premium conversion rate

### Suggested insight object

```ts
type Insight = {
  id: string
  category: "growth" | "supply" | "ops" | "clinic_ops" | "data_quality"
  title: string
  observation: string
  why_it_matters: string
  confidence: "high" | "medium" | "low"
  freshness_minutes: number
  time_window: string
  evidence: Array<{
    metric: string
    current: number | string
    previous?: number | string
    delta?: number | string
    sample_size?: number
  }>
  drilldown_url?: string
  recommendation?: string
}
```

### Suggested automation recommendation object

```ts
type AutomationRecommendation = {
  id: string
  category: "marketing" | "supply" | "clinic_ops" | "data_quality"
  title: string
  evidence: string
  proposed_action: string
  risk_level: "low" | "medium" | "high"
  requires_approval: boolean
  status: "draft" | "approved" | "executed" | "dismissed"
}
```

## Broad Implementation Strategy for Claude Code

### Phase 1: fix information architecture

- regroup nav
- build one-screen overview
- add date range, compare period, filters, freshness
- replace the flat card wall with a structured layout

### Phase 2: define data trust

- create or tighten the tracking plan
- define canonical metric names
- add validation rules
- add a visible trust badge in the UI

### Phase 3: build derived admin views

- growth funnel
- supply by region
- approval aging
- stale / broken opportunity monitor
- premium conversion view

### Phase 4: add evidence-backed AI insights

- generate summaries from governed metrics only
- show evidence, confidence, freshness
- hide insights when validation fails

### Phase 5: add recommendation-driven automation

- create an automation center
- queue recommendations instead of auto-executing them
- require approval for external or record-changing actions
- log every action and dismissal

### Phase 6: add `Clinic Ops`

- build the deeper workflow console for evaluation automation, onboarding reminders, and status tracking
- keep it distinct from the platform overview

## Acceptance Criteria

Claude Code should consider the revamp successful only if:

- the first screen tells a coherent story without a long scroll
- the most important admin work is visible in under 10 seconds
- time windows are consistent within each KPI group
- every AI insight includes evidence and confidence
- every automation recommendation is reviewable before execution
- platform admin and clinic workflow admin concerns are clearly separated
- data freshness and validation status are visible

## Research Signals Used

- Microsoft Power BI dashboard design guidance emphasizes one-screen overviews, uncluttered layouts, clear hierarchy, and consistent time precision.
- dbt guidance supports a semantic layer and test-driven metric governance so downstream tools use the same metric definitions.
- Amplitude guidance supports tracking plans, validation rules, observability, official dashboards, cohort syncs, and dashboard agents for anomaly and trend discovery.

## Source Links

- Microsoft Learn, dashboard design tips: https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips
- dbt data tests: https://docs.getdbt.com/docs/build/data-tests
- dbt semantic layer: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- Amplitude dashboard management: https://amplitude.com/docs/analytics/dashboard-create
- Amplitude tracking plan: https://amplitude.com/docs/data/create-tracking-plan
- Amplitude data overview: https://amplitude.com/docs/data/data-overview
- Amplitude quickstart for data teams: https://amplitude.com/docs/get-started/quickstart-for-data-teams
- Amplitude implementation planning: https://amplitude.com/docs/get-started/plan-your-implementation
- Amplitude admin overview: https://amplitude.com/docs/admin
- Amplitude guides and surveys: https://amplitude.com/docs/guides-and-surveys/get-started
- Amplitude cohort syncs: https://amplitude.com/docs/data/sync-cohorts-with-destinations
- Amplitude third-party syncs: https://amplitude.com/docs/data/audiences/third-party-syncs
