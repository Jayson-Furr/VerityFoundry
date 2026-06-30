---
{
  "id": "unity-library.context.interview-medium.implementation-ready.v1",
  "name": "Unity Shared Library Implementation Context",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-shared-library",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "library-workspace-outline",
    "consumer-contracts"
  ],
  "outputs": [
    "agent-context",
    "implementation-constraints",
    "validation-loop"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "target.implementation-ready.v1",
    "common.output-contract.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Create bounded implementation context for shared Unity library work."
}
---

Generate implementation context for a shared Unity library. Include package
boundaries, exported capabilities, consumer contracts, compatibility risks,
test evidence expectations, and unresolved release or support commitments.
