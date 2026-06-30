# Golden Output Drift Review

Golden outputs are deterministic examples of expected prompt behavior. They
are not claims that a generated VeritySpec workspace is true, complete, or
approved.

Use this process when a prompt, matrix, decision policy, readiness target, or
example changes:

1. Run `verityfoundry validate goldens`.
2. Run `verityfoundry report golden-inventory`.
3. Review changed golden output text for uncertainty preservation.
4. Confirm required sections still match the manifest.
5. Confirm generated claims remain candidate claims.
6. Confirm unresolved decisions and human approval requirements are still
   visible.
7. Confirm the Suggested VeritySpec Validation Loop is still present when the
   workflow produces candidate workspace output.

Golden output drift is acceptable when prompt behavior intentionally improves.
It should be documented in the changelog, roadmap sprint notes, or release PR
when it changes release-facing expectations.
