# Provenance Distribution JSON Schema

`schemas/provenance-distribution-report.schema.json` documents the
machine-readable shape emitted by:

```bash
verityfoundry report provenance-distribution --format json
```

The schema is intended for release-review tooling that needs to inspect
decision-source and confidence distribution without parsing the human-readable
report.

## Stable Fields

Downstream tooling should prefer these fields:

- `exampleCount`
- `decisionExampleCount`
- `recordProvenanceCount`
- `humanApprovalRequiredDecisionCount`
- `humanApprovalRequiredRecordCount`
- `decisionSourceCounts`
- `recordProvenanceSourceCounts`
- `decisionConfidenceCounts`
- `recordConfidenceCounts`
- `examples[].exampleId`
- `examples[].decisionSourceCounts`
- `examples[].recordProvenanceSourceCounts`

The report is an authoring-quality signal. It does not prove that generated
VeritySpec records are true, approved, complete, or release-ready.

## Review Use

Use this schema when checking that prompt-workflow examples preserve:

- human-provided decisions separately from AI-inferred and AI-suggested
  decisions
- unresolved decisions
- confidence levels
- human-approval-required markers

If a release changes the report shape, update this schema, tests, snapshot
docs, README references, changelog, and roadmap in the same sprint.
