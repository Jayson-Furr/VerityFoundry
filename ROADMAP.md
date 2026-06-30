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

The `v0.8.0` milestone is in progress.

| Sprint | Status | Focus |
|---:|---|---|
| 21 | In progress | Workspace fixture readiness |

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

1. Add cross-workspace dependency prompt guidance for shared Unity libraries
   and game portfolios.
2. Add portfolio triage prompts for batches of many game concepts.
3. Add release-readiness gap review prompts for generated VeritySpec
   workspaces.
4. Add maintenance and decommissioning interview flows for shipped products.
5. Add release-integrity checks for README, changelog, roadmap, package
    metadata, and release notes.
6. Add golden output drift review documentation for maintainers.
7. Add a golden output inventory report for maintainers and release reviewers.
8. Add prompt quality trend snapshots for release reviewers.
9. Add generated example inventory reports for release reviewers.
10. Add matrix coverage thresholds once baseline coverage is intentionally
    improved.
11. Add release workflow checks for stale action versions and non-blocking
    workflow annotations.
12. Add a v0.x stabilization checklist for CLI output compatibility,
    manifest compatibility, and report schema compatibility.
13. Add a dedicated GitHub Copilot render profile.
14. Add policy lint severity levels and warning-only advisory checks.
15. Add tests that verify high-risk prompts render safety and provenance
    sections under every non-default agent profile.
16. Add candidate workspace fixture inventory reports for release reviewers.
17. Add fixture provenance coverage reporting across examples.
18. Add docs for mapping candidate fixture `kind` values to VeritySpec packs.
19. Add schema support for image-input manifests once the fixture shape
    stabilizes.
20. Add tests that packaged wheels include all declared example fixture files.

## Working Rule

No sprint is complete unless:

- Tests pass.
- CI passes or an external platform issue is recorded with local verification.
- Documentation and examples match the implemented behavior.
- New behavior has at least one executable test or CLI smoke check.
- The Next 20 roadmap points remain populated when the active roadmap is
  caught up.
