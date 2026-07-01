# Generated Workspace Validation-Result CLI Planning

Generated workspace validation-result snapshots are currently checked JSON
fixtures. A future CLI command can make them easier to refresh without turning
VerityFoundry into the validation authority.

## Possible Command Shape

```bash
verityfoundry fixture validation-result fixtures/generated-workspaces/customer-portal --update
verityfoundry fixture validation-result fixtures/generated-workspaces/dream-extraction --format json
```

The command should:

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

Until this command exists, release reviewers should treat the checked
`validation-result.json` files as manually maintained snapshots and verify them
with:

```bash
python -m unittest tests.test_generated_workspace_validation_results -v
python -m unittest tests.test_packaged_fixture_files -v
```
