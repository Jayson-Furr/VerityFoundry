# Portfolio Dependency Lockfile Assumption Checklist

Portfolio prompt workflows often need to discuss future dependency lockfiles
before VeritySpec has a concrete lockfile in hand. The assumptions must stay
explicit.

## Checklist

- Identify each workspace dependency separately from each pack dependency.
- Preserve the dependency alias, source path, intended version range, and
  expected resolved version when known.
- Mark unknown revisions, record-set hashes, and pack versions as unresolved.
- Do not invent Git commit hashes, package digests, legal approvals, or
  production compatibility claims.
- Include a human approval marker for every dependency that affects release,
  liveops, player data, customer data, or shared runtime behavior.
- Plan a future VeritySpec validation step for dependency resolution and graph
  impact.

## Boundary

This checklist helps VerityFoundry prompts avoid false certainty. VeritySpec
must own the actual dependency lockfile format and validation behavior, and a
human reviewer must approve high-impact assumptions.
