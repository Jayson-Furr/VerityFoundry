from pathlib import Path
import json
import tempfile
import unittest

from verityfoundry.policy_lint import (
    SEVERITY_ERROR,
    SEVERITY_WARNING,
    count_policy_lint_severities,
    format_policy_lint_issues,
    lint_decision_policy,
)


ROOT = Path(__file__).resolve().parents[1]


class PolicyLintTests(unittest.TestCase):
    def test_decision_policy_lint_has_no_repository_errors(self) -> None:
        issues = lint_decision_policy(ROOT)
        counts = count_policy_lint_severities(issues)

        self.assertEqual(counts[SEVERITY_ERROR], 0)
        self.assertGreaterEqual(counts[SEVERITY_WARNING], 1)

    def test_policy_lint_formats_pass(self) -> None:
        self.assertEqual(format_policy_lint_issues([]), "Decision policy lint passed.\n")

    def test_policy_lint_formats_warning_only_pass(self) -> None:
        issues = lint_decision_policy(_fixture_root(include_output_contract=False))
        counts = count_policy_lint_severities(issues)

        self.assertEqual(counts[SEVERITY_ERROR], 0)
        self.assertEqual(counts[SEVERITY_WARNING], 1)
        text = format_policy_lint_issues(issues)
        self.assertIn("Decision policy lint passed with warnings.", text)
        self.assertIn("warning: policy.advisory-missing-output-contract", text)

    def test_policy_lint_reports_errors_separately_from_warnings(self) -> None:
        issues = lint_decision_policy(_fixture_root(include_decision_policy=False))
        counts = count_policy_lint_severities(issues)

        self.assertEqual(counts[SEVERITY_ERROR], 1)
        self.assertEqual(counts[SEVERITY_WARNING], 0)
        text = format_policy_lint_issues(issues)
        self.assertIn("Decision policy lint failed.", text)
        self.assertIn("error: policy.missing-decision-policy", text)


def _fixture_root(
    include_decision_policy: bool = True,
    include_output_contract: bool = True,
) -> Path:
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    prompts = root / "prompts" / "domains" / "product"
    prompts.mkdir(parents=True)
    include_refs = ["common.output-contract.v1"] if include_output_contract else []
    decision_policy = (
        '"decisionPolicyRef": "decision-policy.medium-stakes.v1",'
        if include_decision_policy
        else ""
    )
    (prompts / "fixture.md").write_text(
        f"""---
{{
  "id": "product.fixture.interview-low.design-complete.v1",
  "name": "Fixture",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "product",
  "interviewMode": "interview-low-stakes",
  "targetReadiness": "design-complete",
  "inputTypes": ["brief"],
  "outputs": ["workspace-outline"],
  {decision_policy}
  "includeRefs": {json.dumps(include_refs)},
  "requiresHumanApproval": true
}}
---

Fixture prompt.
""",
        encoding="utf-8",
    )
    # Keep the temporary directory alive for the duration of the test by
    # attaching it to the returned Path object through a module-level cache.
    _TEMP_DIRS.append(tmp)
    return root


_TEMP_DIRS: list[object] = []


if __name__ == "__main__":
    unittest.main()
