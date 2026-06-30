---
{
  "id": "unity-game.gdd.interview-low.design-complete.v1",
  "name": "Unity Game GDD Extraction",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-low-stakes",
  "targetReadiness": "design-complete",
  "inputTypes": [
    "rough-gdd"
  ],
  "outputs": [
    "structured-design-records",
    "assumptions",
    "unresolved-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.provenance-rules.v1",
    "target.design-complete.v1",
    "interview.low-stakes.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Extract structured game design intent from a rough GDD."
}
---

Extract structured game design intent from the GDD. Identify product identity,
pitch, player fantasy, audience, loops, modes, systems, content categories,
telemetry questions, and design gaps. Preserve the GDD as source material and
do not treat inferred details as approved.
