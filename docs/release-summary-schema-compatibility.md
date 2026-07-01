# Release-Summary Schema Compatibility

`verityfoundry report release-summary --format json` is intended for
release-review automation and PR summaries. The JSON shape should remain
stable across v0.x releases unless a release note explicitly calls out the
compatibility impact.

## Additive Fields

Additive fields are allowed when they do not change the meaning or type of
existing fields.

When adding a field:

1. Add it to `schemas/release-summary-report.schema.json`.
2. Add tests that validate current report output against the schema.
3. Update release-summary docs and PR usage guidance.
4. Update release-review bundle guidance if the field should be exported.
5. Update changelog, roadmap, and release notes.

Prefer additive fields under existing sections such as:

- `checks`
- `reports`
- `notes`

Do not rename or remove existing fields casually. Downstream release tooling
may depend on them.

## Compatibility Boundary

The release-summary report describes VerityFoundry repository health. It does
not certify that a VeritySpec workspace is valid, complete, human-approved, or
ready to release.

If a report field summarizes generated workspace state, keep VeritySpec
validation and human approval as separate evidence.
