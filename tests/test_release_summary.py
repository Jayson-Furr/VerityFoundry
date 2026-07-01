from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

from verityfoundry.manifests import read_json
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
        self.assertEqual(
            report["reports"]["generatedWorkspaceValidation"]["snapshotCount"],
            2,
        )
        self.assertEqual(
            report["reports"]["generatedWorkspaceValidation"]["staleFileHashCount"],
            0,
        )

    def test_release_summary_formats_text(self) -> None:
        text = format_release_summary_report(generate_release_summary_report(ROOT))

        self.assertIn("Release Summary Report", text)
        self.assertIn("Release integrity: passed", text)
        self.assertIn("Quality thresholds: passed", text)
        self.assertIn("Workflow hygiene: passed", text)
        self.assertIn("Policy lint trend:", text)
        self.assertIn("Generated workspace validation:", text)
        self.assertIn("Run VeritySpec validation separately", text)

    def test_release_summary_json_schema_validates_current_report(self) -> None:
        schema = read_json(ROOT / "schemas" / "release-summary-report.schema.json")
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        errors = sorted(
            validator.iter_errors(generate_release_summary_report(ROOT)),
            key=lambda error: list(error.path),
        )
        self.assertEqual([error.message for error in errors], [])

    def test_release_summary_snapshots_validate_schema(self) -> None:
        schema = read_json(ROOT / "schemas" / "release-summary-report.schema.json")
        validator = Draft202012Validator(schema)
        snapshot_paths = sorted((ROOT / "snapshots" / "release-summary").glob("v*.json"))

        self.assertIn(ROOT / "snapshots" / "release-summary" / "v0.20.0.json", snapshot_paths)
        for snapshot_path in snapshot_paths:
            with self.subTest(snapshot=snapshot_path.name):
                snapshot = read_json(snapshot_path)
                errors = sorted(
                    validator.iter_errors(snapshot),
                    key=lambda error: list(error.path),
                )
                self.assertEqual([error.message for error in errors], [])
                self.assertEqual(snapshot["status"], "passed")
                self.assertEqual(
                    snapshot["checks"]["releaseIntegrity"]["expectedVersion"],
                    snapshot_path.stem.removeprefix("v"),
                )
                self.assertEqual(
                    snapshot["checks"]["releaseIntegrity"]["expectedTag"],
                    snapshot_path.stem,
                )


if __name__ == "__main__":
    unittest.main()
