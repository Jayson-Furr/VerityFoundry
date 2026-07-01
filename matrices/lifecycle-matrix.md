---
{
  "id": "lifecycle",
  "name": "Lifecycle Prompt Matrix",
  "version": "0.1.0",
  "domain": "lifecycle",
  "rows": [
    {
      "domain": "Lifecycle",
      "input": "candidate workspace + validation/readiness output + release notes",
      "interviewMode": "interview-medium-stakes",
      "target": "production-ready",
      "output": "release-readiness gap report, blocking questions, approval register",
      "promptId": "lifecycle.workspace.interview-medium.production-ready.release-gap-review.v1"
    },
    {
      "domain": "Lifecycle",
      "input": "shipped product spec + release history + support notes",
      "interviewMode": "interview-high-stakes",
      "target": "maintenance-ready",
      "output": "maintenance interview questions, maintenance gaps, support handoff gaps",
      "promptId": "lifecycle.shipped-product.interview-high.maintenance-ready.v1"
    },
    {
      "domain": "Lifecycle",
      "input": "retiring product spec + operations/data/support/platform notes",
      "interviewMode": "interview-all",
      "target": "decommission-ready",
      "output": "decommissioning questions, decommission gaps, archival follow-up items",
      "promptId": "lifecycle.retiring-product.interview-all.decommission-ready.v1"
    },
    {
      "domain": "Lifecycle",
      "input": "retired product spec + final manifests + license/support/archive notes",
      "interviewMode": "interview-all",
      "target": "archival-ready",
      "output": "archival questions, archive manifest gaps, evidence gap register",
      "promptId": "lifecycle.archived-product.interview-all.archival-ready.v1"
    }
  ]
}
---

| Domain | Input | Interview mode | Target | Output |
|---|---|---|---|---|
| Lifecycle | candidate workspace + validation/readiness output + release notes | interview-medium-stakes | production-ready | release-readiness gap report, blocking questions, approval register |
| Lifecycle | shipped product spec + release history + support notes | interview-high-stakes | maintenance-ready | maintenance interview questions, maintenance gaps, support handoff gaps |
| Lifecycle | retiring product spec + operations/data/support/platform notes | interview-all | decommission-ready | decommissioning questions, decommission gaps, archival follow-up items |
| Lifecycle | retired product spec + final manifests + license/support/archive notes | interview-all | archival-ready | archival questions, archive manifest gaps, evidence gap register |
