---
{
  "id": "interview.high-stakes.v1",
  "name": "Interview High Stakes",
  "version": "0.1.0",
  "kind": "interview-mode",
  "domain": "common",
  "interviewMode": "interview-high-stakes",
  "targetReadiness": "not-applicable",
  "inputTypes": [
    "provided-inputs",
    "high-impact-human-answers"
  ],
  "outputs": [
    "candidate-workspace-outline",
    "human-approval-register",
    "high-stakes-gaps"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "High-impact mode for legal, financial, privacy, compliance, platform, monetization, and liveops decisions."
}
---

Ask before making decisions that affect legal, financial, safety, privacy,
compliance, platform certification, monetization, player data, liveops, or
decommissioning. Do not fabricate sensitive commitments.
