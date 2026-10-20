"""Load each numbered stage without requiring pip packaging."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_stage(number):
    folders = sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith(f"{number:02d}-"))
    if len(folders) != 1:
        raise RuntimeError(f"stage {number} not found")
    path = folders[0] / "poc" / "app.py"
    spec = importlib.util.spec_from_file_location(f"stage_{number}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
