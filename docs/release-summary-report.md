# Release Summary Report

`verityfoundry report release-summary` aggregates the repository's deterministic
release-review checks into one local report.

It does not call external AI APIs. It does not replace VeritySpec validation.
It is intended to help release reviewers see the current state before cutting
a release. Human review is still required for release decisions.

## Command

```bash
verityfoundry report release-summary
verityfoundry report release-summary --format json
```

The JSON form is described by
[`schemas/release-summary-report.schema.json`](../schemas/release-summary-report.schema.json)
and summarized in [Release summary JSON schema](release-summary-json-schema.md).

## Included Checks

The summary includes:

- release integrity
- quality thresholds
- workflow hygiene
- decision-policy lint error and warning counts
- prompt quality
- prompt quality trend
- policy-lint trend
- matrix coverage
- golden output inventory
- example inventory
- candidate workspace fixture inventory
- generated workspace validation-result snapshot coverage
- provenance coverage
- provenance distribution
- portfolio fixture coverage

Release integrity and workflow hygiene are source-checkout checks. When the
command is run against installed prompt artifacts that do not include
`pyproject.toml`, README, roadmap, changelog, release notes, or
`.github/workflows`, those checks are reported as `skipped` with zero blocking
issues.

## Status

The report status is `failed` when a blocking release-review check fails:

- release-integrity issue
- quality-threshold issue
- workflow-hygiene issue
- decision-policy lint error

Decision-policy warnings remain warnings. They are visible for review but do
not fail the summary.

Generated workspace validation-result coverage is currently summarized as a
report surface, not a blocking release check. Reviewers should investigate any
stale file hashes or uncovered fixture files before release.

## Boundary

The report summarizes VerityFoundry repository state. Generated VeritySpec
workspaces still need:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

Use this report as a release-review dashboard, not as a product-contract
readiness certificate.
