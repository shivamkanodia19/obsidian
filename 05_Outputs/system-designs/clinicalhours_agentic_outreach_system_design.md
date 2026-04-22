# ClinicalHours Agentic Email Outreach System Design

**Purpose:** Systematize clinic outreach with minimal manual effort  
**Status:** System design phase  
**Target Deployment:** Week of 2026-04-21 (after research completes)

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CLINIC EMAIL OUTREACH SYSTEM                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [1] Contact Finder Agent                                           │
│      ├─ LinkedIn search (targeting roles)                           │
│      ├─ Form 990 database lookup                                    │
│      ├─ Clinic website scraping (staff directory)                   │
│      ├─ Email validation (RocketReach/Hunter API)                  │
│      └─ Output: Validated contact database                          │
│           ↓                                                          │
│  [2] Intelligence Gatherer Agent                                    │
│      ├─ Clinic website analysis (tools, volunteer count)            │
│      ├─ Recent news/funding (Google News, nonprofit databases)      │
│      ├─ LinkedIn company page scraping                              │
│      ├─ Job posting analysis (hiring signals)                       │
│      └─ Output: Enriched clinic intelligence                        │
│           ↓                                                          │
│  [3] Segmentation & Priority Engine                                 │
│      ├─ Calculate urgency score (size, pain signals, timing)        │
│      ├─ Assign clinic segment (small/medium/large)                  │
│      ├─ Identify decision timeline                                  │
│      └─ Output: Prioritized contact list with scores                │
│           ↓                                                          │
│  [4] Email Personalization Agent                                    │
│      ├─ Select subject line variant (A/B test pair)                 │
│      ├─ Choose pain point emphasis (clinic-specific research)       │
│      ├─ Generate personalization detail (from clinic data)          │
│      ├─ Select CTA variant (generic vs specific)                    │
│      └─ Output: Personalized email (subject + body)                 │
│           ↓                                                          │
│  [5] Gmail Draft Agent                                              │
│      ├─ Create Gmail draft (no auto-send)                           │
│      ├─ Add tracking headers (for open/click detection)             │
│      ├─ Log outreach to CSV                                         │
│      └─ Output: Draft ready for manual review                       │
│           ↓                                                          │
│  [6] Follow-Up Manager Agent                                        │
│      ├─ Track email opens/clicks (from tracking headers)            │
│      ├─ Detect responses (Gmail API)                                │
│      ├─ Schedule follow-up emails (per sequence rules)              │
│      ├─ Escalate to phone (if email exhausted)                      │
│      └─ Output: Follow-up status + next actions                     │
│           ↓                                                          │
│  [7] Metrics & Optimization Agent                                   │
│      ├─ Calculate response rates (by subject line, pain point, CTA) │
│      ├─ Analyze conversion funnel (contact → email → reply → mtg)   │
│      ├─ Identify top-performing variants                            │
│      ├─ Recommend optimizations                                     │
│      └─ Output: Weekly optimization report                          │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Agent Specifications

### 1. Contact Finder Agent

**Purpose:** Identify and validate clinic decision-makers  
**Runs:** Once per clinic (or monthly refresh)

**Inputs:**
- Clinic name, website, location

**Process:**
1. **LinkedIn Search**
   - Query: `[clinic_name] "Executive Director" OR "Operations Manager" OR "Volunteer Coordinator"`
   - Extract: Name, title, email (if visible), profile URL
   
2. **Form 990 Database (ProPublica Nonprofit Explorer)**
   - Lookup clinic by EIN or name
   - Extract leadership from most recent 990
   
3. **Website Scraping**
   - Scrape `/staff`, `/team`, `/contact` pages
   - Extract names, titles, emails
   
4. **Email Validation**
   - Use RocketReach/Hunter API to validate/find emails
   - Verify deliverability before outreach
   
5. **Deduplication**
   - Merge records from multiple sources
   - Prefer highest confidence/most recent source

**Outputs:**
```yaml
contacts:
  - contact_name: string
    contact_title: enum[executive_director, operations_manager, volunteer_coordinator]
    email: string
    email_confidence: enum[high, medium, low]
    phone: string (if found)
    linkedin_url: url
    source: string  # LinkedIn, website, Form 990, etc.
```

**Error handling:**
- If no email found: Flag for manual research
- If validation fails: Try alternative contact
- If multiple contacts: Return all, let email agent choose

---

### 2. Intelligence Gatherer Agent

**Purpose:** Collect clinic context for personalization  
**Runs:** Once per clinic (or monthly refresh)

**Inputs:**
- Clinic name, website, location

**Process:**
1. **Website Analysis**
   - Extract: Volunteer count (from website mentions)
   - Extract: Current tools (if mentioned in volunteer info)
   - Extract: Volunteer opportunities listed
   - Extract: Clinic mission + services
   
2. **Recent News & Activity**
   - Google News search for clinic name + grants/funding
   - LinkedIn company page: recent posts, updates
   - Twitter/social media mentions (growth signals)
   
3. **Job Posting Analysis**
   - Search Indeed/LinkedIn for clinic's job postings
   - Detect "Volunteer Coordinator" hiring (pain signal!)
   - Extract: Required skills, job description hints
   
4. **Form 990 Context**
   - Annual budget (for context/fit)
   - Staff headcount trends
   - Mission alignment

**Outputs:**
```yaml
clinic_intelligence:
  volunteer_count: integer
  current_tools: list[string]  # ["Google Forms", "Excel", etc.]
  recent_hiring_activity: boolean
  recent_funding_received: boolean
  recent_news: list[string]
  clinic_mission: string
  estimated_pain_points: list[string]
```

---

### 3. Segmentation & Priority Engine

**Purpose:** Rank clinics by outreach priority and fit  
**Runs:** After contact finder + intelligence gatherer

**Logic:**
```
urgency_score = (
  volunteer_count_score +  # 10-30: +2, 30-100: +4, 100+: +3
  hiring_activity_score +  # Recent volunteer coordinator hiring: +3
  funding_score +          # Recent grant/funding: +2
  growth_indicator_score   # News about expansion: +2
)

fit_score = (
  independent_nonprofit +  # +3 if not hospital network
  current_tools_score +    # Using spreadsheets/forms: +3
  location_score           # DFW: +2, Texas: +1, Other: +0
)

priority_score = urgency_score + fit_score
segment = "Tier 1" if priority_score >= 12 else "Tier 2" if >= 8 else "Tier 3"

decision_timeline = (
  "immediate" if recent_hiring OR recent_funding
  "2_weeks" if visible_pain_signals
  "1_month" if growth_indicators
  "2_months" if general_expansion
  "unknown"
)
```

**Outputs:**
```yaml
segmentation:
  urgency_score: integer [1-10]
  fit_score: integer [1-10]
  priority_score: integer [2-20]
  segment: enum[tier_1, tier_2, tier_3]
  decision_timeline: enum[immediate, 2_weeks, 1_month, 2_months, unknown]
  outreach_order: integer  # position in outreach sequence
```

---

### 4. Email Personalization Agent

**Purpose:** Generate personalized subject + body for each clinic  
**Runs:** Before each email draft

**Inputs:**
- Contact name + role
- Clinic intelligence (size, tools, pain points)
- A/B test variant pair (subject line, pain point, CTA)

**Process:**
1. **Subject Line Selection** (A/B paired)
   - Pair A: Problem-focused
   - Pair B: Curiosity-driven
   - Randomize per clinic for clean test
   
2. **Personalization Detail**
   - Extract clinic-specific fact from intelligence
   - Examples:
     - "managing 140 volunteers must be challenging"
     - "saw that you're hiring a volunteer coordinator"
     - "your recent partnership expansion"
   
3. **Pain Point Emphasis**
   - Small clinic: Efficiency (save time, reduce chaos)
   - Medium clinic: Compliance + scaling
   - Large clinic: Scalability + automation
   
4. **CTA Selection**
   - Variant A: Generic ("15-min call in next few weeks")
   - Variant B: Specific ("15-min Tuesday or Wednesday 2-4pm")
   
5. **Email Generation**
   - Use Claude API with clinic context
   - Constrain to ~120 words, current email structure
   - Insert personalization detail + clinic-specific pain point

**Outputs:**
```yaml
email:
  subject_line: string
  body: string
  personalization_angle: string
  pain_point_emphasis: enum[efficiency, compliance, scalability]
  cta_variant: enum[generic, specific]
  estimated_personalization_depth: enum[level_1, level_2, level_3]
```

---

### 5. Gmail Draft Agent

**Purpose:** Create Gmail draft for manual review + send  
**Runs:** After email generation

**Process:**
1. Authenticate with Gmail API
2. Create draft with personalized subject + body
3. Add tracking headers (optional: tracking pixel for opens)
4. Log outreach to CSV
5. Return draft link for manual review

**Outputs:**
- Gmail draft created
- outreach_log.csv updated
- CLI confirmation with draft link

---

### 6. Follow-Up Manager Agent

**Purpose:** Systematize follow-up sequences based on responses  
**Runs:** Continuously (checks responses daily)

**Process:**
1. **Daily Check**
   - Query Gmail API for responses to prior emails
   - Check tracking pixels for opens/clicks
   - Update database
   
2. **Response Analysis**
   - If no reply after 5 days: Queue email 2 (social proof angle)
   - If no reply after 12 days: Queue email 3 (lower-friction ask)
   - If no reply after 21 days: Flag for phone call
   
3. **Follow-Up Email Generation**
   - Create follow-up variant (new angle, case study, different CTA)
   - Send from outreach system
   
4. **Escalation**
   - If phone call needed: Create task for manual follow-up
   - Provide summary of prior emails + suggested talking points

**Outputs:**
```yaml
follow_up_action:
  clinic_name: string
  last_contact_date: date
  status: enum[awaiting_response, follow_up_queued, phone_call_ready]
  next_follow_up_date: date
  follow_up_email_variant: string
  talking_points: string (for phone call)
```

---

### 7. Metrics & Optimization Agent

**Purpose:** Analyze performance and recommend improvements  
**Runs:** Weekly

**Metrics Tracked:**
```
- Emails drafted: count
- Emails sent: count
- Emails opened: count (via tracking)
- Emails replied to: count
- Reply rate: emails_replied / emails_sent
- Meetings booked: count
- Meeting rate: meetings_booked / emails_replied
- Conversion rate: meetings_booked / emails_sent

By variant:
- Subject line A open rate vs B
- Pain point emphasis: efficiency vs compliance vs scalability
- CTA variant: generic vs specific booking rate

By clinic segment:
- Response rate by clinic size
- Response rate by clinic type
- Response rate by decision timeline
```

**Analysis:**
- Which subject lines get highest opens?
- Which pain points get highest replies?
- Which CTAs get highest booking rate?
- Which clinic segments convert best?

**Outputs:**
```yaml
weekly_metrics:
  total_contacts: integer
  emails_sent: integer
  open_rate: float
  reply_rate: float
  meeting_rate: float
  conversion_rate: float
  top_performer: string  # subject line, pain point, or CTA variant
  recommendation: string  # what to optimize next
```

---

## Data Flow & Integration

```
[Manual Input] City/Region Selection
    ↓
[Contact Finder] → Contacts Database
    ↓
[Intelligence Gatherer] + [Contacts] → Enriched Clinic Database
    ↓
[Segmentation Engine] → Prioritized Outreach Queue
    ↓
[Email Personalization] + [A/B Test Config] → Personalized Email
    ↓
[Gmail Draft Agent] → Human Review → Manual Send
    ↓
[Gmail API Monitor] Tracks Opens/Clicks/Replies
    ↓
[Follow-Up Manager] Schedules & Sends Follow-Ups
    ↓
[Metrics Agent] Analyzes Performance & Recommends Optimizations
```

---

## Integration with Existing Agent

**Current agent location:** `C:\Users\shiva\clinic_outreach\agent.py`

**Proposed architecture:**
- Keep existing agent for basic outreach
- Build new agentic system as wrapper/enhancement
- New agents handle: Contact finding, intelligence, segmentation, follow-up, metrics
- Existing agent handles: Email generation (can be replaced with new Email Personalization Agent)

**Implementation path:**
1. Phase 1: Contact finder + intelligence gatherer (standalone)
2. Phase 2: Email personalization agent (replace/enhance current)
3. Phase 3: Follow-up manager + metrics (new)
4. Phase 4: Full integration into single system

---

## Technology Stack

- **Claude API:** Agent orchestration, email generation, intelligence analysis
- **Gmail API:** Draft creation, response tracking
- **LinkedIn API/Scraping:** Contact discovery
- **Form 990 API:** Leadership lookup (ProPublica/GuideStar)
- **Email validation:** RocketReach or Hunter API
- **Data storage:** CSV files (can migrate to DB later)
- **Scheduling:** Python APScheduler or cron
- **Tracking:** Gmail tracking pixel + API monitoring

---

## Deployment Plan

**Phase 1 (Week of 2026-04-21):** Research agents complete → Integrate findings into system design  
**Phase 2 (Week of 2026-04-28):** Build Contact Finder + Intelligence agents  
**Phase 3 (Week of 2026-05-05):** Build Email Personalization + Follow-Up agents  
**Phase 4 (Week of 2026-05-12):** Launch pilot outreach (20-30 clinics), start A/B testing  
**Phase 5 (Week of 2026-05-26):** Scale to full DFW outreach (100+ clinics), optimize based on metrics

---

## Success Criteria

- **Contact quality:** 80%+ valid emails
- **Email personalization:** 100% personalized (clinic-specific detail)
- **Response rate:** 5-10% (above nonprofit cold email benchmarks)
- **Meeting rate:** 30%+ of replies book calls
- **Conversion rate:** 1-2 new paying customers from first 100 outreach contacts
- **Automation:** 95% of process automated (only human review + send)

