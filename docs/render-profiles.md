# Render Profiles

Render profiles add deterministic agent handoff guidance to rendered prompts.
They do not call external AI APIs and do not change the underlying prompt
workflow.

List available profiles:

```bash
verityfoundry list profiles
```

Render a prompt for a specific agent surface:

```bash
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile codex
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile claude-code
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile chatgpt
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile gemini
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile unity-ai
```

Supported profiles:

- `default`
- `codex`
- `claude-code`
- `chatgpt`
- `gemini`
- `unity-ai`

Use render profiles when handing a VerityFoundry prompt to a specific AI agent
or coding-agent surface. Generated outputs remain candidate drafts and still
require VeritySpec validation and human review.
