from pathlib import Path
import unittest

from verityfoundry.manifests import read_json


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "fixtures" / "generated-workspaces"


def load_records(workspace_path: Path) -> list[dict]:
    records: list[dict] = []
    for record_path in sorted((workspace_path / "records").glob("*.json")):
        payload = read_json(record_path)
        if "records" in payload:
            records.extend(payload["records"])
        else:
            records.append(payload)
    return records


class GeneratedWorkspaceFixtureTests(unittest.TestCase):
    def test_expected_generated_workspace_fixtures_exist(self) -> None:
        self.assertEqual(
            {path.name for path in sorted(FIXTURE_ROOT.iterdir()) if path.is_dir()},
            {"customer-portal", "dream-extraction"},
        )

    def test_generated_workspace_manifests_link_sources(self) -> None:
        for workspace_path in sorted(FIXTURE_ROOT.iterdir()):
            if not workspace_path.is_dir():
                continue
            with self.subTest(workspace=workspace_path.name):
                manifest = read_json(workspace_path / "fixture-manifest.json")
                self.assertTrue((ROOT / manifest["sourceExample"]).exists())
                self.assertTrue((ROOT / manifest["candidateWorkspaceFixture"]).exists())
                self.assertEqual(
                    (ROOT / manifest["workspacePath"]).resolve(),
                    workspace_path.resolve(),
                )
                self.assertTrue(manifest["validation"]["localOnly"])
                self.assertFalse(manifest["validation"]["externalAiApisAllowed"])
                self.assertTrue(manifest["validation"]["skipWhenVerityMissing"])
                self.assertTrue(manifest["validation"]["humanReviewRequired"])
                self.assertIn("VeritySpec", manifest["validation"]["veritySpecAuthorityBoundary"])

    def test_generated_workspaces_use_verityspec_shape(self) -> None:
        for workspace_path in sorted(FIXTURE_ROOT.iterdir()):
            if not workspace_path.is_dir():
                continue
            with self.subTest(workspace=workspace_path.name):
                workspace = read_json(workspace_path / "verityspec.json")
                self.assertEqual(workspace["specVersion"], "v0.2.0")
                self.assertGreaterEqual(len(workspace["packs"]), 2)
                self.assertEqual(workspace["records"], ["records/*.json"])
                records = load_records(workspace_path)
                self.assertGreaterEqual(len(records), 3)
                self.assertEqual(len({record["id"] for record in records}), len(records))
                self.assertTrue(all("kind" in record for record in records))

    def test_generated_workspace_kinds_match_fixture_intent(self) -> None:
        customer_kinds = {record["kind"] for record in load_records(FIXTURE_ROOT / "customer-portal")}
        dream_kinds = {record["kind"] for record in load_records(FIXTURE_ROOT / "dream-extraction")}

        self.assertEqual(customer_kinds, {"product", "schema.object", "api.endpoint"})
        self.assertEqual(
            dream_kinds,
            {
                "product",
                "game.product",
                "game.loop",
                "game.mode",
                "game.prototype-scope",
                "game.gdd-source",
                "game.visual-identity",
                "game.identity-image",
                "unity.project",
                "unity.package-dependency",
            },
        )


if __name__ == "__main__":
    unittest.main()
