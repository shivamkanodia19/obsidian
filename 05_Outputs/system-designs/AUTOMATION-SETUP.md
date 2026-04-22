---
title: LinkedIn Automation Setup & Risk Mitigation
date: 2026-04-16
risk-level: Moderate (with safeguards)
---

# LinkedIn Automation — Complete Setup Guide

## What This Does

This automation script:
1. **Logs into your LinkedIn account** (with stealth mode)
2. **Researches companies** from a list of company names
3. **Finds CEO/leaders** on LinkedIn
4. **Sends connection requests** with personalized messages
5. **Logs all activity** for safety review

**Expected output:** 5-15 successful connections per day (depending on account age/activity level)

---

## Installation

### 1. Install Dependencies

```bash
pip install selenium webdriver-manager anthropic python-dotenv
```

### 2. Set API Key

Create `.env` file in the project folder:
```
ANTHROPIC_API_KEY=your_key_here
```

### 3. Prepare Company List

Create `sent_emails.txt` with company names (one per line):
```
Acme Corporation
TechFlow Systems
Global Logistics Inc
```

Or use the `linkedin-outreach-agent.py` to extract companies from actual emails.

---

## Running the Script

### First Time: Test with 5 Connections

```bash
python linkedin-auto-connect.py \
  --email your-linkedin-email@gmail.com \
  --password your-password \
  --emails sent_emails.txt \
  --daily-limit 5
```

**Monitor what happens:**
- Check if script connects successfully
- Verify each connection request was sent
- Check your LinkedIn inbox for any verification requests
- Review `linkedin-automation.log` for details

### Scale Up (Only if Step 1 Works)

If 5 connections sent fine after 24 hours:
```bash
python linkedin-auto-connect.py \
  --email your-linkedin-email@gmail.com \
  --password your-password \
  --emails sent_emails.txt \
  --daily-limit 10
```

---

## Anti-Detection Safeguards Built In

### Timing Randomization
- Delays between actions: 30-300 seconds (random)
- Delays between connections: 1-3 minutes (random)
- No consistent patterns that LinkedIn can detect

### Human-Like Behavior
- Mouse movements to elements (not instant clicks)
- Random scrolling before/after actions
- Slow typing (0.02-0.1 sec per character)
- Random user-agent rotation (Chrome on Windows/Mac/Linux)

### Stealth Mode
- Hides webdriver signals
- Injects JavaScript to mask automation detection
- Disables Blink automation features
- Removes telltale headers

### Rate Limiting
- Configurable daily limit (default 8)
- Start with 5, increase by 5 every 24 hours
- Never exceed 15 per day (LinkedIn's soft limit)

### Account Monitoring
- Every action logged to `linkedin-automation.log`
- Activity saved to `linkedin-activity.json`
- Can pause/resume between sessions

---

## CRITICAL SAFETY RULES

### ⚠️ DO NOT

- ❌ Run more than 15 connections per day
- ❌ Run the script 24/7 (LinkedIn detects constant patterns)
- ❌ Use multiple accounts from same IP
- ❌ Ignore "verify account" or 2FA prompts (stop immediately)
- ❌ Skip the 5-connection test run
- ❌ Use same connection message for everyone (personalization matters)

### ✅ DO

- ✅ Start with 5, wait 24 hours, increase by 5
- ✅ Stop if you see "Verify your account" message
- ✅ Wait 24-48 hours if account gets flagged
- ✅ Run at "normal hours" (9am-6pm LinkedIn timezone)
- ✅ Mix in manual activity (browse profiles, send messages manually)
- ✅ Review logs before running again

---

## Account Safety Checklist

### Before Running

- [ ] LinkedIn password is STRONG (not reused elsewhere)
- [ ] 2FA is enabled on your LinkedIn account
- [ ] Account is >1 month old (new accounts flagged faster)
- [ ] Account has activity history (not newly created)
- [ ] VPN/Proxy is off (LinkedIn flags IP changes)
- [ ] You're running from same network/device as usual

### After Each Run

- [ ] Check LinkedIn inbox/notifications for alerts
- [ ] Review `linkedin-automation.log` for errors
- [ ] Verify connection requests actually sent
- [ ] Check if LinkedIn is asking for verification (STOP if yes)
- [ ] Log results in `linkedin-activity.json`

### If Account Gets Flagged

**What you might see:**
- "Verify your account" prompt
- CAPTCHA on every action
- "Unusual activity detected" message
- Temporary lockout (24 hours)

**What to do:**
1. Stop the script immediately
2. Complete any verification LinkedIn asks for (solve CAPTCHA, confirm email, etc.)
3. Use LinkedIn manually for 48 hours
4. Resume with daily-limit set to 3 (not 8)

---

## Expected Results

### Week 1
- 5-7 connections accepted
- 0-1 direct replies (too early)
- 0 account flags (if randomization working)

### Week 2-3
- 10-15 total connections accepted
- 1-3 replies to messages
- Monitor for any flags

### Week 4+
- 50-100 connections total
- 5-10 responses
- 1-3 scheduled calls

**Response rate target:** 7-15% (research-backed)

---

## Troubleshooting

### "Login failed"
- Check email/password
- Verify 2FA not blocking
- Try manual login first to ensure credentials work

### "Search results not found"
- Company name might be incorrect
- Try exact legal company name
- Smaller companies might not be on LinkedIn

### "Connection button not found"
- LinkedIn UI changes frequently
- Manually update XPath selectors in script
- Or report issue for script update

### "Message limit exceeded"
- LinkedIn limits messages to new connections (usually <300 chars)
- Script already truncates, but keep messages short

### Account gets flagged
- Follow account safety checklist above
- Reduce daily-limit to 3-5
- Wait 48 hours before resuming

---

## Security & Privacy

### Your Data
- Passwords are entered directly (not saved)
- Activity logged locally (not sent anywhere)
- LinkedIn automation logs saved to your machine only
- .env file with API key never committed to git

### API Key
- Anthropic API key used only for message generation
- API calls made directly (no 3rd party middleman)
- Keep your `.env` file private

### LinkedIn ToS
This script uses LinkedIn's intended features (sending connection requests, messages). However:
- LinkedIn prohibits automation
- Your account could be suspended if LinkedIn detects this
- Use responsibly and at your own risk
- Test with 5 connections first

---

## Files Generated

```
linkedin-automation.log          # Detailed activity log
linkedin-activity.json          # Structured activity data
linkedin-auto-connect.py        # Main automation script
linkedin-outreach-framework.md  # Message framework reference
linkedin-outreach-agent.py      # Research + message generation
AUTOMATION-SETUP.md             # This file
```

---

## Alternative: Manual Hybrid Approach

If you're concerned about account risk, the **hybrid approach is safer**:

1. Run `linkedin-outreach-agent.py` to generate research + messages
2. You manually send connection requests on LinkedIn
3. You manually send follow-up messages

**Why it's safer:**
- LinkedIn sees human behavior (no patterns)
- You control quality (catch bad messages before sending)
- Zero account flag risk
- Only takes ~5 min per person

**Trade-off:** Manual sending takes more time, but account stays safe.

---

## Next Steps

1. **Test:** Run with --daily-limit 5
2. **Monitor:** Check logs and LinkedIn for 24 hours
3. **Review:** If successful, increase to 10
4. **Scale:** Add more companies as account proves stable
5. **Follow up:** Schedule Day 3, Day 7, Day 12 messages manually or via second automation run

---

## Questions?

Review logs:
- `linkedin-automation.log` — What the script did
- `linkedin-activity.json` — Structured data for analysis

Key safeguard: If anything looks wrong, STOP and wait 24 hours before resuming.
