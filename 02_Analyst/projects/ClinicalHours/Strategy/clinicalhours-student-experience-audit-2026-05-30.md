---
title: ClinicalHours Student Experience Audit - 2026-05-30
project: clinicalhours
strategic: true
status: draft
last_updated: 2026-05-30
tags: [clinicalhours, student-experience, retention, activation, product-audit]
---

# ClinicalHours Student Experience Audit - 2026-05-30

## Objective

Audit the current ClinicalHours student experience end to end, identify likely retention blockers, and turn those observations into high-value product and marketing recommendations.

## Scope and Method

- Live product walkthrough on `2026-05-30` using Playwright
- Public funnel review across `/`, `/auth`, `/map`, `/opportunities`
- Fresh student account creation and verification using Gmail alias flow
- Signed-in walkthrough across `/dashboard`, `/opportunities`, `/hours`, `/my-applications`, `/settings`, `/costs`, `/premium`
- Visual review of prior authenticated admin capture from `2026-05-28`
- Local strategy-note review, especially:
  - `clinicalhours-admin-dashboard-revamp-claude-code-brief-2026-05-28.md`
  - `ClinicalHours-Product-Map.md`
  - `clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18.md`

## Constraints

- The requested `codextest@gmail.com` password was not available in the current context, so a direct live admin login could not be reproduced in this session.
- The recent authenticated admin brief and screenshot were used instead for admin-side usage signals.
- Replicate MCP was not available in this session.

## What Is Working

### 1. The map is the clearest immediate value surface

- The map is visually distinctive on both desktop and mobile.
- Search is real and useful. Searching `Houston Methodist` returned a focused set of results quickly.
- The opportunity-detail surface is directionally strong:
  - save to tracker
  - call
  - website
  - review / Q&A shell
  - reminders

### 2. The journal becomes meaningful after the first real action

- Once one opportunity was saved and one hour entry was logged, the product started to feel like a system instead of a directory.
- The dashboard updated correctly:
  - `1` active opportunity
  - `1` total hour logged
  - `1` experience / reflection visible
- The hours journal sync between the tracked opportunity and the reflection view worked.

### 3. The application cost calculator is a legitimate student wedge

- `/costs` is concrete, useful, and marketable even before deep platform adoption.
- It naturally leads into planning, budgeting, and premium upsell.

## Core Weak Points

### 1. The activation loop is fragile

The product only starts feeling valuable after this sequence:

1. sign up
2. find a relevant opportunity
3. save it
4. log hours
5. return later

That loop exists, but the product does very little to guide the student through it.

Observed problems:

- the guest CTA logs a guest session but leaves the user on the auth page instead of clearly taking them into the product
- new users land on a mostly empty dashboard
- profile completion urgency is hidden in settings rather than pulled into the main path
- there is no first-run checklist or explicit next-best-action flow

### 2. “Sort by distance” does not feel truthful for a new user

For a fresh student with no city, no school, and blocked geolocation:

- the opportunities list defaults to `Sort by distance`
- no actual distances are shown
- the first results are broad national entries rather than obviously local results

This makes discovery feel random at the exact moment when users need confidence that the product understands their situation.

### 3. The application step is unreliable

This is the most dangerous issue in the student loop.

Observed on `2026-05-30`:

- guest `Find App Link` returned `401`
- signed-in `Find Application` returned `403`
- signed-in `Volunteer Link` also fell back to `Try again`
- multiple `track` function calls returned `500`, even though save-to-tracker eventually stuck

Implication:

- the product can help students discover and save, but the “help me actually apply” moment is not dependable
- that breaks trust and weakens retention because students will stop coming back if the most important action is flaky

### 4. Empty-state surfaces are everywhere

The signed-in student sees:

- no applications
- no upcoming deadlines
- no tracked opportunities until they create one
- no reflections until they create one
- no reviews
- no Q&A

This creates a cold-start problem. The product looks polished, but emotionally it still feels empty.

### 5. The homepage promise is broader than the experienced product

The public narrative says:

- discover
- track
- review
- connect

What is meaningfully usable today is closer to:

- discover
- save
- log hours
- see an empty shell for future community / application workflow

That gap matters for both retention and marketing credibility.

### 6. Important features exist but are not tied into a strong journey

Current parts:

- map
- opportunities list
- tracker
- hours journal
- reflections
- cost calculator
- premium page

These parts do not yet feel orchestrated into one coherent pre-med operating system.

### 7. Community features exist as shells but not as living value

On opportunity detail pages, there is a `Community` section with `Reviews` and `Q&A`.

What the user sees today:

- no reviews yet
- no visible Q&A activity

Network-effect features that are empty often hurt more than they help because they remind users the product is not yet socially alive.

### 8. Mobile is workable but still has friction

Strengths:

- mobile dashboard is readable
- mobile map looks strong
- bottom navigation helps orientation

Friction:

- mobile map controls are hidden behind the floating opportunities pill
- the opportunities feed is long and card-heavy, which feels heavy rather than guided
- floating bottom nav + floating controls compete for space

## Admin Signals Worth Using Carefully

These metrics came from the authenticated admin observation note dated `2026-05-28`, not from a fresh admin session on `2026-05-30`.

Overview values observed on `2026-05-28`:

- `17` landing visitors today
- `3` guest sessions started today
- `0` new signups today
- `368` total students
- `9,516` opportunities
- `0` applications
- `79` clinical hours logged
- `1,737` active users (30d)

Important caution:

- the same admin review found multiple cross-tab metric contradictions
- examples included:
  - `368 Total Students` in overview vs `0 total users` in students
  - `3 guest sessions today` vs guest tabs showing zero in some places
  - `1,737 Active Users (30d)` vs `43 Active Users` elsewhere

So these numbers should be treated as directional, not authoritative.

Still, even directionally they suggest:

- top-of-funnel traffic exists
- guest exploration exists
- signup conversion is weak
- the hours-journal habit is not yet broadly activated
- the application workflow is likely not a meaningful retention driver yet

## Retention Diagnosis

The current product likely loses students in three places:

### 1. After first visit

Reason:

- the product looks interesting, but it does not immediately become personal
- “near me” is not convincingly established
- guest mode is not smoothly routed into real usage

### 2. After signup

Reason:

- the dashboard is visually polished but mostly empty
- there is no guided setup path toward a first concrete win
- profile completion, saved opportunities, and first hour log are not sequenced as one onboarding journey

### 3. At the application step

Reason:

- students want help getting from “interesting listing” to “I actually applied”
- the application-link actions were unreliable in this audit
- the applications page stays empty unless the user manually manages the system

This means ClinicalHours currently behaves more like a discovery tool plus lightweight journal than a full student operating system.

## Highest-Value Fixes

### 1. Build a real first-run activation checklist

Add a persistent guided checklist on the dashboard for new students:

1. add your city or school
2. save 3 nearby opportunities
3. click your first application link
4. log your first hour
5. write your first reflection

Why this matters:

- turns an empty dashboard into a momentum surface
- gives the user a reason to return
- creates the first durable habit loop

### 2. Make locality real immediately

On signup or first login, require or strongly prompt:

- city
- state
- university
- pre-med track

Then use that data to:

- default the opportunity feed to nearby results
- show actual distances
- pre-populate map focus
- highlight “best next 5” instead of the whole national database

Why this matters:

- relevance is the fastest route to perceived value
- “distance” without obvious locality undermines trust

### 3. Fix every application-link pathway before adding more features

Specifically stabilize:

- `Find App Link`
- `Volunteer Link`
- tracker-save backend reliability

Why this matters:

- if the application step is unreliable, retention will stay capped
- this is the highest-leverage trust repair in the product

### 4. Turn tracked opportunities into an actual application pipeline

Each saved opportunity should support statuses like:

- saved
- researching
- applied
- waiting
- interview
- accepted
- rejected
- archived

Also add:

- date saved
- application deadline
- follow-up reminder
- last contact date
- notes

Why this matters:

- students will return for workflow management, not just browsing
- this creates the real retention engine

### 5. Pull profile completion into the main experience

Do not hide profile completeness only inside settings.

Bring it into:

- dashboard checklist
- onboarding banners
- review / Q&A gating messages

Why this matters:

- completion feels connected to value, not admin chores
- it improves future personalization and community quality

### 6. Seed the community layer or hide it until it is alive

Options:

- import verified early reviews from real users
- manually seed Q&A from common student questions
- add “verified by logged hours” badges
- if activity is too sparse, temporarily hide empty community surfaces from default views

Why this matters:

- social proof can become a retention flywheel
- empty community surfaces currently advertise emptiness

### 7. Make the journal the center of the long-term student story

The strongest retention path is not just “find a clinic.”

It is:

- save an opportunity
- log the experience
- reflect on it
- convert it into application-ready language later

The journal should therefore expand toward:

- structured prompts after each session
- competency tagging
- continuity across entries
- exportable application artifacts

### 8. Use the cost calculator as a top-of-funnel engine

This should be promoted more aggressively because it is:

- useful immediately
- shareable
- emotionally sticky
- naturally tied to premium planning tools

## Best Next Features

### 1. Opportunity Outreach Kit

For each opportunity:

- verified application link
- volunteer email or contact workflow
- “how to reach out” template
- last verified date
- reminder sequence

### 2. Application Tracker with deadlines and reminders

This is the cleanest bridge between discovery and repeat usage.

### 3. Reflection-to-AMCAS preview

After a student logs a few entries, show a free preview:

- “Here is how your shadowing notes can become an AMCAS activity description.”

This is likely the strongest eventual premium conversion path.

### 4. Nearby opportunity digest

Weekly or event-triggered:

- new nearby opportunities
- opportunities matching saved preferences
- reminders to follow up on saved items

### 5. Verified review system

Make reviews more credible with signals like:

- verified hours logged
- verified student status
- verified application / interview / placement stage

## Marketing Implications

The strongest believable marketing angle is not just:

- “Find clinical opportunities.”

It is:

- “Find, track, and document your clinical journey in one place.”

Better positioning:

- `The operating system for pre-med clinical experience`
- `From first opportunity to application-ready reflection`
- `Find nearby opportunities, track your outreach, and turn your hours into a stronger application story`

The current real proof supports messaging around:

- opportunity discovery
- tracking
- journaling / reflection
- planning costs

It does not yet strongly support broad claims around:

- active community
- reliable automated application matching
- full application workflow completion

## Implementation Order

### Phase 1: Stop the leaks

1. Fix guest browse routing
2. Fix application-link and volunteer-link reliability
3. Fix tracker action reliability
4. Make distance sorting truthful

### Phase 2: Drive first habit

1. Add first-run checklist
2. Force location / school personalization
3. Push first save + first hour log
4. Bring profile completion into the dashboard

### Phase 3: Build retention loop

1. Application pipeline
2. Follow-up reminders
3. Journal prompts and reflection structure
4. Review / Q&A seeding

### Phase 4: Monetize the real wedge

1. Reflection-to-AMCAS tools
2. Competency mapping
3. Secondary essay support
4. school-planning / timeline layer

## Most Important Bottom Line

ClinicalHours already has the pieces of a useful student product, but they are not yet arranged into a strong habit loop.

Right now the product is strongest as:

- a discovery map
- a save-and-log system
- an early planning tool

It becomes genuinely sticky only after the user has:

- saved an opportunity
- logged at least one session
- seen their own history reflected back

So the highest-value work is not adding random new pages.

It is getting more students to that first moment of personal momentum, then making the application and reflection workflow dependable enough that coming back feels obviously worthwhile.
