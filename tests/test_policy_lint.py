from pathlib import Path
import unittest

from verityfoundry.policy_lint import format_policy_lint_issues, lint_decision_policy


ROOT = Path(__file__).resolve().parents[1]


class PolicyLintTests(unittest.TestCase):
    def test_decision_policy_lint_passes_repository_prompts(self) -> None:
        self.assertEqual(lint_decision_policy(ROOT), [])

    def test_policy_lint_formats_pass(self) -> None:
        self.assertEqual(format_policy_lint_issues([]), "Decision policy lint passed.\n")


if __name__ == "__main__":
    unittest.main()
