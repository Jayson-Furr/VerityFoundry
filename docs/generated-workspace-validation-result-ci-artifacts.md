# Generated Workspace Validation-Result CI Artifacts

Future CI jobs may export generated workspace validation-result reports as
release-review artifacts. The artifact should help reviewers inspect drift; it
must not replace checked snapshots, VeritySpec validation, or human approval.

## Proposed Artifact Names

Use stable, predictable names:

```text
generated-workspace-validation-report.json
generated-workspace-validation-report.txt
```

If artifacts are grouped by release-review bundle, include the report under:

```text
release-review/generated-workspace-validation-report.json
release-review/generated-workspace-validation-report.txt
```

## Proposed CI Commands

```bash
verityfoundry report generated-workspace-validation --format json > generated-workspace-validation-report.json
verityfoundry report generated-workspace-validation > generated-workspace-validation-report.txt
```

The text form is useful for PR review. The JSON form is useful for downstream
release-review tooling.

## Retention Guidance

CI artifacts are convenience outputs. The checked repository files remain the
durable release record:

- generated workspace fixture files
- fixture manifests
- `validation-result.json` snapshots
- schemas
- tests
- release notes

If GitHub Actions cannot run because of billing, credits, quota, runner
availability, or another platform issue, run the same commands locally and
record the local evidence in the PR. Human reviewers should still verify that
VeritySpec remains the contract authority.

