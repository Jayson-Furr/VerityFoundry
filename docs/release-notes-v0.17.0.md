# VerityFoundry v0.17.0 Release Notes

VerityFoundry v0.17.0 adds an aggregate release-summary report and supporting
release-review documentation so reviewers can see deterministic repository
health in one local command.

## Highlights

- Added `verityfoundry report release-summary` with text and JSON output.
- Aggregated release integrity, quality thresholds, workflow hygiene,
  decision-policy lint counts, prompt quality, prompt quality trend, matrix
  coverage, golden inventory, example inventory, fixture inventory, and
  provenance coverage into one release-review report.
- Added source-checkout boundaries so release integrity and workflow hygiene
  are reported as `skipped` when the report is run from installed prompt
  artifacts outside a repository checkout.
- Added release-summary documentation for downstream reviewers.
- Added workflow hygiene history, action-version policy, quality-threshold
  ratcheting, and render-profile compatibility documentation.
- Added release-summary coverage to CI, release workflow smoke checks,
  README, release checklist, release reviewer checklist, tests, changelog,
  roadmap, and AI-agent guidance.
- Updated repository guidance so future sprints should bundle about a week of
  related work into coherent releasable increments.

## Verification

- Package version: `0.17.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`,
  `verityfoundry report prompt-quality-trend`,
  `verityfoundry report matrix-coverage`,
  `verityfoundry report release-summary`,
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
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.17.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
