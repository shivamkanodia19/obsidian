---
title: ClinicalHours TikTok Future Agent Prompt - Expiring Clearances Issue - 2026-05-20
description: Paste-ready prompt for generating a new issue-specific ClinicalHours slideshow about expiring volunteer clearances and renewal visibility
last_updated: 2026-05-20
---

# ClinicalHours TikTok Future Agent Prompt - Expiring Clearances Issue - 2026-05-20

## Why This Issue

This angle is specific, operational, and still truth-safe inside the current ClinicalHours clinic-ops wedge:

- status tracking across admin steps
- onboarding reminders
- fragmented coordination across email, forms, Drive, and manual follow-up

It is different from the broader canonical `v1` deck and different from the onboarding-visibility issue prompt. The story here is not generic onboarding chaos. The story is that renewal and expiration status can go unseen until a coordinator has to scramble.

## Paste-Ready Prompt

```text
You are extending the ClinicalHours TikTok slideshow system in c:\Users\shiva\obsidian.

Assignment:
Generate a new 5-slide ClinicalHours slideshow about this specific issue:
"Volunteer clearances and onboarding requirements expire quietly because renewal status is scattered across emails, folders, and memory."

Before you build:
1. If Shivam has not explicitly confirmed this issue, ask one short question confirming that this is the topic he wants.
2. If delegation is available, use two explorer subagents in parallel:
   - one to verify what current decks already cover so the new branch does not feel repetitive
   - one to verify truthful proof assets and claim boundaries for expiration, reminders, and status visibility
3. While the subagents run, inspect the current canonical clinic-ops path locally.

Required read order:
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18.md
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18.md
- 02_Analyst/projects/ClinicalHours/Strategy/ClinicalHours-Product-Map.md
- 02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_playwright_future_agent_playbook_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_strategy_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_codex_image_prompt_system_v1_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v1.md

Truth and lane constraints:
- lane: clinic_ops_primary
- audience: clinic coordinator, volunteer coordinator, or operations lead at a small clinic
- use canonical metadata: evidence_tier = product_surface, proof_access = public_site
- keep the story inside workflow relief for small clinics
- do not imply automated compliance guarantees, full credentialing automation, or full staffing coverage
- do not claim ClinicalHours prevents every expiration event
- do not broaden the story into general operations software
- do not drift into the other narrow issue prompt about onboarding visibility loss

Visual and psychology constraints:
- Shivam does not want darker slides for this branch.
- There is a vault contradiction here: older clinic-ops defaults mention a dark stage, but `clinicalhours_visual_strategy_2026-05-19.md` argues for a brighter editorial palette.
- Resolve that contradiction in favor of the brighter direction for this assignment.
- Use screenshot-first proof, bright mobile hierarchy, operational clarity, and a calm credible CTA.
- The psychology target is relief from hidden renewal risk, not panic, hype, or drama.

Build approach:
- create a new issue-specific branch instead of overwriting the canonical v1 deck
- suggested composition file: 05_Outputs/images/clinicalhours_tiktok_2026-05-18/composition/clinicalhours_tiktok_clinic_expiring_clearances.html
- suggested deck spec: 05_Outputs/images/clinicalhours_tiktok_2026-05-18/pipeline/specs/clinicalhours_tiktok_clinic_expiring_clearances_v1_deck_spec.json
- suggested export suffix: v4expiry
- start from the current clinic-ops composition and tighten the story around expiring items, reminder burden, and renewal visibility

Issue framing to preserve:
- the pain is not "compliance is impossible"
- the pain is "expiring items disappear into manual follow-up"
- focus on renewal deadlines, missing updates, scattered reminders, buried email threads, and one visible status view
- keep the tone calm, credible, and operational

Visual direction to preserve:
- bright editorial palette instead of a dark-tech stage
- off-white or softly tinted backgrounds
- clinical blue as the primary accent, restrained green for success/status support
- strong contrast for mobile in bright light
- oversized proof cards, layered but not cluttered
- screenshots should feel embedded in a designed system, not floating in empty dark space

Preferred proof inventory:
- captures/enterprise/clinicalhours_enterprise_problem_section_live_recapture_v2.png
- captures/enterprise/clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png
- captures/enterprise/clinicalhours_enterprise_platform_figure_2_live_recapture.png
- captures/enterprise/clinicalhours_enterprise_trust_section_live_recapture_v2.png
- captures/enterprise/clinicalhours_enterprise_mobile_430x932_live.png

Suggested slide structure:
1. friction
   - Show the scramble created by scattered renewal follow-up.
   - Example message direction: expiration dates still live in inboxes, folders, and coordinator memory.
2. unification
   - Show one place to track onboarding and clearance status.
   - Keep the promise narrow: fewer blind spots, fewer last-minute surprises.
3. workflow_proof
   - Show review activity and missing requirements becoming visible instead of buried.
   - Emphasize tracking and follow-up, not a broader platform thesis.
4. control
   - Show what is complete, what is expiring, and what still needs action.
   - This is the strongest proof slide for this issue.
5. activation
   - Close on a believable CTA for clinics that want renewal status and follow-up in one place.

Copy rules:
- one dominant message per slide
- short headlines, one short sentence of subtext
- no internal-strategy language
- no media-buying jargon
- no placeholder metrics
- no repeated number conflicts
- no claims stronger than the screenshot evidence

Required deliverables:
- the new HTML composition
- the new machine-readable deck spec
- a short iteration note documenting issue framing, proof mapping, and what changed
- rendered exports
- QA screenshots if generated by the standard workflow

Verification requirements:
- run the local render script with QA enabled
- run the copy audit
- fix every warning before shipping
- visually inspect the final slides for collisions, cropping, and proof/text tension

Final response format:
- state the chosen issue and why it is truth-safe
- link the new composition, spec, and iteration note
- say whether render QA passed
- call out any remaining proof limitations
```

## References

- [[02_Analyst/projects/ClinicalHours/Strategy/ClinicalHours-Product-Map]]
- [[02_Analyst/projects/ClinicalHours/clinicalhours-experiment-log-framing-2026-05-07]]
- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v1]]
