---
title: Second Brain Dashboard
type: dashboard
last-updated: 2026-04-13
---

# Dashboard

## Active Projects & Work

```dataview
TABLE status, stage, tags
FROM ""
WHERE type = "project" AND status = "active"
SORT file.mtime DESC
```

```dataview
TABLE status, target-roles, offers
FROM "career"
WHERE type = "career" AND status = "active-search"
SORT file.mtime DESC
```

```dataview
TABLE status, paper-1-status, advisor
FROM "research"
WHERE type = "research" AND status = "in-progress"
SORT file.mtime DESC
```

---

## Urgent Deadlines

```dataview
TABLE urgent-deadline, active-programs
FROM ""
WHERE urgent-deadline
SORT urgent-deadline ASC
```

> **Manual reminders:**
> - Zachry Leadership Program — June 2026 (not yet submitted)

---

## Recent Session Logs

```dataview
TABLE file.mtime AS "Last Updated", type, status
FROM ""
WHERE type = "session-log"
SORT file.mtime DESC
LIMIT 10
```

---

## Open Next Steps

```dataview
TASK
FROM ""
WHERE !completed
SORT file.mtime DESC
```

---

## All Notes by Area

```dataview
TABLE type, status, last-updated
FROM ""
WHERE type != "dashboard" AND type != "vault-config"
SORT file.folder ASC, file.name ASC
```

---

## Vault Index

**Career**
- [[resume-current]] — current resume
- [[summer-2026-search]] — summer 2026 internship search
- [[fellowships-tracker]] — programs, fellowships, leadership apps
- [[avf-prep]] — Aggie Venture Fund second round prep

**Projects**
- [[platform-status]] — ClinicalHours project overview
- [[pitch-deck]] — ClinicalHours pitch deck

**Research**
- [[research-tracker]] — FEDVT research overview
- [[paper-outline]] — FEDVT paper 1 outline
- [[working-paper]] — FEDVT ASAS-CSAS working paper
