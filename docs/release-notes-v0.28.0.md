# VerityFoundry v0.28.0 Release Notes

VerityFoundry v0.28.0 hardens generated workspace fixture review for
cross-workspace dependency scenarios, dependency lockfile assumptions,
provenance, graph review, and future VeritySpec dependency-import workflows.

## Highlights

- Added `schemas/generated-workspace-fixture-provenance.schema.json`.
- Added tests validating generated workspace fixture manifest provenance.
- Added cross-workspace dependency fixture compatibility guidance.
- Added portfolio dependency lockfile assumption checklist.
- Added VeritySpec workspace dependency importer design notes.
- Added executable fixture release-summary coverage notes.
- Added generated workspace fixture README examples.
- Added cross-workspace fixture graph review checklist.
- Added VeritySpec dependency lockfile prompt-workflow guidance.
- Updated README, changelog, roadmap, release-review docs tests, and release
  notes for the v0.28.0 release.

## Verification

- Package version: `0.28.0`.
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
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.28.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
