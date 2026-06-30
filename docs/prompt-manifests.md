# Prompt Manifests

Prompt files use JSON front matter:

```markdown
---
{
  "id": "unity-game.gdd-art.interview-medium.implementation-ready.v1",
  "name": "Unity Game GDD and Art to Implementation-Ready Workspace",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "unity-game",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": ["rough-gdd"],
  "outputs": ["candidate-verityspec-workspace"],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": ["common.verityspec-context.v1"],
  "requiresHumanApproval": true,
  "notes": "Preserve uncertainty."
}
---
```

Prompt IDs are stable. Use a new `.vN` suffix for breaking prompt behavior.

Validate manifests with:

```bash
verityfoundry validate prompts
```

Golden output manifests use `schemas/golden-output.schema.json` and can be
validated with:

```bash
verityfoundry validate goldens
```
