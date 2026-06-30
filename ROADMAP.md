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
improvements, continuation work, and expansion.

1. Add a local command summary report that aggregates release-review command
    results without invoking external AI APIs.
2. Add historical workflow hygiene snapshot documentation for release
    reviewers.
3. Add configurable action-version policy documentation for workflow hygiene
    checks.
4. Add quality threshold ratcheting guidance for raising baselines
    intentionally.
5. Add render-profile compatibility matrix documentation for supported AI
    agent surfaces.
6. Add policy-lint warning baseline snapshots for release reviewers.
7. Add non-blocking warning thresholds for policy-lint advisory counts.
8. Add CLI smoke tests for rendering prompts with every supported profile to
    files.
9. Add fixture inventory JSON schema documentation for downstream release
    tooling.
10. Add example fixture diff snapshots for release reviewers.
11. Add provenance decision-source distribution reporting.
12. Add generated fixture-to-VeritySpec conversion checklist.
13. Add image-input manifest examples for product and software-library
    domains.
14. Add portfolio fixture coverage reporting grouped by game concept and
    dependency assumption.
15. Add cross-workspace dependency reference syntax guidance for generated
    VeritySpec workspace drafts.
16. Add lifecycle golden output drift snapshots for release reviewers.
17. Add lifecycle prompt matrix examples for archival-ready outputs.
18. Add release-review report examples in JSON form under checked fixtures.
19. Add local documentation tests for every README documentation link.
20. Add package-data coverage tests for prompt, matrix, golden, config, and
    snapshot artifacts.

## Working Rule

No sprint is complete unless:

- Tests pass.
- CI passes or an external platform issue is recorded with local verification.
- Documentation and examples match the implemented behavior.
- New behavior has at least one executable test or CLI smoke check.
- The Next 20 roadmap points remain populated when the active roadmap is
  caught up.
