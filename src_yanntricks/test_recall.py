#! /usr/bin/python3

# This script compares the files "*.pstricks" with the corresponding one
# "*.pstricks.recall" and prints a warning if they are not equal.

from pathlib import Path
import os

AUTO_TEX_DIR = (Path('.') / ".." / "auto" / "pictures_tex").resolve()
SRC_YANNTRICKS = Path('.').resolve()


def split_filepath(path):
    """Return the tupe (dir, radical, ext)."""
    parent = path.parent
    radical = path.with_suffix('').name
    ext = path.suffix
    return parent, radical, ext


def pstricks_files_iterator():
    for elem in AUTO_TEX_DIR.iterdir():
        _, _, ext = split_filepath(elem)
        if ext == ".pstricks":
            yield elem

def get_recall(pstricks_file):
    """Return the recall file for the provided filename."""
    recall_filename = Path(str(pstricks_file) + ".recall")
    _, radical, ext = split_filepath(recall_filename)
    return SRC_YANNTRICKS / f"{radical}{ext}"


def do_work():
    """Makes the work."""
    for pstricks_file in pstricks_files_iterator():
        recall_file = get_recall(pstricks_file)
        get_text = open(pstricks_file, 'r').read()

        try:
            recall_text = open(recall_file, 'r').read()
        except FileNotFoundError as err:
            print(f"No recall file for {pstricks_file}")
            continue

        if get_text != recall_text:
            print(f"Wrong: {pstricks_file}")
            with open('auto_vimdiff.sh', 'a') as shell:
                shell.write(f"vimdiff {pstricks_file} "
                            f"{recall_file} \n")

do_work()
