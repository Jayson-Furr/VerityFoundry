# Roadmap

VerityFoundry is the prompt workflow companion to VeritySpec. It fabricates,
interviews for, refines, and gap-reviews candidate VeritySpec workspace drafts
while preserving uncertainty and human approval requirements.

## v0.1.0

The `v0.1.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 1 | Complete | Repository scaffold, AI-agent entry point, prompt manifest schema, and basic validation CLI |
| 2 | Complete | Interview modes and readiness target documentation |
| 3 | Complete | Unity game prompt matrix and examples |
| 4 | Complete | Unity shared-library prompt matrix and examples |
| 5 | Complete | Decision policy and provenance rules hardening |
| 6 | Complete | Golden output examples and prompt quality rubric |
| 7 | Complete | VeritySpec integration documentation and generated workspace validation notes |
| 8 | Complete | v0.1.0 release preparation |

## Sprint 1 Priorities

- Create the installable `verityfoundry` package and CLI.
- Add machine-checkable prompt, matrix, example, and decision-policy schemas.
- Add the canonical `AGENTS.md` entry point and thin agent adapters.
- Add CI and local tests for deterministic repository validation.
- Add public project metadata and basic documentation.

## Sprint 8 Priorities

Sprint 8 should release the completed `v0.1.0` scope:

- Add v0.1.0 release notes.
- Update README release badge, latest-release text, install guidance, and
  release-notes link to `v0.1.0`.
- Add a GitHub release workflow that builds, checks, smoke-tests, uploads
  release assets, and creates the GitHub release on tags.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Tag and publish the v0.1.0 GitHub release when checks pass.
- Close the v0.1.0 milestone after release verification.

## v0.2.0

The `v0.2.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 9 | Complete | Unity game implementation-ready golden output fixture |
| 10 | Complete | v0.2.0 release preparation |

## Sprint 9 Priorities

Sprint 9 should add the first deterministic golden output fixture:

- Add a golden output manifest schema and validator.
- Add `verityfoundry validate goldens`.
- Add a Unity game implementation-ready golden output fixture for Dream
  Extraction.
- Require golden outputs to preserve assumptions, unresolved decisions, human
  approval requirements, readiness gaps, and the VeritySpec validation loop.
- Add tests for golden manifest validation and CLI coverage.
- Update README, changelog, roadmap, and golden output guidance.
- Keep the Next 20 roadmap points populated after converting this item.

## Sprint 10 Priorities

Sprint 10 should release the completed `v0.2.0` scope:

- Add v0.2.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.2.0`.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Tag and publish the v0.2.0 GitHub release when checks pass.
- Close the v0.2.0 milestone after release verification.

## v0.3.0

The `v0.3.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 11 | Complete | Unity shared-library implementation-ready golden output fixture |
| 12 | Complete | v0.3.0 release preparation |

## Sprint 11 Priorities

Sprint 11 should add the next deterministic golden output fixture:

- Add a Unity shared-library implementation-ready golden output fixture for
  Shared Unity Runtime.
- Require the output to preserve assumptions, unresolved decisions, human
  approval requirements, public/exported versus internal/private uncertainty,
  readiness gaps, and the VeritySpec validation loop.
- Add tests proving the fixture exists and validates.
- Update README, changelog, roadmap, and golden output guidance.
- Keep the Next 20 roadmap points populated after converting this item.

## Sprint 12 Priorities

Sprint 12 should release the completed `v0.3.0` scope:

- Add v0.3.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.3.0`.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Tag and publish the v0.3.0 GitHub release when checks pass.
- Close the v0.3.0 milestone after release verification.

## v0.4.0

The `v0.4.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 13 | Complete | Prompt quality report for uncertainty and provenance evidence |
| 14 | Complete | v0.4.0 release preparation |

## Sprint 13 Priorities

Sprint 13 should add the first deterministic quality report:

- Add local prompt quality scoring for uncertainty preservation and provenance
  completeness.
- Add `verityfoundry report prompt-quality` with text and JSON output.
- Keep the report deterministic and free of external AI API calls.
- Add tests for scoring and CLI output.
- Update README, docs, CI, agent guidance, changelog, and roadmap.
- Keep the Next 20 roadmap points populated after converting this item.

## Sprint 14 Priorities

Sprint 14 should release the completed `v0.4.0` scope:

- Add v0.4.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.4.0`.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Tag and publish the v0.4.0 GitHub release when checks pass.
- Close the v0.4.0 milestone after release verification.

## v0.5.0

The `v0.5.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 15 | Complete | Optional VeritySpec integration smoke check |
| 16 | Complete | v0.5.0 release preparation |

## Sprint 15 Priorities

Sprint 15 should add an optional local VeritySpec integration smoke check:

- Add `verityfoundry check verityspec`.
- Skip cleanly when the `verity` CLI is not installed.
- Run `verity validate` when `verity` is available and a workspace is provided
  or detected.
- Keep VeritySpec optional; do not add it as a package dependency.
- Add tests for skipped, passed, and failed smoke-check behavior.
- Update README, docs, CI, release workflow smoke checks, agent guidance,
  changelog, and roadmap.
- Keep the Next 20 roadmap points populated after converting this item.

## Sprint 16 Priorities

Sprint 16 should release the completed `v0.5.0` scope:

- Add v0.5.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.5.0`.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Tag and publish the v0.5.0 GitHub release when checks pass.
- Close the v0.5.0 milestone after release verification.

## v0.6.0

The `v0.6.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 17 | Complete | Example expansion and matrix coverage reporting bundle |
| 18 | Complete | v0.6.0 release preparation |

## Sprint 17 Priorities

Sprint 17 should bundle about a week of related work into one coherent
release increment:

- Add a software-library example for a shared authentication package.
- Add a product example for a customer portal.
- Add `verityfoundry report matrix-coverage` with text and JSON output.
- Include matrix coverage in CI, release workflow smoke tests, local checks,
  README, and agent guidance.
- Document the grouped sprint model so routine roadmap work can be bundled
  into about one week of related work instead of one release per small item.
- Update changelog and roadmap.
- Keep the Next 20 roadmap points populated after converting completed or
  stale items.

## Sprint 18 Priorities

Sprint 18 should release the completed `v0.6.0` scope:

- Add v0.6.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.6.0`.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Tag and publish the v0.6.0 GitHub release when checks pass.
- Close the v0.6.0 milestone after release verification.

## v0.7.0

The `v0.7.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 19 | Complete | Policy linting and agent handoff profiles |
| 20 | Complete | v0.7.0 release preparation |

## Sprint 19 Priorities

Sprint 19 should bundle related policy and handoff work:

- Add `verityfoundry lint decision-policy` with text and JSON output.
- Enforce decision policy, safety, provenance, human approval, and interview
  mode controls for high-risk prompt workflows.
- Add deterministic render profiles for Codex, Claude Code, ChatGPT, Gemini,
  and Unity AI.
- Add `verityfoundry list profiles`.
- Update high-risk prompt manifests to include safety and provenance rules.
- Add contributor guidance for prompt workflow policy expectations.
- Update README, docs, CI, release workflow smoke checks, agent guidance,
  changelog, and roadmap.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 20 Priorities

Sprint 20 should release the completed `v0.7.0` scope:

- Add v0.7.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.7.0`.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Verify the installed wheel from outside the source checkout so packaged
  prompt-library artifacts cannot drift.
- Tag and publish the v0.7.0 GitHub release when checks pass.
- Close the v0.7.0 milestone after release verification.

## v0.8.0

The `v0.8.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 21 | Complete | Workspace fixture readiness |
| 22 | Complete | v0.8.0 release preparation |

## Sprint 21 Priorities

Sprint 21 should bundle related workspace-fixture readiness work:

- Add example manifests that reference candidate VeritySpec workspace files.
- Add generated workspace outline validation for expected record categories.
- Add image-input manifest fixtures for concept art and identity images.
- Add provenance examples aligned with future VeritySpec evidence records.
- Add docs explaining how to convert VerityFoundry expected outputs into
  concrete VeritySpec workspace fixtures.
- Keep packaged artifact coverage aligned so installed wheels include the new
  fixture files.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 22 Priorities

Sprint 22 should release the completed `v0.8.0` scope:

- Add v0.8.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.8.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.8.0 GitHub release when checks pass.
- Close the v0.8.0 milestone after release verification.

## v0.9.0

The `v0.9.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 23 | Complete | Cross-workspace and portfolio workflows |
| 24 | Complete | v0.9.0 release preparation |

## Sprint 23 Priorities

Sprint 23 should bundle related multi-workspace and portfolio work:

- Add cross-workspace dependency prompt guidance for shared Unity libraries
  and game portfolios.
- Add portfolio triage prompts for batches of many game concepts.
- Add matrix coverage for the new portfolio workflow domain.
- Document dependency assumptions, lockfile questions, exported-record
  assumptions, triage outputs, and VeritySpec authority boundaries.
- Update tests, README, changelog, roadmap, and packaged artifact coverage.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 24 Priorities

Sprint 24 should release the completed `v0.9.0` scope:

- Add v0.9.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.9.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.9.0 GitHub release when checks pass.
- Close the v0.9.0 milestone after release verification.

## v0.10.0

The `v0.10.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 25 | Complete | Lifecycle readiness prompt workflows |
| 26 | Complete | v0.10.0 release preparation |

## Sprint 25 Priorities

Sprint 25 should bundle related lifecycle-readiness work:

- Add release-readiness gap review prompts for generated VeritySpec
  workspaces.
- Add maintenance and decommissioning interview flows for shipped products.
- Add lifecycle matrix coverage for release, maintenance, and
  decommissioning workflows.
- Document lifecycle authority boundaries: VerityFoundry interviews and
  gap-reviews, while VeritySpec and humans remain readiness authorities.
- Update tests, README, changelog, roadmap, and packaged artifact coverage.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 26 Priorities

Sprint 26 should release the completed `v0.10.0` scope:

- Add v0.10.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.10.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.10.0 GitHub release when checks pass.
- Close the v0.10.0 milestone after release verification.

## v0.11.0

The `v0.11.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 27 | Complete | Release integrity and reviewer reports |
| 28 | Complete | v0.11.0 release preparation |

## Sprint 27 Priorities

Sprint 27 should bundle related release-review tooling:

- Add release-integrity checks for README, changelog, roadmap, package
  metadata, release checklist, and release notes.
- Add golden output inventory reporting for maintainers and release reviewers.
- Add example inventory reporting for release reviewers.
- Add golden output drift review documentation for maintainers.
- Update CI, release checklist, README, changelog, roadmap, tests, and
  agent guidance for the new commands.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 28 Priorities

Sprint 28 should release the completed `v0.11.0` scope:

- Add v0.11.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.11.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.11.0 GitHub release when checks pass.
- Close the v0.11.0 milestone after release verification.

## v0.12.0

The `v0.12.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 29 | Complete | Release-review hardening checks |
| 30 | Complete | v0.12.0 release preparation |

## Sprint 29 Priorities

Sprint 29 should bundle about a week of release-review hardening work:

- Add prompt quality trend snapshots for release reviewers.
- Add release-quality threshold checks for prompt quality and matrix coverage.
- Add workflow hygiene checks for stale or risky GitHub Actions versions.
- Keep the checks deterministic and free of external AI API calls.
- Include source-checkout CI coverage and installed-wheel smoke coverage where
  the packaged artifact contains the required data.
- Update README, docs, CI, release checklist, changelog, roadmap, tests, and
  agent guidance for the new commands.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 30 Priorities

Sprint 30 should release the completed `v0.12.0` scope:

- Add v0.12.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.12.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.12.0 GitHub release when checks pass.
- Close the v0.12.0 milestone after release verification.

## v0.13.0

The `v0.13.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 31 | Complete | Stabilization and agent handoff hardening |
| 32 | Complete | v0.13.0 release preparation |

## Sprint 31 Priorities

Sprint 31 should bundle about a week of stabilization and agent-handoff work:

- Add a v0.x stabilization checklist for CLI output compatibility, manifest
  compatibility, report schema compatibility, and release discipline.
- Add a dedicated GitHub Copilot render profile.
- Add policy lint severity levels and warning-only advisory checks.
- Add tests that verify high-risk prompts render safety and provenance
  sections under every non-default agent profile.
- Update README, docs, changelog, roadmap, tests, and agent guidance.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 32 Priorities

Sprint 32 should release the completed `v0.13.0` scope:

- Add v0.13.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.13.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.13.0 GitHub release when checks pass.
- Close the v0.13.0 milestone after release verification.

## v0.14.0

The `v0.14.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 33 | Complete | Fixture inventory, provenance coverage, image-input validation, and packaged fixture tests |
| 34 | Complete | v0.14.0 release preparation |

## Sprint 33 Priorities

Sprint 33 should bundle about a week of fixture and release-review work:

- Add candidate workspace fixture inventory reports for release reviewers.
- Add provenance coverage reporting across example workspace fixtures.
- Add documentation mapping fixture `kind` values to recommended VeritySpec
  packs.
- Add schema validation for image-input manifests.
- Add tests proving packaged distributions include declared example fixture
  files.
- Include the new reports in CI, release workflow smoke tests, local checks,
  README, docs, changelog, roadmap, tests, and agent guidance.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 34 Priorities

Sprint 34 should release the completed `v0.14.0` scope:

- Add v0.14.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.14.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.14.0 GitHub release when checks pass.
- Close the v0.14.0 milestone after release verification.

## v0.15.0

The `v0.15.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 35 | Complete | Portfolio and cross-workspace dependency examples |
| 36 | Complete | v0.15.0 release preparation |

## Sprint 35 Priorities

Sprint 35 should bundle about a week of portfolio example work:

- Add portfolio example manifests for multi-game triage inputs and expected
  outputs.
- Add cross-workspace dependency fixture examples for shared Unity runtime
  consumers.
- Add candidate workspace fixtures and provenance examples for both workflows.
- Keep dependency aliases, exported-record status, version constraints,
  lockfiles, and canonical URI forms unresolved unless source inputs prove
  them.
- Update packaged artifact coverage, fixture kind pack mapping, inventory
  expectations, README, docs, changelog, roadmap, and tests.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 36 Priorities

Sprint 36 should release the completed `v0.15.0` scope:

- Add v0.15.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.15.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.15.0 GitHub release when checks pass.
- Close the v0.15.0 milestone after release verification.

## v0.16.0

The `v0.16.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 37 | Complete | Lifecycle golden outputs and release-review documentation |
| 38 | Complete | v0.16.0 release preparation |

## Sprint 37 Priorities

Sprint 37 should bundle about a week of lifecycle and release-review work:

- Add lifecycle golden output fixtures for release-readiness,
  maintenance-readiness, and decommission-readiness reviews.
- Add docs for translating lifecycle gap reports into VeritySpec evidence and
  readiness records.
- Add release-integrity JSON schema documentation for downstream tooling.
- Add report schema stability notes for release-review JSON outputs.
- Add a release reviewer checklist that combines integrity, inventory,
  prompt-quality, matrix-coverage, local VeritySpec smoke checks, and local CI
  fallback expectations.
- Update README, changelog, roadmap, tests, and packaged artifact coverage.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 38 Priorities

Sprint 38 should release the completed `v0.16.0` scope:

- Add v0.16.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.16.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.16.0 GitHub release when checks pass.
- Close the v0.16.0 milestone after release verification.

## v0.17.0

The `v0.17.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 39 | Complete | Release-summary report and release-review automation docs |
| 40 | Complete | v0.17.0 release preparation |

## Sprint 39 Priorities

Sprint 39 should bundle about a week of release-review automation work:

- Add a local `release-summary` report that aggregates release-review command
  results without invoking external AI APIs.
- Add historical workflow hygiene snapshot documentation for release
  reviewers.
- Add configurable action-version policy documentation for workflow hygiene
  checks.
- Add quality threshold ratcheting guidance for raising baselines
  intentionally.
- Add render-profile compatibility matrix documentation for supported AI-agent
  surfaces.
- Add release-summary coverage to CI, release workflow smoke checks, README,
  release checklist, release reviewer checklist, tests, changelog, roadmap,
  and agent guidance.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 40 Priorities

Sprint 40 should release the completed `v0.17.0` scope:

- Add v0.17.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.17.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.17.0 GitHub release when checks pass.
- Close the v0.17.0 milestone after release verification.

## v0.18.0

The `v0.18.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 41 | Complete | Release-review baselines and policy threshold hardening |
| 42 | Complete | v0.18.0 release preparation |

## Sprint 41 Priorities

Sprint 41 should bundle about a week of release-review baseline hardening work:

- Add policy-lint warning baseline snapshots for release reviewers.
- Add non-blocking warning thresholds for policy-lint advisory counts.
- Add CLI smoke tests for rendering prompts with every supported profile to
  files.
- Add fixture inventory JSON schema documentation for downstream release
  tooling.
- Add example fixture diff snapshot guidance for release reviewers.
- Update README, changelog, roadmap, tests, CI, release workflow smoke checks,
  release checklist, and release-review documentation together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 42 Priorities

Sprint 42 should release the completed `v0.18.0` scope:

- Add v0.18.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.18.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.18.0 GitHub release when checks pass.
- Close the v0.18.0 milestone after release verification.

## v0.19.0

The `v0.19.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 43 | Complete | Provenance distribution, fixture handoff, portfolio coverage, and cross-workspace reference guidance |
| 44 | Complete | v0.19.0 release preparation |

## Sprint 43 Priorities

Sprint 43 should bundle about a week of related fixture handoff and reporting
work:

- Add provenance decision-source distribution reporting.
- Add generated fixture-to-VeritySpec conversion checklist.
- Add image-input manifest examples for product and software-library domains.
- Add portfolio fixture coverage reporting grouped by game concept and
  dependency assumption.
- Add cross-workspace dependency reference syntax guidance for generated
  VeritySpec workspace drafts.
- Update README, changelog, roadmap, tests, CI, release workflow smoke checks,
  release checklist, and release-review documentation together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 44 Priorities

Sprint 44 should release the completed `v0.19.0` scope:

- Add v0.19.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.19.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.19.0 GitHub release when checks pass.
- Close the v0.19.0 milestone after release verification.

## v0.20.0

The `v0.20.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 45 | Complete | Release-review fixtures, lifecycle archival coverage, README link tests, and package-data hardening |
| 46 | Complete | v0.20.0 release preparation |

## Sprint 45 Priorities

Sprint 45 should bundle about a week of release-review fixture hardening work:

- Add lifecycle golden output drift snapshots for release reviewers.
- Add lifecycle prompt matrix examples for archival-ready outputs.
- Add release-review report examples in JSON form under checked fixtures.
- Add local documentation tests for every README documentation link.
- Add package-data coverage tests for prompt, matrix, golden, config, snapshot,
  and release-review fixture artifacts.
- Update README, changelog, roadmap, tests, package data, and release-review
  documentation together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 46 Priorities

Sprint 46 should release the completed `v0.20.0` scope:

- Add v0.20.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.20.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.20.0 GitHub release when checks pass.
- Close the v0.20.0 milestone after release verification.

## v0.21.0

The `v0.21.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 47 | Complete | Release-summary schema docs, snapshots, comparison notes, PR usage, and release-review bundle guidance |
| 48 | Complete | v0.21.0 release preparation |

## Sprint 47 Priorities

Sprint 47 should bundle about a week of release-summary and release-review
bundle hardening work:

- Add release-summary JSON schema documentation for downstream tooling.
- Add release-summary fixture snapshots for release reviewers.
- Add release-summary comparison notes for release-to-release movement.
- Add docs for using release-summary output in PR descriptions.
- Add optional machine-readable release-review bundle export guidance.
- Update README, changelog, roadmap, tests, package data, and release-review
  documentation together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 48 Priorities

Sprint 48 should release the completed `v0.21.0` scope:

- Add v0.21.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.21.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.21.0 GitHub release when checks pass.
- Close the v0.21.0 milestone after release verification.

## v0.22.0

The `v0.22.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 49 | Complete | Policy-lint trend schema docs, advisory remediation, render-profile snapshots, quality-threshold warning notes, and release-review bundle CLI design |
| 50 | Complete | v0.22.0 release preparation |

## Sprint 49 Priorities

Sprint 49 should bundle about a week of policy-lint and render-profile
release-review hardening work:

- Add policy-lint trend JSON schema documentation for downstream tooling.
- Add policy-lint advisory remediation planning guidance.
- Add render-profile output fixture snapshots for release reviewers.
- Add quality-threshold warning trend notes for release reviewers.
- Add release-review bundle export CLI design notes.
- Update README, changelog, roadmap, tests, package data, and release-review
  documentation together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 50 Priorities

Sprint 50 should release the completed `v0.22.0` scope:

- Add v0.22.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.22.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.22.0 GitHub release when checks pass.
- Close the v0.22.0 milestone after release verification.

## v0.23.0

The `v0.23.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 51 | Complete | Provenance schema docs, portfolio and cross-workspace snapshots, fixture handoff examples, and executable fixture validation design |
| 52 | Complete | v0.23.0 release preparation |

## Sprint 51 Priorities

Sprint 51 should bundle about a week of release-review fixture handoff and
cross-workspace snapshot hardening work:

- Add provenance distribution JSON schema documentation for downstream
  tooling.
- Add portfolio coverage fixture snapshots for release reviewers.
- Add cross-workspace reference output fixture snapshots for dependency-map
  examples.
- Add fixture-to-VeritySpec checklist examples for one product and one Unity
  workspace draft.
- Add optional local VeritySpec validation design notes for executable
  workspace fixtures.
- Update README, changelog, roadmap, tests, package data, and release-review
  documentation together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 52 Priorities

Sprint 52 should release the completed `v0.23.0` scope:

- Add v0.23.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.23.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.23.0 GitHub release when checks pass.
- Close the v0.23.0 milestone after release verification.

## v0.24.0

The `v0.24.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 53 | Complete | Release-review fixture schema docs, lifecycle archival drift notes, package-data audit docs, README link coverage, and fixture update instructions |
| 54 | Complete | v0.24.0 release preparation |

## Sprint 53 Priorities

Sprint 53 should bundle about a week of release-review maintenance work:

- Add release-review fixture JSON schema documentation for downstream tooling.
- Add lifecycle archival-readiness fixture drift comparison notes.
- Add package-data verification documentation for installed-wheel artifact
  audits.
- Add docs for maintaining README link coverage tests.
- Add release-review fixture update instructions for future report changes.
- Update README, changelog, roadmap, tests, and release-review documentation
  together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 54 Priorities

Sprint 54 should release the completed `v0.24.0` scope:

- Add v0.24.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.24.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.24.0 GitHub release when checks pass.
- Close the v0.24.0 milestone after release verification.

## v0.25.0

The `v0.25.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 55 | Complete | Release-summary schema compatibility, warning triage, snapshot checklist, release-review bundle retention, and CI artifact naming |
| 56 | Complete | v0.25.0 release preparation |

## Sprint 55 Priorities

Sprint 55 should bundle about a week of release-summary and release-review
bundle maintenance work:

- Add release-summary schema compatibility notes for additive fields.
- Add release-review bundle retention policy notes.
- Add release-summary warning triage examples.
- Add CI artifact naming guidance for release-review bundles.
- Add release-summary snapshot update checklist for future releases.
- Update README, changelog, roadmap, tests, and release-review documentation
  together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 56 Priorities

Sprint 56 should release the completed `v0.25.0` scope:

- Add v0.25.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.25.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.25.0 GitHub release when checks pass.
- Close the v0.25.0 milestone after release verification.

## v0.26.0

The `v0.26.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 57 | Complete | Release-review bundle manifest schema, dry-run fixture, checksums, snapshot retention, and warning triage |
| 58 | Complete | v0.26.0 release preparation |

## Sprint 57 Priorities

Sprint 57 should bundle about a week of release-review bundle manifest work:

- Add render-profile snapshot retention policy notes.
- Add policy-lint trend snapshot update checklist.
- Add quality-threshold warning triage checklist.
- Add release-review bundle manifest design notes.
- Add release-review bundle checksum design notes.
- Add release-review bundle manifest JSON schema and example fixture.
- Add release-review bundle dry-run CLI design validation tests.
- Update README, changelog, roadmap, tests, and release-review documentation
  together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 58 Priorities

Sprint 58 should release the completed `v0.26.0` scope:

- Add v0.26.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.26.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.26.0 GitHub release when checks pass.
- Close the v0.26.0 milestone after release verification.

## v0.27.0

The `v0.27.0` milestone is active.

| Sprint | Status | Focus |
|---:|---|---|
| 59 | In Progress | Generated workspace fixture manifests, executable customer portal and Dream Extraction candidates, package-data coverage, and smoke-check guidance |
| 60 | Planned | v0.27.0 release preparation |

## Sprint 59 Priorities

Sprint 59 should bundle about a week of generated workspace fixture work:

- Add generated workspace fixture manifest design notes.
- Add first executable workspace fixture candidate for customer portal.
- Add first executable workspace fixture candidate for Dream Extraction.
- Add generated workspace fixture package-data audit tests.
- Add optional generated workspace fixture smoke-check docs for CI.
- Update README, changelog, roadmap, tests, and documentation together.
- Keep the Next 20 roadmap points populated after converting completed items.

## Sprint 60 Priorities

Sprint 60 should release the completed `v0.27.0` scope:

- Add v0.27.0 release notes.
- Update package metadata, README release badge, latest-release text, install
  guidance, changelog, roadmap, and release checklist to `v0.27.0`.
- Run local release verification, package build checks, `twine check`,
  installed-wheel smoke tests, and GitHub Actions.
- Tag and publish the v0.27.0 GitHub release when checks pass.
- Close the v0.27.0 milestone after release verification.

## Later Candidates

These are intentionally not committed to a release until the initial scaffold
is complete:

- Additional golden prompt output fixtures for selected workflows.
- Optional VeritySpec workspace generation fixtures.
- Richer prompt rendering profiles for specific AI-agent surfaces.

## Next 20 Roadmap Points

These points define the next backlog once the active roadmap is caught up. They
are planning inputs, not release commitments. Convert each point into a GitHub
issue and milestone before implementation begins.

AI agents must keep this section populated with up to 20 concrete points when
the active roadmap is caught up. The points should balance fixes,
improvements, continuation work, and expansion. Convert related points into
week-sized sprint bundles rather than one release per small point.

1. Add cross-workspace dependency fixture compatibility notes.
2. Add portfolio dependency lockfile assumption checklist.
3. Add VeritySpec workspace dependency importer design notes.
4. Add generated workspace fixture provenance schema notes.
5. Add executable fixture release-summary coverage notes.
6. Add generated workspace fixture README examples.
7. Add cross-workspace fixture graph review checklist.
8. Add VeritySpec dependency lockfile prompt-workflow notes.
9. Add generated workspace fixture validation CLI design notes.
10. Add generated workspace fixture checksum and manifest pairing notes.
11. Add VeritySpec validation result snapshot schema notes.
12. Add agent-context fixture dry-run design notes.
13. Add cross-workspace dependency lockfile example fixture.
14. Add portfolio impact report prompt matrix notes.
15. Add release-review bundle export implementation planning.
16. Add generated workspace fixture VeritySpec smoke-result snapshot notes.
17. Add generated workspace fixture unresolved-decision report notes.
18. Add generated workspace fixture conversion-diff examples.
19. Add generated workspace fixture lifecycle-gap mapping notes.
20. Add generated workspace fixture agent-handoff README examples.

## Working Rule

No sprint is complete unless:

- Tests pass.
- CI passes or an external platform issue is recorded with local verification.
- Documentation and examples match the implemented behavior.
- New behavior has at least one executable test or CLI smoke check.
- The Next 20 roadmap points remain populated when the active roadmap is
  caught up.
