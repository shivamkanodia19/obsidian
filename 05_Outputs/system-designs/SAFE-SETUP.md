---
title: Safe LinkedIn Automation Setup
date: 2026-04-16
security: Maximum (no stored credentials)
---

# Safe LinkedIn Automation — Step-by-Step Setup

## Overview

**No passwords stored anywhere.** Everything uses secure browser-based authentication.

```
Step 1: Gmail OAuth (browser sign-in)
  ↓
Step 2: Extract companies from sent emails
  ↓
Step 3: LinkedIn password prompt (typed at runtime, never saved)
  ↓
Step 4: Automated connections with personalized messages
```

---

## Step 1: Gmail OAuth Setup

### 1.1 Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create new project: "LinkedIn Automation"
3. Enable Gmail API:
   - Search "Gmail API"
   - Click "Enable"
4. Create OAuth credentials:
   - Go to "Credentials" → "Create Credentials" → "OAuth 2.0 Desktop App"
   - Download as JSON
   - Save as `credentials.json` in your project folder

### 1.2 Install Dependencies

```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client anthropic selenium webdriver-manager python-dotenv
```

### 1.3 Set Environment Variable

Create `.env` file:
```
ANTHROPIC_API_KEY=your_api_key_here
```

---

## Step 2: Extract Companies from Gmail

### 2.1 Run Gmail Extraction

```bash
python gmail-extract-oauth.py
```

**What happens:**
1. Browser opens: "Sign in with Google"
2. You log in (I never see password)
3. You click "Allow" (grants email read permission)
4. Script extracts sent emails
5. Saves:
   - `sent_emails.txt` — Company names (one per line)
   - `email_context.json` — Email details for reference
   - `token.json` — OAuth token (encrypted on your machine)

**Output example:**

```
sent_emails.txt:
Acme Corporation
TechFlow Systems
Global Logistics Inc
```

```
email_context.json:
{
  "Acme Corporation": {
    "to": "hr@acme.com",
    "subject": "Internship interest - Supply chain",
    "date": "2026-04-10",
    "body_preview": "Hi, I'm interested in..."
  }
}
```

### 2.2 Review Extracted Data

```bash
cat sent_emails.txt
cat email_context.json
```

Verify:
- ✅ Companies are correct
- ✅ Email context looks good
- ✅ No sensitive data exposed

---

## Step 3: LinkedIn Automation (Safe Mode)

### 3.1 Test with 5 Connections First

```bash
python linkedin-safe-connect.py \
  --emails sent_emails.txt \
  --daily-limit 5
```

**What to expect:**

```
🔐 LinkedIn Credentials (never stored)
----------------------------------------
LinkedIn Email: your-email@gmail.com
LinkedIn Password: [typing hidden]
```

Then:
- Chrome browser opens
- Logs in
- Searches for CEOs
- Sends 5 connection requests with personalized messages
- Logs all activity to `linkedin-automation.log`

### 3.2 Monitor the Test Run

While script is running:
- Watch the browser window (should look human-like)
- Check logs: `tail -f linkedin-automation.log`
- Wait for all 5 connections to complete

After completion:
- Check your LinkedIn notifications (did requests go through?)
- Check for any "verify account" messages
- Review `linkedin-activity.json` for details

### 3.3 Wait 24 Hours

**Don't run again for 24 hours.** Let LinkedIn normalize your activity.

Check your email:
- ❌ "Suspicious activity detected" → Account flagged (wait 48h before retrying)
- ✅ Silence → All good

---

## Step 4: Scale Up (Only if Test Passed)

If 24 hours passed with no flags:

```bash
# Increase to 10 connections
python linkedin-safe-connect.py \
  --emails sent_emails.txt \
  --daily-limit 10
```

**Wait 24 hours again** before increasing further.

**Recommended scaling:**
- Day 1-2: 5 connections
- Day 3-4: 10 connections
- Day 5+: 15 connections (don't exceed)

---

## Security Checklist

### Before Running

- [ ] `.env` file created with `ANTHROPIC_API_KEY`
- [ ] `credentials.json` downloaded from Google Cloud
- [ ] `sent_emails.txt` contains correct company names
- [ ] LinkedIn password is STRONG (not reused elsewhere)
- [ ] 2FA enabled on LinkedIn account
- [ ] Running from same device/IP as usual
- [ ] VPN/Proxy OFF

### After Each Run

- [ ] Check `linkedin-automation.log` for errors
- [ ] Review `linkedin-activity.json` for activity
- [ ] Check LinkedIn inbox for alerts/verification requests
- [ ] Verify connection requests actually sent
- [ ] Wait 24 hours before running again

### If Account Flagged

1. **Check LinkedIn:**
   - Look for "Verify your account" prompt
   - Complete any verification (solve CAPTCHA, etc.)

2. **Wait 48 hours:**
   - Use LinkedIn manually only
   - No automation

3. **Resume carefully:**
   - Set `--daily-limit` to 3 (not 10)
   - Wait 24h between runs
   - Gradually increase

---

## File Security

### What's Stored Locally

| File | Contains | Safe? |
|------|----------|-------|
| `.env` | API key | ✅ Keep private |
| `credentials.json` | OAuth app credentials | ✅ App-level, not personal |
| `token.json` | OAuth token (encrypted) | ✅ Encrypted by Google |
| `sent_emails.txt` | Company names only | ✅ Your emails sent them |
| `email_context.json` | Email subjects + previews | ✅ Your own emails |
| `linkedin-automation.log` | Activity log | ✅ Local only |
| `linkedin-activity.json` | Connection details | ✅ Local only |

### What's NEVER Stored

- ❌ LinkedIn password (never stored, never logged)
- ❌ Gmail password (never stored, OAuth only)
- ❌ Full email bodies (previews only)
- ❌ API credentials in code

---

## Troubleshooting

### Gmail Extraction

**"credentials.json not found"**
- Download from Google Cloud Console
- Save to project folder

**"No sent emails found"**
- Check Gmail actually has sent emails
- Gmail API might need permission refresh

**"Authentication failed"**
- Restart the script (token might be corrupted)
- Delete `token.json` and run again

### LinkedIn Automation

**"Login failed"**
- Check email/password are correct
- Try logging in manually first
- Check if account is locked

**"Chrome driver error"**
- Update Chrome browser
- Restart computer
- Try different Chrome version

**"2FA blocking automation"**
- Complete 2FA manually in browser
- Script waits for you (press Enter when done)

**"Account flagged"**
- Complete verification LinkedIn asks for
- Wait 48 hours
- Resume with lower daily-limit

---

## Expected Results

### Week 1
- 5-10 connections sent
- 0-1 responses (too early)
- 0 account flags (if setup correct)

### Week 2-3
- 20-40 total connections
- 1-5 responses
- Monitor for any issues

### Week 4+
- 50+ connections
- 5-15 responses (7-15% rate)
- 1-3 calls scheduled

---

## Next Steps

1. **Create Google Cloud project**
   - Enable Gmail API
   - Download `credentials.json`

2. **Run `gmail-extract-oauth.py`**
   - Authenticate with Google
   - Extract companies

3. **Review extracted data**
   - Check `sent_emails.txt`
   - Check `email_context.json`

4. **Run `linkedin-safe-connect.py` with `--daily-limit 5`**
   - Test with 5 connections
   - Monitor for 24 hours

5. **Scale up (only if safe)**
   - Increase to 10, then 15

---

## Key Principles

✅ **Do:**
- Start small (5 connections)
- Wait 24 hours between runs
- Monitor logs carefully
- Stop if flagged

❌ **Don't:**
- Store passwords
- Run >15/day
- Ignore warnings
- Automate 24/7

---

## Questions?

Review logs:
- `linkedin-automation.log` — Detailed activity
- `linkedin-activity.json` — Structured data

**Rule:** If anything looks wrong, STOP and wait 48 hours.

Your account safety is priority #1.
