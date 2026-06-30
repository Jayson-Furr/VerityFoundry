---
{
  "id": "lifecycle.shipped-product.interview-high.maintenance-ready.v1",
  "name": "Shipped Product Maintenance Interview",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "lifecycle",
  "interviewMode": "interview-high-stakes",
  "targetReadiness": "maintenance-ready",
  "inputTypes": [
    "shipped-product-spec",
    "release-history",
    "support-notes",
    "telemetry-summary",
    "dependency-list"
  ],
  "outputs": [
    "maintenance-interview-questions",
    "maintenance-readiness-gap-report",
    "support-handoff-gaps",
    "approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "common.output-contract.v1",
    "interview.high-stakes.v1",
    "target.maintenance-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Interview for shipped-product maintenance readiness without inventing operational commitments."
}
---

Interview for shipped-product maintenance readiness. The goal is to identify
which product-contract records, evidence, owners, and human approvals are still
needed before a workspace can honestly support ongoing maintenance.

Ask about:

1. Patch ownership and escalation paths.
2. Dependency update policy and shared-library impact review.
3. Security patch policy.
4. Known issue triage.
5. Customer or player support ownership.
6. Telemetry, crash, error, and support watchlists.
7. Rollback, hotfix, and release communication process.
8. Platform, compliance, privacy, and data-retention obligations.
9. Documentation, support notes, and runbooks.
10. Evidence required for maintenance readiness.

Mark unknowns as unresolved. Do not invent support commitments, security
claims, compliance coverage, privacy posture, service-level promises, or
platform obligations.
