# Portfolio Coverage Report

`verityfoundry report portfolio-coverage` summarizes portfolio example fixture
coverage by game concept and dependency assumption.

```bash
verityfoundry report portfolio-coverage
verityfoundry report portfolio-coverage --format json
```

The report currently inspects checked portfolio examples and counts:

- portfolio examples
- game concept records
- dependency assumption records
- cross-workspace reference records
- coverage-gap records
- per-game dependency and cross-reference groupings

Dependency assumption records include candidate future VeritySpec concepts
such as:

- `workspace.dependency`
- `workspace.cross-reference`
- `workspace.dependency-risk`
- `unity.package-dependency`
- `unity.exported-record-assumption`

The report is intentionally conservative. A dependency or cross-workspace
reference in a fixture is a candidate authoring assumption, not a resolved
VeritySpec dependency graph.

Human review is still required before any portfolio dependency assumption is
accepted as product truth.

Use it during portfolio review with:

```bash
verityfoundry report fixture-inventory
verityfoundry report portfolio-coverage
verityfoundry report provenance-distribution
```

For real workspace validation, convert the candidate fixture and run VeritySpec
validation and graph checks.
