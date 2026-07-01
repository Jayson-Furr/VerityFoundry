# VerityFoundry v0.21.0 Release Notes

VerityFoundry v0.21.0 hardens release-summary review artifacts for downstream
tooling and release reviewers.

## Highlights

- Added `schemas/release-summary-report.schema.json` for deterministic
  release-summary JSON output.
- Added schema validation tests for current release-summary output and checked
  release-summary snapshots.
- Added checked release-summary snapshots for v0.20.0 and v0.21.0.
- Added documentation for release-summary snapshot usage, release-to-release
  comparison, PR descriptions, and release-review bundle export guidance.
- Updated README, changelog, roadmap, report schema stability docs, package
  data, and release notes for the v0.21.0 release.

## Verification

- Package version: `0.21.0`.
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
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.21.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
