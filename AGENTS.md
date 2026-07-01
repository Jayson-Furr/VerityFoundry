# AI Agent Entry Point

This is the canonical instruction file for AI agents working in this
repository. Agent-specific files are adapters only; if they conflict with this
file, `AGENTS.md` wins.

This entry point is intended for Codex, GitHub Copilot, Claude, Claude Code,
ChatGPT, Gemini, Unity AI, and other coding agents.

## Project Identity

VerityFoundry is the AI-assisted authoring and prompt workflow layer for
VeritySpec. It helps fabricate, interview for, refine, and gap-review candidate
VeritySpec workspace drafts from rough inputs.

The core promise is:

> Turn rough intent into validated VeritySpec workspace drafts.

VerityFoundry does not replace VeritySpec. VeritySpec remains the contract
engine and validation authority.

## Architecture Summary

The repository is a Python package with a CLI named `verityfoundry`.

Core concepts:

- Prompt manifest: JSON front matter describing a prompt workflow.
- Matrix manifest: machine-readable rows that combine domain, input,
  interview mode, target readiness, and output type.
- Example manifest: example inputs and expected authoring outputs.
- Decision policy: rules for what AI may infer, default, suggest, ask, leave
  unresolved, require approval for, or must not invent.
- Renderer: deterministic prompt assembly for local inspection.
- Validator: local checks for manifests, examples, matrices, and prompt
  references.
- Linter: deterministic decision-policy checks for high-stakes invention
  risks, with blocking errors and non-blocking advisory warnings.
- Agent handoff: deterministic render profiles for Codex, Claude Code,
  ChatGPT, Gemini, GitHub Copilot, and Unity AI.
- Reports: deterministic prompt quality and matrix coverage inspection.
- Release checks: deterministic release/version bookkeeping checks.
- Release-review reports: deterministic golden output and example inventory
  reports.
- Release hardening: deterministic prompt quality trends, quality thresholds,
  and workflow hygiene checks.

Keep the utility package small. The repository is primarily a prompt workflow
library, not an AI application and not a VeritySpec replacement.

## Working Rules

- Keep the repository releasable after every sprint.
- Update tests, examples, docs, CI, roadmap entries, and changelog entries
  with behavior changes.
- Keep `README.md` aligned with `CHANGELOG.md`, `ROADMAP.md`, release notes,
  install instructions, version references, and public bookkeeping.
- When the active roadmap is caught up, plan up to the next 20 roadmap points
  for fixing, improving, continuing, and expanding the project.
- Follow the repository branching strategy in `docs/branching.md`.
- After each commit, refresh agent context by re-reading this file and checking
  `git status --short --branch` and the latest commit.
- At the entry point, determine whether commands should run under `zsh`,
  `bash`, or PowerShell, then keep command syntax consistent with that shell.
- Prefer sprints that bundle about a week of related work into a coherent
  releasable increment. Avoid turning every small roadmap point into a
  separate release when related work can be reviewed and verified together.
- Do not commit secrets, tokens, API keys, private product data, or local
  environment files.
- Do not call external AI APIs in tests or CI.
- Do not publish releases or packages unless the user explicitly asks.
- Preserve user changes. Do not revert unrelated dirty files.
- Use structured JSON parsing/writing for JSON artifacts.
- Keep documentation command examples executable from a clean checkout.
- If GitHub workflow checks cannot run or fail because of billing, credits,
  quota, runner availability, or another platform issue, verify equivalent
  checks locally, record that CI was unavailable for external reasons, and
  continue from the local evidence.

## Prompt Safety and Uncertainty Rules

The main risk is AI converting uncertainty into fake certainty. Preserve
uncertainty explicitly.

Prompt workflows must distinguish:

- human-provided decisions
- AI-inferred decisions
- AI-defaulted decisions
- AI-suggested decisions
- unresolved decisions
- human-approval-required decisions

Generated outputs should include source references, assumptions, decision
provenance, confidence, unresolved questions, human approval requirements, and
readiness gaps.

Do not claim generated workspaces are production-ready, implementation-ready,
legally compliant, platform approved, commercially cleared, privacy safe, or
archived unless the input evidence supports that claim and human approval is
recorded.

## Shell Discipline

At the start of work, determine the command shell before running repository
commands. Use one of:

- `zsh`: normal local shell on macOS developer machines.
- `bash`: normal shell for GitHub Actions and portable Unix-like scripts.
- PowerShell: Windows or explicitly PowerShell-based automation.

Maintain that shell discipline until there is a concrete reason to switch.

## Required Operating Loop

1. Start by reading this file, checking `git status --short --branch`, checking
   the latest commit, confirming the active shell, and identifying the active
   issue, milestone, branch, and roadmap section.
2. Convert substantive work into a public sprint, release, feature, fix, or
   docs branch with a GitHub issue and milestone before implementation when
   the work is not already tracked.
3. Keep work in small executable increments. Read relevant files first and
   follow existing patterns.
4. Update behavior, tests, examples, docs, README, changelog, roadmap, release
   notes, workflow templates, and public version references together when they
   are part of the same change.
5. Run focused checks first when useful, then standard local checks.
6. Commit only after local verification. After every commit, re-read this file,
   check `git status --short --branch`, and check the latest commit.
7. Push the branch, open a PR with a concise summary and exact local
   verification, then watch GitHub Actions until checks pass or fail.
8. If GitHub Actions is unavailable for external platform reasons, run and
   record equivalent local checks in the PR and continue from that evidence.
9. Merge only after checks pass or the local-verification fallback is recorded.
10. When the active roadmap is caught up, keep the Next 20 roadmap planning
    section populated.

## Standard Local Checks

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools
pip install -e .

python -m unittest discover -s tests -v
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
git diff --check
```

## Common Commands

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
verityfoundry matrix unity-game
```

## Important Files

- `README.md`: public overview and quick start.
- `ROADMAP.md`: sprint roadmap and Next 20 planning points.
- `CHANGELOG.md`: release-facing change log.
- `src/verityfoundry/cli.py`: CLI contract and command wiring.
- `src/verityfoundry/manifests.py`: manifest discovery and parsing.
- `src/verityfoundry/validation.py`: local validation checks.
- `src/verityfoundry/rendering.py`: deterministic prompt rendering.
- `src/verityfoundry/quality.py`: deterministic prompt quality reporting.
- `src/verityfoundry/quality_trend.py`: prompt quality trend reporting.
- `src/verityfoundry/matrix_coverage.py`: deterministic matrix coverage reporting.
- `src/verityfoundry/inventory.py`: deterministic release-review inventory reports.
- `src/verityfoundry/policy_lint.py`: deterministic decision-policy linting.
- `src/verityfoundry/policy_lint_trend.py`: policy-lint trend reporting.
- `src/verityfoundry/integration.py`: optional local companion-tool checks.
- `src/verityfoundry/release_integrity.py`: release/version bookkeeping checks.
- `src/verityfoundry/thresholds.py`: release quality threshold checks.
- `src/verityfoundry/workflow_hygiene.py`: GitHub Actions hygiene checks.
- `config/`: release-review threshold configuration.
- `snapshots/`: checked-in release-review snapshots.
- `fixtures/`: checked release-review JSON fixtures.
- `schemas/`: JSON schemas for manifests.
- `prompts/`: prompt workflow library.
- `matrices/`: prompt matrices.
- `examples/`: example inputs and expected outputs.
- `goldens/`: deterministic prompt output fixtures.
- `evaluations/`: prompt quality guidance.
- `tests/`: executable coverage.
- `.github/workflows/ci.yml`: CI contract.

## Release Rules

- Version lives in both `pyproject.toml` and `src/verityfoundry/__init__.py`.
- Release tags use `vMAJOR.MINOR.PATCH`.
- Do not create tags, GitHub releases, or package publishes without explicit
  user direction.

## Agent Adapter Policy

Agent-specific files such as `CODEX.md`, `CHATGPT.md`, `CLAUDE.md`,
`GEMINI.md`, `UNITY_AI.md`, and `.github/copilot-instructions.md` should remain
thin pointers to this file.
