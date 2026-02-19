#!/usr/bin/env python3
"""
⟡ MirrorDNA Doc Sync Agent — Automated doc accuracy keeper.
Runs via LaunchAgent daily (and on SHIPLOG changes).

1. Reads SHIPLOG.md
2. Runs generate_docs.py
3. Checks if anything changed
4. If changed → commit + push
5. Logs to bus

Run: python3 scripts/doc_sync.py
"""

import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime

DOCS_DIR = Path.home() / "repos" / "MirrorDNA-Docs"
SHIPLOG = Path.home() / ".mirrordna" / "SHIPLOG.md"
BUS_DIR = Path.home() / ".mirrordna" / "bus" / "changelog.jsonl"
LOG_FILE = Path.home() / ".mirrordna" / "logs" / "doc_sync.log"


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    try:
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def main():
    log("⟡ Doc Sync Agent starting")

    # 1. Check SHIPLOG exists
    if not SHIPLOG.exists():
        log("ERROR: SHIPLOG.md not found")
        sys.exit(1)

    # 2. Get SHIPLOG hash to detect changes
    shiplog_stat = os.stat(SHIPLOG)
    log(f"SHIPLOG: {shiplog_stat.st_size} bytes, modified {datetime.fromtimestamp(shiplog_stat.st_mtime).isoformat()}")

    # 3. Run the doc generator
    gen_script = DOCS_DIR / "scripts" / "generate_docs.py"
    if not gen_script.exists():
        log("ERROR: generate_docs.py not found")
        sys.exit(1)

    stdout, stderr, rc = run(f"python3 {gen_script}", cwd=str(DOCS_DIR))
    if rc != 0:
        log(f"ERROR: generate_docs.py failed: {stderr}")
        sys.exit(1)

    log(f"Generator output: {stdout}")

    # 4. Check git status for changes
    stdout, _, _ = run("git diff --stat", cwd=str(DOCS_DIR))
    if not stdout:
        log("No changes detected — docs are current")
        return

    log(f"Changes detected:\n{stdout}")

    # 5. Commit and push
    today = datetime.now().strftime("%Y-%m-%d")
    commit_msg = f"doc-sync: auto-update from SHIPLOG ({today})"

    _, _, rc1 = run("git add -A", cwd=str(DOCS_DIR))
    _, stderr, rc2 = run(f'git commit -m "{commit_msg}"', cwd=str(DOCS_DIR))
    if rc2 != 0:
        log(f"Commit failed: {stderr}")
        return

    _, stderr, rc3 = run("git push", cwd=str(DOCS_DIR))
    if rc3 != 0:
        log(f"Push failed: {stderr}")
        return

    log(f"Deployed: {commit_msg}")

    # 6. Write to bus
    try:
        import json
        entry = {
            "timestamp": datetime.now().isoformat(),
            "source": "doc_sync_agent",
            "event": "docs_updated",
            "message": commit_msg,
        }
        BUS_DIR.parent.mkdir(parents=True, exist_ok=True)
        with open(BUS_DIR, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        log(f"Bus write failed: {e}")

    log("⟡ Doc Sync complete")


if __name__ == "__main__":
    main()
