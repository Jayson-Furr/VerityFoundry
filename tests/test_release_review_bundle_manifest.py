from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

from verityfoundry.manifests import read_json


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "release-review-bundle-manifest.schema.json"
EXAMPLE_PATH = ROOT / "fixtures" / "release-review" / "bundle" / "manifest.example.json"


class ReleaseReviewBundleManifestTests(unittest.TestCase):
    def test_bundle_manifest_schema_validates_example(self) -> None:
        schema = read_json(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        errors = sorted(
            validator.iter_errors(read_json(EXAMPLE_PATH)),
            key=lambda error: list(error.path),
        )
        self.assertEqual([error.message for error in errors], [])

    def test_bundle_manifest_example_documents_required_reports(self) -> None:
        manifest = read_json(EXAMPLE_PATH)
        paths = {artifact["path"] for artifact in manifest["artifacts"]}

        self.assertEqual(
            paths,
            {
                "release-summary.json",
                "prompt-quality.json",
                "policy-lint-trend.json",
                "matrix-coverage.json",
                "golden-inventory.json",
                "example-inventory.json",
                "fixture-inventory.json",
                "provenance-coverage.json",
                "provenance-distribution.json",
                "portfolio-coverage.json",
                "manifest.json",
            },
        )
        self.assertTrue(all(artifact["required"] for artifact in manifest["artifacts"]))

    def test_bundle_manifest_example_preserves_dry_run_boundaries(self) -> None:
        manifest = read_json(EXAMPLE_PATH)

        self.assertEqual(manifest["mode"], "planned-dry-run")
        self.assertTrue(manifest["validation"]["localOnly"])
        self.assertFalse(manifest["validation"]["externalAiApisAllowed"])
        self.assertTrue(manifest["validation"]["humanReviewRequired"])
        self.assertIn("VeritySpec", manifest["validation"]["veritySpecAuthorityBoundary"])
        for artifact in manifest["artifacts"]:
            with self.subTest(path=artifact["path"]):
                self.assertEqual(artifact["checksum"]["algorithm"], "sha256")
                self.assertEqual(artifact["checksum"]["state"], "planned")
                self.assertIsNone(artifact["checksum"]["digest"])


if __name__ == "__main__":
    unittest.main()
