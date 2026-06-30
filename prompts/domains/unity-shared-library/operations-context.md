---
{
  "id": "unity-library.full-package.interview-high.operations-ready.v1",
  "name": "Unity Shared Library Operations Context",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-shared-library",
  "interviewMode": "interview-high-stakes",
  "targetReadiness": "operations-ready",
  "inputTypes": [
    "library-workspace-outline",
    "release-process-notes",
    "consumer-games"
  ],
  "outputs": [
    "operations-gap-report",
    "consumer-impact-questions",
    "human-approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "interview.high-stakes.v1",
    "target.operations-ready.v1",
    "target.maintenance-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Operations prompt for shared runtime libraries used by multiple games."
}
---

Review operational expectations for a shared Unity library. Identify release,
versioning, compatibility, support, telemetry, deprecation, rollback,
consumer-impact, and maintenance gaps.
