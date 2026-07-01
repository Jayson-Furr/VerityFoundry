# Generated Workspace Validation-Result CLI Planning

Generated workspace validation-result snapshots are checked JSON fixtures.
VerityFoundry includes a deterministic report command for inspecting them
without turning VerityFoundry into the validation authority.

## Current Report Command

```bash
verityfoundry report generated-workspace-validation
verityfoundry report generated-workspace-validation --format json
```

The report reads fixture manifests and `validation-result.json` snapshots,
checks file-hash freshness, and keeps unresolved decisions visible.

## Possible Update Command Shape

```bash
verityfoundry fixture validation-result fixtures/generated-workspaces/customer-portal --update
verityfoundry fixture validation-result fixtures/generated-workspaces/dream-extraction --format json
```

The future update command should:

- load `fixture-manifest.json`
- run the manifest validation command when `verity` is available
- skip cleanly when VeritySpec is not installed and `skipWhenVerityMissing` is
  true
- record status, exit code, output summary, and timestamp
- recompute fixture file hashes
- preserve unresolved decisions and human-review requirements
- refuse to write a snapshot that omits the VeritySpec authority boundary

## Non-Goals

The command should not:

- call external AI APIs
- weaken VeritySpec validation so generated fixtures pass
- convert validation success into readiness, release, compliance, or approval
  claims
- hide unresolved decisions
- overwrite reviewer notes without an explicit update flag

## Release-Review Use

Until this update command exists, release reviewers should treat the checked
`validation-result.json` files as manually maintained snapshots and inspect
them with:

```bash
verityfoundry report generated-workspace-validation
python -m unittest tests.test_generated_workspace_validation_results -v
python -m unittest tests.test_packaged_fixture_files -v
```
