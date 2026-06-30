---
{
  "id": "product",
  "name": "Product Prompt Matrix",
  "version": "0.1.0",
  "domain": "product",
  "rows": [
    {
      "domain": "Product",
      "input": "brief + goals + users",
      "interviewMode": "interview-low-stakes",
      "target": "design-complete",
      "output": "product spec outline, assumptions, questions, gaps",
      "promptId": "product.brief.interview-low.design-complete.v1"
    },
    {
      "domain": "Product",
      "input": "product spec + operations notes",
      "interviewMode": "interview-high-stakes",
      "target": "operations-ready",
      "output": "operations gap report and approval register",
      "promptId": "product.workspace.interview-high.operations-ready.v1"
    },
    {
      "domain": "Product",
      "input": "release history + support notes",
      "interviewMode": "interview-high-stakes",
      "target": "maintenance-ready",
      "output": "maintenance gap report and support handoff questions",
      "promptId": "product.workspace.interview-high.maintenance-ready.v1"
    }
  ]
}
---

| Domain | Input | Interview mode | Target | Output |
|---|---|---|---|---|
| Product | brief + goals + users | interview-low-stakes | design-complete | product spec outline, assumptions, questions, gaps |
| Product | product spec + operations notes | interview-high-stakes | operations-ready | operations gap report and approval register |
| Product | release history + support notes | interview-high-stakes | maintenance-ready | maintenance gap report and support handoff questions |
