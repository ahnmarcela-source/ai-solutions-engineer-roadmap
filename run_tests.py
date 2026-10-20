import subprocess
import sys
from pathlib import Path
root = Path(__file__).resolve().parent
for stage in sorted(p for p in root.iterdir() if p.is_dir() and p.name[:2].isdigit()):
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', str(stage / 'poc'), '-p', 'test_*.py', '-v'], cwd=root)
    if result.returncode:
        raise SystemExit(result.returncode)
print('All stage suites passed')
