import os
from pathlib import Path


init_dir = Path('.')
base_dir = (init_dir / ".." / "..").resolve()
os.chdir(base_dir)
