# Policy-Lint Trend JSON Schema

`schemas/policy-lint-trend-report.schema.json` documents the machine-readable
shape emitted by:

```bash
verityfoundry report policy-lint-trend --format json
```

The report compares current decision-policy lint findings with checked
snapshots under `snapshots/policy-lint/`.

## Stable Fields

Downstream tooling should prefer these fields:

- `status`
- `snapshotCount`
- `current.errorCount`
- `current.warningCount`
- `current.issueCodeCounts`
- `latestSnapshot.label`
- `deltaFromLatest.warningCount`

Policy-lint trend output is a release-review aid. It is not a VeritySpec
workspace validation result.
