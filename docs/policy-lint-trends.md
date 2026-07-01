# Policy Lint Trends

`verityfoundry report policy-lint-trend` compares current decision-policy lint
counts with checked-in snapshots.

Run:

```bash
verityfoundry report policy-lint-trend
verityfoundry report policy-lint-trend --format json
```

The JSON report shape is documented in
[Policy-lint trend JSON schema](policy-lint-trend-json-schema.md).

Snapshots live in:

```text
snapshots/policy-lint/
```

The first snapshot is `v0.17.0`, captured after the release-summary report was
added. The snapshot records the current warning baseline without converting
advisory output-contract warnings into release blockers.

Policy-lint trend reports are release-review aids. They help reviewers see
whether advisory warning counts increased, decreased, or stayed flat. They do
not replace human review, prompt inspection, or VeritySpec validation.
