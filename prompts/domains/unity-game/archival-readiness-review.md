---
{
  "id": "unity-game.shipped-docs.interview-all.archival-ready.v1",
  "name": "Unity Game Archival Readiness Review",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-all",
  "targetReadiness": "archival-ready",
  "inputTypes": [
    "shipped-game-docs",
    "archive-notes",
    "decommission-notes"
  ],
  "outputs": [
    "archive-gap-report",
    "decommission-questions",
    "human-approval-register"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "interview.all.v1",
    "target.decommission-ready.v1",
    "target.archival-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Full interview prompt for decommissioning and archival readiness."
}
---

Assess decommissioning and archival readiness. Identify required source,
build, asset, data-retention, support, communication, telemetry shutdown,
license, evidence, and archive-location records. Do not invent final artifact
hashes or completion evidence.
