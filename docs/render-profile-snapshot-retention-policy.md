# Render-Profile Snapshot Retention Policy

Render-profile snapshots are checked review fixtures, not temporary CI
artifacts. Keep them in Git when they are needed to prove how a prompt renders
for a supported AI-agent profile.

## Retention Rules

- Retain one current snapshot for each supported render profile.
- Retain historical snapshots only when they explain a release-review decision
  or a compatibility change.
- Remove obsolete snapshots in the same change that removes the profile,
  prompt, or compatibility guarantee.
- Document intentional snapshot churn in release notes when it changes agent
  handoff behavior.

## Review Boundary

Snapshots help a human reviewer inspect prompt shape and agent handoff drift.
They do not prove that a generated VeritySpec workspace is valid, complete, or
ready. VeritySpec validation and readiness remain separate checks.
