---
{
  "id": "unity-game.identity-images.interview-low.concept-complete.v1",
  "name": "Unity Game Identity Image Analysis",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-low-stakes",
  "targetReadiness": "concept-complete",
  "inputTypes": [
    "identity-images",
    "brand-notes"
  ],
  "outputs": [
    "visual-identity-notes",
    "brand-tone",
    "approval-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Classify identity image implications without claiming brand approval."
}
---

Interpret identity images as inputs for visual identity records. Suggest brand
tone, color direction, logo usage assumptions, UI mood, store capsule needs,
and approval questions. Mark commercial clearance and licensing as unresolved
unless the input explicitly provides them.
