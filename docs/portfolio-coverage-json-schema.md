# Portfolio Coverage JSON Schema

`schemas/portfolio-coverage-report.schema.json` documents the machine-readable
shape emitted by:

```bash
verityfoundry report portfolio-coverage --format json
```

The schema is intended for release-review tooling that needs to inspect
portfolio fixture coverage, dependency assumptions, and cross-workspace
reference counts without parsing the human-readable report.

## Stable Fields

Downstream tooling should prefer these fields:

- `portfolioExampleCount`
- `gameConceptCount`
- `dependencyAssumptionCount`
- `crossWorkspaceReferenceCount`
- `coverageGapCount`
- `examples[].exampleId`
- `examples[].gameConcepts`
- `examples[].dependencyAssumptions`
- `examples[].coverageGaps`
- `examples[].gameConceptGroups`

Dependency assumptions remain candidate authoring outputs. A
`workspace.cross-reference` entry in this report is not a resolved VeritySpec
dependency graph edge.

## Review Use

Use this schema when checking that portfolio examples preserve:

- game concept coverage
- shared library dependency assumptions
- unresolved version and exported-record decisions
- cross-workspace reference counts
- readiness or coverage gaps

For product-contract authority, convert the fixture into a VeritySpec
workspace and run VeritySpec validation, graph, and readiness checks.
