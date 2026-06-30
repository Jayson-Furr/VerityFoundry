---
{
  "id": "unity-game.concept-art.interview-low.prototype-ready.v1",
  "name": "Unity Game Concept Art Analysis",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-low-stakes",
  "targetReadiness": "prototype-ready",
  "inputTypes": [
    "concept-art-images",
    "image-notes"
  ],
  "outputs": [
    "asset-record-candidates",
    "visual-tags",
    "art-direction-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Treat image interpretation as interpretation, not objective truth."
}
---

Analyze concept art or image notes as interpretive source material. Suggest
asset records, subjects, style tags, possible gameplay implications, and art
direction questions. Do not claim ownership, licensing rights, brand approval,
accessibility compliance, or commercial clearance unless provided.
