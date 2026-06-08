---
title: ClinicalHours TikTok Future Agent Prompt - Onboarding Visibility Issue - 2026-05-20
description: Paste-ready prompt for generating a new issue-specific ClinicalHours slideshow about onboarding visibility loss in small clinics
last_updated: 2026-05-20
---

# ClinicalHours TikTok Future Agent Prompt - Onboarding Visibility Issue - 2026-05-20

## Why This Issue

This angle is specific enough to feel new, but still sits inside the strongest validated clinic-ops pain cluster:

- onboarding reminders
- status tracking across admin steps
- fragmented coordination across email, forms, Drive, and manual follow-up

It is narrower than the broad canonical `v1` clinic-ops deck and less overused than `evaluation follow-up`.

## Paste-Ready Prompt

```text
You are extending the ClinicalHours TikTok slideshow system in c:\Users\shiva\obsidian.

Assignment:
Generate a new 5-slide ClinicalHours slideshow about this specific issue:
"Clinics lose visibility during volunteer onboarding because no one can quickly tell who is fully cleared, who is missing a form, and who still needs a reminder."

Before you build:
1. If Shivam has not explicitly confirmed this issue, ask one short question confirming that this is the topic he wants.
2. If delegation is available, use two explorer subagents in parallel:
   - one to verify which current decks already cover this issue and what would feel repetitive
   - one to verify truthful proof assets and claim boundaries from strategy notes, captures, and specs
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
- do not imply full staffing automation, supply orchestration, guaranteed compliance, or autonomous reminder handling
- do not drift into evaluation automation for this deck
- do not broaden the story into "entire clinic operations"

Visual and psychology constraints:
- Shivam does not want darker slides for this branch.
- Treat that as a hard preference update from 2026-05-20: use light colors only for this branch.
- There is a vault contradiction here: older clinic-ops defaults mention a dark stage, but `clinicalhours_visual_strategy_2026-05-19.md` argues for a brighter editorial palette.
- Resolve that contradiction in favor of the brighter direction for this assignment.
- Use screenshot-first proof, strong upper-frame hierarchy, brighter editorial healthcare styling, and a calm credible CTA.
- The psychology target is operational relief and regained control, not hype, fear, or abstract polish.

Build approach:
- create a new issue-specific branch instead of overwriting the canonical v1 deck
- suggested composition file: 05_Outputs/images/clinicalhours_tiktok_2026-05-18/composition/clinicalhours_tiktok_clinic_onboarding_visibility.html
- suggested deck spec: 05_Outputs/images/clinicalhours_tiktok_2026-05-18/pipeline/specs/clinicalhours_tiktok_clinic_onboarding_visibility_v1_deck_spec.json
- suggested export suffix: v4onboard
- start from the current clinic-ops composition and tighten the story around onboarding visibility loss

Issue framing to preserve:
- the pain is not "ops are hard"
- the pain is "manual onboarding chase creates blind spots"
- focus on missing forms, unclear clearance status, forwarded emails, reminder burden, and one visible queue
- make the deck feel operationally credible, not dramatic
- keep the slides bright, mobile-readable, and information-dense without feeling dark or heavy

Visual direction to preserve:
- bright editorial palette instead of a dark-tech stage
- off-white or softly tinted backgrounds
- clinical blue as the primary accent, restrained green for success/status support
- strong contrast for mobile in bright light
- oversized proof cards, layered but not cluttered
- screenshots should feel embedded in a designed system, not floating in empty dark space

Preferred proof inventory:
- captures/enterprise/clinicalhours_enterprise_problem_section_live_recapture_v2.png
- captures/enterprise/clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png
- captures/enterprise/clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png
- captures/enterprise/clinicalhours_enterprise_platform_figure_2_live_recapture.png
- captures/enterprise/clinicalhours_enterprise_trust_section_live_recapture_v2.png
- captures/enterprise/clinicalhours_enterprise_mobile_430x932_live.png

Suggested slide structure:
1. friction
   - Show the manual chase problem.
   - Example message direction: onboarding still lives in forwarded emails, forms, and reminder notes.
2. unification
   - Show that applications and onboarding steps can sit in one visible workflow.
   - Keep the promise narrow: one queue, fewer blind spots.
3. workflow_proof
   - Show document or credential review moving out of the inbox.
   - Emphasize visibility into what is missing, not a bigger platform thesis.
4. control
   - Show live status: complete, missing, expiring, or still waiting.
   - This is the strongest proof slide for the chosen issue.
5. activation
   - Close on a believable CTA for clinics that want onboarding status in one place.

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
