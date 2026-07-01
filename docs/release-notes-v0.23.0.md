# VerityFoundry v0.23.0 Release Notes

VerityFoundry v0.23.0 hardens release-review fixture handoff, portfolio
coverage snapshots, cross-workspace dependency-map snapshots, and future
VeritySpec fixture validation planning.

## Highlights

- Added `schemas/provenance-distribution-report.schema.json` for deterministic
  provenance distribution JSON output.
- Added `schemas/portfolio-coverage-report.schema.json` for deterministic
  portfolio coverage JSON output.
- Added schema validation tests for current provenance distribution and
  portfolio coverage reports.
- Added checked portfolio coverage and cross-workspace reference snapshots for
  release reviewers.
- Added concrete fixture-to-VeritySpec checklist examples for customer portal
  and Dream Extraction workspace drafts.
- Added optional executable workspace fixture validation design notes.
- Updated README, changelog, roadmap, report schema stability docs, release
  reviewer docs, package data, and release notes for the v0.23.0 release.

## Verification

- Package version: `0.23.0`.
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
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.23.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
