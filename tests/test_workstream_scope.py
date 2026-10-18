"""Exercise the actual CLI against temporary Git histories (no network)."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_workstream_scope.py"
ROOT = "courses/studios/cross-domain/round-03/"
BRANCH = "agent/cross-domain/issue-26"


class ScopeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Scope Test")
        self.git("config", "user.email", "scope-test@example.invalid")
        self.write("README.md")
        self.write(ROOT + "existing.md")
        self.base = self.commit()

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, text=True, stderr=subprocess.STDOUT
        ).strip()

    def write(self, path, content="fixture\n"):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-qm", "fixture")
        return self.git("rev-parse", "HEAD")

    def check(self, code, message, branch=BRANCH):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--base", self.base,
             "--head", "HEAD", "--branch", branch],
            cwd=self.repo, text=True, capture_output=True,
        )
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        self.assertIn(message, result.stdout + result.stderr)

    def test_r03_three_files_pass(self):
        for name in ("README.md", "WORKSHOP.md", "ANSWERS.md"):
            self.write(ROOT + name)
        self.commit()
        self.check(0, "checked_files=3")

    def test_other_round_rejected(self):
        self.write("courses/studios/cross-domain/round-04/README.md")
        self.commit()
        self.check(1, "outside assigned workstream")

    def test_prefix_lookalike_rejected(self):
        self.write("courses/studios/cross-domain/round-03-extra/README.md")
        self.commit()
        self.check(1, "outside assigned workstream")

    def test_shared_script_rejected(self):
        self.write("scripts/check_workstream_scope.py")
        self.commit()
        self.check(1, "outside assigned workstream")

    def test_unregistered_branch_rejected(self):
        self.check(2, "Unregistered branch scope", "agent/unregistered/issue-26")

    def test_branch_prefix_lookalike_rejected(self):
        self.check(2, "Unregistered branch scope", "agent/cross-domain-extra/issue-26")

    def test_banned_binary_in_scope_rejected(self):
        self.write(ROOT + "source.PDF")
        self.commit()
        self.check(1, "forbidden binary/private path")

    def test_out_of_scope_deletion_rejected(self):
        (self.repo / "README.md").unlink()
        self.commit()
        self.check(1, "outside assigned workstream: README.md")

    def test_rename_into_scope_checks_source(self):
        self.git("mv", "README.md", ROOT + "moved.md")
        self.commit()
        self.check(1, "outside assigned workstream: README.md")

    def test_rename_out_of_scope_checks_destination(self):
        self.git("mv", ROOT + "existing.md", "moved.md")
        self.commit()
        self.check(1, "outside assigned workstream: moved.md")

    def test_legal_unicode_and_newline_filenames(self):
        self.write(ROOT + "中文\nnotes.md")
        self.commit()
        self.check(0, "checked_files=1")

    def test_existing_workstream_still_passes(self):
        self.write("courses/daily/new.md")
        self.commit()
        self.check(0, "Scope OK", "agent/daily-learning/issue-14")

    def test_coord_still_rejects_private_path(self):
        self.write("private/example.md")
        self.commit()
        self.check(1, "forbidden binary/private path", "coord/test")

    def test_sync_from_main_excludes_reviewed_engineering_changes(self):
        self.git("branch", "r03")
        self.write("scripts/reviewed-fix.py")
        reviewed_base = self.commit()
        self.git("checkout", "-q", "r03")
        self.write(ROOT + "WORKSHOP.md")
        self.commit()
        self.git("merge", "--no-edit", reviewed_base)
        self.base = reviewed_base
        self.check(0, "checked_files=1")


if __name__ == "__main__":
    unittest.main()
