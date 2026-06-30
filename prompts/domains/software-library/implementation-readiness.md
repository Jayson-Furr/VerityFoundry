---
{
  "id": "software-library.workspace.interview-medium.implementation-ready-review.v1",
  "name": "Software Library Implementation Readiness Review",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "software-library",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "candidate-library-spec",
    "validation-output"
  ],
  "outputs": [
    "implementation-gap-report",
    "next-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "target.implementation-ready.v1",
    "common.safety-and-uncertainty.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Review implementation readiness without certifying final release readiness."
}
---

Review whether the candidate software-library spec can guide implementation.
Identify missing API details, compatibility risks, versioning gaps, test
expectations, documentation gaps, and approval requirements.
