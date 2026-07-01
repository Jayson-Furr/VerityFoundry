# Generated Workspace Validation-Result Drift Examples

Validation-result snapshots can drift when generated workspace fixtures change
without updating their checked evidence. The deterministic report command helps
reviewers catch that drift before release.

## Stale Hash

Example:

```text
fixtures/generated-workspaces/customer-portal/records/product.json changed
but validation-result.json still contains the old SHA-256 value.
```

Expected response:

- run `verityfoundry report generated-workspace-validation`
- re-run the recorded VeritySpec validation command
- update the snapshot hash only if the validation result is still accurate
- preserve unresolved decisions and the human-review-required marker

## Uncovered Fixture File

Example:

```text
fixtures/generated-workspaces/dream-extraction/records/telemetry.json was
added, but validation-result.json does not list it under fileHashes.
```

Expected response:

- decide whether the file belongs to the generated workspace fixture
- run VeritySpec validation after adding it
- add the new hash to the snapshot
- update unresolved decisions if the new file introduces unknowns

## Missing Human Review Marker

Example:

```text
humanReviewRequired was removed or set to false in validation-result.json.
```

Expected response:

- treat the snapshot as release-review drift
- restore the marker unless there is a documented human approval process
- do not claim VeritySpec validation replaces human approval

## Authority Boundary Regression

Example:

```text
The authority boundary no longer says that VeritySpec is the validation
authority or that readiness is not certified.
```

Expected response:

- fail the release review until the boundary is restored
- keep generated workspace snapshots honest about uncertainty and scope

