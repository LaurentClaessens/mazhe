"""Manage the subdirectory issue."""


import os
import sys
from pathlib import Path


this_dir = Path(__file__).parent
init_dir = Path(os.getcwd()).resolve()
base_dir = (this_dir / "..").resolve()
sys.path.append(str(base_dir))
