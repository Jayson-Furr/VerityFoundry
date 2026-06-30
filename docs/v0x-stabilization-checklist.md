# v0.x Stabilization Checklist

This checklist defines the compatibility work VerityFoundry should harden
before stronger v1.0-style guarantees.

## CLI Compatibility

- Keep command names stable once they are documented in `README.md`.
- Preserve exit-code meanings:
  - `0`: success or warning-only advisory output
  - `1`: validation, lint, check, or threshold failure
  - `2`: usage error
  - `3`: unexpected internal error
- Treat text output as human-readable and JSON output as the automation
  surface.
- Add tests before changing command names, argument names, or JSON fields.

## Manifest Compatibility

- Keep prompt, matrix, example, decision-policy, and golden-output manifests
  valid against their schemas.
- Prefer additive manifest fields during v0.x.
- When a field needs a breaking change, add a new manifest version or prompt
  ID suffix rather than silently changing meaning.
- Preserve prompt IDs unless the workflow contract changes materially.

## Report Schema Compatibility

- Keep JSON report fields additive when practical.
- Document any field removal or type change in `CHANGELOG.md` and release
  notes.
- Prefer explicit counts such as `errorCount`, `warningCount`, and
  `issueCount` for downstream automation.
- Keep warning-only advisory findings non-blocking unless the release notes
  explicitly promote them to errors.

## Release Discipline

- Run source checks, build checks, installed-wheel smoke tests, PR CI, main CI,
  and release workflow verification.
- Keep README, changelog, roadmap, release notes, release checklist, and
  package version references aligned.
- Keep the Next 20 roadmap populated when the active roadmap is caught up.
- Close completed issues and milestones after release verification.
