# Golden Output Guidelines

Golden outputs should be deterministic examples of expected prompt behavior.
They should not call external AI APIs in tests or CI.

Good golden outputs include:

- Source summary.
- Candidate workspace outline.
- Assumptions.
- AI-inferred decisions.
- AI-defaulted decisions.
- Unresolved questions.
- Human approval requirements.
- Readiness gaps.
- Suggested VeritySpec validation commands.

Do not create golden outputs that imply AI-generated records are final truth.

Current checked fixtures include:

- Unity game implementation-ready output for Dream Extraction.
- Unity shared-library implementation-ready output for Shared Unity Runtime.

## Manifest Contract

Each golden output should include a `manifest.json` with:

- stable golden ID
- prompt reference
- example reference
- interview mode
- target readiness
- output path
- required section headings
- notes explaining the review purpose

Validate golden outputs with:

```bash
verityfoundry validate goldens
```
