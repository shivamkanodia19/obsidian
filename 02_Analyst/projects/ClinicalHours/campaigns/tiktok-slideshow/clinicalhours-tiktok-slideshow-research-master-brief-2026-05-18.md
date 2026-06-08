---
title: ClinicalHours TikTok Slideshow Research Master Brief - 2026-05-18
project: clinicalhours
strategic: true
status: active
last_updated: 2026-05-29
tags: [clinicalhours, tiktok, slideshow, creative, research, marketing]
---

# ClinicalHours TikTok Slideshow Research Master Brief - 2026-05-18

## Purpose

This is the strategy note future Codex agents should read before generating, editing, grading, or exporting ClinicalHours TikTok slides.

It adapts the strongest durable logic from the Felt slideshow system:

- screenshot-first proof selection
- one dominant message per slide
- fixed slide roles inside one deck lane
- machine QA for safe zones and overlap
- human QA for proof strength and pacing

But it changes the story logic to fit ClinicalHours.

ClinicalHours is not a card-game product with one audience and one emotional loop. It currently has:

- a student-facing discovery lane
- a clinic-facing operations lane
- a broader two-sided/network story that is directionally real, but not equally validated at every layer

## Findings First

The most important adaptation from Felt is not the aesthetics. It is the discipline.

ClinicalHours slides should:

- choose one audience lane before composing
- choose proof assets before writing headlines
- keep every claim inside a clear evidence tier
- reward each swipe with more specificity
- feel calm, credible, and operational rather than startup-hypey
- let truthful captured product proof do the persuasion, with generated support imagery only strengthening pacing or atmosphere

The main failure mode to avoid is mixing three stories at once:

- "premed opportunity search"
- "clinic workforce operations"
- "big future infrastructure company"

That mixture can work in a pitch deck, but it weakens a five-slide TikTok sequence.

## The Two Most Important Truths

### 1. The vault's strongest validated product truth is narrower than the public enterprise page

From the internal strategy notes:

- pilot evidence is strongest around evaluation follow-up, onboarding reminders, status tracking, and adjacent admin coordination
- the safest current claim is workflow relief for small clinics
- the most defensible customer shape is small clinics with 15-100 volunteers using email, forms, sheets, paper, and phone coordination

From the current public site inspected with Playwright on `2026-05-18`:

- the student site publicly shows discovery-oriented surfaces
- the enterprise site publicly frames ClinicalHours as a broader workforce-operations layer for safety-net clinics

That means the system must distinguish between:

- `validated_pilot`
- `product_surface`
- `market_hypothesis`

Do not write as if those are interchangeable.

### 2. The enterprise page is currently the strongest truthful proof inventory for a TikTok deck

Publicly accessible states confirmed with Playwright on `2026-05-18`:

- student home hero
- student map page with `9,512` visible opportunities
- auth page
- enterprise hero section
- enterprise platform figures for applications, credentialing, status, and supply
- enterprise outputs list
- enterprise trust-signals section
- enterprise demo CTA section

Important weakness discovered on the live site on `2026-05-18`:

- the student homepage includes visible `0+` and `0%` placeholder stat blocks lower on the page

Those placeholder metrics should not be used as hero proof and should usually be cropped out entirely.

## Audience Lanes

Future agents should choose one lane before generating or refining slides.

### Lane A: `clinic_ops_primary`

Use this by default.

Best for:

- clinics
- operations directors
- volunteer coordinators
- healthcare admin buyers
- B2B demos and founder-led outreach support

Why it is the default:

- strongest public proof inventory is here
- strongest internal pain clarity is here
- strongest near-term product wedge is here

Primary emotional sequence:

1. friction
2. unification
3. workflow proof
4. control
5. activation

### Lane B: `student_discovery_secondary`

Use only when the assignment is explicitly student-facing.

Best for:

- premed students
- campus distribution
- broad awareness
- student pain storytelling

Current public proof is real but weaker than the enterprise lane because:

- discovery and map proof are accessible
- stronger logged-in application-tracking and AMCAS-output proof is not currently public

Primary emotional sequence:

1. friction
2. discovery
3. simplification
4. documentation direction
5. activation

### Lane C: `two_sided_network_explainer`

Use sparingly.

This lane is for:

- investor-adjacent storytelling
- founder explainers
- higher-context audiences

It should only be used when the assignment explicitly wants the bigger company story. It is easy to overclaim if used casually.

## Interactive Intake

When working directly with Shivam on a ClinicalHours slide request, do not guess the deck topic.

Ask at least one short question first:

- what content or topic should this deck cover?

If the answer still leaves important ambiguity, ask one short follow-up about:

- audience lane
- desired CTA

If the task is automated or the user is unavailable, then default to `clinic_ops_primary`.

## Evidence Tiers

Every deck should declare one evidence tier per major claim.

### `validated_pilot`

Allowed content:

- evaluation follow-up
- onboarding reminders
- status tracking
- fragmented admin coordination across email, Drive, Notes, forms, and sheets
- small-clinic workflow relief

### `product_surface`

Allowed content:

- whatever the current captured product states visibly show today
- enterprise hero language
- public student discovery surfaces
- enterprise platform figure states

Guardrail:

- product surface is not the same as cross-clinic validation

### `proof_access`

Store proof visibility separately from `evidence_tier`.

Allowed values:

- `public_site`
- `authenticated_preview`
- `mixed_public_and_authenticated_preview`

Guardrail:

- do not invent hybrid `evidence_tier` strings when the real difference is proof visibility
- keep claim strength in `evidence_tier` and access level in `proof_access`

### `market_hypothesis`

Allowed only when labeled or obviously framed as directional:

- larger national scale
- broader supply density
- stronger time-to-credential outcomes
- hospital-tier expansion

If you cannot support the claim cleanly, weaken it.

## Current Public Capture Inventory

All of these were captured from the live site with Playwright on `2026-05-18` and saved under `05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/`.

Best current clinic-ops assets:

- `captures/enterprise/clinicalhours_enterprise_hero_section_live.png`
- `captures/enterprise/clinicalhours_enterprise_problem_section_live.png`
- `captures/enterprise/clinicalhours_enterprise_platform_applications_live.png`
- `captures/enterprise/clinicalhours_enterprise_platform_hipaa_live.png`
- `captures/enterprise/clinicalhours_enterprise_platform_status_live.png`
- `captures/enterprise/clinicalhours_enterprise_platform_supply_live.png`
- `captures/enterprise/clinicalhours_enterprise_outputs_list_live.png`
- `captures/enterprise/clinicalhours_enterprise_trust_signals_live.png`
- `captures/enterprise/clinicalhours_enterprise_ready_demo_section_live.png`

Best current student-facing assets:

- `captures/home/clinicalhours_home_hero_section_live.png`
- `captures/home/clinicalhours_home_desktop_1440x1200_live.png`
- `captures/home/clinicalhours_home_mobile_430x932_live.png`
- `captures/map/clinicalhours_map_desktop_1440x1200_live.png`
- `captures/map/clinicalhours_map_panel_live.png`
- `captures/auth/clinicalhours_auth_desktop_1440x1200_live.png`

Weak or caution-tagged assets:

- lower student-home stat cards with `0+` placeholders
- any crop that turns enterprise copy into unreadable body text
- any map crop where the filter panel becomes too small to prove the story

## ClinicalHours-Specific Psychology

The Felt system emphasized curiosity, proof, mastery, and return.

What transfers well:

- create a clean question on slide 1
- answer it quickly on slide 2
- make proof more specific as the deck progresses
- keep one dominant proof asset per slide
- make the CTA calm and credible

What changes for ClinicalHours:

- clinic buyers care more about relief and control than thrill
- student viewers care more about path clarity than novelty
- proof must feel operational, not flashy
- trust is more important than hype

## What Should Feel "Sticky" Here

For `clinic_ops_primary`, the deck should feel sticky because:

- the pain is instantly recognizable
- the workflow looks more orderly than the status quo
- the product looks credible enough to hand to a coordinator
- the CTA feels like a rational next step

For `student_discovery_secondary`, the deck should feel sticky because:

- the search pain is familiar
- the platform looks faster than manual searching
- the map/search/auth flow feels real
- the next step feels easy

## Brand And Visual Direction

Use the best parts of the ClinicalHours investor-design comments:

- deep charcoal/navy stage
- bright clinical blue as the main action color
- restrained green for successful state and control
- red only for pain, warning, or status-quo friction
- off-white product and text surfaces
- modern sans with mono only for tiny labels

Recommended palette:

- near-black `#06080D`
- off-white `#F7F8FA`
- slate `#5B6472`
- clinical blue `#2563EB`
- soft blue `#DBEAFE`
- success green `#14B87A`
- alert red `#EF4444`

Current Shivam preference to preserve:

- For ClinicalHours clinic-ops slides, use light color treatments only and avoid dark-tech background shells unless he explicitly asks for them.

## Do Not Copy Felt Blindly

Do not bring over Felt-specific ideas that do not fit:

- mastery loops as the default ending
- social-game return language
- gold-heavy reward accents
- any framing that feels like consumer entertainment

ClinicalHours should feel more like:

- healthcare workflow infrastructure
- clinic operations relief
- founder-close software with real process knowledge

Not like:

- growth-hack startup ads
- wellness fluff
- med-school promise bait

## Default Recommendation

When Shivam asks for ClinicalHours slides and has not yet specified the topic, ask first:

- what content or topic should the slides cover?

If needed, ask one short follow-up about audience or CTA.

If the work is automated or no answer is available, generate a `clinic_ops_primary` deck first.

Reason:

- it has the strongest combination of pain clarity, public proof, and near-term buyer value
- it is the cleanest way to keep the deck truthful without depending on private product states

## Operational Companions

Use these notes with this strategy brief when the task is execution rather than ideation:

- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/_index|ClinicalHours TikTok QA docs]]

## Sources Used

Internal sources:

- `02_Analyst/projects/ClinicalHours/Strategy/ClinicalHours-Product-Map.md`
- `02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07.md`
- `02_Analyst/projects/ClinicalHours/Strategy/niche-refinement.md`
- `02_Analyst/projects/ClinicalHours/Market/DFW-Clinic-Market-Analysis-2026-04.md`
- `02_Analyst/projects/ClinicalHours/Outreach/DFW-Strategy.md`
- `02_Analyst/projects/ClinicalHours/Outreach/Personas-Reference.md`
- `02_Analyst/research/ClinicalHours/clinicalhours-deck-claude-design-comments-2026-04-21.md`
- `02_Analyst/research/clinicalhours_market_research/clinic_pain_points.md`
- `02_Analyst/research/clinicalhours_market_research/clinic_decision_makers.md`

Execution source:

- live `clinicalhours.org` states inspected with Playwright on `2026-05-18`
