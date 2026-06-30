# VerityFoundry v0.8.0 Release Notes

VerityFoundry v0.8.0 adds candidate workspace fixtures and example-level
validation that moves examples closer to concrete VeritySpec workspace drafts.

## Highlights

- Added `workspaceFixtures`, `expectedRecordCategories`, and
  `provenanceExamples` support to example manifests.
- Added candidate workspace JSON fixtures for product, software-library, Unity
  game, and Unity shared-library examples.
- Added expected record-category validation for example workspace fixtures.
- Added provenance example files for all examples.
- Added a Unity game image-input manifest that preserves interpretation
  limits for concept and identity art notes.
- Added workspace fixture conversion documentation for VeritySpec handoff.
- Updated packaged wheel data so installed CLI validation includes the new
  example fixture files.

## Verification

- Package version: `0.8.0`.
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
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.8.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
