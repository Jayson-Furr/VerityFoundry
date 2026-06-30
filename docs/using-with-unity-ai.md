# Using With Unity AI

Unity AI workflows should use VerityFoundry prompts to structure rough Unity
game and shared-library inputs before implementation.

Prompts should preserve:

- Unity version assumptions
- package dependency assumptions
- shared runtime assumptions
- scene, prefab, ScriptableObject, addressables, input, save, and telemetry
  gaps
- licensing and approval unknowns

Run VeritySpec validation after a candidate workspace is produced.

Recommended render command:

```bash
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile unity-ai
```
