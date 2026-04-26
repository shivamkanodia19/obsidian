# Wave 4 Gmail Follow-up System

**Date:** 2026-04-25
**Session Focus:** OAuth Gmail integration + smart follow-up drafting

## Situation

Had Gmail MCP connected in Claude Code but authentication was broken (bearer token incompatibility error: "does not support dynamic client registration"). Needed to access inbox to draft follow-ups for internship outreach sent 2+ weeks ago.

## Solution Implemented

### 1. Gmail OAuth Authentication
- Extracted Google Cloud OAuth credentials from user
  - Client ID: 1026688455855-2i8uj37fiapajihv5u1k8uqroa60cr8a.apps.googleusercontent.com
  - Client Secret: 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
- Ran OAuth flow via browser (user approved)
- Generated and saved token.json with refresh token
- Result: Direct Python API access to Gmail

### 2. Smart Follow-up Identification
Query: `from:me before:2026-04-20 subject:(internship OR opportunity OR position OR offer)`

Filtering rules:
- ✅ Only emails I SENT (from:me)
- ✅ Sent on or before April 20, 2026
- ✅ Exclude bounced/delivery failure emails
- ✅ Only draft for threads with NO external replies yet
- ✅ Skip emails that already got responses

Results:
- Found 9 emails matching search
- 1 already had reply (AMD) → skipped
- 8 identified needing follow-ups

### 3. Follow-ups Drafted

**8 follow-up drafts created:**

1. **Bowdark (James Wood)** — 3 email variants in thread
   - jwood@bowdark.com
   - Status: no reply yet (original sent ~2 weeks ago)

2. **FieldPulse** — gabriel@fieldpulse.com
   - Subject: TAMU Engineering Freshman – SaaS/ML background, summer internship
   - Status: no reply

3. **Go High Level** — shaun@gohighlevel.com
   - Subject: TAMU Engineering Freshman – SaaS/full-stack background, summer internship
   - Status: no reply

4. **G3 Tech Consultants** — contact@g3techconsultants.com
   - Subject: Summer Internship – Cybersecurity & Consulting Interest at G3 Tech Consultants
   - Status: no reply

5. **Denco** — melinda.camp@denco.org & employment@denco.org
   - Subject: Re: Summer Internship
   - Status: no reply (2 email variants)

**Excluded:**
- AMD (Lisa Ramos) — already replied, no follow-up needed
- All other outreach from March 30 → removed because they had issues (bounces, duplicates, etc.)

### 4. Follow-up Email Template

Generic template (user to customize per thread):
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

All drafts created directly in Gmail threads (not as standalone emails).

## Key Decisions

1. **OAuth over MCP:** Gmail MCP had auth incompatibility; direct Python API with OAuth token is more reliable
2. **Smart filtering:** Only follow up on emails with 0 replies (not the "received 1 recruiting email" case)
3. **Date cutoff April 20:** Ensures we're only following up on intentional outreach, not random recruiting emails
4. **Drafts not sends:** All 8 emails created as Gmail drafts for user review before sending

## Next Steps

- [ ] User reviews 8 drafts in Gmail
- [ ] Customize template per company if needed
- [ ] Send in staggered batches (not all at once)
- [ ] Monitor responses; set up second-follow-up if needed by May 1
