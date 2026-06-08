---
title: ClinicalHours TikTok Future Agent Prompt - Student Topic Proof Alignment Repair - 2026-05-29
description: Paste-ready prompt for the next CloudEx Codex agent to audit current student slides for topic-to-proof mismatch and improve them using the vault's marketing strategy and psychology
last_updated: 2026-05-29
---

# ClinicalHours TikTok Future Agent Prompt - Student Topic Proof Alignment Repair - 2026-05-29

## Why This Prompt Exists

The current student slideshow system has a new failure mode:

- some slides use truthful Playwright captures
- the captures pass layout QA and copy audit
- but the hero proof is not specific enough to the slide topic

So the deck can still feel off even when the screenshots are real.

This is not mainly a rendering problem.

It is a topic-to-proof alignment problem:

- the headline promises one student pain or payoff
- the screenshot proves something adjacent, generic, or later-stage
- the result is weaker swipe logic, weaker trust, and weaker recall

There is also a workflow constraint:

- Replicate MCP was registered in `C:\Users\shiva\.codex\config.toml`
- but it did not hot-load in the already running Codex session
- so several recent branches stayed proof-safe but visually and semantically conservative

Your job is not just to make the slides prettier.

Your job is to review the current student-facing branches, find where the claim/proof relationship is weak, and improve the system using the existing marketing strategy, psychology, and QA standards already stored in the vault.

## What Seems Wrong Right Now

Use this as a starting hypothesis, not as gospel:

- a slide may use a real screenshot that is only loosely related to the topic
- a safe screenshot may have been chosen because it was available, not because it was the best proof
- a branch may have chosen the right marketing angle but the wrong visual proof
- a branch may have chosen the right proof but copy that outruns what the screenshot visibly supports
- some slides may be better retired than patched if the topic cannot be proven cleanly

Treat this as a stricter standard than "the screenshot is real."

The standard is:

- the screenshot is real
- the screenshot is the right proof for that exact slide job
- the biggest readable text inside the proof supports the hook
- the viewer can understand why that screenshot is there within about `2` seconds

## Highest-Risk Branches To Audit First

Audit these first because they are the newest and most likely to contain topic/proof tension:

- `v5firstpath`
- `v6realleads`
- `v6guestfirst`

Then compare them against the stronger student baselines:

- `v3bright7`
- `v4memory`
- `v4impact`

Do not assume the newer branch is better just because it is newer.

## Paste-Ready Prompt

```text
You are the next CloudEx Codex agent working in:

c:\Users\shiva\obsidian

Assignment:
Review the existing ClinicalHours student-facing TikTok slideshow branches, identify topic-to-proof mismatches and other persuasive weaknesses, then improve the strongest opportunities using the strategy, psychology, and QA standards already stored in the vault.

Core problem to solve:
Some current slides use truthful Playwright captures, but the captures are not specific enough to the actual slide topic. The deck may therefore pass truth and layout checks while still feeling weak, generic, or psychologically unconvincing.

Your goal:
Make the slides feel more relevant, more persuasive, and more student-real without weakening truth discipline.

Before you build:
1. Read the required notes in the order below.
2. If delegation is available, use three explorer subagents in parallel:
   - one to audit the current student branches slide by slide and rank the worst topic/proof mismatches
   - one to audit proof inventory, live captures, and crop quality, including whether tighter Playwright recaptures could solve the issue
   - one to extract the strongest marketing strategy and psychology tactics from the vault and map them to fixes
3. While the subagents run, inspect the current student compositions and iteration notes locally.
4. Start with findings, not redesign. Diagnose first.
5. After any rebuild, run at least two fresh-context judge passes before calling the branch ready.

Required read order:
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18.md
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18.md
- 02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/social_media_expert/clinicalhours-tiktok-social-rubric-2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_strategy_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_replication_playbook_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_iteration_loop_v1_2026-05-31.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_playwright_future_agent_playbook_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_codex_image_prompt_system_v1_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_skill_mcp_guardrails_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_compliance_qa_checklist.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/handoff/clinicalhours_tiktok_system_handoff_2026-05-19.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/captures/clinicalhours_live_capture_notes_2026-05-18.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v3bright7.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v4impact.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v4memory.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v5firstpath.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v6realleads.md
- 05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v6guestfirst.md

Student branches to inspect:
- composition/clinicalhours_tiktok_student_auth_v3bright.html
- composition/clinicalhours_tiktok_student_search_memory.html
- composition/clinicalhours_tiktok_student_first_path.html
- composition/clinicalhours_tiktok_student_real_leads.html
- composition/clinicalhours_tiktok_student_guest_first.html

Audit standard:
Do not stop at "truthful screenshot" or "layout passed."
Audit whether each slide deserves to exist.

For each student branch, score every slide on:
- topic/proof alignment
- hook clarity
- psychological specificity
- visible proof quality
- lane discipline
- CTA credibility

Findings to look for:
- headline promises a pain or payoff that the hero screenshot does not visibly prove
- the biggest readable text inside the screenshot fights the headline
- a public or auth screen is technically safe but semantically generic
- the slide is trying to tell a topic the product proof cannot actually support
- the branch uses support imagery or atmosphere to compensate for weak proof
- the branch repeats proof types without deepening the story
- the deck passes QA but fails "why this screenshot for this topic?"

Known hypotheses to verify or reject:
- `v5firstpath` may have weak proof tension around the first logged-shift idea, especially where setup-adjacent dashboard or journal surfaces are doing too much work
- `v6realleads` may be using truthful story or auth surfaces that feel too indirect for a sharp "real leads" trust claim
- `v6guestfirst` may have places where auth or later-stage account proof weakens the clean guest-first promise

Psychology and strategy rules to enforce:
- use hook -> body -> close progression
- make each swipe feel more useful and more specific than the last
- prioritize fast recognition over cleverness
- prioritize relief, control, and credibility over hype
- use one promise per slide
- use one dominant hero proof asset per slide
- prefer proof-first rewriting over decoration-first redesign
- keep the student tone practical, calm, and credible
- avoid med-school anxiety bait, fake urgency, or startup-slogan vagueness

Tool / MCP rules:
- start a fresh Codex session if needed so the registered MCP servers are available
- keep using Playwright for truthful proof capture and recapture
- if Replicate MCP is now callable in the fresh session, use it only for secondary support imagery after proof is locked
- do not use generated imagery as claim-bearing proof
- if Replicate is still unavailable, do not block; solve the problem with better topic selection, tighter crops, stronger proof mapping, and narrower copy
- use Figma only for layout exploration or alternate visual systems, not as claim-bearing proof
- use the review bundle plus exported PNGs as the cold-review packet for fresh-context judges

Required decision framework:
For each branch, decide:
- keep
- revise
- retire

Use `revise` only if the topic can be made strong with better proof, crops, or copy.
Use `retire` if the slide topic is not truthfully supportable with the current product proof.

Preferred improvement order:
1. Re-rank the existing branches by marketing strength and truth-safe relevance.
2. Fix the highest-upside existing branch before inventing a new one.
3. If none of the weak branches are worth saving, propose a better student topic grounded in the vault and supported by actual proof.
4. Only after the proof and copy are fixed should you add Replicate support imagery, if available and still useful.
5. After every serious revision round, run at least two fresh-context judges before deciding whether to keep iterating, retire, or ship.

Deliverables:
- a ranked findings memo across the current student decks
- a slide-by-slide issue list with concrete reasons
- keep / revise / retire decisions for each branch
- at least one improved student branch rendered end to end
- updated iteration notes explaining what was wrong and what changed
- updated pipeline spec if the revised branch is meant to be durable
- updated relevant indexes if you add or retire a durable branch

Verification requirements:
- run the local render script with QA enabled
- run the copy audit
- confirm the render produced a review bundle for the current suffix
- run at least two fresh-context judge reviews that do not see prior judge notes before their initial verdict
- visually inspect for topic/proof fit, not just collisions
- explicitly check that the screenshot text helps the headline
- explicitly check that each revised slide is more specific than the slide before it
- confirm final exports are `1080 x 1920`

Final response format:
- begin with the main findings, ordered by severity
- say which branch you revised or replaced and why
- link the updated composition, spec, iteration note, and exports
- say whether render QA passed
- call out any remaining proof limitations or MCP limitations
```

## References

- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-research-master-brief-2026-05-18]]
- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/clinicalhours-tiktok-slideshow-retention-strategy-2026-05-18]]
- [[02_Analyst/projects/ClinicalHours/campaigns/tiktok-slideshow/social_media_expert/clinicalhours-tiktok-social-rubric-2026-05-18]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_visual_strategy_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/docs/qa/clinicalhours_tiktok_skill_mcp_guardrails_2026-05-18]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v5firstpath]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v6realleads]]
- [[05_Outputs/images/clinicalhours_tiktok_2026-05-18/clinicalhours_tiktok_iteration_notes_v6guestfirst]]
