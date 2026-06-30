# VerityFoundry v0.7.0 Release Notes

VerityFoundry v0.7.0 adds deterministic decision-policy linting and
agent-specific render profiles for safer prompt handoff.

## Highlights

- Added `verityfoundry lint decision-policy` with text and JSON output.
- Added `verityfoundry list profiles`.
- Added `render --profile` support for `codex`, `claude-code`, `chatgpt`,
  `gemini`, and `unity-ai`.
- Updated high-risk prompt manifests to include shared safety and provenance
  rules.
- Added contributor guidance for prompt workflow policy expectations.
- Added docs for decision-policy linting and render profiles.
- Bundled prompt, matrix, schema, example, and golden-output artifacts in the
  installable wheel so the CLI can inspect the prompt library outside a source
  checkout.
- Added lint/profile checks to CI, release workflow wheel smoke tests, and
  local verification guidance.

## Verification

- Package version: `0.7.0`.
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
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.7.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.
