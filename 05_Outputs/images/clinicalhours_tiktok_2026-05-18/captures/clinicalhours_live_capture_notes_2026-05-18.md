# ClinicalHours Live Capture Notes - 2026-05-18

These captures were taken from the live public ClinicalHours site with Playwright on `2026-05-18`.

## Follow-up student recaptures on 2026-05-29

To support new student-facing trust and activation topics, the live public student surfaces were rechecked with Playwright again on `2026-05-29`.

New captures added:

- `home/clinicalhours_home_our_story_live_2026-05-29.png`
- `home/clinicalhours_home_hero_live_2026-05-29.png`
- `auth/clinicalhours_auth_live_2026-05-29.png`

Why they matter:

- `home_our_story_live_2026-05-29.png` gives a truthful student-pain proof surface with explicit language about `outdated lists`, `word of mouth`, and not knowing what was real or accessible.
- `auth_live_2026-05-29.png` gives a current public auth-state proof surface for the guest-first entry story.
- `home_hero_live_2026-05-29.png` reflects the refreshed homepage headline and count, but it should still be used carefully because the visible count can drift relative to older map captures.

## Follow-up auth recheck on 2026-05-30

While auditing topic-to-proof fit across the student branches on `2026-05-30`, the live public auth page was rechecked with Playwright again.

New capture added:

- `auth/clinicalhours_auth_live_2026-05-30.png`

Why it matters:

- it confirms that `Browse as guest` is still publicly visible on the current auth page
- it also confirms that the full auth page still gives `Continue with Google` and the sign-in form more visual weight than the guest action
- for browse-first or sign-in-later CTA slides, the tighter derived guest-action crop remains the safer proof than the full auth page

## Recapture note

Several first-pass enterprise section captures looked blank or washed out when dropped into the deck.

The reliable fix was:

- navigate to the live enterprise page
- target the real `figure` or `section` element instead of taking an approximate viewport crop
- call `scrollIntoViewIfNeeded()`
- wait about `1-2` seconds before taking the screenshot

These corrected recaptures are now part of the proof inventory:

- `enterprise/clinicalhours_enterprise_problem_section_live_recapture_v2.png`
- `enterprise/clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png`
- `enterprise/clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png`
- `enterprise/clinicalhours_enterprise_platform_figure_2_live_recapture.png`
- `enterprise/clinicalhours_enterprise_trust_section_live_recapture_v2.png`
- `enterprise/clinicalhours_enterprise_outputs_section_live_recapture_v2.png`

## Verified public states

Student-facing:

- `home/clinicalhours_home_desktop_1440x1200_live.png`
- `home/clinicalhours_home_mobile_430x932_live.png`
- `home/clinicalhours_home_hero_section_live.png`
- `home/clinicalhours_home_how_it_works_live.png`
- `home/clinicalhours_home_our_story_live_2026-05-29.png`
- `home/clinicalhours_home_hero_live_2026-05-29.png`
- `map/clinicalhours_map_desktop_1440x1200_live.png`
- `map/clinicalhours_map_panel_live.png`
- `auth/clinicalhours_auth_desktop_1440x1200_live.png`
- `auth/clinicalhours_auth_live_2026-05-29.png`

Clinic-facing:

- `enterprise/clinicalhours_enterprise_desktop_1440x1200_live.png`
- `enterprise/clinicalhours_enterprise_mobile_430x932_live.png`
- `enterprise/clinicalhours_enterprise_hero_section_live.png`
- `enterprise/clinicalhours_enterprise_problem_section_live.png`
- `enterprise/clinicalhours_enterprise_platform_applications_live.png`
- `enterprise/clinicalhours_enterprise_platform_hipaa_live.png`
- `enterprise/clinicalhours_enterprise_platform_status_live.png`
- `enterprise/clinicalhours_enterprise_platform_supply_live.png`
- `enterprise/clinicalhours_enterprise_outputs_list_live.png`
- `enterprise/clinicalhours_enterprise_trust_signals_live.png`
- `enterprise/clinicalhours_enterprise_ready_demo_section_live.png`

Element-level recaptures used in the final `v1` deck:

- `enterprise/clinicalhours_enterprise_problem_section_live_recapture_v2.png`
- `enterprise/clinicalhours_enterprise_platform_figure_0_live_recapture_v2.png`
- `enterprise/clinicalhours_enterprise_platform_figure_1_live_recapture_v2.png`
- `enterprise/clinicalhours_enterprise_platform_figure_2_live_recapture.png`
- `enterprise/clinicalhours_enterprise_trust_section_live_recapture_v2.png`

## Important warnings

- The student homepage lower stat cards show `0+` and `0%` placeholder metrics in the live public state captured on `2026-05-18`.
- Those placeholder metrics should be cropped out or avoided entirely.
- The strongest current public proof for a TikTok deck lives on the enterprise page, not the logged-out student homepage.
- The student lane is still usable, but it depends more heavily on discovery/map/auth surfaces and less on deeper in-product proof.
- The newer student homepage hero capture from `2026-05-29` shows `9,516+` opportunities while the map capture used in the current deck system still shows `9,512 opportunities`; avoid mixing those counts inside the same deck unless all visible proof is refreshed to the same number.

## Bright-lane raw asset warnings

These files are still truthful, but future agents should not use them as uncropped hero proof in the bright student lane:

- `home/clinicalhours_home_mobile_430x932_live.png`
  Reason: dominant readable text is the generic slogan `Find your clinical future.`
- `auth/clinicalhours_dashboard_overview_auth_live_v3.png`
  Reason: dominant readable text includes empty-state strings like `No upcoming deadlines`
- `auth/clinicalhours_journal_section_auth_live_v3.png`
  Reason: dominant readable text includes `No hours logged yet. Start tracking!`
- `auth/clinicalhours_auth_signin_card_auth_live_v3.png`
  Reason: dominant readable text includes generic onboarding copy above the more useful `Browse as guest` action

When using the bright student lane, prefer derived crops from `captures/derived/` and follow the copy-plus-screenshot gate documented in `docs/playbooks/clinicalhours_tiktok_student_marketing_sequence_and_copy_audit_2026-05-19.md`.

## Default recommendation

Build `clinic_ops_primary` decks first unless the assignment explicitly asks for a student-facing sequence.
