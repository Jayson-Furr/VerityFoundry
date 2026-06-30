# CI

CI is lightweight and deterministic. It does not call external AI APIs.

The GitHub Actions workflow runs:

```bash
python -m unittest discover -s tests -v
verityfoundry --version
verityfoundry list prompts
verityfoundry list matrices
verityfoundry list profiles
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate matrices
verityfoundry validate examples
verityfoundry validate goldens
verityfoundry lint decision-policy
verityfoundry report prompt-quality
verityfoundry report prompt-quality-trend
verityfoundry report policy-lint-trend
verityfoundry report matrix-coverage
verityfoundry report golden-inventory
verityfoundry report example-inventory
verityfoundry report fixture-inventory
verityfoundry report provenance-coverage
verityfoundry check verityspec
verityfoundry check release-integrity
verityfoundry check quality-thresholds
verityfoundry check workflow-hygiene
git diff --check
```

`verityfoundry check verityspec` is optional by design. If the VeritySpec
`verity` CLI is unavailable in CI, it reports `skipped` and exits
successfully. If `verity` is available and a workspace is provided or detected,
the command runs `verity validate`.

If GitHub Actions is unavailable because of billing, credits, quota, runner
availability, or another platform issue, run equivalent local checks and record
that fallback evidence in the PR.

Release workflow wheel smoke tests install the built wheel into a clean virtual
environment and run CLI inspection from `/tmp`, outside the source checkout.
That check verifies the packaged prompt-library artifacts are available to an
installed CLI.

`verityfoundry check release-integrity` runs from the source checkout because
it checks repository files such as `README.md`, `CHANGELOG.md`, `ROADMAP.md`,
`pyproject.toml`, and release notes. It is not part of the installed-wheel
smoke test.

`verityfoundry check workflow-hygiene` also runs from the source checkout
because it checks `.github/workflows/`. Installed-wheel smoke tests do run
`verityfoundry report prompt-quality-trend`,
`verityfoundry report policy-lint-trend`, and
`verityfoundry check quality-thresholds` to verify packaged snapshots and
threshold configuration.
