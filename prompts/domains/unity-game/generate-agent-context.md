---
{
  "id": "unity-game.workspace.interview-medium.implementation-ready.agent-context.v1",
  "name": "Unity Game Agent Context Generation",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "candidate-verityspec-workspace",
    "readiness-gaps"
  ],
  "outputs": [
    "agent-context",
    "implementation-constraints",
    "validation-loop"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.output-contract.v1",
    "target.implementation-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Create bounded implementation context for AI coding agents."
}
---

Generate bounded implementation context for an AI coding agent or engineer.
Include relevant records, constraints, shared Unity runtime assumptions,
required artifacts, evidence expectations, readiness gates, files likely
affected, and records that should not drift. Keep unresolved decisions visible.
