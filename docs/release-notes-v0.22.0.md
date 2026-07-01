# VerityFoundry v0.22.0 Release Notes

VerityFoundry v0.22.0 hardens policy-lint trend reporting, render-profile
review fixtures, and release-review bundle planning.

## Highlights

- Added `schemas/policy-lint-trend-report.schema.json` for deterministic
  policy-lint trend JSON output.
- Added schema validation tests for current policy-lint trend output.
- Added policy-lint advisory remediation guidance.
- Added quality-threshold warning trend guidance for release reviewers.
- Added render-profile output snapshots for every supported profile.
- Added release-review bundle export CLI design notes for a future command.
- Updated README, changelog, roadmap, report schema stability docs, package
  data, and release notes for the v0.22.0 release.

## Verification

- Package version: `0.22.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`,
  `verityfoundry report prompt-quality-trend`,
  `verityfoundry report policy-lint-trend`,
  `verityfoundry report matrix-coverage`,
  `verityfoundry report release-summary`,
  `verityfoundry report golden-inventory`,
  `verityfoundry report example-inventory`,
  `verityfoundry report fixture-inventory`,
  `verityfoundry report provenance-coverage`,
  `verityfoundry report provenance-distribution`,
  `verityfoundry report portfolio-coverage`,
  `verityfoundry check verityspec`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.22.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
