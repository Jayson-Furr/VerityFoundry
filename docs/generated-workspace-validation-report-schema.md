# Generated Workspace Validation Report Schema

`schemas/generated-workspace-validation-report.schema.json` documents the
machine-readable shape emitted by:

```bash
verityfoundry report generated-workspace-validation --format json
```

The report summarizes checked `validation-result.json` snapshots for generated
VeritySpec workspace fixtures. It is designed for release reviewers and local
automation that need deterministic evidence about snapshot coverage and drift.

## Stable Fields

The report includes:

- overall report status
- generated workspace count
- validation snapshot count
- passed, failed, skipped, and missing snapshot counts
- hashed file count
- stale file-hash count
- uncovered fixture-file count
- human-review-required snapshot count
- unresolved decision count
- per-workspace snapshot details

Per-workspace entries include the fixture manifest path, snapshot path,
validation status, validation command, VeritySpec tool metadata, file hashes,
uncovered files, unresolved decision count, and authority-boundary text.

## Review Boundary

This schema validates VerityFoundry report shape. It does not prove that a
generated VeritySpec workspace is complete, ready, compliant, approved, or safe
to ship.

Human reviewers should treat stale hashes, uncovered files, missing human
review markers, and unresolved decisions as release-review signals. VeritySpec
remains the final authority for product-contract validation.

