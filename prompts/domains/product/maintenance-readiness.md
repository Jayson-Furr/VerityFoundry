---
{
  "id": "product.workspace.interview-high.maintenance-ready.v1",
  "name": "Product Maintenance Readiness Review",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "product",
  "interviewMode": "interview-high-stakes",
  "targetReadiness": "maintenance-ready",
  "inputTypes": [
    "product-spec",
    "support-notes",
    "release-history"
  ],
  "outputs": [
    "maintenance-gap-report",
    "support-handoff-questions",
    "approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "interview.high-stakes.v1",
    "target.maintenance-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Maintenance readiness review for product workspaces."
}
---

Review maintenance readiness for shipped products. Identify patch process,
support ownership, telemetry watchlists, dependency updates, customer
communication, known issue handling, security patching, and unresolved
approval requirements.
