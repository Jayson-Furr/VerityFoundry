---
{
  "id": "unity-game",
  "name": "Unity Game Prompt Matrix",
  "version": "0.1.0",
  "domain": "unity-game",
  "rows": [
    {
      "domain": "Unity game",
      "input": "name + short description",
      "interviewMode": "interview-none",
      "target": "concept-complete",
      "output": "rough workspace, assumptions, questions",
      "promptId": "unity-game.identity-images.interview-low.concept-complete.v1"
    },
    {
      "domain": "Unity game",
      "input": "GDD only",
      "interviewMode": "interview-low-stakes",
      "target": "design-complete",
      "output": "structured game records",
      "promptId": "unity-game.gdd.interview-low.design-complete.v1"
    },
    {
      "domain": "Unity game",
      "input": "GDD + concept art",
      "interviewMode": "interview-medium-stakes",
      "target": "prototype-ready",
      "output": "game, core, asset, and Unity record candidates",
      "promptId": "unity-game.concept-art.interview-low.prototype-ready.v1"
    },
    {
      "domain": "Unity game",
      "input": "GDD + art + platform goals",
      "interviewMode": "interview-medium-stakes",
      "target": "implementation-ready",
      "output": "feature, Unity, QA, telemetry, and agent-context records",
      "promptId": "unity-game.gdd-art.interview-medium.implementation-ready.v1"
    },
    {
      "domain": "Unity game",
      "input": "full design package",
      "interviewMode": "interview-high-stakes",
      "target": "operations-ready",
      "output": "release, liveops, monitoring, rollback, and approval gaps",
      "promptId": "unity-game.full-package.interview-high.operations-ready.v1"
    },
    {
      "domain": "Unity game",
      "input": "retiring product",
      "interviewMode": "interview-all",
      "target": "archival-ready",
      "output": "archive, decommission, data-retention, and evidence gaps",
      "promptId": "unity-game.shipped-docs.interview-all.archival-ready.v1"
    }
  ]
}
---

| Domain | Input | Interview mode | Target | Output |
|---|---|---|---|---|
| Unity game | name + short description | interview-none | concept-complete | rough workspace, assumptions, questions |
| Unity game | GDD only | interview-low-stakes | design-complete | structured game records |
| Unity game | GDD + concept art | interview-medium-stakes | prototype-ready | game, core, asset, and Unity record candidates |
| Unity game | GDD + art + platform goals | interview-medium-stakes | implementation-ready | feature, Unity, QA, telemetry, and agent-context records |
| Unity game | full design package | interview-high-stakes | operations-ready | release, liveops, monitoring, rollback, and approval gaps |
| Unity game | retiring product | interview-all | archival-ready | archive, decommission, data-retention, and evidence gaps |
