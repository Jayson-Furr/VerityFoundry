# Report Schema Stability

VerityFoundry reports are deterministic local inspection aids. They are useful
for release reviewers and downstream tooling, but they are not VeritySpec
readiness certifications.

## Current Report Families

| Command | Purpose |
|---|---|
| `verityfoundry report prompt-quality --format json` | Prompt quality scoring for uncertainty and provenance evidence |
| `verityfoundry report prompt-quality-trend --format json` | Comparison against checked-in prompt quality snapshots |
| `verityfoundry report matrix-coverage --format json` | Domain prompt coverage across matrices |
| `verityfoundry report release-summary --format json` | Aggregate release-review summary across checks and inventories |
| `verityfoundry report golden-inventory --format json` | Golden output inventory |
| `verityfoundry report example-inventory --format json` | Example manifest inventory |
| `verityfoundry report fixture-inventory --format json` | Candidate workspace fixture inventory and kind mapping |
| `verityfoundry report provenance-coverage --format json` | Provenance coverage across fixture records |

## v0.x Compatibility Policy

For v0.x releases:

- Existing top-level JSON fields should not be renamed or removed casually.
- Existing field types should remain stable unless a changelog entry calls out
  the compatibility impact.
- New additive fields are allowed in minor releases.
- Text output is intended for humans and may change more freely than JSON
  output.
- Report values are deterministic for the checked-in repository state.
- Reports must not call external AI APIs.

## Release Review Expectations

When a report JSON shape changes, update:

- command tests
- README command examples, when affected
- this document
- changelog
- release notes during release preparation

If a downstream workflow depends on a report shape, prefer reading JSON output
and checking field presence instead of parsing human text.

## Authority Boundary

Reports explain repository and prompt-library state. They do not prove that a
generated VeritySpec workspace is valid, ready, compliant, approved, or
released. Use VeritySpec validation and readiness gates for product-contract
authority.
