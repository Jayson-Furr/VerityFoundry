---
{
  "id": "lifecycle.workspace.interview-medium.production-ready.release-gap-review.v1",
  "name": "Release Readiness Gap Review",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "lifecycle",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "production-ready",
  "inputTypes": [
    "candidate-verityspec-workspace",
    "verity-validation-output",
    "verity-readiness-output",
    "release-notes-draft"
  ],
  "outputs": [
    "release-readiness-gap-report",
    "blocking-questions",
    "approval-register",
    "verityspec-validation-loop"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "common.output-contract.v1",
    "interview.medium-stakes.v1",
    "target.production-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Review generated workspace release gaps without certifying release readiness."
}
---

Review a candidate VeritySpec workspace, validation output, readiness output,
and release notes draft for release-readiness gaps.

Preserve uncertainty. Treat VerityFoundry as the gap-review and interview
layer only. VeritySpec validation, VeritySpec readiness gates, CI evidence,
and human approval remain the release authorities.

Produce:

1. Release-readiness summary.
2. Blocking gaps.
3. Non-blocking gaps.
4. Missing or unresolved VeritySpec records.
5. Missing evidence, QA, docs, support, telemetry, rollback, or ownership.
6. Human-provided decisions.
7. AI-inferred decisions.
8. AI-defaulted decisions.
9. AI-suggested decisions.
10. Unresolved decisions.
11. Human approval requirements.
12. Recommended VeritySpec validation loop.

Do not claim the workspace is release-ready unless VeritySpec readiness output,
CI evidence, release evidence, and explicit human approval support that claim.
