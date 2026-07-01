# Release Summary JSON Schema

`schemas/release-summary-report.schema.json` documents the machine-readable
shape emitted by:

```bash
verityfoundry report release-summary --format json
```

The schema is intended for downstream release-review tooling that wants to
inspect stable fields without parsing human text.

## Stability

For v0.x releases, existing top-level fields should remain stable unless the
changelog calls out a compatibility impact. Additive fields may appear in minor
releases when a new report family becomes part of the release summary.

Schema updates should be made in the same sprint as:

- command tests
- release-summary snapshot updates
- README links
- changelog entries
- roadmap entries
- release notes during release preparation

## Additive Report Fields

`reports.generatedWorkspaceValidation` summarizes generated workspace
validation-result snapshot coverage. It includes snapshot counts, passed
snapshot counts, stale file-hash counts, uncovered fixture-file counts, and
unresolved decision counts.

This field is a release-review signal. It is not a blocking readiness
certificate, and human reviewers should still inspect any generated VeritySpec
workspace fixture changes directly.

## Boundary

The schema validates VerityFoundry release-review report shape. It does not
prove that a generated VeritySpec workspace is valid, ready, compliant, or
approved.

Generated workspaces still require:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```
