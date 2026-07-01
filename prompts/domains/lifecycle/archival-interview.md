---
{
  "id": "lifecycle.archived-product.interview-all.archival-ready.v1",
  "name": "Archived Product Archival Readiness Interview",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "lifecycle",
  "interviewMode": "interview-all",
  "targetReadiness": "archival-ready",
  "inputTypes": [
    "retired-product-spec",
    "final-build-manifest",
    "source-archive-manifest",
    "asset-archive-manifest",
    "license-review-notes",
    "support-handoff-notes"
  ],
  "outputs": [
    "archival-readiness-interview-questions",
    "archive-manifest-gap-report",
    "evidence-gap-register",
    "human-approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "common.output-contract.v1",
    "interview.all.v1",
    "target.archival-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Interview-all workflow for archival readiness without fabricating final archive, license, data-retention, or support completion claims."
}
---

Interview for archival readiness of a retired product, software system, game,
service, or shared library.

Ask about:

1. Final source, build, package, configuration, and asset manifests.
2. Artifact hashes, storage locations, retention policies, and archive owner.
3. License, third-party asset, dependency, and commercial rights review.
4. Data retention, deletion, anonymization, or export evidence.
5. Support handoff, historical support notes, and post-retirement contacts.
6. Documentation, runbooks, release notes, known issues, and final decisions.
7. Telemetry, analytics, dashboards, monitoring, and alert shutdown evidence.
8. Store delisting, package registry state, domain ownership, and platform
   distribution status.
9. Legal, compliance, privacy, finance, and business approvals.
10. Evidence records required before any archival-ready claim.

Classify every answer as human-provided, AI-inferred, AI-defaulted,
AI-suggested, unresolved, or human-approval-required. Do not claim archival
completion, commercial clearance, legal approval, data-retention compliance,
support completion, or final artifact integrity unless provided evidence and
human approval support it.
