# CI Artifact Naming

Release-review bundles and report snapshots should use predictable artifact
names so humans and agents can find them in GitHub Actions.

## Suggested Pattern

Use names that include project, purpose, event, and ref:

```text
verityfoundry-release-review-<event>-<ref>
```

Examples:

```text
verityfoundry-release-review-pr-92
verityfoundry-release-review-main-abc4075
verityfoundry-release-review-tag-v0.24.0
```

For file names inside a bundle, prefer stable report names:

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

## Review Rule

Artifact names should not include secrets, private product names, private
customer names, or local machine paths.

CI artifacts are release-review aids. They do not replace VeritySpec
validation, human approval, GitHub release assets, or durable project records.
