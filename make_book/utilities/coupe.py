#!/usr/bin/python3

"""
Le script qui découpe le fichier d'index thématique en petits fichiers.

Ce script a été utilisé le 16 avril 2022 et n'a plus d'utilité plus tard.
"""


from pathlib import Path


def pairs(L):
    for num in range(0, len(L)):
        yield L[num], L[num + 1]


def get_cut_numbers(lines):
    answer = []
    for num, line in enumerate(lines):
        if "InternalLinks" in line:
            answer.append(num - 1)
    return answer


def split_thematic():
    """Create the files for the thematic index."""
    thm_filename = Path(".").resolve() / "158_thematique.tex"
    lines = open(thm_filename, 'r').read().splitlines()
    numbers = get_cut_numbers(lines)
    file_num = 0
    for pair in pairs(numbers):
        file_num += 1
        part = lines[pair[0]: pair[1]]
        base = f"{file_num + 500}_thm"
        text = "\n".join(part)
        Path(f"{base}.tex").write_text(text)
        print(f"\\input{{{base}}}")


def get_thm_files(front_dir):
    """Yield the _*thm.tex files"""
    for elem in front_dir.iterdir():
        if elem.suffix != '.tex':
            continue
        if not elem.name.endswith("_thm.tex"):
            continue
        yield elem


def no_label(line):
    """Remove \\label{{}}"""
    if "\\label" not in line:
        return line

    init = line.find("\\label{")
    return line[0:init]


def get_title_line(content):
    """Return the line with InternalLinks"""
    for line in content.splitlines():
        if "InternalLinks" in line:
            return no_label(line).strip()


def get_title(content):
    """return the title of the given index."""
    title_line = get_title_line(content)
    sub = title_line.replace("\\InternalLinks{", "")
    title = sub[:-1]
    return title


def add_comment():
    """For each input{xxx_thm} we add a comment with the title."""
    base_dir = (Path('.') / ".." / "..").resolve()
    front_dir = base_dir / "tex" / "front_back_matter"
    commented = []
    for elem in get_thm_files(front_dir):
        content = elem.read_text()
        title = get_title(content)
        input_line = f"\\input{{{elem.stem}}}  % {title}"
        commented.append((elem.stem, input_line))

    commented.sort(key=lambda x: x[0])
    for foo in commented:
        print(foo[1])


add_comment()
