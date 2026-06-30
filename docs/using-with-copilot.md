# Using With GitHub Copilot

Use rendered VerityFoundry prompts to give Copilot bounded authoring context
for candidate VeritySpec workspaces. Keep prompts focused on source material,
assumptions, unresolved questions, and readiness gaps.

Copilot repository guidance lives in `.github/copilot-instructions.md`, which
points back to the canonical `AGENTS.md` entry point.

Use the dedicated GitHub Copilot render profile for Copilot-assisted authoring
or repository edits:

```bash
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile github-copilot
```

Generated output remains candidate authoring context. It still needs
VeritySpec validation, local repository checks, and human review for
high-stakes decisions.
