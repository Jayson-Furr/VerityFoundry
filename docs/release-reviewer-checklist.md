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
verityfoundry report matrix-coverage
verityfoundry report release-summary
verityfoundry report golden-inventory
verityfoundry report example-inventory
verityfoundry report fixture-inventory
verityfoundry report provenance-coverage
verityfoundry check quality-thresholds
verityfoundry check workflow-hygiene
verityfoundry check release-integrity
```

Review the report output for:

- prompt quality regressions
- matrix coverage gaps
- missing or unexpected golden fixtures
- missing example fixtures
- fixture kind mappings that need documentation
- missing provenance
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

Do not publish package artifacts or create a release unless the user has
explicitly authorized that release action.
