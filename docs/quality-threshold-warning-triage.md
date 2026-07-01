# Quality-Threshold Warning Triage

`verityfoundry check quality-thresholds` can pass while still surfacing
non-blocking warning movement. Warnings should be triaged before release even
when they are not blockers.

## Triage Steps

1. Identify the warning source, such as decision-policy lint or trend movement.
2. Decide whether the warning is existing, improved, newly introduced, or no
   longer relevant.
3. Create a remediation issue for new or growing warnings unless the release
   deliberately accepts them.
4. Update snapshots only when the new baseline is intentional.
5. Record the decision in the PR or release notes when warnings affect agent
   handoff, uncertainty preservation, or human approval flow.

## Boundary

A passing quality-threshold check does not certify a candidate VeritySpec
workspace. Human review and VeritySpec validation remain required for generated
workspace claims.
