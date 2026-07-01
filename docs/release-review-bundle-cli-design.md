# Release-Review Bundle CLI Design

This is a design note for a future command. It is not implemented yet.

Potential command:

```bash
verityfoundry export release-review-bundle --out build/release-review
```

## Desired Behavior

The command should write deterministic JSON reports and selected checked
snapshot references into an output directory.

Initial bundle candidates:

- `release-summary.json`
- `prompt-quality.json`
- `prompt-quality-trend.json`
- `policy-lint-trend.json`
- `matrix-coverage.json`
- `golden-inventory.json`
- `example-inventory.json`
- `fixture-inventory.json`
- `provenance-coverage.json`
- `provenance-distribution.json`
- `portfolio-coverage.json`
- `manifest.json`

The manifest should follow the
[Release-review bundle manifest schema](release-review-bundle-manifest-schema.md)
and include planned or computed checksums for every artifact.

## Dry Run

The future dry-run mode is documented in
[Release-review bundle dry-run CLI design](release-review-bundle-dry-run-cli-design.md).
It should validate the manifest shape, list planned producer commands, and
avoid writing report artifacts.

## Non-Goals

- Do not call external AI APIs.
- Do not publish artifacts.
- Do not certify VeritySpec workspace readiness.
- Do not replace the GitHub release workflow.
- Do not replace human release review.

The command should be a convenience wrapper around existing deterministic
reports, not a new release authority.
