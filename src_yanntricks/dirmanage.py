import os
import sys
from pathlib import Path


base_dir = Path("..").resolve()
pak_dir = base_dir / "venv/lib/python3.10/site-packages"
auto_dir = base_dir / "auto/pictures_tex"

sys.path.append(os.getcwd())
sys.path.append('/usr/lib/python3/dist-packages/')
sys.path.append(str(pak_dir))

os.chdir(str(auto_dir))
