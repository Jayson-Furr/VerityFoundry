---
{
  "id": "interview.medium-stakes.v1",
  "name": "Interview Medium Stakes",
  "version": "0.1.0",
  "kind": "interview-mode",
  "domain": "common",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "not-applicable",
  "inputTypes": [
    "provided-inputs",
    "implementation-answers"
  ],
  "outputs": [
    "candidate-workspace-outline",
    "implementation-questions",
    "agent-context"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Architecture and implementation handoff mode."
}
---

Ask questions that affect architecture, implementation, telemetry, production,
or team handoff. Clarify save model, platforms, liveops expectations,
telemetry, content pipeline, shared systems, release milestone, and ownership.
