# Using With GitHub Copilot

Use rendered VerityFoundry prompts to give Copilot bounded authoring context
for candidate VeritySpec workspaces. Keep prompts focused on source material,
assumptions, unresolved questions, and readiness gaps.

Copilot repository guidance lives in `.github/copilot-instructions.md`, which
points back to the canonical `AGENTS.md` entry point.

Use the Codex-oriented render profile as the nearest current coding-agent
handoff profile until a dedicated Copilot profile is added:

```bash
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile codex
```
