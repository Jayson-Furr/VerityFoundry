from pathlib import Path
import shutil
import tempfile
import unittest

from jsonschema import Draft202012Validator

from verityfoundry.inventory import (
    format_generated_workspace_validation_report,
    generate_generated_workspace_validation_report,
)
from verityfoundry.manifests import read_json


ROOT = Path(__file__).resolve().parents[1]


class GeneratedWorkspaceValidationReportTests(unittest.TestCase):
    def test_report_counts_and_formats_current_snapshots(self) -> None:
        report = generate_generated_workspace_validation_report(ROOT)

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["generatedWorkspaceCount"], 2)
        self.assertEqual(report["snapshotCount"], 2)
        self.assertEqual(report["passedSnapshotCount"], 2)
        self.assertEqual(report["failedSnapshotCount"], 0)
        self.assertEqual(report["skippedSnapshotCount"], 0)
        self.assertEqual(report["missingSnapshotCount"], 0)
        self.assertEqual(report["fileHashCount"], 17)
        self.assertEqual(report["staleFileHashCount"], 0)
        self.assertEqual(report["uncoveredFileCount"], 0)
        self.assertEqual(report["humanReviewRequiredCount"], 2)
        self.assertEqual(report["unresolvedDecisionCount"], 6)
        self.assertTrue(all(item["status"] == "passed" for item in report["workspaces"]))

        text = format_generated_workspace_validation_report(report)
        self.assertIn("Generated Workspace Validation Report", text)
        self.assertIn("Freshness: 17 file hashes, 0 stale, 0 uncovered files", text)
        self.assertIn("Human review required: 2/2 snapshots", text)
        self.assertIn("VeritySpec remains the contract authority", text)

    def test_report_json_schema_validates_current_report(self) -> None:
        schema = read_json(ROOT / "schemas" / "generated-workspace-validation-report.schema.json")
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        errors = sorted(
            validator.iter_errors(generate_generated_workspace_validation_report(ROOT)),
            key=lambda error: list(error.path),
        )
        self.assertEqual([error.message for error in errors], [])

    def test_report_detects_stale_snapshot_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp) / "repo"
            shutil.copytree(ROOT, temp_root, ignore=shutil.ignore_patterns(".git", ".venv", "dist", "build"))
            record_path = (
                temp_root
                / "fixtures"
                / "generated-workspaces"
                / "customer-portal"
                / "records"
                / "product.json"
            )
            record_path.write_text(
                record_path.read_text(encoding="utf-8") + "\n",
                encoding="utf-8",
            )

            report = generate_generated_workspace_validation_report(temp_root)

        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["staleFileHashCount"], 1)
        customer = {
            item["workspacePath"]: item
            for item in report["workspaces"]
        }["fixtures/generated-workspaces/customer-portal"]
        self.assertEqual(customer["status"], "failed")
        self.assertEqual(customer["staleFileHashCount"], 1)


if __name__ == "__main__":
    unittest.main()
