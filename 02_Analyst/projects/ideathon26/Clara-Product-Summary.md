---
title: Clara — Pre-Visit AI Intake System (Ideathon 2026)
project: ideathon26
status: active
origin_dump: [[01_Source/ideathon26/CLARA_RUBRIC_RESPONSES.md]]
last_synced_dump: [[01_Source/ideathon26/CLARA_RUBRIC_RESPONSES.md]]
last_updated: 2026-04-19
tags: [ideathon, product, ai-healthcare, pre-visit, intake]
---

# Clara — Pre-Visit AI Intake System

**Team:** Aryan Shah (CS), Dhir Parekh (Biomedical Engineering)  
**Track:** Product@TAMU Ideathon, General Track  
**Status:** Working prototype deployed with 8 pulmonologists

## The Problem

Clinicians interrupt patients every 18 seconds during visits because they're drowning in intake paperwork. Physicians spend **30% of each appointment on medical history** instead of actual care. The gap: everyone's building tools *for the visit*; nobody's optimizing *before it*.

## The Solution: Clara

**Pre-visit AI intake system** that calls patients 24 hours before their appointment and extracts structured clinical data.

### Flow

1. **Patient receives call** (Twilio) 24h before appointment
2. **Clara asks targeted questions** (LLM-powered, flowchart-based, adapts by chief complaint)
3. **Extracts structured clinical data** (symptoms, duration, severity, meds, red flags)
4. **Physician dashboard lights up** 5 min before patient arrives with clean SOAP note + alerts
5. **Result**: Doctor has full attention for patient

### Key Outcomes (Pilot Data)

- **4.5 minutes saved per visit**
- **100 minutes saved daily per clinic**
- **Reduced no-shows**
- **Increased EOC scores + patient satisfaction**
- **Reduced missed diagnoses** (red flag detection)

## Technical Architecture

**Stack:**
- **Voice**: Twilio (outbound pre-visit calls)
- **Conversation**: LLM-powered clinical chatbot (smart follow-ups)
- **Data extraction**: Transcript → structured SOAP note
- **Red flags**: Detects critical alerts (e.g., chest pain + SOB = cardiac risk)
- **EHR sync**: FHIR API → Epic (data flows seamlessly)
- **Dashboard**: Physician view (intake summary + alerts 5 min before patient)

**Key advantage**: No manual entry, no paperwork. Structured data flows directly into existing hospital systems.

## Challenges Solved

| Challenge | Solution |
|-----------|----------|
| **Medical speech-to-text errors** ("Lasix" → "lasics") | Post-process transcripts with medical LLM |
| **Over-questioning patients** | Refined flow based on pilot feedback; only ask what matters |
| **Epic integration security** | Built FHIR integration without manual entry |
| **Red flag false positives** | Tuned thresholds with real physician feedback |
| **Regulatory clarity** | Confirmed: Clara is *not* a medical device (supports judgment, doesn't diagnose) → removes deployment barriers |

## Competitive Advantages

1. **Real clinical outcomes** — Validated with 8 actual pulmonologists (not hypothetical users)
2. **Explainability** — Doctors see *why* Clara flags alerts (builds trust)
3. **Existing system integration** — Epic FHIR connection means deployable *tomorrow*; no workflow rip-out
4. **Non-regulated** — Cleared as support tool (not medical device) = faster adoption

## Validation & Next

**Currently**: Measuring outcomes with 8 pulmonologists (time saved, no-shows, satisfaction)

**Next**: Expand to primary care clinics (same system, 10x larger market)

**Vision**: Every clinic has Clara running intake. Doctors have more time for patients. Diagnoses don't get missed.

## Cross-Project Insight

**Note:** Clara target = clinics. ClinicalHours target = clinics. Potential integration point: Clara handles pre-visit intake; ClinicalHours could handle volunteer scheduling for post-visit follow-ups or administrative support.
