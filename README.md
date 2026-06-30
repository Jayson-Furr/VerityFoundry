# VerityFoundry

[![CI](https://github.com/Jayson-Furr/VerityFoundry/actions/workflows/ci.yml/badge.svg)](https://github.com/Jayson-Furr/VerityFoundry/actions/workflows/ci.yml)
[![Release](https://img.shields.io/badge/release-v0.3.0-blue)](https://github.com/Jayson-Furr/VerityFoundry/releases/tag/v0.3.0)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](pyproject.toml)
[![License](https://img.shields.io/github/license/Jayson-Furr/VerityFoundry)](LICENSE)

Turn rough intent into validated VeritySpec workspace drafts.

VerityFoundry is the AI-assisted authoring and prompt workflow layer for
VeritySpec. It provides prompt matrices, interview modes, decision policies,
provenance rules, examples, and local validation utilities for creating
candidate VeritySpec workspaces from rough product, software, game, Unity, and
operations inputs.

VerityFoundry does not replace VeritySpec:

```text
VeritySpec    = contract engine
VerityFoundry = AI-assisted authoring and prompt workflow layer
```

VerityFoundry fabricates candidate workspace drafts. VeritySpec validates and
enforces product contracts. Human review remains required for high-stakes
decisions.

In this repository, fabrication means generating a candidate VeritySpec
workspace from partial inputs with explicit assumptions, provenance,
confidence, unresolved decisions, and human-approval markers. It does not mean
that AI-generated records are automatically true, complete, or approved.

## Current Scope

Latest release: `v0.3.0`. Release history is tracked in
[CHANGELOG.md](CHANGELOG.md) and [ROADMAP.md](ROADMAP.md).

The repository currently provides:

- A small installable Python package named `verityfoundry`.
- A deterministic local CLI named `verityfoundry`.
- Prompt manifest, matrix manifest, example manifest, and decision policy
  schemas.
- Prompt library folders for common rules, interview modes, readiness targets,
  Unity games, Unity shared libraries, software libraries, and products.
- Unity game and Unity shared-library prompt matrices.
- Example inputs and expected outputs for a Unity game and a shared Unity
  runtime library.
- Golden output fixtures for Unity game and Unity shared-library
  implementation-ready workflows.
- A deterministic prompt quality report for uncertainty preservation and
  provenance completeness.
- Prompt quality and uncertainty-preservation evaluation guidance.
- Canonical AI-agent operating instructions in `AGENTS.md`.
- GitHub Actions CI that validates the library without calling external AI
  APIs.

## Installation

Install the latest GitHub release:

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.3.0"
verityfoundry --version
```

PyPI publishing is not enabled yet. Use the GitHub release install path until
package publishing is explicitly configured.

## Local Development

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools
pip install -e .

verityfoundry --version
verityfoundry list prompts
verityfoundry list matrices
verityfoundry validate
```

Without installation:

```bash
PYTHONPATH=src python3 -m verityfoundry --version
PYTHONPATH=src python3 -m verityfoundry validate
```

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

## CLI Examples

```bash
verityfoundry --version
verityfoundry list prompts
verityfoundry list matrices
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate examples
verityfoundry validate goldens
verityfoundry report prompt-quality
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1
verityfoundry matrix unity-game
```

The CLI is intentionally small. It validates and inspects the prompt workflow
library. It does not call OpenAI, Anthropic, Gemini, Copilot, Unity AI, or any
other AI API.

## Prompt Library

Prompts are Markdown files with JSON front matter. The front matter is the
machine-checkable prompt manifest. The body is the human-readable prompt
workflow.

Prompt manifests declare:

- stable prompt ID
- version
- domain
- interview mode
- target readiness
- input types
- output types
- decision policy
- human approval requirements
- reusable common prompt sections

Example prompt ID:

```text
unity-game.gdd-art.interview-medium.implementation-ready.v1
```

Prompt IDs should be stable. Breaking changes should use a new version suffix.

## Interview Modes

VerityFoundry documents five interview modes:

| Mode | Purpose |
|---|---|
| `interview-none` | No questions; conservative low-stakes draft with unresolved decisions. |
| `interview-low-stakes` | A small number of high-value questions for concept and prototype work. |
| `interview-medium-stakes` | Architecture, implementation, telemetry, and team handoff questions. |
| `interview-high-stakes` | Human input before sensitive legal, financial, privacy, compliance, platform, or liveops commitments. |
| `interview-all` | Full questioning for formal completion, decommissioning, or archival planning. |

## Readiness Targets

VerityFoundry supports prompt-workflow readiness targets:

```text
concept-complete
design-complete
prototype-ready
vertical-slice-ready
implementation-ready
production-ready
operations-ready
liveops-ready
maintenance-ready
decommission-ready
archival-ready
```

These are authoring targets, not final certification claims. VerityFoundry
should generate candidate outputs and gap reports. VeritySpec remains the
validation authority.

## Matrix Examples

Prompt matrices combine domain, input type, interview mode, readiness target,
and expected output.

```bash
verityfoundry matrix unity-game
verityfoundry matrix unity-shared-library
```

## Golden Outputs

Golden outputs are deterministic examples of expected prompt behavior. They
are not truth claims and do not replace VeritySpec validation or human review.

The current golden fixtures cover Unity game and Unity shared-library
implementation-ready workflows:

```text
goldens/unity-game/dream-extraction-implementation-ready/
goldens/unity-shared-library/shared-unity-runtime-implementation-ready/
```

Validate golden output manifests and required sections with:

```bash
verityfoundry validate goldens
```

## Prompt Quality Report

The prompt quality report scores visible evidence in rendered prompt text for
uncertainty preservation and provenance completeness. It is deterministic and
does not call external AI APIs.

```bash
verityfoundry report prompt-quality
verityfoundry report prompt-quality --format json
```

The report is an inspection aid, not a readiness certification.

## Unity Game Workflow

The Unity game prompts support rough inputs such as:

- game name and short description
- rough GDD
- concept art notes or image summaries
- identity image notes
- target platforms
- Unity version
- shared Unity runtime assumptions
- prototype goals
- liveops assumptions

Expected candidate outputs include workspace outlines, game product records,
GDD source records, visual identity records, concept art records, loops,
features, Unity dependency records, telemetry intent, readiness gaps, and
agent implementation context.

## Unity Shared Library Workflow

The Unity shared-library prompts support library briefs, Unity package notes,
README content, API notes, shared systems, target Unity versions, consumer
games, operations expectations, and archive expectations.

Expected candidate outputs include library product outlines, Unity package
records, capability records, dependency notes, consumer-facing contract notes,
version compatibility assumptions, readiness gaps, and archive gaps.

## VeritySpec Validation Loop

The intended loop is:

```text
rough input
  -> VerityFoundry prompt workflow
  -> candidate VeritySpec workspace
  -> verity validate
  -> verity lint
  -> verity readiness
  -> gap report
  -> human approval / further interview
  -> more complete workspace
```

When VeritySpec is available locally, generated workspaces should be checked
with:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

## AI-Agent Usage

AI agents should start with `AGENTS.md`. Agent-specific files such as
`CODEX.md`, `CHATGPT.md`, `CLAUDE.md`, `GEMINI.md`, and `UNITY_AI.md` are
adapters that point back to the canonical instructions.

Agents must preserve uncertainty. Generated records and reports should
distinguish human-provided decisions, AI-inferred decisions, AI-defaulted
decisions, AI-suggested decisions, unresolved decisions, and decisions that
require human approval.

## Documentation

- [Architecture](docs/architecture.md)
- [Prompt manifests](docs/prompt-manifests.md)
- [Interview modes](docs/interview-modes.md)
- [Readiness targets](docs/readiness-targets.md)
- [Decision provenance](docs/decision-provenance.md)
- [Image input guidance](docs/image-input-guidance.md)
- [Unity game workflows](docs/unity-game-workflows.md)
- [Unity shared-library workflows](docs/unity-shared-library-workflows.md)
- [Golden output guidelines](evaluations/golden-output-guidelines.md)
- [Using with VeritySpec](docs/using-with-verityspec.md)
- [Using with Codex](docs/using-with-codex.md)
- [Using with Copilot](docs/using-with-copilot.md)
- [Using with Claude Code](docs/using-with-claude-code.md)
- [Using with ChatGPT](docs/using-with-chatgpt.md)
- [Using with Gemini](docs/using-with-gemini.md)
- [Using with Unity AI](docs/using-with-unity-ai.md)
- [Branching](docs/branching.md)
- [CI](docs/ci.md)
- [Release checklist](docs/release-checklist.md)
- [v0.3.0 release notes](docs/release-notes-v0.3.0.md)
- [v0.2.0 release notes](docs/release-notes-v0.2.0.md)
- [v0.1.0 release notes](docs/release-notes-v0.1.0.md)
