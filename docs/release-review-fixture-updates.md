# Release-Review Fixture Updates

Use this process when a release-review fixture or snapshot changes because a
report, example, golden output, or workspace fixture changed intentionally.

## Current Fixtures

Current release-review fixtures live under:

```text
fixtures/release-review/current/
```

They are expected to match current deterministic report output.

Regenerate them with the matching report commands:

```bash
verityfoundry report golden-inventory --format json > fixtures/release-review/current/golden-inventory.json
verityfoundry report matrix-coverage --format json > fixtures/release-review/current/matrix-coverage.json
verityfoundry report portfolio-coverage --format json > fixtures/release-review/current/portfolio-coverage.json
verityfoundry report provenance-distribution --format json > fixtures/release-review/current/provenance-distribution.json
```

Then run:

```bash
python -m unittest tests.test_release_review_fixtures -v
python -m unittest tests.test_release_review_snapshots -v
```

## Snapshots

Snapshots under `snapshots/` are historical or baseline references. Do not
overwrite them casually.

Add a new snapshot when reviewers need release-to-release context that current
fixtures cannot provide.

Examples:

```bash
verityfoundry report portfolio-coverage --format json > snapshots/portfolio-coverage/<label>.json
```

For cross-workspace reference snapshots, derive the snapshot from the source
candidate workspace fixture and preserve `snapshotLabel`, `sourceFixture`,
`exampleId`, `recordCount`, and `records`.

## Review Checklist

Before merging fixture changes, confirm:

- the report command is deterministic
- generated JSON is sorted or stable enough for review
- schema docs are updated when fields change
- package-data tests include the changed files
- release-review docs explain the authority boundary
- changelog and roadmap mention the fixture update
- VeritySpec validation remains the final product-contract authority
- human approval requirements remain visible when fixture content includes
  candidate workspace or provenance decisions
