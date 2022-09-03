#!/usr/bin/python3

"""
This is a single-usage script.

It renames 'phystricks*.py' -> 'yanntricks*.py' in the requested
directory.
"""

import sys
from pathlib import Path

directory = Path(sys.argv[1]).resolve()

for elem in directory.iterdir():
    dirname = elem.parent
    filename = elem.name
    ext = elem.suffix
    if not filename.startswith('phystricks'):
        continue
    new_filename = filename.replace("phystricks", "yanntricks")
    old_path = dirname / filename
    new_path = dirname / new_filename
    print("---")
    print(old_path)
    print(new_path)
    old_path.rename(new_path)
