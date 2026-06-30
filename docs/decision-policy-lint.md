# Decision Policy Lint

Decision-policy linting checks prompt manifests for high-stakes
invention-risk controls.

Run it with:

```bash
verityfoundry lint decision-policy
verityfoundry lint decision-policy --format json
```

The linter reports blocking `error` findings and non-blocking `warning`
advisories. Warning-only output exits successfully so release reviewers can
track advisory gaps without blocking unrelated work.

The linter currently checks domain prompts for:

- decision policy references
- human approval requirements
- safety and uncertainty guidance for high-risk prompts
- provenance guidance for high-risk prompts
- matching interview-mode includes for `interview-high-stakes` and
  `interview-all` prompts
- advisory output-contract includes for consistent generated sections

High-risk prompts include prompts using high-stakes or all-question interview
modes, and prompts targeting production, operations, liveops, maintenance,
decommissioning, or archival readiness.

The linter is deterministic and does not call external AI APIs.

Policy-lint snapshots can be reviewed with:

```bash
verityfoundry report policy-lint-trend
verityfoundry report policy-lint-trend --format json
```

Snapshots track advisory drift without making advisory warnings blocking.
