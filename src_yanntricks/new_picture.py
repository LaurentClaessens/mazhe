#! /usr/bin/python3

import sys
import os
import random
import string
from pathlib import Path

import dirmanage    # working directory is mazhe's main dir.


def via_random(alphabet, n):
    """Return a string of `n` random letters."""
    a = ""
    for k in range(0, n):
        a = a + random.choice(alphabet)
    return a


def create_name():
    """Create a name for the picture."""
    a = via_random(string.ascii_uppercase, 4)
    b = via_random(string.ascii_letters, 8)
    return a + "oo" + b


def create_file(filename, text):
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write(text)
    else:
        print(f"Le fichier {filename} existe déjà. Je ne fais rien.")


def do_work():
    figure_name = create_name()
    src_dir = Path('.') / "src_yanntricks"

    skel_path = src_dir / "picture.skel"
    with open(skel_path, 'r') as skel_file:
        code_base = skel_file.read()

    code = code_base.replace("XXXX", figure_name)

    yanntricks_file = Path('.')\
                    / "src_yanntricks"\
                    / f"yanntricks{figure_name}.py"

    fig_file = Path('.')\
                / "auto"\
                / "pictures_tex"\
                / f"Fig_{figure_name}.pstricks"

    pdf_file = Path('.')\
                / "auto"\
                / "pictures_tikz"\
                / f"tikzFIGLabelFig{figure_name}PICT{figure_name}.pdf"

    md5_file = Path('.')\
                / "auto"\
                / "pictures_tikz"\
                / f"tikzFIGLabelFig{figure_name}PICT{figure_name}.md5"

    yanntricks_file = yanntricks_file.resolve()
    fig_file = fig_file.resolve()
    pdf_file = pdf_file.resolve()
    md5_file = md5_file.resolve()

    for f in [yanntricks_file, fig_file, pdf_file]:
        create_file(f, code)
    create_file(md5_file, "")

    print("")
    print("For `src_yanntricks/figures_mazhe.py :`")
    print(f"from yanntricks{figure_name} import {figure_name}")
    print(f"append_picture({figure_name}, 1)")
    print("")
    print(f"git add {yanntricks_file} "
            f" {fig_file}"
            f" {pdf_file}"
            f" {md5_file}")
    print("")
    print(f"attach('{yanntricks_file}');{figure_name}();exit()")

do_work()
