---
title: Wave 4 Gmail Follow-ups System (2026-04-25)
project: internships
strategic: false
status: execution_ready
origin_dump: [[01_Source/career/internships/wave-4-gmail-followups-2026-04-25]]
last_synced_dump: [[01_Source/career/internships/wave-4-gmail-followups-2026-04-25]]
conflict_detected: false
last_updated: 2026-04-25
tags: [gmail, outreach, followups, wave-4, internships]
---

# Wave 4 Gmail Follow-ups (2026-04-25)

## Overview

Established direct Gmail access via OAuth (bypassing broken MCP) and identified 8 internship outreach emails from March 30–April 20 that need follow-ups. All drafts created in Gmail threads (not standalone).

**Status:** 8 drafts ready for user review + send.

## OAuth Integration

**Problem:** Gmail MCP in Claude Code had auth error ("does not support dynamic client registration"). Service account approach required domain-wide delegation (not configured).

**Solution:** Direct Python API via OAuth token
- Extracted Google Cloud OAuth credentials
- Ran browser OAuth flow (user approved)
- Generated token.json with refresh token
- Python scripts now access Gmail directly

**Result:** Reliable access to [[01_Source/career/internships/wave-4-gmail-followups-2026-04-25|internship outreach]] email threads.

## Smart Follow-up Filtering

Applied filters to avoid drafting to unrelated emails:

**Query:** `from:me before:2026-04-20 subject:(internship OR opportunity OR position OR offer)`

**Rules applied:**
- Only emails I sent (from:me filter)
- Sent on/before April 20, 2026
- Skip bounced emails (automatic detection)
- Skip if external already replied (check thread message count + sender)
- Skip if duplicate/variant emails to same company

**Results:**
- 9 emails matched search
- 1 excluded (AMD — already replied)
- 8 identified for follow-ups

## Drafts Created

**All 8 drafts placed directly in Gmail threads (user to customize + send):**

| Company | Contact | Original Subject | Status |
|---------|---------|-----------------|--------|
| Bowdark | James Wood / jwood@bowdark.com | Shivam Kanodia – Internship Interest | Draft created (Re: variant) |
| FieldPulse | gabriel@fieldpulse.com | TAMU Eng Freshman – SaaS/ML | Draft created |
| Go High Level | shaun@gohighlevel.com | TAMU Eng Freshman – SaaS/full-stack | Draft created |
| G3 Tech Consultants | contact@g3techconsultants.com | Summer Internship – Cybersecurity | Draft created |
| Denco | melinda.camp@denco.org, employment@denco.org | Re: Summer Internship | Draft created (2 variants) |

### Generic Follow-up Template

```
Hi,

I wanted to follow up on my previous email regarding summer internship opportunities. 
I'm still very interested in exploring potential roles at your organization.

If you have any openings or if my application is still being reviewed, I'd love to discuss further.

Looking forward to hearing from you!

Best regards,
Shivam Kanodia
TAMU Engineering
shivamkanodia77@gmail.com
```

User to customize per company context if needed.

## Key Decisions

1. **OAuth over MCP:** Direct Python API more reliable than MCP connector
2. **Smart filtering:** Only follow up on emails with zero external replies (not spam recruiting emails)
3. **Date cutoff April 20:** Ensures following up on intentional outreach, not random inbound
4. **Drafts not auto-send:** All created as Gmail drafts for user review

## Next Steps

- [ ] User reviews 8 drafts in Gmail Drafts folder
- [ ] Customize template per company if needed (personalization > generic)
- [ ] Send in staggered batches (not all at once) to reduce spam appearance
- [ ] Set up tracking: expect 20-30% response rate
- [ ] If no response by May 1, queue second follow-up

## Related Work

- [[career/internships/_index]] — Full internship strategy + OA pipeline
- [[career/internships/outreach/wave-4]] — Wave 4 outreach execution (30 companies, contact finding, sending workflow)
- [[02_Analyst/projects/ClinicalHours]] — Parallel cold outreach system (60+ clinic emails) using similar smart filtering
