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
        self.assertEqual(report["matrixCoverage"]["coveragePercent"], 88.0)

        text = format_quality_threshold_report(report)
        self.assertIn("Quality Threshold Check", text)
        self.assertIn("Quality threshold check passed.", text)

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


if __name__ == "__main__":
    unittest.main()
