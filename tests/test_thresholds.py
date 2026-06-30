from pathlib import Path
import tempfile
import unittest

from verityfoundry.thresholds import (
    check_quality_thresholds,
    format_quality_threshold_report,
)


ROOT = Path(__file__).resolve().parents[1]


class QualityThresholdTests(unittest.TestCase):
    def test_quality_thresholds_pass_current_baseline(self) -> None:
        report = check_quality_thresholds(ROOT)

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["issueCount"], 0)
        self.assertEqual(report["warningCount"], 0)
        self.assertEqual(report["matrixCoverage"]["coveragePercent"], 88.0)
        self.assertEqual(report["policyLint"]["warningCount"], 14)

        text = format_quality_threshold_report(report)
        self.assertIn("Quality Threshold Check", text)
        self.assertIn("Quality threshold check passed.", text)
        self.assertIn("Policy lint: 0 errors, 14 warnings", text)

    def test_quality_thresholds_fail_when_config_is_too_high(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / "thresholds.json"
            config.write_text(
                """{
  "promptQuality": {
    "minOverallPercent": 100,
    "minUncertaintyPercent": 100,
    "minProvenancePercent": 100
  },
  "matrixCoverage": {
    "minCoveragePercent": 100,
    "maxMissingDomainPrompts": 0,
    "maxUnknownPromptRefs": 0
  },
  "policyLint": {
    "maxErrors": 0,
    "maxWarnings": 14
  }
}
""",
                encoding="utf-8",
            )

            report = check_quality_thresholds(ROOT, config_path=config)

        self.assertEqual(report["status"], "failed")
        self.assertGreater(report["issueCount"], 0)
        codes = {issue["code"] for issue in report["issues"]}
        self.assertIn("threshold.prompt-quality-overall", codes)
        self.assertIn("threshold.matrix-coverage", codes)

    def test_policy_lint_warning_threshold_is_non_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / "thresholds.json"
            config.write_text(
                """{
  "promptQuality": {
    "minOverallPercent": 0,
    "minUncertaintyPercent": 0,
    "minProvenancePercent": 0
  },
  "matrixCoverage": {
    "minCoveragePercent": 0,
    "maxMissingDomainPrompts": 999,
    "maxUnknownPromptRefs": 999
  },
  "policyLint": {
    "maxErrors": 0,
    "maxWarnings": 0
  }
}
""",
                encoding="utf-8",
            )

            report = check_quality_thresholds(ROOT, config_path=config)

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["issueCount"], 0)
        self.assertEqual(report["warningCount"], 1)
        self.assertEqual(report["warnings"][0]["code"], "threshold.policy-lint-warnings")

        text = format_quality_threshold_report(report)
        self.assertIn("Warnings:", text)
        self.assertIn("Quality threshold check passed with warnings.", text)


if __name__ == "__main__":
    unittest.main()
