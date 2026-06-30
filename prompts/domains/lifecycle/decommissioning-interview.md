---
{
  "id": "lifecycle.retiring-product.interview-all.decommission-ready.v1",
  "name": "Retiring Product Decommissioning Interview",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "lifecycle",
  "interviewMode": "interview-all",
  "targetReadiness": "decommission-ready",
  "inputTypes": [
    "retiring-product-spec",
    "operations-notes",
    "data-retention-notes",
    "support-notes",
    "platform-distribution-notes"
  ],
  "outputs": [
    "decommissioning-interview-questions",
    "decommission-readiness-gap-report",
    "human-approval-register",
    "archive-follow-up-items"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "common.output-contract.v1",
    "interview.all.v1",
    "target.decommission-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Interview-all workflow for decommissioning without fabricating legal, privacy, or archival completion claims."
}
---

Interview for decommissioning readiness of a retiring product, software system,
game, service, or shared library.

Ask about:

1. Shutdown scope and final operating date.
2. User, customer, player, partner, and support communication.
3. Data retention, deletion, export, and privacy obligations.
4. Store delisting, package deprecation, platform removal, or service shutdown.
5. Telemetry, analytics, monitoring, alerting, and dashboard shutdown.
6. Rollback or reactivation policy.
7. Final build, source, artifact, configuration, and asset preservation.
8. Support handoff and post-shutdown contact ownership.
9. Legal, compliance, license, and financial approval needs.
10. Archival follow-up needed after decommissioning.

Classify every answer as human-provided, AI-inferred, AI-defaulted,
AI-suggested, unresolved, or human-approval-required. Do not claim legal
clearance, privacy completion, data deletion, platform approval, customer
notification, or archival completion unless provided evidence supports it.
