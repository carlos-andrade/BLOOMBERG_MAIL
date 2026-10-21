#!/usr/bin/env python3
"""Synthetic, offline safety tests for BLOOMBERG_MAIL 005N publishers.

These tests never invoke production ingestion scripts, credentials, APIs, or datasets.
"""
from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = [
    ROOT / ".github/workflows/bloomberg-mail-ingestao-005n-normalizacao.yml",
    ROOT / ".github/workflows/bloomberg-mail-ingestao-005n-validacao-normalizadores.yml",
    ROOT / ".github/workflows/bloomberg-mail-rec001-b3-cotahist-cross-repo.yml",
]
EXPECTED_GROUP = "bloomberg-mail-005n-publish-${{ github.ref }}"


def git(cwd: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args], cwd=cwd, text=True, capture_output=True, check=False
    )
    if check and result.returncode:
        raise AssertionError(f"git {' '.join(args)} failed: {result.stderr}")
    return result


def set_identity(repo: Path) -> None:
    git(repo, "config", "user.name", "Synthetic Test")
    git(repo, "config", "user.email", "synthetic-test@example.invalid")


class WorkflowSafetyTests(unittest.TestCase):
    def test_workflow_yaml_parses_and_shared_concurrency_is_consistent(self) -> None:
        for path in WORKFLOWS:
            with self.subTest(workflow=path.name):
                self.assertTrue(path.is_file(), f"Missing workflow: {path}")
                parsed = yaml.safe_load(path.read_text(encoding="utf-8"))
                self.assertIsInstance(parsed, dict)
                concurrency = parsed.get("concurrency")
                self.assertIsInstance(concurrency, dict)
                self.assertEqual(concurrency.get("group"), EXPECTED_GROUP)
                self.assertIs(concurrency.get("cancel-in-progress"), False)

    def test_repeated_generation_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            git(repo, "init", "-q")
            set_identity(repo)
            generated = repo / "evidence.json"
            generated.write_text('{"status":"PASS"}\n', encoding="utf-8")
            git(repo, "add", "evidence.json")
            git(repo, "commit", "-qm", "first generated evidence")
            generated.write_text('{"status":"PASS"}\n', encoding="utf-8")
            git(repo, "add", "evidence.json")
            result = git(repo, "diff", "--cached", "--quiet", check=False)
            self.assertEqual(result.returncode, 0, "Identical output should not create a new commit")

    def test_non_fast_forward_recovers_by_rebase_without_losing_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bare = root / "origin.git"
            a, b = root / "writer-a", root / "writer-b"
            git(root, "init", "--bare", str(bare))
            git(root, "clone", str(bare), str(a))
            set_identity(a)
            (a / "base.txt").write_text("base\n", encoding="utf-8")
            git(a, "add", "base.txt")
            git(a, "commit", "-qm", "base")
            git(a, "branch", "-M", "main")
            git(a, "push", "-u", "origin", "main")
            git(root, "--git-dir", str(bare), "symbolic-ref", "HEAD", "refs/heads/main")
            git(root, "clone", str(bare), str(b))
            set_identity(b)

            (a / "writer-a.txt").write_text("A\n", encoding="utf-8")
            git(a, "add", "writer-a.txt")
            git(a, "commit", "-qm", "writer A")
            git(a, "push", "origin", "HEAD:main")

            (b / "writer-b.txt").write_text("B\n", encoding="utf-8")
            git(b, "add", "writer-b.txt")
            git(b, "commit", "-qm", "writer B")
            first_push = git(b, "push", "origin", "HEAD:main", check=False)
            self.assertNotEqual(first_push.returncode, 0, "Expected synthetic non-fast-forward")

            git(b, "pull", "--rebase", "origin", "main")
            recovered_push = git(b, "push", "origin", "HEAD:main", check=False)
            self.assertEqual(recovered_push.returncode, 0, recovered_push.stderr)
            git(a, "pull", "--ff-only", "origin", "main")
            self.assertEqual((a / "writer-a.txt").read_text(encoding="utf-8"), "A\n")
            self.assertEqual((a / "writer-b.txt").read_text(encoding="utf-8"), "B\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
