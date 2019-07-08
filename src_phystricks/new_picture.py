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
    src_dir = Path('.') / "src"

    skel_path = src_dir / "picture.skel"
    with open(skel_path, 'r') as skel_file:
        code_base = skel_file.read()

    code = code_base.replace("XXXX", figure_name)

    phystricks_file = Path('.')\
                    / "src"\
                    / f"phystricks{figure_name}.py"

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

    for f in [phystricks_file, fig_file, pdf_file]:
        create_file(f, code)
    create_file(md5_file, "")

    print(f"from phystricks{figure_name} import {figure_name}")
    print(f"git add {filename.from_here()}"
            "{pstricksfilename.from_here()}"
            "{pdffilename.from_here()}"
            "{md5filename.from_here()}"
    print(f"attach('{filename.filename}');{figure_name}();exit()")

do_work()
