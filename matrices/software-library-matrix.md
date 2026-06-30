---
{
  "id": "software-library",
  "name": "Software Library Prompt Matrix",
  "version": "0.1.0",
  "domain": "software-library",
  "rows": [
    {
      "domain": "Software library",
      "input": "README + API notes",
      "interviewMode": "interview-medium-stakes",
      "target": "implementation-ready",
      "output": "library spec outline and API contract candidates",
      "promptId": "software-library.readme.interview-medium.implementation-ready.v1"
    },
    {
      "domain": "Software library",
      "input": "candidate spec + validation output",
      "interviewMode": "interview-medium-stakes",
      "target": "implementation-ready",
      "output": "implementation gap report",
      "promptId": "software-library.workspace.interview-medium.implementation-ready-review.v1"
    },
    {
      "domain": "Software library",
      "input": "release process + support notes",
      "interviewMode": "interview-high-stakes",
      "target": "maintenance-ready",
      "output": "maintenance gaps and support questions",
      "promptId": "software-library.workspace.interview-high.maintenance-ready.v1"
    },
    {
      "domain": "Software library",
      "input": "archive notes",
      "interviewMode": "interview-all",
      "target": "archival-ready",
      "output": "archive gaps and deprecation questions",
      "promptId": "software-library.workspace.interview-all.archival-ready.v1"
    }
  ]
}
---

| Domain | Input | Interview mode | Target | Output |
|---|---|---|---|---|
| Software library | README + API notes | interview-medium-stakes | implementation-ready | library spec outline and API contract candidates |
| Software library | candidate spec + validation output | interview-medium-stakes | implementation-ready | implementation gap report |
| Software library | release process + support notes | interview-high-stakes | maintenance-ready | maintenance gaps and support questions |
| Software library | archive notes | interview-all | archival-ready | archive gaps and deprecation questions |
