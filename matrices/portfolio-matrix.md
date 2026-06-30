---
{
  "id": "portfolio",
  "name": "Portfolio Prompt Matrix",
  "version": "0.1.0",
  "domain": "portfolio",
  "rows": [
    {
      "domain": "Portfolio",
      "input": "many game briefs + source-material index",
      "interviewMode": "interview-low-stakes",
      "target": "concept-complete",
      "output": "portfolio triage table, coverage gaps, candidate priority groups",
      "promptId": "portfolio.games.interview-low.concept-complete.v1"
    },
    {
      "domain": "Portfolio",
      "input": "workspace summaries + shared library dependency notes",
      "interviewMode": "interview-medium-stakes",
      "target": "implementation-ready",
      "output": "cross-workspace dependency map, reference candidates, lockfile questions",
      "promptId": "portfolio.dependencies.interview-medium.implementation-ready.v1"
    }
  ]
}
---

| Domain | Input | Interview mode | Target | Output |
|---|---|---|---|---|
| Portfolio | many game briefs + source-material index | interview-low-stakes | concept-complete | portfolio triage table, coverage gaps, candidate priority groups |
| Portfolio | workspace summaries + shared library dependency notes | interview-medium-stakes | implementation-ready | cross-workspace dependency map, reference candidates, lockfile questions |
