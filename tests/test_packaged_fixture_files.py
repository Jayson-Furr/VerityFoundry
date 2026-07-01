from ast import literal_eval
from fnmatch import fnmatch
from pathlib import Path
import unittest

from verityfoundry.manifests import (
    load_example_manifests,
    load_golden_manifests,
    matrix_paths,
    prompt_paths,
)


ROOT = Path(__file__).resolve().parents[1]


def data_file_patterns() -> set[str]:
    patterns: set[str] = set()
    in_section = False
    for line in (ROOT / "pyproject.toml").read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("["):
            in_section = stripped == "[tool.setuptools.data-files]"
            continue
        if not in_section or "=" not in stripped:
            continue
        _, value = stripped.split("=", 1)
        parsed = literal_eval(value.strip())
        if isinstance(parsed, list):
            patterns.update(str(item) for item in parsed)
    return patterns


def is_packaged(relative_path: Path, patterns: set[str]) -> bool:
    target = relative_path.as_posix()
    return any(fnmatch(target, pattern) for pattern in patterns)


class PackagedFixtureFileTests(unittest.TestCase):
    def test_example_fixture_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        self.assertTrue(patterns)

        referenced: list[Path] = []
        for manifest_path, manifest in load_example_manifests(ROOT):
            referenced.append(manifest_path.relative_to(ROOT))
            base = manifest_path.parent
            for section in (
                "inputs",
                "expectedOutputs",
                "workspaceFixtures",
                "provenanceExamples",
            ):
                for relative in manifest.get(section, []):
                    referenced.append((base / relative).relative_to(ROOT))

        unpackaged = [
            path.as_posix()
            for path in sorted(set(referenced))
            if not is_packaged(path, patterns)
        ]
        self.assertEqual(unpackaged, [])

    def test_schemas_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        unpackaged = [
            path.relative_to(ROOT).as_posix()
            for path in sorted((ROOT / "schemas").glob("*.json"))
            if not is_packaged(path.relative_to(ROOT), patterns)
        ]

        self.assertEqual(unpackaged, [])

    def test_config_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        unpackaged = [
            path.relative_to(ROOT).as_posix()
            for path in sorted((ROOT / "config").glob("*.json"))
            if not is_packaged(path.relative_to(ROOT), patterns)
        ]

        self.assertEqual(unpackaged, [])

    def test_snapshot_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        unpackaged = [
            path.relative_to(ROOT).as_posix()
            for path in sorted((ROOT / "snapshots").glob("*/*.json"))
            if not is_packaged(path.relative_to(ROOT), patterns)
        ]

        self.assertEqual(unpackaged, [])

    def test_render_profile_snapshot_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        unpackaged = [
            path.relative_to(ROOT).as_posix()
            for path in sorted((ROOT / "snapshots" / "render-profiles").glob("*.md"))
            if not is_packaged(path.relative_to(ROOT), patterns)
        ]

        self.assertEqual(unpackaged, [])

    def test_release_review_fixture_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        unpackaged = [
            path.relative_to(ROOT).as_posix()
            for path in sorted((ROOT / "fixtures").glob("*/*/*.json"))
            if not is_packaged(path.relative_to(ROOT), patterns)
        ]

        self.assertEqual(unpackaged, [])

    def test_prompt_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        unpackaged = [
            path.relative_to(ROOT).as_posix()
            for path in prompt_paths(ROOT)
            if not is_packaged(path.relative_to(ROOT), patterns)
        ]

        self.assertEqual(unpackaged, [])

    def test_matrix_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        unpackaged = [
            path.relative_to(ROOT).as_posix()
            for path in matrix_paths(ROOT)
            if not is_packaged(path.relative_to(ROOT), patterns)
        ]

        self.assertEqual(unpackaged, [])

    def test_golden_output_files_are_included_in_data_files(self) -> None:
        patterns = data_file_patterns()
        referenced: list[Path] = []
        for manifest_path, manifest in load_golden_manifests(ROOT):
            referenced.append(manifest_path.relative_to(ROOT))
            referenced.append((manifest_path.parent / manifest["outputPath"]).relative_to(ROOT))

        unpackaged = [
            path.as_posix()
            for path in sorted(set(referenced))
            if not is_packaged(path, patterns)
        ]
        self.assertEqual(unpackaged, [])


if __name__ == "__main__":
    unittest.main()
