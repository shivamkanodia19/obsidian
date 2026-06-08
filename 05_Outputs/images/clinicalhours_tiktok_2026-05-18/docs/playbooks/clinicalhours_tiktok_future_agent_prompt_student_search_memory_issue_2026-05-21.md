---
title: ClinicalHours TikTok Future Agent Prompt - Student Search Memory Issue - 2026-05-21
description: Paste-ready prompt for generating a new student-facing ClinicalHours slideshow about losing track after discovering clinics
last_updated: 2026-05-21
---

# ClinicalHours TikTok Future Agent Prompt - Student Search Memory Issue - 2026-05-21

## Why This Issue

This is the best next student-side angle because it is different from the current bright branch without outrunning the product proof.

What the current student system already covers:

- random search pain
- one map as the first payoff
- clinic preview
- one account / browse-first CTA

What this issue adds:

- the search does not just feel scattered at the start
- it also loses memory after discovery
- students find clinics, then lose track of which ones mattered, where they left off, and what to do next

Why this feels newer:

- it is not another `9,512 openings. One map.` deck
- it is not another generic `browse first` CTA branch
- it is not another broad `one account / one journal` story

Cross-checked alternatives that were considered but not chosen:

- `Let me filter before I open ten tabs.`
  - too close to the current map-led discovery story
- `Browse first. Decide later.`
  - safe, but too close to the existing CTA logic
- `Logging after a shift should be obvious.`
  - interesting, but the current journal proof is more fragile if it becomes the whole topic

Chosen issue:

- `Students lose track after discovery because their clinical search lives across tabs, screenshots, saved links, and separate notes instead of one place that remembers what they found and what to do next.`

Safest fallback if the proof read breaks during execution:

- `Browse first. Decide later.`

## Paste-Ready Prompt

```text
You are extending the ClinicalHours TikTok slideshow system in c:\Users\shiva\obsidian.

Assignment:
Generate a new 5-slide ClinicalHours student-facing slideshow about this specific issue:
"Students lose track after discovery because their clinical search lives across tabs, screenshots, saved links, and separate notes instead of one place that remembers what they found and what to do next."

Before you build:
1. If Shivam has not explicitly confirmed this issue, ask one short question confirming that this is the topic he wants.
2. If delegation is available, use three explorer subagents in parallel:
   - one to verify which current student decks already cover adjacent ground and what would feel repetitive
   - one to verify truthful student proof assets and claim boundaries from strategy notes, captures, specs, and QA docs
   - one to scan broader ClinicalHours vault notes for underused student pain themes and verify that this is still the best new angle
3. While the subagents run, inspect the current bright student branch locally.
4. If the subagents show that this issue is too repetitive or proof-weak, fall back to:
   - "Browse first. Decide later."
   and explain the switch in the final response.

Required read order:
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18.md
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_strategy_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_playwright_future_agent_playbook_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/clinicalhours_live_capture_notes_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v3bright7.md
- 02_Analyst/projects/ClinicalHours/campaigns/clinicalhours_hera_launch_additional_notes_2026-05-20.md
- 02_Analyst/research/ClinicalHours/ClinicalHours-readable-slide-comments.md
- 02_Analyst/research/ClinicalHours/clinicalhours-deck-claude-design-comments-2026-04-21.md
- 05_Outputs/images/clinicalhours-product-audit-2026-05-18/clinicalhours_dashboard_auth_snapshot_2026-05-18.md
- 05_Outputs/images/clinicalhours-product-audit-2026-05-18/clinicalhours_hours_auth_snapshot_2026-05-18.md
- 05_Outputs/images/clinicalhours-product-audit-2026-05-18/clinicalhours_opportunities_auth_snapshot_2026-05-18.md

Truth and lane constraints:
- lane: student_discovery_secondary
- audience: premed or health-track students looking for clinical hours
- use metadata: evidence_tier = product_surface, proof_access = mixed_public_and_authenticated_preview
- keep the story inside student search clarity, save/track follow-through, and low-friction progress
- do not imply guaranteed placements, guaranteed admissions, guaranteed acceptance, or guaranteed hours
- do not imply AMCAS-ready export, application standardization, or deeper admissions workflow unless the screenshot visibly proves it
- do not imply authenticated dashboard states are a guest-visible public flow
- do not drift into clinic-ops, big network thesis, or enterprise workflow language
- if you use an opportunity count, standardize on one exact number only
- prefer `9,512` if you use the current derived map proof

Visual and psychology constraints:
- use the brighter editorial student direction, not the old dark student branch
- use visibly fewer words than the current `v3bright7` deck
- aim for shorter than the current bright branch on both headline and subtext
- off-white or warm cream base, dark navy typography, blue/mint/coral accents
- the psychology target is relief from scattered follow-through, not hype or med-school anxiety bait
- each swipe should feel more useful and more specific than the last one
- if an empty-state crop is used, the slide must explicitly be about not having a place to save, track, or log yet

Build approach:
- create a new issue-specific student branch instead of overwriting `v3bright7`
- suggested composition file: 05_Outputs/images/clinicalhours_tiktok_2026-05-18/composition/clinicalhours_tiktok_student_search_memory.html
- suggested deck spec: 05_Outputs/images/clinicalhours_tiktok_2026-05-18/pipeline/specs/clinicalhours_tiktok_student_search_memory_v1_deck_spec.json
- suggested export suffix: v4memory
- start from the current bright student composition, not the older dark `v2auth` branch
- keep the new branch tighter and less wordy than `v3bright7`

Issue framing to preserve:
- the pain is not "finding clinical hours is impossible"
- the pain is not "students need a full productivity operating system"
- the pain is "the search has no memory after you find something worth keeping"
- focus on tabs, screenshots, saved links, preview before click, tracked opportunities, and keeping progress together
- make the deck feel student-real, calm, and practical

Preferred proof inventory:
- captures/derived/clinicalhours_map_tall_controls_focus_v1.png
- captures/derived/clinicalhours_map_focus_v1.png
- captures/auth/clinicalhours_dashboard_featured_card_auth_live_v3.png
- captures/auth/clinicalhours_dashboard_hero_auth_live_v2.png
- captures/derived/clinicalhours_dashboard_tall_focus_v2.png
- captures/derived/clinicalhours_journal_toolbar_tile_v2.png
- captures/derived/clinicalhours_auth_actions_focus_v2.png

Assets to avoid as uncropped hero proof:
- captures/home/clinicalhours_home_mobile_430x932_live.png
- captures/auth/clinicalhours_dashboard_overview_auth_live_v3.png
- captures/auth/clinicalhours_journal_section_auth_live_v3.png
- captures/auth/clinicalhours_auth_signin_card_auth_live_v3.png

Suggested slide structure:
1. friction
   - Name the memory problem after discovery.
   - Example direction: found clinics, still lost track?
2. discovery
   - Show one clearer search starting point.
   - Example direction: filter first instead of opening ten tabs.
3. simplification
   - Show that a clinic can be previewed and judged before wasting a click.
   - Keep the promise concrete: better next click, not a giant platform promise.
4. documentation_direction
   - Show that tracked opportunities, saved progress, or journal workflow give the search somewhere to live after discovery.
   - Emphasize follow-through and organization, not AMCAS export or deep application automation.
5. activation
   - Close on a believable CTA for students who want to browse, save, and track without committing too early.

Copy rules:
- one dominant message per slide
- shorter copy than `v3bright7`
- headlines ideally `3-6` words when possible
- one short sentence of subtext
- no internal-strategy language
- no media-buying jargon
- no placeholder metrics
- no repeated number conflicts
- no claims stronger than the screenshot evidence
- if the screenshot text is weaker than the copy, weaken the copy

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
- visually inspect the final slides for collisions, screenshot-text quality, and proof tension
- explicitly check whether the word count now feels tighter than `v3bright7`

Final response format:
- state the chosen issue and why it is truth-safe
- if you changed to the fallback angle, say so and explain why
- link the new composition, spec, and iteration note
- say whether render QA passed
- call out any remaining proof limitations
```

## References

- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18]]
- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v3bright7]]
- [[02_Analyst/projects/ClinicalHours/campaigns/clinicalhours_hera_launch_additional_notes_2026-05-20]]
