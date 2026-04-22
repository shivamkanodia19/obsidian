# ClinicalHours Clinic Contact & Intelligence Database

**Purpose:** Structured data model for tracking clinic prospects and outreach performance  
**Status:** Template defined, to be populated by research agents + contact finder agent

---

## Clinic Intelligence Record

```yaml
clinic_metadata:
  clinic_name: string
  clinic_type: enum[community_health_center, free_clinic, standalone_nonprofit, hospital_network]
  location:
    city: string
    state: string
    region: string  # DFW, Houston, Austin, etc.
  size:
    estimated_volunteer_count: integer  # 10-30, 30-100, 100+
    paid_staff_count: integer  # estimate from website
  operational:
    fiscal_year_start: month  # Jan, July, etc.
    annual_budget_estimate: integer  # for context
    recent_funding: string  # grants, donations, news
  web_presence:
    website: url
    facebook: url
    linkedin: url
    instagram: url

decision_makers:
  executive_director:
    name: string
    title: string
    email: string
    phone: string
    linkedin_url: url
  operations_manager:
    name: string
    title: string
    email: string
    phone: string
    linkedin_url: url
  volunteer_coordinator:
    name: string
    title: string
    email: string
    phone: string
    linkedin_url: url
  board_chair:
    name: string
    title: string
    email: string  # if available

volunteer_management:
  current_tools: list[string]  # VSys, Forms, spreadsheets, etc.
  volunteer_application_process: string  # description of current workflow
  estimated_hours_tracked: boolean
  estimated_pain_points: list[string]  # from research
  estimated_monthly_volunteer_hours: integer

pain_point_assessment:
  recruitment_difficulty: score[1-10]
  scheduling_complexity: score[1-10]
  compliance_overhead: score[1-10]
  hour_tracking_friction: score[1-10]
  volunteer_retention_challenge: score[1-10]
  primary_pain_point: string
  secondary_pain_points: list[string]

urgency_indicators:
  recent_volunteer_coordinator_job_posting: boolean
  recent_news_about_expansion: boolean
  appears_understaffed: boolean
  recent_funding_received: boolean
  visible_volunteer_shortage: boolean
  urgency_score: integer  # 1-10, impacts outreach priority

outreach_status:
  status: enum[new, contacted_waiting, meeting_scheduled, pilot_offered, customer, rejected]
  primary_contact: string  # email or name
  first_contact_date: date
  last_contact_date: date
  contact_count: integer
  response_received: boolean
  response_date: date
  notes: string
  next_action: string
  next_action_date: date

email_personalization:
  personalization_angle: string  # which pain point we emphasized
  subject_line_used: string
  cta_variant: string  # specific vs generic CTA
  tool_mentioned: string  # if they have existing tool
  clinic_specific_detail: string  # what made it personal

metrics:
  email_opened: boolean
  email_open_date: date
  email_clicked: boolean
  email_click_date: date
  reply_received: boolean
  reply_date: date
  meeting_booked: boolean
  meeting_date: date
  response_time_hours: integer
  conversion_stage: enum[lead, prospect, opportunity, customer]

segmentation:
  clinic_size_segment: enum[small, medium, large]
  decision_timeline: enum[immediate, 2_weeks, 1_month, 2_months, unknown]
  budget_sensitivity: enum[high, medium, low]
  compliance_driven: boolean
  efficiency_driven: boolean
  growth_driven: boolean
  competition_threat: string  # which tool are they considering?
```

---

## Database Structure (CSV Export Format)

```
clinic_name,city,state,volunteer_count,clinic_type,ed_name,ed_email,ed_phone,vc_name,vc_email,vc_phone,
current_tools,primary_pain_point,urgency_score,status,first_contact_date,last_contact_date,contact_count,
response_received,response_date,meeting_booked,meeting_date,email_opened,email_subject,personalization_angle,
segmentation_size,decision_timeline,next_action,next_action_date,notes
```

---

## Intelligence Gathering Checklist

For each clinic, collect:

### From Website
- [ ] Clinic name, address, phone, website
- [ ] Staff directory (ED, Operations Manager, Volunteer Coordinator names/emails)
- [ ] Volunteer information page (application process, requirements, opportunities)
- [ ] Contact page (general inquiry email)
- [ ] Recent news/updates
- [ ] Social media links

### From LinkedIn
- [ ] Executive Director profile (recent activity, connections)
- [ ] Operations Manager profile (title, experience)
- [ ] Volunteer Coordinator profile (title, recent job changes)
- [ ] Company page (follower count, recent updates)
- [ ] Mutual connections (for warm introductions)

### From Public Records (Form 990)
- [ ] Annual budget
- [ ] Staff headcount
- [ ] Recent funding/grants
- [ ] Leadership changes
- [ ] Mission statement

### From Research
- [ ] Estimated volunteer count (website, LinkedIn, news mentions)
- [ ] Current volunteer management tool (job postings, website mentions, inferred from process)
- [ ] Recent hiring activity (recruiting for volunteer coordinator = pain signal)
- [ ] Growth indicators (recent grants, expansion news)
- [ ] Competitive positioning (what tools are mentioned?)

---

## Outreach Priority Scoring

**Formula:** Urgency Score + Fit Score + Timing Score

### Urgency Score (1-10)
- Volunteer count 50-100: +3 (sweet spot for our pricing)
- Volunteer count 100+: +2 (larger, slower decision)
- Recent volunteer coordinator hiring: +3 (pain signal)
- Recent funding received: +2 (budget available)
- Visible operational stress: +2 (understaffed signals)

### Fit Score (1-10)
- Independent nonprofit (not hospital network): +3
- Currently using spreadsheets/manual processes: +3
- Not using VSys/Volgistics: +2 (less switching cost)
- DFW location: +2 (local advantage)
- Community health center (matches our positioning): +1

### Timing Score (1-10)
- Decision timeline immediate (grant deadline, new ED): +3
- Decision timeline 2 weeks: +2
- Decision timeline 1-2 months: +1
- Unknown timeline: +0
- Budget cycle approaching: +2

**Target:** Score 18+ for Tier 1 outreach, 12-17 for Tier 2

---

## Sample Intelligence Record (Mercy Clinic Friends)

```yaml
clinic_metadata:
  clinic_name: Mercy Clinic Friends
  clinic_type: community_health_center
  location:
    city: Dallas
    state: TX
    region: DFW
  size:
    estimated_volunteer_count: 140
    paid_staff_count: 25

decision_makers:
  executive_director:
    name: "John Smith" # example
    title: Executive Director
    email: "john.smith@mercyclinicfriends.org"
  volunteer_coordinator:
    name: "Jane Doe" # example
    title: Volunteer Manager
    email: "jane.doe@mercyclinicfriends.org"

volunteer_management:
  current_tools: ["Google Forms", "Excel", "Email list"]
  volunteer_application_process: "Online form + email confirmation"
  estimated_hours_tracked: false
  estimated_pain_points: ["Scheduling coordination", "Hour tracking", "Volunteer retention"]

urgency_indicators:
  recent_volunteer_coordinator_job_posting: true  # signal!
  appears_understaffed: true
  urgency_score: 8

outreach_status:
  status: new
  next_action: "Research Jane Doe on LinkedIn, draft personalized email"
```

---

## To Be Filled By Agents & Agentic Systems

- [ ] Clinic intelligence gathered (contacts, tools, pain points)
- [ ] Decision-maker profiles created
- [ ] Personalization angles identified (which pain point per clinic)
- [ ] Email variants generated and tracked
- [ ] Response metrics collected
- [ ] Conversion analysis (which angles work?)
- [ ] Follow-up performance tracked
