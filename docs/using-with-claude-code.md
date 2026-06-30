# Using With Claude Code

Use rendered prompts as bounded task context for candidate VeritySpec workspace
authoring. Keep uncertainty and human approval requirements explicit.

Claude Code repository work should follow `AGENTS.md`; agent-specific adapter
files must remain thin pointers to that canonical entry point.

Recommended render command:

```bash
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile claude-code
```
