---
{
  "id": "unity-game.gdd-art.interview-medium.implementation-ready.v1",
  "name": "Unity Game GDD and Art to Implementation-Ready Workspace",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "name",
    "short-description",
    "rough-gdd",
    "concept-art-images",
    "identity-images",
    "target-platforms",
    "unity-version"
  ],
  "outputs": [
    "candidate-verityspec-workspace",
    "assumptions",
    "unresolved-questions",
    "readiness-gap-report",
    "agent-context"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "common.output-contract.v1",
    "target.implementation-ready.v1",
    "interview.medium-stakes.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Preserve uncertainty and avoid high-stakes invention while drafting Unity game workspace records."
}
---

Create a candidate VeritySpec workspace outline for a Unity game from the
provided GDD and art notes.

Include candidate records for game identity, GDD source, visual identity,
concept art, core loop, session loop, progression loop, game modes, features,
Unity project assumptions, Unity package dependencies, shared runtime
assumptions, telemetry intent, QA gaps, implementation context, and readiness
gaps.

Ask or mark unresolved any production platform, save model, multiplayer,
telemetry, content pipeline, monetization, liveops, legal, licensing,
certification, privacy, or archival decision that is not provided.
