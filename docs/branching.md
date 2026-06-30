# Branching

Use `main` as the releasable branch.

Recommended branch names:

- `sprint/<number>-<topic>`
- `feature/<topic>`
- `fix/<topic>`
- `docs/<topic>`
- `release/vX.Y.Z`

Substantive changes should use a branch, issue, milestone, PR, local checks,
and CI before merge.

Prefer sprint branches that bundle roughly one week of related work into a
coherent releasable increment. Small urgent fixes can still use focused fix
branches, but routine roadmap work should not force a separate release for
every tiny item when related items can be verified together.
