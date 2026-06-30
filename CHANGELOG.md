# Changelog

## Unreleased

- Added `verityfoundry report policy-lint-trend` with a checked v0.17.0
  policy-lint warning baseline snapshot.
- Added non-blocking policy-lint warning thresholds to
  `verityfoundry check quality-thresholds`.
- Added render-to-file CLI smoke coverage for every supported agent profile.
- Added fixture inventory report schema, example fixture diff snapshot, and
  policy-lint trend documentation.

## 0.17.0

- Added `verityfoundry report release-summary` to aggregate deterministic
  release-review checks and inventory counts.
- Added release-summary, workflow-hygiene history, action-version policy,
  quality-threshold ratcheting, and render-profile compatibility
  documentation.
- Added release-summary coverage to CI, release workflow smoke checks,
  README, release checklist, release reviewer checklist, and AI-agent
  guidance.

## 0.16.0

- Added lifecycle golden output fixtures for release-readiness,
  maintenance-readiness, and decommission-readiness review workflows.
- Added documentation for translating lifecycle gap reports into VeritySpec
  evidence/readiness records.
- Added release-integrity JSON report schema notes, report schema stability
  guidance, and a combined release reviewer checklist.
- Updated packaged artifact coverage and tests for lifecycle golden outputs.

## 0.15.0

- Added portfolio example manifests and workspace fixtures for multi-game
  triage inputs and expected outputs.
- Added cross-workspace dependency fixture examples for shared Unity runtime
  consumers.
- Updated fixture kind pack mapping, packaged artifact coverage, inventory
  report expectations, README, and roadmap for the new portfolio examples.

## 0.14.0

- Added `verityfoundry report fixture-inventory` and
  `verityfoundry report provenance-coverage` for release reviewers.
- Added image input manifest schema validation for example workflows.
- Added packaged fixture-file tests to prove declared example files are
  included in built distributions.
- Added fixture kind pack mapping and provenance coverage documentation.

## 0.13.0

- Added a dedicated `github-copilot` render profile for GitHub Copilot
  handoff.
- Added policy-lint severity counts with non-blocking warning advisories.
- Added tests proving high-risk prompts render safety and provenance sections
  under every non-default agent profile.
- Added a v0.x stabilization checklist covering CLI output, manifest
  compatibility, report schema compatibility, and release discipline.

## 0.12.0

- Added `verityfoundry report prompt-quality-trend` for deterministic
  comparison against checked-in prompt-quality snapshots.
- Added `verityfoundry check quality-thresholds` for release-review prompt
  quality and matrix coverage baselines.
- Added `verityfoundry check workflow-hygiene` for GitHub Actions action
  version hygiene.
- Added checked-in release-quality threshold configuration, a v0.11.0 prompt
  quality baseline snapshot, documentation, CI coverage, release checklist
  coverage, and AI-agent guidance for release hardening.

## 0.11.0

- Added `verityfoundry check release-integrity` for deterministic package,
  README, changelog, roadmap, release checklist, and release-note version
  checks.
- Added `verityfoundry report golden-inventory` and
  `verityfoundry report example-inventory` for release reviewers.
- Added release integrity, release reviewer inventory, and golden output drift
  review documentation.
- Added CI, release-checklist, and AI-agent guidance coverage for the new
  release-review commands.

## 0.10.0

- Added lifecycle prompt workflows for release-readiness gap review,
  shipped-product maintenance interviews, and decommissioning interviews.
- Added a lifecycle prompt matrix and matrix coverage for the new lifecycle
  domain.
- Added lifecycle readiness workflow documentation and packaged prompt-library
  coverage for installed CLI inspection.

## 0.9.0

- Added portfolio prompt workflows for game portfolio triage and
  cross-workspace dependency mapping.
- Added a portfolio prompt matrix and matrix coverage for the new domain.
- Added portfolio workflow documentation covering authority boundaries,
  dependency assumptions, lockfile questions, and triage outputs.

## 0.8.0

- Added candidate workspace fixture references to example manifests.
- Added expected record-category validation for example workspace fixtures.
- Added provenance example files for all examples.
- Added an image-input manifest fixture for the Unity game example.
- Added workspace fixture conversion documentation for VeritySpec handoff.

## 0.7.0

- Added `verityfoundry lint decision-policy` with text and JSON output.
- Added deterministic render profiles for Codex, Claude Code, ChatGPT,
  Gemini, and Unity AI prompt handoff.
- Updated high-risk prompt manifests to include safety and provenance rules.
- Added prompt workflow contribution guidance for policy linting and render
  profiles.
- Bundled prompt, matrix, schema, example, and golden-output artifacts in the
  installable wheel so the CLI can inspect the prompt library outside a source
  checkout.

## 0.6.0

- Added software-library and product examples for a shared authentication
  library and customer portal.
- Added `verityfoundry report matrix-coverage` with text and JSON output.
- Updated standard CI, release, README, roadmap, and agent guidance for
  week-sized grouped sprints and matrix coverage checks.

## 0.5.0

- Added `verityfoundry check verityspec`, an optional local VeritySpec smoke
  check that skips when `verity` is unavailable and runs `verity validate`
  when a workspace is provided or detected.
- Added tests, CI coverage, release workflow coverage, README guidance, and
  VeritySpec handoff documentation for the optional smoke check.

## 0.4.0

- Added a deterministic prompt quality report for uncertainty preservation and
  provenance completeness.
- Added `verityfoundry report prompt-quality` with text and JSON output.
- Updated CI, README, agent guidance, release checklist, and evaluation docs
  for prompt quality reporting.

## 0.3.0

- Added the Unity shared-library implementation-ready golden output fixture for
  Shared Unity Runtime.
- Added tests proving the shared-library golden fixture exists and validates.
- Updated README, roadmap, and golden output guidance for the second checked
  golden fixture.

## 0.2.0

- Added the first Unity game implementation-ready golden output fixture and
  golden output manifest validation.
- Added `verityfoundry validate goldens` CLI coverage.
- Updated CI, README, agent guidance, roadmap, and golden output guidance for
  deterministic golden fixture validation.

## 0.1.0

- Added the initial VerityFoundry repository scaffold.
- Added prompt, matrix, example, and decision policy schemas.
- Added deterministic local CLI validation and rendering helpers.
- Added Unity game and Unity shared-library prompt matrices and examples.
- Added AI-agent guidance, project-management docs, tests, and CI.
- Added v0.1.0 release notes and GitHub release workflow.
