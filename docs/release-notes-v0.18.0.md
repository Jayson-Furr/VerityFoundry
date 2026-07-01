# VerityFoundry v0.18.0 Release Notes

VerityFoundry v0.18.0 adds release-review baseline hardening for policy-lint
advisories, threshold visibility, packaged snapshots, and agent render-profile
smoke coverage.

## Highlights

- Added `verityfoundry report policy-lint-trend` with text and JSON output.
- Added a checked `v0.17.0` policy-lint warning baseline snapshot under
  `snapshots/policy-lint/`.
- Added non-blocking policy-lint advisory warning thresholds to
  `verityfoundry check quality-thresholds`.
- Included policy-lint trend movement and quality-threshold warning counts in
  `verityfoundry report release-summary`.
- Added render-to-file CLI smoke coverage for every supported agent profile.
- Added fixture inventory report schema documentation for downstream release
  tooling.
- Added example fixture diff snapshot guidance for release reviewers.
- Added policy-lint trend documentation and wired the new report into README,
  AGENTS, CI, release workflow smoke checks, release checklist, release
  reviewer checklist, changelog, and roadmap.

## Verification

- Package version: `0.18.0`.
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
  `verityfoundry check verityspec`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.18.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
