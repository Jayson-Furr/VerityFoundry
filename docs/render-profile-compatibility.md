# Render Profile Compatibility

Render profiles add deterministic agent handoff guidance for supported AI
agent surfaces. They do not alter prompt manifests or call external AI APIs.

## Supported Profiles

| Profile | Intended surface | Notes |
|---|---|---|
| `default` | Generic prompt rendering | No agent-specific handoff block |
| `codex` | Codex | Repository-agent workflow guidance |
| `claude-code` | Claude Code | Repository-agent workflow guidance |
| `chatgpt` | ChatGPT | Human-operated prompt handoff |
| `gemini` | Gemini | Human-operated prompt handoff |
| `github-copilot` | GitHub Copilot | Coding assistant handoff guidance |
| `unity-ai` | Unity AI | Unity/game workflow handoff guidance |

## Compatibility Expectations

Every non-default profile should preserve:

- VerityFoundry project identity
- prompt manifest content
- safety and uncertainty guidance
- provenance guidance
- human approval requirements
- VeritySpec validation authority

Profiles may add agent-specific handoff language, but they should not rewrite
the prompt workflow's decisions or remove uncertainty controls.

## Smoke Check

Render a prompt with each supported profile before release-impacting changes:

```bash
verityfoundry list profiles
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile codex
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile github-copilot
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile unity-ai
```

Future smoke tests may render every profile to files and compare stable
sections.
