# Example Fixture Diff Snapshots

Example fixture diff snapshots are a release-review pattern for comparing
candidate workspace fixture shape across releases.

The current repository does not store full fixture diff snapshots yet. Until a
dedicated command exists, reviewers should use:

```bash
verityfoundry report example-inventory --format json
verityfoundry report fixture-inventory --format json
verityfoundry report provenance-coverage --format json
verityfoundry report provenance-distribution --format json
verityfoundry report portfolio-coverage --format json
```

Recommended comparison points:

- example count by domain
- fixture count by example
- record count by fixture
- record kind distribution
- recommended VeritySpec pack mappings
- provenance coverage
- decision-example coverage
- decision-source distribution
- portfolio dependency assumption counts
- cross-workspace reference counts

Diff snapshots should preserve the VerityFoundry authority boundary. A fixture
shape diff can show that candidate authoring output changed; it does not prove
that a generated VeritySpec workspace is valid, complete, ready, or approved.
Human review remains required before treating fixture changes as product
decisions.
