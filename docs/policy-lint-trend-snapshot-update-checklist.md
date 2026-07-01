# Policy-Lint Trend Snapshot Update Checklist

Policy-lint trend snapshots preserve warning-count history for release review.
Update them only when warning movement is intentional and understood.

## Checklist

1. Run `verityfoundry lint decision-policy`.
2. Run `verityfoundry report policy-lint-trend --format json`.
3. Confirm whether warning movement is expected, fixed, or newly introduced.
4. If a new baseline is needed, add a versioned snapshot under
   `snapshots/policy-lint/`.
5. Update documentation and release notes with the reason for the new baseline.
6. Run tests and `verityfoundry check quality-thresholds`.

## Review Boundary

A policy-lint snapshot is evidence for VerityFoundry prompt-policy drift. It is
not human approval for unresolved decisions, and it is not VeritySpec validation
for generated workspace records.
