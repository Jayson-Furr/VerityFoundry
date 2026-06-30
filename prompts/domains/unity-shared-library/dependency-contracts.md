---
{
  "id": "unity-library.dependencies.interview-medium.implementation-ready.v1",
  "name": "Unity Shared Library Dependency Contracts",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-shared-library",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "consumer-games",
    "package-dependencies",
    "capability-list"
  ],
  "outputs": [
    "dependency-contract-notes",
    "cross-workspace-assumptions",
    "compatibility-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.provenance-rules.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Prepares future cross-workspace dependency assumptions."
}
---

Identify candidate dependency contracts between a shared Unity runtime and
consumer game workspaces. Mark cross-workspace references, exported records,
version ranges, and lockfile behavior as assumptions until VeritySpec supports
them directly.
