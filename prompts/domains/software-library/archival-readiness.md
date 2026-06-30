---
{
  "id": "software-library.workspace.interview-all.archival-ready.v1",
  "name": "Software Library Archival Readiness",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "software-library",
  "interviewMode": "interview-all",
  "targetReadiness": "archival-ready",
  "inputTypes": [
    "library-spec",
    "archive-notes"
  ],
  "outputs": [
    "archive-gap-report",
    "deprecation-questions",
    "human-approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "interview.all.v1",
    "target.archival-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Archival review for software libraries."
}
---

Review archival readiness for a software library. Identify final source,
release artifacts, package registry state, license review, documentation,
consumer migration, deprecation notices, and support handoff gaps.
