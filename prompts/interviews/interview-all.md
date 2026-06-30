---
{
  "id": "interview.all.v1",
  "name": "Interview All",
  "version": "0.1.0",
  "kind": "interview-mode",
  "domain": "common",
  "interviewMode": "interview-all",
  "targetReadiness": "not-applicable",
  "inputTypes": [
    "provided-inputs",
    "complete-human-answers"
  ],
  "outputs": [
    "complete-question-set",
    "candidate-workspace-outline",
    "approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Full interview mode for formal completion, decommissioning, and archival planning."
}
---

Ask everything required to minimize assumptions. Use this mode for formal
design completion, production milestone planning, decommissioning, and archival
planning. Prefer unresolved decisions over unsupported invention.
