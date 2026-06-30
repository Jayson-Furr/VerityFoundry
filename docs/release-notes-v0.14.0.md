# VerityFoundry v0.14.0 Release Notes

VerityFoundry v0.14.0 hardens release-review coverage for candidate workspace
fixtures and provenance.

## Highlights

- Added `verityfoundry report fixture-inventory` with text and JSON output.
- Added `verityfoundry report provenance-coverage` with text and JSON output.
- Added image input manifest schema validation for example workflows.
- Added packaged fixture-file tests proving declared example files and schemas
  are included in built distributions.
- Added fixture kind pack mapping documentation for recommended VeritySpec pack
  ownership.
- Added provenance coverage documentation for release reviewers.
- Updated README, CI, release workflow smoke tests, release checklist,
  changelog, roadmap, and AI-agent guidance.

## Verification

- Package version: `0.14.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`,
  `verityfoundry report prompt-quality-trend`,
  `verityfoundry report matrix-coverage`,
  `verityfoundry report golden-inventory`,
  `verityfoundry report example-inventory`,
  `verityfoundry report fixture-inventory`,
  `verityfoundry report provenance-coverage`,
  `verityfoundry check verityspec`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.14.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
