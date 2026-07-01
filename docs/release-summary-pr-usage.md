# Release Summary in Pull Requests

Use release-summary output in PR descriptions when a change affects prompt
coverage, report shape, release checks, fixtures, snapshots, or package data.

Recommended PR section:

```markdown
## Release Review

- `verityfoundry report release-summary`: passed
- Blocking issues: 0
- Warnings: 14
- Matrix coverage: 88.5%
- Golden outputs: 6
- Provenance coverage: 100.0% records

Authority boundary: this report summarizes VerityFoundry repository state. Any
generated VeritySpec workspace still needs `verity validate`, `verity lint`,
`verity readiness`, and human review.
```

For JSON-driven PR tooling, prefer:

```bash
verityfoundry report release-summary --format json
```

Do not paste long JSON into normal PR bodies unless a reviewer asks for it.
Link to checked snapshots or CI artifacts instead.
