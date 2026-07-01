# Release-Review Bundle Export

VerityFoundry does not yet provide a dedicated bundle export command. Until it
does, a release-review bundle can be assembled from deterministic local
commands.

## Suggested Bundle Contents

```text
release-summary.json
prompt-quality.json
prompt-quality-trend.json
policy-lint-trend.json
matrix-coverage.json
golden-inventory.json
example-inventory.json
fixture-inventory.json
provenance-coverage.json
provenance-distribution.json
portfolio-coverage.json
```

## Manual Export

```bash
mkdir -p build/release-review
verityfoundry report release-summary --format json > build/release-review/release-summary.json
verityfoundry report prompt-quality --format json > build/release-review/prompt-quality.json
verityfoundry report prompt-quality-trend --format json > build/release-review/prompt-quality-trend.json
verityfoundry report policy-lint-trend --format json > build/release-review/policy-lint-trend.json
verityfoundry report matrix-coverage --format json > build/release-review/matrix-coverage.json
verityfoundry report golden-inventory --format json > build/release-review/golden-inventory.json
verityfoundry report example-inventory --format json > build/release-review/example-inventory.json
verityfoundry report fixture-inventory --format json > build/release-review/fixture-inventory.json
verityfoundry report provenance-coverage --format json > build/release-review/provenance-coverage.json
verityfoundry report provenance-distribution --format json > build/release-review/provenance-distribution.json
verityfoundry report portfolio-coverage --format json > build/release-review/portfolio-coverage.json
```

## Future CLI Shape

A future command could be:

```bash
verityfoundry export release-review-bundle --out build/release-review
```

That command should remain deterministic, local-only, and free of external AI
API calls. It should not claim VeritySpec readiness authority.
