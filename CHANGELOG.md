# Changelog

## Unreleased

No unreleased changes.

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
