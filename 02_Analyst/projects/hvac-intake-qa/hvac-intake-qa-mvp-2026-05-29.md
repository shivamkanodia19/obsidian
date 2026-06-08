---
title: HVAC Intake QA MVP - 2026-05-29
description: Durable decision memo for the AI-assisted HVAC intake audit and cold-outreach idea
project: hvac-intake-qa
status: incubating
last_updated: 2026-05-29
tags:
  - startup-idea
  - b2b
  - hvac
  - intake
  - ai
---

# HVAC Intake QA MVP - 2026-05-29

## What This Is

This idea started as an "AI mystery shopper" system for local service businesses. After pressure-testing it, the strongest version is narrower:

- target HVAC first
- use one short simulated customer call as a prospecting wedge
- score the intake behavior from the transcript
- send a short human-reviewed cold email based on one concrete finding
- sell a deeper paid audit or operational fixes if the owner responds

The real product is not "AI calls." The real product is lead-handling and intake-process diagnosis.

## Brutal Verdict

- Worth saving as a lightweight founder-led experiment.
- Not worth treating as a broad SaaS or flashy autonomous AI-calling startup yet.
- The cold-call engine can be a useful wedge, but it is not strong enough by itself to be the whole business.

## Strongest Version

The strongest practical version has two layers:

1. Cold prospecting wedge
   - one short call
   - one clear operational observation
   - one short outbound email
2. Real service
   - 3-5 scenario-based calls for a paying client
   - structured findings
   - recommended fixes
   - possible monthly monitoring later

## Weakest Assumptions

- "One call is enough to prove a broken process." It usually is not.
- "AI caller tech is the moat." It is not; the value is in the diagnosis and follow-up.
- "Owner finding and cold email automation are easy." Local-business contact data is messy.
- "Reports should be sent automatically." Bad transcripts, spam-likely issues, and weak evidence can burn leads fast.
- "This should start multi-vertical." It should not; each vertical has different intake expectations.

## Best First Vertical

HVAC is the best first vertical because:

- phone response matters a lot
- missed calls can plausibly mean lost revenue
- scenarios are simple and standardized
- privacy/compliance drag is lower than healthcare and legal

## Recommended MVP Shape

Build this as a narrow pipeline:

1. AI cold call engine
   - one scenario only
   - example: "My AC isn't blowing cold air. Do you service [city], and what would the next step be?"
   - hard stop around 60-90 seconds
2. Transcript and findings engine
   - answered or not
   - live human, voicemail, AI, or IVR
   - time to useful response
   - did they ask qualifying questions
   - did they attempt to schedule
   - did they explain next steps
3. Internal report draft
   - one-page internal summary for review
   - factual, not consultant fluff
4. Cold email draft engine
   - plain text
   - one observation
   - one sentence on why it matters
   - one CTA
5. Human approval gate
   - review every report and every outbound email in v1

## What Not To Build

- no dashboard
- no multi-vertical framework
- no polished PDF for first-touch cold outreach
- no revenue leakage math in v1
- no automatic email sending without review
- no large-scale owner-enrichment system before the wedge proves it gets replies

## Simple Technical Shape

- call provider: `Bland` or `Vapi`
- storage and workflow: `Supabase`
- extraction and drafting: `OpenAI API`
- outbound email: `Resend`
- review surface: tiny internal page or CLI, not customer software

## Recommended Data Model

- `businesses`
- `call_jobs`
- `calls`
- `findings`
- `contacts`
- `email_drafts`
- `email_events`

The key is to store structured factual findings, not just transcript blobs.

## Suggested Outreach Shape

Do not send a full unsolicited audit report first.

Send something like:

- "Called Tuesday at 7:18 PM as a new no-cooling customer."
- "The line went to voicemail with no emergency guidance or callback expectation."
- "If helpful, I can send the 3-bullet breakdown and show how I'd test this across business hours and after-hours."

That keeps the evidence bounded and creates curiosity without overclaiming.

## Best Future Pivot If The Cold Wedge Feels Bad

If cold AI calling feels too noisy, creepy, or unreliable, pivot to:

- opt-in intake QA for HVAC businesses that knowingly hire you to run simulated calls

That version is less edgy but stronger as a real recurring service.

## Best Next Step If Revived

Start with:

1. one metro
2. 50-100 HVAC businesses
3. one scenario
4. one call per business
5. structured findings only
6. human-reviewed plain-text outreach

Only add deeper automation if the first calls produce believable findings and the emails get replies.
