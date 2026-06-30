---
{
  "id": "unity-game.full-package.interview-high.operations-ready.v1",
  "name": "Unity Game Operations Readiness Review",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-high-stakes",
  "targetReadiness": "operations-ready",
  "inputTypes": [
    "candidate-verityspec-workspace",
    "release-notes",
    "operations-notes"
  ],
  "outputs": [
    "operations-gap-report",
    "human-approval-register",
    "rollback-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "interview.high-stakes.v1",
    "target.operations-ready.v1",
    "target.liveops-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "High-stakes operations review for Unity game workspaces."
}
---

Review operations readiness for monitoring, rollback, support, liveops,
feature flags, telemetry, patch notes, known issues, customer communication,
platform constraints, and incident response. Do not fabricate approvals.
