from pathlib import Path
import unittest

from verityfoundry.release_summary import (
    format_release_summary_report,
    generate_release_summary_report,
)


ROOT = Path(__file__).resolve().parents[1]


class ReleaseSummaryTests(unittest.TestCase):
    def test_release_summary_aggregates_release_review_state(self) -> None:
        report = generate_release_summary_report(ROOT)

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["blockingIssueCount"], 0)
        self.assertGreater(report["warningCount"], 0)
        self.assertEqual(report["checks"]["releaseIntegrity"]["status"], "passed")
        self.assertEqual(report["checks"]["qualityThresholds"]["status"], "passed")
        self.assertEqual(report["checks"]["workflowHygiene"]["status"], "passed")
        self.assertEqual(report["reports"]["goldenInventory"]["goldenCount"], 6)
        self.assertEqual(report["reports"]["exampleInventory"]["exampleCount"], 6)
        self.assertEqual(
            report["reports"]["policyLintTrend"]["latestSnapshotLabel"],
            "v0.17.0",
        )
        self.assertEqual(
            report["reports"]["provenanceCoverage"]["recordProvenancePercent"],
            100.0,
        )

    def test_release_summary_formats_text(self) -> None:
        text = format_release_summary_report(generate_release_summary_report(ROOT))

        self.assertIn("Release Summary Report", text)
        self.assertIn("Release integrity: passed", text)
        self.assertIn("Quality thresholds: passed", text)
        self.assertIn("Workflow hygiene: passed", text)
        self.assertIn("Policy lint trend:", text)
        self.assertIn("Run VeritySpec validation separately", text)


if __name__ == "__main__":
    unittest.main()
