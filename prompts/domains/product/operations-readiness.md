---
{
  "id": "product.workspace.interview-high.operations-ready.v1",
  "name": "Product Operations Readiness Review",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "product",
  "interviewMode": "interview-high-stakes",
  "targetReadiness": "operations-ready",
  "inputTypes": [
    "product-spec",
    "operations-notes"
  ],
  "outputs": [
    "operations-gap-report",
    "approval-register",
    "support-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "interview.high-stakes.v1",
    "target.operations-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Operations readiness review for product workspaces."
}
---

Review operations readiness for ownership, support, monitoring, privacy,
security, rollback, customer communication, release governance, and unresolved
high-stakes commitments.
