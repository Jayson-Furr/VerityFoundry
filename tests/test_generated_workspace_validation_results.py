from pathlib import Path
import hashlib
import unittest

from jsonschema import Draft202012Validator, FormatChecker

from verityfoundry.manifests import read_json


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "generated-workspace-validation-result.schema.json"
FIXTURE_ROOT = ROOT / "fixtures" / "generated-workspaces"


class GeneratedWorkspaceValidationResultTests(unittest.TestCase):
    def test_validation_result_schema_validates_snapshots(self) -> None:
        schema = read_json(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        result_paths = sorted(FIXTURE_ROOT.glob("*/validation-result.json"))

        self.assertEqual(
            [path.relative_to(ROOT).as_posix() for path in result_paths],
            [
                "fixtures/generated-workspaces/customer-portal/validation-result.json",
                "fixtures/generated-workspaces/dream-extraction/validation-result.json",
            ],
        )
        for result_path in result_paths:
            with self.subTest(result=result_path.relative_to(ROOT).as_posix()):
                result = read_json(result_path)
                errors = sorted(
                    validator.iter_errors(result),
                    key=lambda error: list(error.path),
                )
                self.assertEqual([error.message for error in errors], [])
                self.assertEqual(result["status"], "passed")
                self.assertTrue(result["humanReviewRequired"])
                self.assertIn("does not certify", result["authorityBoundary"])
                self.assertGreaterEqual(len(result["unresolvedDecisions"]), 1)

    def test_manifest_links_validation_result_snapshots(self) -> None:
        for manifest_path in sorted(FIXTURE_ROOT.glob("*/fixture-manifest.json")):
            with self.subTest(manifest=manifest_path.relative_to(ROOT).as_posix()):
                manifest = read_json(manifest_path)
                snapshot_path = ROOT / manifest["validation"]["resultSnapshot"]
                self.assertTrue(snapshot_path.exists())
                result = read_json(snapshot_path)
                self.assertEqual(result["workspaceId"], manifest["id"])
                self.assertEqual(result["workspacePath"], manifest["workspacePath"])
                self.assertEqual(
                    (ROOT / result["sourceManifest"]).resolve(),
                    manifest_path.resolve(),
                )

    def test_validation_result_file_hashes_match_workspace_files(self) -> None:
        for result_path in sorted(FIXTURE_ROOT.glob("*/validation-result.json")):
            result = read_json(result_path)
            with self.subTest(result=result_path.relative_to(ROOT).as_posix()):
                hash_entries = {entry["path"]: entry["sha256"] for entry in result["fileHashes"]}
                expected_paths = {
                    path.relative_to(ROOT).as_posix()
                    for path in result_path.parent.glob("*.json")
                    if path.name != "validation-result.json"
                }
                expected_paths.update(
                    path.relative_to(ROOT).as_posix()
                    for path in (result_path.parent / "records").glob("*.json")
                )
                self.assertEqual(set(hash_entries), expected_paths)
                for relative_path, expected_hash in sorted(hash_entries.items()):
                    digest = hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()
                    self.assertEqual(digest, expected_hash, relative_path)


if __name__ == "__main__":
    unittest.main()
