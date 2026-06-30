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
