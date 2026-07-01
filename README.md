# VerityFoundry

[![CI](https://github.com/Jayson-Furr/VerityFoundry/actions/workflows/ci.yml/badge.svg)](https://github.com/Jayson-Furr/VerityFoundry/actions/workflows/ci.yml)
[![Release](https://img.shields.io/badge/release-v0.19.0-blue)](https://github.com/Jayson-Furr/VerityFoundry/releases/tag/v0.19.0)
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

Latest release: `v0.19.0`. Release history is tracked in
[CHANGELOG.md](CHANGELOG.md) and [ROADMAP.md](ROADMAP.md).

The repository currently provides:

- A small installable Python package named `verityfoundry`.
- A deterministic local CLI named `verityfoundry`.
- Bundled prompt, matrix, schema, example, and golden-output artifacts for
  installed CLI inspection outside a source checkout.
- Prompt manifest, matrix manifest, example manifest, and decision policy
  schemas.
- Agent-specific render profiles for Codex, Claude Code, ChatGPT, Gemini,
  GitHub Copilot, and Unity AI handoff.
- Prompt library folders for common rules, interview modes, readiness targets,
  Unity games, Unity shared libraries, software libraries, products,
  portfolios, and lifecycle readiness.
- Unity game, Unity shared-library, product, software-library, portfolio, and
  lifecycle prompt matrices.
- Example inputs and expected outputs for Unity game, Unity shared-library,
  software-library, product, portfolio triage, and cross-workspace dependency
  mapping workflows.
- Candidate workspace fixtures, expected record-category checks, provenance
  examples, and image-input metadata for example workflows.
- Golden output fixtures for Unity game, Unity shared-library, and lifecycle
  release/maintenance/decommissioning review workflows.
- A deterministic prompt quality report for uncertainty preservation and
  provenance completeness.
- A deterministic prompt quality trend report backed by checked-in snapshots.
- A deterministic policy-lint trend report backed by checked-in snapshots.
- A deterministic matrix coverage report for prompt matrix coverage across
  domain prompt workflows.
- Deterministic quality threshold checks for release-review baselines,
  including non-blocking policy-lint advisory thresholds.
- Deterministic release-review inventory reports for golden outputs and
  examples, candidate workspace fixtures, and provenance coverage.
- Deterministic provenance distribution and portfolio fixture coverage reports
  for release reviewers.
- Fixture-to-VeritySpec conversion checklist and cross-workspace reference
  syntax guidance for generated workspace drafts.
- A deterministic aggregate release-summary report for release reviewers.
- Image input manifest schema validation for example workflows.
- A deterministic release-integrity check for package and documentation
  version bookkeeping.
- A deterministic workflow hygiene check for GitHub Actions versions.
- A deterministic decision-policy linter with error and warning severities for
  high-stakes invention risks and advisory prompt-workflow consistency.
- An optional local VeritySpec smoke check that runs when `verity` is
  available and skips cleanly when it is not installed.
- Prompt quality and uncertainty-preservation evaluation guidance.
- Canonical AI-agent operating instructions in `AGENTS.md`.
- GitHub Actions CI that validates the library without calling external AI
  APIs.

## Installation

Install the latest GitHub release:

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.19.0"
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
verityfoundry list profiles
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate matrices
verityfoundry validate examples
verityfoundry validate goldens
verityfoundry lint decision-policy
verityfoundry report prompt-quality
verityfoundry report prompt-quality-trend
verityfoundry report policy-lint-trend
verityfoundry report matrix-coverage
verityfoundry report release-summary
verityfoundry report golden-inventory
verityfoundry report example-inventory
verityfoundry report fixture-inventory
verityfoundry report provenance-coverage
verityfoundry report provenance-distribution
verityfoundry report portfolio-coverage
verityfoundry check verityspec
verityfoundry check release-integrity
verityfoundry check quality-thresholds
verityfoundry check workflow-hygiene
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile codex
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile github-copilot
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

## Render Profiles

Render profiles add deterministic agent handoff guidance without calling any AI
API or changing the underlying prompt workflow.

```bash
verityfoundry list profiles
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile codex
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile github-copilot
verityfoundry render --prompt unity-game.gdd-art.interview-medium.implementation-ready.v1 --profile unity-ai
```

Supported profiles are `default`, `codex`, `claude-code`, `chatgpt`, `gemini`,
`github-copilot`, and `unity-ai`.

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
verityfoundry matrix lifecycle
```

## Golden Outputs

Golden outputs are deterministic examples of expected prompt behavior. They
are not truth claims and do not replace VeritySpec validation or human review.

The current golden fixtures cover Unity game, Unity shared-library, and
lifecycle review workflows:

```text
goldens/unity-game/dream-extraction-implementation-ready/
goldens/unity-shared-library/shared-unity-runtime-implementation-ready/
goldens/lifecycle/customer-portal-release-readiness/
goldens/lifecycle/customer-portal-archival-readiness/
goldens/lifecycle/shared-auth-maintenance-readiness/
goldens/lifecycle/shared-unity-runtime-decommission-readiness/
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
verityfoundry report prompt-quality-trend
verityfoundry report policy-lint-trend
```

The report is an inspection aid, not a readiness certification.

Trend snapshots live under `snapshots/prompt-quality/` so release reviewers can
see whether prompt quality moved relative to a checked-in baseline.

Policy-lint snapshots live under `snapshots/policy-lint/` so release reviewers
can see whether decision-policy advisory counts changed relative to a checked
baseline.

## Matrix Coverage Report

The matrix coverage report shows how domain prompt workflows are represented in
the prompt matrices. It reports covered domain prompts, uncovered domain
prompts, domain summaries, and unknown matrix references.

```bash
verityfoundry report matrix-coverage
verityfoundry report matrix-coverage --format json
```

The report is deterministic and does not call external AI APIs.

## Quality Thresholds

Quality threshold checks compare prompt quality, matrix coverage, and
policy-lint counts against
`config/release-quality-thresholds.json`.

```bash
verityfoundry check quality-thresholds
verityfoundry check quality-thresholds --format json
```

Thresholds are intentionally conservative baselines. Raising them should be an
explicit sprint decision backed by the current reports.
Policy-lint warning thresholds are non-blocking advisories; policy-lint error
thresholds remain blocking.

## Release Reviewer Reports

Release reviewer reports summarize examples, golden outputs, candidate
workspace fixtures, provenance coverage, provenance distribution, and
portfolio coverage without calling external AI APIs.

```bash
verityfoundry report release-summary
verityfoundry report policy-lint-trend
verityfoundry report golden-inventory
verityfoundry report example-inventory
verityfoundry report fixture-inventory
verityfoundry report provenance-coverage
verityfoundry report provenance-distribution
verityfoundry report portfolio-coverage
```

Use these reports to confirm release integrity, quality thresholds, workflow
hygiene, matrix coverage, examples, golden outputs, fixture record kinds,
recommended VeritySpec pack mappings, provenance examples, decision-source
distribution, and portfolio dependency assumptions in scope for a release
review. They do not replace manifest validation, VeritySpec validation, or
human review.

Checked release-review JSON fixtures live under
`fixtures/release-review/current/` for downstream tooling examples and drift
review.

## Release Integrity Check

Release integrity checks compare release-facing version references across
package metadata and public docs.

```bash
verityfoundry check release-integrity
verityfoundry check release-integrity --expected-version 0.19.0
verityfoundry check release-integrity --format json
```

The check is intended to run from a source checkout because it inspects
`README.md`, `CHANGELOG.md`, `ROADMAP.md`, `pyproject.toml`, release notes, and
the release checklist.

## Workflow Hygiene Check

Workflow hygiene checks scan `.github/workflows/` for action versions that are
below the repository's current minimums.

```bash
verityfoundry check workflow-hygiene
verityfoundry check workflow-hygiene --format json
```

This is a source-checkout check. It helps catch stale action versions before
they reintroduce known runner annotations.

## Decision Policy Lint

Decision-policy linting checks domain prompts for controls that reduce
high-stakes invention risk. It reports blocking `error` findings and
non-blocking `warning` advisories.

```bash
verityfoundry lint decision-policy
verityfoundry lint decision-policy --format json
```

High-risk prompts must preserve human approval, decision policy references,
safety and uncertainty guidance, provenance guidance, and the appropriate
high-stakes or all-questions interview mode include.

Warning-only advisory output exits successfully and is intended for release
review visibility.

## VeritySpec Smoke Check

VerityFoundry can run a local optional smoke check against the VeritySpec CLI:

```bash
verityfoundry check verityspec
verityfoundry check verityspec --workspace <generated-workspace>
verityfoundry check verityspec --format json
```

If `verity` is not installed, the command reports `skipped` and exits
successfully. If `verity` is available and a workspace is provided or detected,
the command runs `verity validate` against that workspace. This check does not
make VeritySpec a required dependency of VerityFoundry.

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

## Lifecycle Readiness Workflow

Lifecycle prompts support release-readiness gap review, shipped-product
maintenance interviews, decommissioning interviews, and archival-readiness
interviews for candidate VeritySpec workspaces.

Expected outputs include release gap reports, blocking questions, maintenance
handoff questions, decommissioning questions, archival evidence gaps,
unresolved decisions, approval registers, and suggested VeritySpec validation
loops.

These workflows do not certify readiness. They preserve uncertainty so humans
and VeritySpec readiness gates can decide what is actually ready.

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
verityfoundry check verityspec --workspace <generated-workspace>
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

## AI-Agent Usage

AI agents should start with `AGENTS.md`. Agent-specific files such as
`CODEX.md`, `CHATGPT.md`, `CLAUDE.md`, `GEMINI.md`, `UNITY_AI.md`, and
`.github/copilot-instructions.md` are adapters that point back to the
canonical instructions.

Agents must preserve uncertainty. Generated records and reports should
distinguish human-provided decisions, AI-inferred decisions, AI-defaulted
decisions, AI-suggested decisions, unresolved decisions, and decisions that
require human approval.

## Documentation

- [Architecture](docs/architecture.md)
- [Prompt manifests](docs/prompt-manifests.md)
- [Render profiles](docs/render-profiles.md)
- [Decision policy lint](docs/decision-policy-lint.md)
- [v0.x stabilization checklist](docs/v0x-stabilization-checklist.md)
- [Matrix coverage](docs/matrix-coverage.md)
- [Prompt quality trends](docs/prompt-quality-trends.md)
- [Policy lint trends](docs/policy-lint-trends.md)
- [Quality thresholds](docs/quality-thresholds.md)
- [Workflow hygiene](docs/workflow-hygiene.md)
- [Workflow hygiene history](docs/workflow-hygiene-history.md)
- [Action version policy](docs/action-version-policy.md)
- [Release integrity](docs/release-integrity.md)
- [Release integrity report schema](docs/release-integrity-report-schema.md)
- [Report schema stability](docs/report-schema-stability.md)
- [Release summary report](docs/release-summary-report.md)
- [Release reviewer checklist](docs/release-reviewer-checklist.md)
- [Quality threshold ratcheting](docs/quality-threshold-ratcheting.md)
- [Release reviewer inventory reports](docs/reviewer-inventory-reports.md)
- [Release-review fixtures](docs/release-review-fixtures.md)
- [Fixture inventory report schema](docs/fixture-inventory-report-schema.md)
- [Example fixture diff snapshots](docs/example-fixture-diff-snapshots.md)
- [Fixture kind pack mapping](docs/fixture-kind-pack-mapping.md)
- [Provenance coverage](docs/provenance-coverage.md)
- [Provenance distribution](docs/provenance-distribution.md)
- [Portfolio coverage report](docs/portfolio-coverage-report.md)
- [Golden output drift review](docs/golden-output-drift-review.md)
- [Workspace fixtures](docs/workspace-fixtures.md)
- [Fixture to VeritySpec checklist](docs/fixture-to-verityspec-checklist.md)
- [Portfolio workflows](docs/portfolio-workflows.md)
- [Cross-workspace reference guidance](docs/cross-workspace-reference-guidance.md)
- [Lifecycle readiness workflows](docs/lifecycle-readiness-workflows.md)
- [Lifecycle gap reports to VeritySpec records](docs/lifecycle-gap-to-verityspec.md)
- [Prompt workflow contributions](docs/prompt-workflow-contributions.md)
- [Interview modes](docs/interview-modes.md)
- [Readiness targets](docs/readiness-targets.md)
- [Decision provenance](docs/decision-provenance.md)
- [Image input guidance](docs/image-input-guidance.md)
- [Unity game workflows](docs/unity-game-workflows.md)
- [Unity shared-library workflows](docs/unity-shared-library-workflows.md)
- [Golden output guidelines](evaluations/golden-output-guidelines.md)
- [Render profile compatibility](docs/render-profile-compatibility.md)
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
- [v0.19.0 release notes](docs/release-notes-v0.19.0.md)
- [v0.18.0 release notes](docs/release-notes-v0.18.0.md)
- [v0.17.0 release notes](docs/release-notes-v0.17.0.md)
- [v0.16.0 release notes](docs/release-notes-v0.16.0.md)
- [v0.15.0 release notes](docs/release-notes-v0.15.0.md)
- [v0.14.0 release notes](docs/release-notes-v0.14.0.md)
- [v0.13.0 release notes](docs/release-notes-v0.13.0.md)
- [v0.12.0 release notes](docs/release-notes-v0.12.0.md)
- [v0.11.0 release notes](docs/release-notes-v0.11.0.md)
- [v0.10.0 release notes](docs/release-notes-v0.10.0.md)
- [v0.9.0 release notes](docs/release-notes-v0.9.0.md)
- [v0.8.0 release notes](docs/release-notes-v0.8.0.md)
- [v0.7.0 release notes](docs/release-notes-v0.7.0.md)
- [v0.6.0 release notes](docs/release-notes-v0.6.0.md)
- [v0.5.0 release notes](docs/release-notes-v0.5.0.md)
- [v0.4.0 release notes](docs/release-notes-v0.4.0.md)
- [v0.3.0 release notes](docs/release-notes-v0.3.0.md)
- [v0.2.0 release notes](docs/release-notes-v0.2.0.md)
- [v0.1.0 release notes](docs/release-notes-v0.1.0.md)
