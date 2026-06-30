from pathlib import Path
import unittest

from verityfoundry.policy_lint_trend import (
    format_policy_lint_trend_report,
    generate_policy_lint_trend_report,
)


ROOT = Path(__file__).resolve().parents[1]


class PolicyLintTrendTests(unittest.TestCase):
    def test_policy_lint_trend_uses_snapshot(self) -> None:
        report = generate_policy_lint_trend_report(ROOT)

        self.assertGreaterEqual(report["snapshotCount"], 1)
        self.assertEqual(report["latestSnapshot"]["label"], "v0.17.0")
        self.assertEqual(report["current"]["errorCount"], 0)
        self.assertEqual(report["current"]["warningCount"], 14)
        self.assertEqual(report["deltaFromLatest"]["warningCount"], 0)

        text = format_policy_lint_trend_report(report)
        self.assertIn("Policy Lint Trend Report", text)
        self.assertIn("Latest snapshot: v0.17.0", text)


if __name__ == "__main__":
    unittest.main()
