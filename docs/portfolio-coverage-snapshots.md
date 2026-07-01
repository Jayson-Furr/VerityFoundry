# Portfolio Coverage Snapshots

Portfolio coverage snapshots are checked JSON captures of:

```bash
verityfoundry report portfolio-coverage --format json
```

Current snapshots live under:

```text
snapshots/portfolio-coverage/
```

The initial snapshot is:

```text
snapshots/portfolio-coverage/v0.22.0.json
```

It records the portfolio fixture state used by the v0.23.0 sprint, including:

- portfolio example count
- game concept count
- dependency assumption count
- cross-workspace reference count
- coverage-gap count
- per-game dependency and cross-reference groupings

## Boundary

Portfolio snapshots are release-review artifacts. They do not resolve
cross-workspace dependencies and they do not certify a VeritySpec workspace.

Records such as `workspace.dependency`, `workspace.cross-reference`, and
`unity.exported-record-assumption` remain candidate authoring assumptions until
VeritySpec validates the converted workspace.

## Updating

Update the snapshot when portfolio examples, fixture records, or portfolio
coverage report fields intentionally change.

Use:

```bash
verityfoundry report portfolio-coverage --format json > snapshots/portfolio-coverage/<label>.json
python -m unittest tests.test_release_review_snapshots -v
```

The label should identify the release or baseline that reviewers should use
for comparison.
