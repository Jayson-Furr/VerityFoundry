# VerityFoundry v0.25.0 Release Notes

VerityFoundry v0.25.0 hardens release-summary compatibility guidance,
release-summary warning triage, release-summary snapshot update planning, and
release-review bundle maintenance guidance.

## Highlights

- Added release-summary schema compatibility guidance for additive JSON fields.
- Added release-summary warning triage guidance for non-blocking advisory
  movement.
- Added release-summary snapshot update checklist for future releases.
- Added release-review bundle retention policy notes.
- Added CI artifact naming guidance for future release-review bundles.
- Updated README, changelog, roadmap, release-review docs tests, and release
  notes for the v0.25.0 release.

## Verification

- Package version: `0.25.0`.
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
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.25.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
