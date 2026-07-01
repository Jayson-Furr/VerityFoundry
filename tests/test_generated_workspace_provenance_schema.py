from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

from verityfoundry.manifests import read_json


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "generated-workspace-fixture-provenance.schema.json"
FIXTURE_ROOT = ROOT / "fixtures" / "generated-workspaces"


class GeneratedWorkspaceProvenanceSchemaTests(unittest.TestCase):
    def test_generated_workspace_fixture_provenance_schema_validates_manifests(self) -> None:
        schema = read_json(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        manifest_paths = sorted(FIXTURE_ROOT.glob("*/fixture-manifest.json"))

        self.assertGreaterEqual(len(manifest_paths), 2)
        for manifest_path in manifest_paths:
            with self.subTest(manifest=manifest_path.relative_to(ROOT).as_posix()):
                provenance = read_json(manifest_path)["provenance"]
                errors = sorted(
                    validator.iter_errors(provenance),
                    key=lambda error: list(error.path),
                )
                self.assertEqual([error.message for error in errors], [])
                self.assertTrue(provenance["humanApprovalRequired"])


if __name__ == "__main__":
    unittest.main()
