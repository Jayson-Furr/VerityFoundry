# Provenance Distribution

`verityfoundry report provenance-distribution` summarizes the decision-source
and confidence distribution across checked example provenance files and
candidate workspace fixture provenance.

```bash
verityfoundry report provenance-distribution
verityfoundry report provenance-distribution --format json
```

The report helps reviewers answer:

- Are examples preserving human-provided decisions separately from AI-inferred
  and AI-suggested decisions?
- Are unresolved decisions still visible?
- How many provenance decisions and fixture records require human approval?
- Are confidence values distributed honestly, or did a prompt workflow turn
  uncertainty into fake certainty?

The report includes:

- decision examples by `decisionSource`
- fixture record provenance by `decisionSource`
- decision and record confidence counts
- human-approval-required counts
- per-example distribution summaries

Use it with:

```bash
verityfoundry validate examples
verityfoundry report provenance-coverage
verityfoundry report provenance-distribution
```

This is an authoring-quality signal. It does not prove that generated
VeritySpec records are true, approved, complete, or release-ready.
