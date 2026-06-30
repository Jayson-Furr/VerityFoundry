---
{
  "id": "unity-library.full-package.interview-all.archival-ready.v1",
  "name": "Unity Shared Library Archival Context",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-shared-library",
  "interviewMode": "interview-all",
  "targetReadiness": "archival-ready",
  "inputTypes": [
    "library-docs",
    "archive-notes",
    "consumer-impact-notes"
  ],
  "outputs": [
    "archive-gap-report",
    "consumer-handoff-questions",
    "human-approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "interview.all.v1",
    "target.archival-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Archival prompt for shared libraries with consumer impact."
}
---

Assess archive readiness for a shared Unity library. Identify source,
package, documentation, release artifact, license, consumer migration, and
support-handoff gaps. Do not invent artifact hashes or final approvals.
