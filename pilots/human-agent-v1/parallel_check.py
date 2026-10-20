"""Concurrent engineering processes, not independent AI agents."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=HERE/'checks')
    parser.add_argument('--render-only', action='store_true')
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    commands = {
        'regression': [sys.executable, '-m', 'unittest', 'discover', '-s', str(HERE), '-p', 'test_*.py', '-v'],
        'build': [sys.executable, str(HERE/'build.py'), '--out', str(out/'build')],
        'browser': [sys.executable, str(HERE/'browser_check.py'), '--out', str(out/'browser')] + (['--render-only'] if args.render_only else []),
    }
    def run(item):
        name, command = item
        started = time.monotonic()
        r = subprocess.run(command, cwd=HERE, capture_output=True, text=True, timeout=180)
        (out/(name+'.log')).write_text(r.stdout+r.stderr, encoding='utf-8')
        return {'name': name, 'returncode': r.returncode, 'elapsed_seconds': round(time.monotonic()-started, 3), 'command': command}
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run, commands.items()))
    report = {'timestamp': datetime.now(timezone.utc).isoformat(), 'execution_kind': 'parallel_subprocesses_not_agents',
              'independent_agent_runs': 0, 'browser_mode': 'render_only' if args.render_only else 'file_navigation', 'results': results}
    (out/'parallel_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))
    return int(any(r['returncode'] for r in results))

if __name__ == '__main__':
    raise SystemExit(main())
