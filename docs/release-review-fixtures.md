# Release-Review Fixtures

Release-review fixtures are checked JSON examples of deterministic report
output. They help reviewers and downstream tools understand report shape
without running external AI APIs.

Current fixtures live under:

```text
fixtures/release-review/current/
```

The current fixture set includes:

- `golden-inventory.json`
- `matrix-coverage.json`
- `portfolio-coverage.json`
- `provenance-distribution.json`

These fixtures are generated from local report functions and tested against
current report output. If a report shape or count changes intentionally,
update the fixture in the same sprint as the code, tests, README, changelog,
and roadmap.

## Boundary

Release-review fixtures describe VerityFoundry repository state. They are not
VeritySpec validation results, product-contract readiness certificates, or
human approval records.

Generated VeritySpec workspaces still require:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

## Packaging

Release-review fixtures are included in package data so installed-wheel smoke
tests and downstream review tooling can inspect them outside a source
checkout.
