# Using With VeritySpec

VerityFoundry creates candidate authoring outputs. VeritySpec validates the
generated workspace.

Recommended loop:

```bash
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1
# Use the rendered prompt with an AI agent and source materials.
# Create or refine a candidate VeritySpec workspace.
verityfoundry check verityspec --workspace <generated-workspace>
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

`verityfoundry check verityspec` is an optional local smoke check. It exits
successfully with a `skipped` result when the `verity` CLI is not installed. If
`verity` is available and a workspace is provided or detected, it runs
`verity validate` against that workspace.

Do not treat a rendered prompt or generated draft as final authority. Human
review and VeritySpec checks are required.

## Candidate Workspace Fixtures

Some examples include `expected/candidate-workspace.json`. These files are
structured drafts that show the kind of VeritySpec workspace records an AI
workflow should produce. They are intentionally marked as candidate fixtures.

Use them as conversion guides:

```bash
verityfoundry validate examples
# Convert the candidate fixture into a real VeritySpec workspace directory.
verity validate <converted-workspace>
verity lint <converted-workspace> --strict
verity readiness <converted-workspace> --strict
```

Keep these distinctions intact during conversion:

- user-provided decisions
- AI-inferred decisions
- AI-suggested decisions
- unresolved decisions
- human-approval-required decisions

If the candidate fixture and VeritySpec disagree, VeritySpec wins.
