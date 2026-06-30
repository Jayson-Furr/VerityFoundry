# Release Reviewer Inventory Reports

VerityFoundry includes deterministic inventory reports for release reviewers.

```bash
verityfoundry report golden-inventory
verityfoundry report golden-inventory --format json
verityfoundry report example-inventory
verityfoundry report example-inventory --format json
verityfoundry report fixture-inventory
verityfoundry report fixture-inventory --format json
verityfoundry report provenance-coverage
verityfoundry report provenance-coverage --format json
```

The golden inventory report lists:

- golden output ID
- domain
- target readiness
- prompt reference
- required section count
- whether the output file exists

The example inventory report lists:

- example ID
- domain
- target readiness
- input count
- expected-output count
- workspace fixture count
- provenance example count

The fixture inventory report lists:

- workspace fixture path
- example ID
- record count
- record kind count
- kind-to-pack recommendation
- missing or present status

The provenance coverage report lists:

- records with provenance metadata
- records represented by decision examples
- human-approval-required record counts
- missing provenance record references
- missing decision example record references

These reports help reviewers see what is in scope before a release. They do
not replace `verityfoundry validate`, golden-output review, or human review.

Installed wheel smoke tests run these reports from `/tmp` to prove packaged
example and golden artifacts are available outside a source checkout.
