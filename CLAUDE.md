---
title: Second Brain — Vault Configuration
type: vault-config
last-updated: 2026-04-13
---

# Second Brain

## Vault Location
C:\Users\shiva\claude\

## Folder Structure
- projects/clinicalhours → ClinicalHours startup work
- research/fedvt → feedlot cattle futures forecasting research
- research/dairy-farming → dairy farm system dynamics research
- academics/csce120 → C++ coursework
- academics/math251 → multivariable calculus
- academics/engr216 → engineering dynamics
- career/internships → internship outreach and tracking
- career/resume → resume versions and targeting
- career/applications → fellowship and program applications
- knowledge → frameworks, concepts, things learned
- chats → imported Claude conversations

## Session Protocol
- On /resume: read the relevant project folder for context before starting work
- On /save: write a session log to the relevant project folder with decisions made, progress, and next steps
- Always check C:\Users\shiva\ClinicalHours\graphify-out\GRAPH_REPORT.md before answering ClinicalHours codebase questions

## Inbox Processing
When asked to "process inbox":
- Read every file in inbox\ except README.md
- Determine the correct vault folder based on content
- Add frontmatter with title, type, status, last-updated, and relevant tags
- Add [[links]] to related existing notes
- Move the file to the correct folder
- Update dashboard.md if needed

## Documents Processing
When asked to "process documents":
- Read every file in documents\inbox\
- Extract key information into a markdown summary note
- Save summary to the correct vault folder
- Move original file to documents\processed\
