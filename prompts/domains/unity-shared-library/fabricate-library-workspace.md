---
{
  "id": "unity-library.description.interview-medium.implementation-ready.v1",
  "name": "Unity Shared Library Workspace Fabrication",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-shared-library",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "library-name",
    "short-description",
    "readme",
    "unity-package-notes",
    "shared-systems"
  ],
  "outputs": [
    "library-workspace-outline",
    "unity-package-records",
    "capability-records",
    "readiness-gaps"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "target.implementation-ready.v1",
    "interview.medium-stakes.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Draft a shared Unity library VeritySpec workspace without inventing compatibility guarantees."
}
---

Create a candidate VeritySpec workspace outline for a shared Unity library.
Include product identity, Unity package records, capabilities, dependency
contracts, consumer-facing notes, target Unity version assumptions, version
compatibility gaps, implementation gaps, and evidence requirements.
