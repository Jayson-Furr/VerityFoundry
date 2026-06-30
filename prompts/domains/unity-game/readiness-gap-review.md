---
{
  "id": "unity-game.workspace.interview-medium.readiness-gap-review.v1",
  "name": "Unity Game Readiness Gap Review",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "candidate-verityspec-workspace",
    "verity-validation-output"
  ],
  "outputs": [
    "readiness-gap-report",
    "next-questions",
    "human-approval-items"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.output-contract.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Review candidate workspace gaps without certifying final readiness."
}
---

Review the candidate workspace and VeritySpec validation output. Identify
structural gaps, semantic gaps, readiness gaps, missing evidence, unresolved
decisions, and questions that should be asked before implementation.
