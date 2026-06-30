---
{
  "id": "software-library.workspace.interview-high.maintenance-ready.v1",
  "name": "Software Library Maintenance Readiness",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "software-library",
  "interviewMode": "interview-high-stakes",
  "targetReadiness": "maintenance-ready",
  "inputTypes": [
    "library-spec",
    "release-process-notes",
    "support-notes"
  ],
  "outputs": [
    "maintenance-gap-report",
    "support-questions",
    "human-approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "interview.high-stakes.v1",
    "target.maintenance-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Maintenance review for shared software libraries."
}
---

Review maintenance readiness for support ownership, dependency updates,
deprecation policy, compatibility communication, security patching, evidence,
and release governance.
