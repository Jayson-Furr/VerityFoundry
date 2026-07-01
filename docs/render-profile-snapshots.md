# Render-Profile Snapshots

Render-profile snapshots are checked rendered prompts for a stable workflow
and every supported render profile.

Current snapshots live under:

```text
snapshots/render-profiles/
```

They render:

```text
unity-game.gdd-art.interview-medium.implementation-ready.v1
```

for these profiles:

- `default`
- `codex`
- `claude-code`
- `chatgpt`
- `gemini`
- `github-copilot`
- `unity-ai`

## Review Use

Use these snapshots to inspect how agent handoff context differs by profile.
They are deterministic release-review fixtures. They do not call external AI
APIs and do not certify generated VeritySpec workspace readiness.

When render-profile guidance changes intentionally, update the snapshots and
tests in the same sprint.
