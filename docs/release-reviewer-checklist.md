# Release Reviewer Checklist

Use this checklist before merging a release-preparation PR or cutting a tag.
It combines local VerityFoundry checks with the VeritySpec authority boundary
and required human review.

## Local Repository Checks

```bash
python -m unittest discover -s tests -v
verityfoundry --version
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate matrices
verityfoundry validate examples
verityfoundry validate goldens
git diff --check
```

## Release-Review Reports

```bash
verityfoundry lint decision-policy
verityfoundry report prompt-quality
verityfoundry report prompt-quality-trend
verityfoundry report policy-lint-trend
verityfoundry report matrix-coverage
verityfoundry report release-summary
verityfoundry report golden-inventory
verityfoundry report example-inventory
verityfoundry report fixture-inventory
verityfoundry report generated-workspace-validation
verityfoundry report provenance-coverage
verityfoundry report provenance-distribution
verityfoundry report portfolio-coverage
verityfoundry check quality-thresholds
verityfoundry check workflow-hygiene
verityfoundry check release-integrity
```

Review the report output for:

- prompt quality regressions
- policy-lint warning drift
- matrix coverage gaps
- missing or unexpected golden fixtures
- missing example fixtures
- fixture kind mappings that need documentation
- missing provenance
- decision-source distribution drift
- portfolio dependency assumptions and cross-workspace reference counts
- portfolio coverage and cross-workspace reference snapshot drift
- generated workspace validation-result snapshot drift
- generated workspace unresolved-decision drift
- stale workflow action versions
- release version drift

## VeritySpec Boundary Check

If a generated workspace is in scope and `verity` is installed, run:

```bash
verityfoundry check verityspec --workspace <generated-workspace>
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

If GitHub Actions cannot run because of billing, credits, quota, runner
availability, or another platform issue, run equivalent local checks and record
the local evidence in the PR.

## Distribution Checks

```bash
rm -rf dist build
python -m build
python -m twine check dist/*
```

Install the wheel into a clean virtual environment outside the source checkout
and run representative CLI checks, including packaged artifact validation.

## Release Bookkeeping

Confirm these are aligned:

- `pyproject.toml`
- `src/verityfoundry/__init__.py`
- `README.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `docs/release-checklist.md`
- release notes for the target tag
- GitHub issue, milestone, branch, PR, tag, and release

When candidate workspace fixtures are part of the release, also review
[fixture-to-verityspec-checklist-examples.md](fixture-to-verityspec-checklist-examples.md)
and
[executable-workspace-fixture-validation-design.md](executable-workspace-fixture-validation-design.md)
for the VeritySpec handoff boundary.

When generated workspace fixtures are part of the release, also review
[generated-workspace-validation-result-schema.md](generated-workspace-validation-result-schema.md),
[generated-workspace-validation-report-schema.md](generated-workspace-validation-report-schema.md),
[generated-workspace-validation-result-triage.md](generated-workspace-validation-result-triage.md),
[generated-workspace-validation-result-package-data.md](generated-workspace-validation-result-package-data.md),
[generated-workspace-validation-result-update-dry-run.md](generated-workspace-validation-result-update-dry-run.md),
[generated-workspace-validation-result-drift-examples.md](generated-workspace-validation-result-drift-examples.md),
and
[generated-workspace-validation-result-ci-artifacts.md](generated-workspace-validation-result-ci-artifacts.md).
Confirm checked `validation-result.json` files still require human review and
do not claim readiness that VeritySpec did not prove.

Do not publish package artifacts or create a release unless the user has
explicitly authorized that release action.
