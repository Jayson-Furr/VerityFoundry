# VerityFoundry v0.1.0 Release Notes

VerityFoundry v0.1.0 establishes the public sibling repository for AI-assisted
VeritySpec workspace authoring.

## Highlights

- Added the first installable `verityfoundry` Python package and CLI.
- Added local deterministic commands for listing prompts, listing matrices,
  validating the prompt workflow library, rendering prompts, and rendering
  matrices.
- Added schemas for prompt manifests, matrix manifests, example manifests, and
  decision policies.
- Added prompt workflows for common rules, interview modes, readiness targets,
  Unity games, Unity shared libraries, software libraries, and products.
- Added Unity game, Unity shared-library, software-library, and product prompt
  matrices.
- Added examples for a Unity game and shared Unity runtime.
- Added AI-agent entry points and documentation for Codex, Copilot, Claude,
  ChatGPT, Gemini, and Unity AI.
- Added CI and release automation.

## Compatibility

- Package version: `0.1.0`.
- Python support: `>=3.9`.
- VerityFoundry does not call external AI APIs.
- VerityFoundry creates candidate authoring outputs; VeritySpec remains the
  validation authority.

## Installation

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.1.0"
```

PyPI publishing is not enabled yet. Use the GitHub release install path until
package publishing is explicitly configured.
