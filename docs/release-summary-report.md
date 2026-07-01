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
