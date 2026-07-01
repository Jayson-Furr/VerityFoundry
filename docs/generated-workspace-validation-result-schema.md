# Generated Workspace Validation Result Schema

[`schemas/generated-workspace-validation-result.schema.json`](../schemas/generated-workspace-validation-result.schema.json)
describes the checked validation-result snapshots stored beside generated
workspace fixtures.

Each snapshot records:

- the generated workspace fixture ID and path
- the source fixture manifest
- the local validation command that was run
- the observed status and exit code
- hashes for the fixture manifest, workspace manifest, and records
- unresolved decisions that validation did not settle
- the VeritySpec authority boundary and human-review requirement

The schema intentionally does not model a complete VeritySpec readiness report.
It records local validation evidence for release reviewers while preserving the
fact that VeritySpec and human review remain authoritative.

## Snapshot Files

Current snapshots live beside generated workspace fixtures:

```text
fixtures/generated-workspaces/customer-portal/validation-result.json
fixtures/generated-workspaces/dream-extraction/validation-result.json
```

The corresponding fixture manifest points at the snapshot through
`validation.resultSnapshot`.

## Updating Snapshots

When a generated workspace fixture changes:

1. Re-run the validation command listed in the fixture manifest.
2. Update the validation-result status, output summary, and timestamp.
3. Recompute hashes for the fixture manifest, `verityspec.json`, and every
   record file.
4. Keep unresolved decisions visible.
5. Run the generated workspace validation-result tests.

The snapshot should never claim implementation, release, liveops, compliance,
or archive readiness. Validation success only means the generated workspace
passed the recorded VeritySpec validation command at the recorded fixture
state.
