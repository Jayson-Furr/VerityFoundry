# VerityFoundry v0.26.0 Release Notes

VerityFoundry v0.26.0 hardens release-review bundle planning with a
machine-readable bundle manifest schema, a planned dry-run fixture, checksum
guidance, and additional snapshot and warning-triage process documentation.

## Highlights

- Added `schemas/release-review-bundle-manifest.schema.json`.
- Added a planned dry-run bundle manifest example fixture.
- Added tests that validate the bundle manifest schema and dry-run authority
  boundaries.
- Added release-review bundle manifest, checksum, and dry-run CLI design
  guidance.
- Added render-profile snapshot retention, policy-lint trend snapshot update,
  and quality-threshold warning triage guidance.
- Updated README, changelog, roadmap, package-data coverage, and release-review
  docs tests for the v0.26.0 release.

## Verification

- Package version: `0.26.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry report release-summary`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.26.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
