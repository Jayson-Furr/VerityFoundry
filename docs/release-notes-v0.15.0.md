# VerityFoundry v0.15.0 Release Notes

VerityFoundry v0.15.0 expands checked portfolio examples for multi-game
triage and cross-workspace dependency mapping.

## Highlights

- Added a portfolio triage example for rough multi-game inputs.
- Added a shared Unity runtime dependency-map example for game workspace
  consumers.
- Added candidate workspace fixtures and provenance examples for both new
  portfolio workflows.
- Added fixture kind mappings for portfolio records, Unity export assumptions,
  and future VeritySpec workspace dependency records.
- Updated packaged artifact coverage so installed wheels include the new
  example files.
- Updated portfolio workflow documentation, README, changelog, roadmap, and
  tests.

## Verification

- Package version: `0.15.0`.
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
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.15.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
