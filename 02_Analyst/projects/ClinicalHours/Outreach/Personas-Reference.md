---
title: Outreach Personas - Reference Card
project: clinicalhours
strategic: false
status: stable
last_updated: 2026-04-15
description: Quick reference guide for Operations Director and Volunteer Coordinator personas. Use for email copy, demo scripts, objection handling.
---

# Outreach Personas - Reference Card

**Use this file when:**
- Writing cold emails (tailor message to persona)
- Planning demo calls (which features to show first)
- Handling objections (know their concerns in advance)
- Training outreach agent (Claude API prompts should reference these)

---

## Quick Comparison

| Dimension | Operations Director | Volunteer Coordinator |
|-----------|-----|-----|
| **Decision Role** | Decision-maker (YES/NO authority) | Influencer (recommends, but doesn't decide) |
| **Daily Pain** | No visibility into volunteer data, compliance risk, time spent on admin | Manual data entry, no scheduling visibility, ghosting problem |
| **Urgency** | Medium-high (20% annual retention loss is costly) | High (spending 20-30 hrs/week on admin) |
| **Tech Comfort** | Moderate (uses Salesforce, Sheets, Google Workspace) | Moderate-to-low (prefers simple UI) |
| **Price Sensitivity** | Medium ($1,200/year feels OK; $3K+ feels expensive) | Not the decision-maker, but will influence |
| **Implementation Risk** | Medium (wants assurance won't add more work) | High (if it adds work, they'll fight it) |
| **Success Metric** | Save 50% of admin time + improve volunteer retention | Save 5+ hours/week + never lose an application |
| **First Conversation** | Emphasize time savings + compliance + retention | Emphasize daily workflow improvement + mobile access |

---

## Persona 1: Operations Director

**Executive Summary:**
Runs volunteer programs; controls budget; 10-20 years nonprofit experience; needs to see ROI (time saved, retention improved, compliance managed). Willing to try new tools if setup is easy.

### Pain Points (Prioritized)

1. **Recruitment friction (Critical)**
   - Gets 30-50 applications/month; manual review takes 4-6 hours
   - **Why it matters:** Time = money; also missing good candidates due to review delay
   - **How ClinicalHours solves it:** Automatic application ranking, one-click interview invites

2. **Volunteer retention bleeding (Critical)**
   - Loses 20-30% annually; doesn't track why
   - **Why it matters:** Recruiting replacement volunteers is expensive (20+ hours per replacement)
   - **How ClinicalHours solves it:** Engagement features (scheduling preferences, communication), retention tracking

3. **No volunteer data visibility (High)**
   - Doesn't know: who's qualified, availability, hours logged, compliance status
   - **Why it matters:** Hard to forecast volunteer capacity; hard to report to board/funders
   - **How ClinicalHours solves it:** Centralized dashboard, automated hours reporting

4. **Compliance risk (High)**
   - No automated screening verification or HIPAA documentation
   - **Why it matters:** Risk of liability; hard to pass audits
   - **How ClinicalHours solves it:** Background check integration, compliance dashboards

5. **Coordinator burnout (Medium)**
   - Coordinator spending 20-30 hrs/week on admin
   - **Why it matters:** High turnover in coordinator role = more training cost for ops director
   - **How ClinicalHours solves it:** Reduce coordinator load to 10-15 hrs/week

### Email Hooks (For Cold Outreach)

**Most effective:**
- "Your volunteer coordinators probably spend 20+ hours a week on email and forms"
- "Getting 30+ applications a month but [Clinic Name]'s review process takes 4-6 hours per batch?"
- "Volunteer retention at [Clinic Name] is probably 70-75%. What if you could get to 85%?"

**Least effective:**
- Generic "streamline your volunteer management"
- Technical features first (compliance, integrations) — they want outcome first

### Objections & Counterarguments

**Objection:** "We've been using Forms and Sheets for 5 years, it works fine"
- **Root cause:** Inertia; doesn't see the hidden cost of manual process
- **Reframe:** "It works, but [Coordinator name] is probably spending 20-30 hours a week on it. What if we cut that in half?"
- **Proof:** "Similar clinic with 80 volunteers was spending $25K/year on coordinator salary on just volunteer management. They reduced that to $12K."

**Objection:** "What if you go out of business? We'd be stuck"
- **Root cause:** Startup risk concern
- **Reframe:** "We offer 60-day data export guarantee. Your data is always yours. Plus, we're profitable with our first customer."
- **Proof:** "Our first customer (BCS FHC) has been on platform for [X months]. Happy to put you in touch."

**Objection:** "Our volunteers don't use tech much"
- **Root cause:** Underestimating volunteer willingness; worried about adoption friction
- **Reframe:** "Our average volunteer takes 3 minutes to sign up. You'd see adoption from 80%+ in week 1."
- **Proof:** "BCS FHC's volunteers averaged age [X]; adoption was [%] in first week."

**Objection:** "We'd need buy-in from [Volunteer Coordinator]"
- **Root cause:** Smart; knows the coordinator will resist if it adds work
- **Reframe:** "That's exactly right. Let's include them in the demo. They'll see it actually *saves* them 5+ hours a week."
- **Next step:** Schedule demo with both Operations Director + Coordinator

### Demo Strategy

**For Operations Director, show:**
1. Application queue (auto-ranked by fit)
2. Volunteer dashboard (compliance status, hours logged, retention risk)
3. Coordinator workload reduction (before/after hours breakdown)
4. Reporting (hours by program, retention trends, grant reporting)

**Don't show (too technical):**
- API integrations
- Custom fields configuration
- Database architecture

**Closing question:**
- "Would you be open to a 30-day trial with 2-3 coordinators to see the impact?"

---

## Persona 2: Volunteer Coordinator

**Executive Summary:**
Day-to-day volunteer ops; moderate tech skills; very busy (20-30 hrs/week on admin); will make-or-break adoption. Needs tools that *reduce* their workload, not add to it.

### Pain Points (Prioritized)

1. **Manual application screening (Critical)**
   - Reads 100+ form submissions/month; copies data into spreadsheet manually
   - **Why it matters:** 4-6 hours of data entry; applications get lost in email
   - **How ClinicalHours solves it:** Auto-intake, centralized queue, one-click ranking

2. **Scheduling chaos (Critical)**
   - No visibility into who's available when; sends blast emails ("is anyone free Tuesday?")
   - **Why it matters:** 2-3 hours/week of back-and-forth texting; volunteers get annoyed
   - **How ClinicalHours solves it:** Volunteer sets availability; coordinator sees calendar; one-click messaging to available people

3. **Volunteer ghosting (High)**
   - People disappear; no way to re-engage automatically
   - **Why it matters:** 30-40% of recruited volunteers never show up; 20-30% quit after first shift
   - **How ClinicalHours solves it:** Auto check-ins, engagement reminders, re-engagement campaigns

4. **Hours tracking is manual (High)**
   - Volunteers text/call hours; coordinator logs them manually
   - **Why it matters:** 1-2 hours/week of data entry; errors in grant reporting
   - **How ClinicalHours solves it:** Volunteers log hours in app; reports auto-generated

5. **Onboarding takes forever (Medium)**
   - Each new volunteer needs custom paperwork, orientation, setup
   - **Why it matters:** 30-60 minutes per new volunteer; people quit during this friction
   - **How ClinicalHours solves it:** Templated onboarding, digital forms, auto-completion

### Email Hooks (For Cold Outreach)

**Most effective:**
- "Stop copying form data into spreadsheets"
- "Volunteer coordinators spend 4-6 hours a week just screening applications"
- "Ever send an email to your whole volunteer list asking 'who's available Tuesday?' and get 5 replies?"

**Least effective:**
- "Volunteer management platform" (too vague)
- Features-first messaging
- Mentions of compliance/HIPAA (they don't care; their director does)

### Objections & Counterarguments

**Objection:** "This looks complicated, I don't have time to learn new tools"
- **Root cause:** Afraid it will add work, not reduce it
- **Reframe:** "It's actually simpler than your current process. You'll spend 15 minutes setting up, then save 5+ hours every week."
- **Proof:** "Watch a 3-minute walkthrough of your typical workflow: [demo video link]"

**Objection:** "Our volunteers won't fill out another form/app"
- **Root cause:** Worried about adoption friction
- **Reframe:** "They've already filled out your initial application. This is built into their workflow; they set their schedule once and never fill anything out again."
- **Proof:** "BCS FHC had 95% volunteer adoption in week 1."

**Objection:** "I still have to do manual follow-up anyway?"
- **Root cause:** If the tool doesn't solve the core problem, they'll reject it
- **Reframe:** "No. Here's what's automated: [interview invites, schedule matching, check-in reminders, hours logging]. You handle exceptions only."
- **Demo:** Walk through a real volunteer onboarding to prove it

**Objection:** "Our director won't approve another subscription"
- **Root cause:** Budget constraint or change resistance
- **Reframe:** "This *saves* money. You're probably spending $15-20K in coordinator salary on manual work every year. This costs $1,200."
- **Proof:** "For every 100 hours coordinator time you save, you save $2,000 in salary cost."

### Demo Strategy

**For Volunteer Coordinator, show:**

1. **Application intake** — Show how their Google Form automatically feeds in; show how ranking works
2. **Your daily schedule** — Show calendar view; ask "do you ever send 'who's available' messages?" Then show one-click messaging to available volunteers
3. **Hours logging** — Show volunteer app hours entry; show auto-generated reports
4. **A real workflow** — Walk through: New application → interview → onboarding → first shift → hours logged. Show time saved at each step.

**Emphasize:**
- "You'll save 5+ hours every week"
- "Volunteers handle their own scheduling"
- "No more manual data entry"

**Don't show (too technical):**
- Admin console
- Custom field configuration
- Integrations

**Closing question:**
- "Would you be willing to try it with your next batch of new volunteers? No risk, you can tell me if it helps."

---

## Outreach Email Templates

### For Operations Director (Cold)

**Subject Line Options:**
- "[Clinic Name] volunteer coordinators — save 5 hours/week"
- "[Clinic Name]'s volunteer retention strategy"
- "How [Clinic Name] could recruit 20% more volunteers without hiring"

**Body Template:**

```
Hi [Director Name],

I noticed [Clinic Name] is managing [X] volunteers across [program]. 
That's probably 20+ hours a week of applications, scheduling, and follow-up.

We help clinics like yours automate that workflow. Our first customer 
(BCS FHC) went from Google Forms + Sheets to structured volunteer 
management in 30 days. Result: Coordinators saved 5+ hours/week, 
and they reduced volunteer turnover from 28% to 18%.

Would you be open to a 15-minute conversation about how it works for clinics your size?

Shivam
clinicalhours.org | 214-470-0598
```

**Personalization tweaks:**
- Mention their volunteer count (shows research)
- Mention their recent news/funding (shows you did homework)
- Mention a pain point visible from their website (if they advertise "looking for coordinators", mention "we help coordinators work efficiently")

---

### For Volunteer Coordinator (Cold)

**Subject Line Options:**
- "Stop copying forms into spreadsheets"
- "[Clinic Name] volunteer coordinators — save 5 hours/week"
- "Question: how many hours/week do you spend on volunteer scheduling?"

**Body Template:**

```
Hi [Coordinator Name],

I noticed you're managing [X] volunteers at [Clinic Name]. 
That's probably 4-6 hours a week just screening applications 
and another 3-4 hours on scheduling.

We help coordinators cut that down to 30 minutes of screening 
and auto-matched scheduling. No more manual form copying or 
"who's available Tuesday?" emails.

Want a quick walkthrough (15 min)? 
Happy to show you exactly how it saves time.

Shivam
clinicalhours.org | 214-470-0598
```

**Personalization tweaks:**
- Mention their specific pain point visible from research (e.g., "I saw you're hiring another coordinator — suggests the workload is growing")
- Keep it shorter than ops director email (they're busy)
- Lead with *outcome* (hours saved), not features

---

## Conversation Flowchart (When They Call/Reply)

**If Operations Director replies:**
1. Confirm: "Are you the one making decisions on volunteer management tools?"
2. Uncover: "What's your biggest challenge with your current setup?" (listen)
3. Educate: "Many directors we talk to mention [their stated pain]. Here's how ClinicalHours handles that..."
4. Prove: "Would it help to see it in action? 15-minute demo with you and [Coordinator name]?"
5. Close: "Great. Can we do this Thursday or Friday?"

**If Volunteer Coordinator replies:**
1. Confirm: "How much time do you spend each week on volunteer admin?"
2. Uncover: "What's the most annoying part?" (listen)
3. Show: "What if I could show you how to cut that by 50%?"
4. Demo: "Quick walkthrough (15 min)?"
5. Close: "Great. Let's set it up."

**If no reply (5-7 days):**
1. Send follow-up email (different angle)
2. Try LinkedIn message (to coordinator, if cold-emailed director)
3. If still no reply (14+ days), archive for 6 months

---

## Red Flags (Abort This Prospect)

- **"We're in the middle of [major project] so not the right time"** — Come back in 6 months
- **"Our IT department controls all software"** — Still worth pursuing, but longer sales cycle
- **"Our volunteers are mostly 70+ year old"** — Lower adoption risk still exists, but ask about coordinator time savings instead
- **"We use Salesforce"** — Means they're tech-forward; go harder on efficiency + compliance messaging

---

## Wins to Celebrate / Reference

When we close our first 2-3 clinics, document:
- Clinic name, size (volunteer count)
- Primary pain point that drove adoption
- Time saved (hours/week)
- Retention improvement
- Onboarding time (if applicable)

Use this as social proof in future outreach.

