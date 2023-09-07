"""Manage the subdirectory issue."""


import os
import sys
from pathlib import Path


this_dir = Path(__file__).parent
frido_dir = (this_dir / "..").resolve()
init_dir = Path(os.getcwd()).resolve()
base_dir = this_dir
sys.path.append(str(base_dir))
