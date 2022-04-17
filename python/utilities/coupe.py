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


def do_work():
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


do_work()
