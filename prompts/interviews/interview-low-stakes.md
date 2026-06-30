---
{
  "id": "interview.low-stakes.v1",
  "name": "Interview Low Stakes",
  "version": "0.1.0",
  "kind": "interview-mode",
  "domain": "common",
  "interviewMode": "interview-low-stakes",
  "targetReadiness": "not-applicable",
  "inputTypes": [
    "provided-inputs",
    "short-human-answers"
  ],
  "outputs": [
    "candidate-draft",
    "high-value-questions",
    "readiness-gaps"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Small question set for prototype planning and first-pass workspace generation."
}
---

Ask a small number of high-value questions. Prefer questions that clarify the
primary platform, core loop, player mode, prototype scope, and shared runtime
assumptions. Keep unresolved production and high-stakes decisions explicit.
