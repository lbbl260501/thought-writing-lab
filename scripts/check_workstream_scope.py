#!/usr/bin/env python3
"""Check task-branch changed paths before merging into main.

Does not replace protected-branch settings, scientific editorial review, or the
private Google Sheets single-writer convention.

Usage:
  python scripts/check_workstream_scope.py --base BASE_SHA --head HEAD_SHA --branch agent/miccai25/issue-2
"""
from __future__ import annotations
import argparse
from pathlib import Path
import subprocess
import sys

ALLOWED = {
    "agent/miccai25/": ("corpora/miccai/2025/",),
    "agent/miccai26/": ("corpora/miccai/2026/",),
    "agent/academic-english/": ("language/academic-writing/",),
    "agent/scientific-reasoning/": ("knowledge/scientific-reasoning/",),
    "agent/interdisciplinary/": ("knowledge/interdisciplinary/",),
}
# Integration and core-governance PRs are main-chat owned and manually reviewed.
MAINTAINER_PREFIX = "coord/"
BANNED_SUFFIXES = (".pdf", ".epub", ".mobi", ".djvu", ".sqlite", ".db", ".zip", ".7z", ".env")
BANNED_DIRS = (".git/", "private/", "raw/", "cache/")

def run(*cmd: str) -> str:
    return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT).strip()

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--base", required=True)
    p.add_argument("--head", required=True)
    p.add_argument("--branch", required=True)
    args = p.parse_args()

    if args.branch.startswith(MAINTAINER_PREFIX):
        # This exception is procedural: only the main coordination chat should
        # work on coord/* and every such PR needs manual review.
        allowed_paths = None
    else:
        match = next(((prefix, paths) for prefix, paths in ALLOWED.items()
                      if args.branch.startswith(prefix)), None)
        if match is None:
            print(f"Unregistered branch scope: {args.branch}", file=sys.stderr)
            return 2
        allowed_paths = match[1]

    merge_base = run("git", "merge-base", args.base, args.head)
    files = run("git", "diff", "--name-only", "--diff-filter=ACMRD",
                merge_base, args.head).splitlines()
    failures = []
    for fn in files:
        path = fn.replace("\\", "/")
        if Path(path).suffix.lower() in BANNED_SUFFIXES or path.startswith(BANNED_DIRS):
            failures.append(f"forbidden binary/private path: {path}")
        if allowed_paths is not None and not any(path.startswith(prefix)
                                                for prefix in allowed_paths):
            failures.append(f"outside assigned workstream: {path}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Scope OK: branch={args.branch}, checked_files={len(files)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
