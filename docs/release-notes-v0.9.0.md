# VerityFoundry v0.9.0 Release Notes

VerityFoundry v0.9.0 adds portfolio prompt workflows for multi-game triage and
cross-workspace dependency mapping.

## Highlights

- Added `portfolio.games.interview-low.concept-complete.v1` for game
  portfolio triage.
- Added `portfolio.dependencies.interview-medium.implementation-ready.v1` for
  cross-workspace dependency mapping.
- Added the `portfolio` prompt matrix.
- Added matrix coverage for the new portfolio domain.
- Added portfolio workflow documentation covering dependency assumptions,
  lockfile questions, exported-record assumptions, triage outputs, and
  VeritySpec authority boundaries.
- Updated packaged wheel data so installed CLI inspection includes the new
  portfolio prompt files.

## Verification

- Package version: `0.9.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`, `verityfoundry report matrix-coverage`,
  and `verityfoundry check verityspec`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.9.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
