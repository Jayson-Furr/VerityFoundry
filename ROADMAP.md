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

1. Add a decision-policy linter for high-stakes invention risks.
2. Add Markdown rendering profiles for Codex, Claude Code, ChatGPT, Gemini,
   and Unity AI prompt handoff.
3. Add example manifests that reference candidate VeritySpec workspace files
   once workspace fixtures exist.
4. Add generated workspace outline validators for expected record categories.
5. Add image-input manifest fixtures for concept art and identity images.
6. Add provenance examples aligned with future VeritySpec evidence records.
7. Add cross-workspace dependency prompt guidance for shared Unity libraries
   and game portfolios.
8. Add portfolio triage prompts for batches of many game concepts.
9. Add release-readiness gap review prompts for generated VeritySpec
    workspaces.
10. Add maintenance and decommissioning interview flows for shipped products.
11. Add contributor docs for proposing new prompt workflows.
12. Add release-integrity checks for README, changelog, roadmap, package
    metadata, and release notes.
13. Add golden output drift review documentation for maintainers.
14. Add a golden output inventory report for maintainers and release reviewers.
15. Add prompt quality trend snapshots for release reviewers.
16. Add generated example inventory reports for release reviewers.
17. Add matrix coverage thresholds once baseline coverage is intentionally
    improved.
18. Add docs explaining how to convert VerityFoundry expected outputs into
    concrete VeritySpec workspace fixtures.
19. Add release workflow checks for stale action versions and non-blocking
    workflow annotations.
20. Add a v0.x stabilization checklist for CLI output compatibility,
    manifest compatibility, and report schema compatibility.

## Working Rule

No sprint is complete unless:

- Tests pass.
- CI passes or an external platform issue is recorded with local verification.
- Documentation and examples match the implemented behavior.
- New behavior has at least one executable test or CLI smoke check.
- The Next 20 roadmap points remain populated when the active roadmap is
  caught up.
