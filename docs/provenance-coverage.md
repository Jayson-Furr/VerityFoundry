# Provenance Coverage

`verityfoundry report provenance-coverage` summarizes how well candidate
workspace fixtures preserve uncertainty and decision provenance.

```bash
verityfoundry report provenance-coverage
verityfoundry report provenance-coverage --format json
```

The report distinguishes two levels:

- record provenance coverage: candidate workspace records that include a
  `provenance` object
- decision example coverage: records that are represented in example
  `provenance.json` decision examples

Record provenance should normally be complete for checked-in workspace
fixtures. Decision example coverage is intentionally partial: examples should
show representative human-provided, AI-inferred, AI-defaulted, unresolved, and
human-approval-required decisions without pretending every record has been
formally interviewed.

Use this report during release review with:

```bash
verityfoundry validate examples
verityfoundry report fixture-inventory
verityfoundry report provenance-coverage
verityfoundry report provenance-distribution
```

The report is not a VeritySpec readiness certification. It is a VerityFoundry
authoring-quality signal that helps reviewers spot fixture drift before a
release.

Use [provenance-distribution.md](provenance-distribution.md) when you need to
review the mix of human-provided, AI-inferred, AI-suggested, unresolved, and
human-approval-required decisions across examples.
