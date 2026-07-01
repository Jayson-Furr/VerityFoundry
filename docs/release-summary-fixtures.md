# Release Summary Fixtures

Release-summary fixtures are checked historical snapshots of:

```bash
verityfoundry report release-summary --format json
```

Current snapshots live under:

```text
snapshots/release-summary/
```

The first snapshot is:

- `v0.20.0.json`

## Why Historical Snapshots

Release-summary output includes the active package version and release tag.
For that reason, snapshots are historical baselines instead of `current`
fixtures. A future release branch can bump the package version without having
to rewrite an old snapshot.

Use these snapshots to compare release-review movement over time:

- prompt count
- prompt quality percentages
- matrix coverage
- golden output count
- fixture inventory counts
- provenance coverage
- portfolio coverage
- warning counts

## Update Rule

When cutting a release that intentionally changes release-summary shape or
meaningful release-review counts, add a new `vX.Y.Z.json` snapshot after the
release branch has updated the package version.

Do not remove older snapshots unless there is a documented retention reason.
