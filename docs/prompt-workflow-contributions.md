# Prompt Workflow Contributions

Prompt workflow contributions should preserve uncertainty, provenance, and
human approval requirements.

Every domain prompt should include:

- stable prompt ID with a `.vN` suffix
- JSON front matter that validates against `schemas/prompt-manifest.schema.json`
- decision policy reference
- clear input and output declarations
- human approval requirement
- unresolved-question behavior

High-risk prompts should also include:

- `common.safety-and-uncertainty.v1`
- `common.provenance-rules.v1`
- `interview.high-stakes.v1` for high-stakes prompts
- `interview.all.v1` for all-question prompts

High-risk work includes production, operations, liveops, maintenance,
decommissioning, archival, legal, privacy, certification, commercial,
licensing, player-data, or platform-approval commitments.

Before opening a PR, run:

```bash
verityfoundry validate prompts
verityfoundry lint decision-policy
verityfoundry report prompt-quality
verityfoundry report matrix-coverage
```

If a prompt adds a new domain workflow, update the relevant matrix, examples,
or roadmap entry so maintainers can track coverage.
