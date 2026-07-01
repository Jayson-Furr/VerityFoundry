from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

from verityfoundry.inventory import (
    generate_portfolio_fixture_coverage_report,
    generate_provenance_distribution_report,
)
from verityfoundry.manifests import read_json


ROOT = Path(__file__).resolve().parents[1]
CROSS_WORKSPACE_KINDS = {
    "unity.exported-record-assumption",
    "workspace.cross-reference",
    "workspace.dependency",
    "workspace.dependency-risk",
}


class ReleaseReviewSnapshotTests(unittest.TestCase):
    def test_provenance_distribution_json_schema_validates_current_report(self) -> None:
        schema = read_json(ROOT / "schemas" / "provenance-distribution-report.schema.json")
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        errors = sorted(
            validator.iter_errors(generate_provenance_distribution_report(ROOT)),
            key=lambda error: list(error.path),
        )

        self.assertEqual([error.message for error in errors], [])

    def test_portfolio_coverage_json_schema_validates_current_report_and_snapshot(self) -> None:
        schema = read_json(ROOT / "schemas" / "portfolio-coverage-report.schema.json")
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        current = generate_portfolio_fixture_coverage_report(ROOT)
        snapshot = read_json(ROOT / "snapshots" / "portfolio-coverage" / "v0.22.0.json")

        for payload in (current, snapshot):
            errors = sorted(
                validator.iter_errors(payload),
                key=lambda error: list(error.path),
            )
            self.assertEqual([error.message for error in errors], [])

        self.assertEqual(snapshot, current)

    def test_cross_workspace_reference_snapshot_matches_dependency_map_fixture(self) -> None:
        snapshot_path = (
            ROOT
            / "snapshots"
            / "cross-workspace-references"
            / "shared-unity-dependency-map-v0.22.0.json"
        )
        snapshot = read_json(snapshot_path)
        fixture = read_json(ROOT / snapshot["sourceFixture"])
        expected_records = [
            record
            for record in fixture["records"]
            if record.get("kind") in CROSS_WORKSPACE_KINDS
        ]

        self.assertEqual(snapshot["snapshotLabel"], "v0.22.0")
        self.assertEqual(snapshot["exampleId"], "example.portfolio.shared-unity-dependency-map")
        self.assertEqual(snapshot["recordCount"], len(expected_records))
        self.assertEqual(snapshot["records"], expected_records)

        cross_refs = [
            record
            for record in snapshot["records"]
            if record.get("kind") == "workspace.cross-reference"
        ]
        self.assertEqual(len(cross_refs), 2)
        self.assertTrue(all("::" in record["target"] for record in cross_refs))
        self.assertTrue(
            all(
                record.get("provenance", {}).get("humanApprovalRequired") is True
                for record in snapshot["records"]
            )
        )


if __name__ == "__main__":
    unittest.main()
