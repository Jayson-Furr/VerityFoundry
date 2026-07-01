# Generated Workspace Validation-Result Package Data

Validation-result snapshots are packaged with the generated workspace fixtures
so installed-wheel release reviews can inspect them outside the source
checkout.

They remain VerityFoundry review artifacts. VeritySpec validation and human
approval remain required before treating a generated workspace as product
truth.

The package-data coverage is enforced by:

```bash
python -m unittest tests.test_packaged_fixture_files -v
python -m unittest tests.test_generated_workspace_validation_results -v
```

The first test proves every `fixtures/**/*.json` file is included in
`pyproject.toml` data-file patterns. The second test proves each generated
workspace manifest links to a `validation-result.json` snapshot that matches
the expected workspace ID and fixture path.

## Reviewer Checklist

When validation-result snapshots change, confirm:

- the snapshot is next to the generated workspace fixture
- `validation.resultSnapshot` points to the snapshot
- the snapshot validates against
  `schemas/generated-workspace-validation-result.schema.json`
- the snapshot keeps `humanReviewRequired` set to `true`
- file hashes cover the fixture manifest, workspace manifest, and all records
- README, changelog, roadmap, and release notes mention the change when it is
  release-facing
