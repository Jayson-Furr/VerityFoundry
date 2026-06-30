# VerityFoundry v0.12.0 Release Notes

VerityFoundry v0.12.0 hardens release review with deterministic prompt quality
trends, quality thresholds, and GitHub Actions workflow hygiene checks.

## Highlights

- Added `verityfoundry report prompt-quality-trend` for comparing the current
  prompt quality report against checked-in snapshots.
- Added the first prompt quality baseline snapshot, captured from v0.11.0.
- Added `verityfoundry check quality-thresholds` for release-review baselines
  covering prompt quality and matrix coverage.
- Added `verityfoundry check workflow-hygiene` for checking GitHub Actions
  action versions against repository minimums.
- Added release-quality threshold configuration under `config/`.
- Updated CI, release workflow smoke tests, release checklist, README,
  changelog, roadmap, and AI-agent guidance for the new checks.
- Updated the roadmap to preserve the week-sized grouped sprint cadence and
  refresh the Next 20 planning points.

## Verification

- Package version: `0.12.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`,
  `verityfoundry report prompt-quality-trend`,
  `verityfoundry report matrix-coverage`,
  `verityfoundry report golden-inventory`,
  `verityfoundry report example-inventory`, `verityfoundry check verityspec`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.12.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
