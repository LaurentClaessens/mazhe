#!/usr/bin/python3

"""Reconstitue deux fichiers depuis un rej."""


import dirmanage


def sanitize(line):
    """Remove the trailing +/- and the spaces."""
    one = line[1:]
    return one.lstrip()


def do_work():
    """Create the files for the thematic index."""
    rej_filename = dirmanage.base_dir / "197_racines.tex.rej"
    print(rej_filename)
    lines = open(rej_filename, 'r').read().splitlines()
    plus = []
    minus = []
    for line in lines:
        if line.startswith('+'):
            new_line = sanitize(line)
            plus.append(new_line)
        if line.startswith('-'):
            new_line = sanitize(line)
            minus.append(new_line)

    with open('plus.tex', 'w') as plus_file:
        plus_file.write("\n".join(plus))
    with open('minus.tex', 'w') as minus_file:
        minus_file.write("\n".join(minus))


do_work()
