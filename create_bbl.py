#!venv/bin/python3


import sys
from pathlib import Path

from utilities import read_json_file
from utilities import write_json_file
from utilities import random_string
from utilities import json_to_str
from utilities import text_hash
_ = write_json_file
_ = random_string
_ = sys


dprint = print


def line_to_labels(line):
    """Return the labels on a citation line."""
    start = line.find("{") + 1
    end = line.find("}")
    content = line[start:end]
    return content.split(",")


def is_citation_line(line):
    """Say if a line is a citation line."""
    return line.startswith("\\citation")


def filter_duplicates(labels):
    """
    Return a list without the duplicates.

    The point of this function is to maintain the order.
    """
    new_list = []
    for elem in labels:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


def get_labels(aux_file):
    """Return the list of labels in the given aux file."""
    lines = aux_file.read_text().splitlines()

    cited_labels = []
    for line in lines:
        if not is_citation_line(line):
            continue
        line_labels = line_to_labels(line)
        for label in line_labels:
            # label can be "" when in the LaTeX source we write
            # \cite{onelabe,}
            if label:
                cited_labels.append(label)

    cited_labels = filter_duplicates(cited_labels)
    return cited_labels


def get_json(json_bib, label):
    """Return the json of the requested label"""
    for elem in json_bib:
        if elem["id"] == label:
            return elem


def get_bibtex_lines(bibtex_lines, label):
    found = False
    lines = []
    for line in bibtex_lines:
        if found:
            if line.startswith("@"):
                return lines
            lines.append(line)
        if label not in line:
            continue
        found = True

    if found:
        return lines


def bib_hash(elem):
    """Return a hash of the element."""
    txt = json_to_str(elem)
    return text_hash(txt)


def get_elem_bibitem(elem):
    """Return the bibitem line of a bbl entry."""
    label = elem["id"]
    _ = label
    return f"\\bibitem[{bib_hash(elem)}]{{{label}}}"


def get_elem_author(elem):
    """Return the author line."""
    if elem.get("author", None) is None:
        return None
    authors = [f"{author.get('given', '')} {author.get('family', '')}"
               for author in elem["author"]]
    return "and".join(authors)+"."


def json_to_bbl_elem(elem):
    """From a json element, return the bbl code."""
    if elem is None:
        raise

    list_ans = []
    list_ans.append(get_elem_bibitem(elem))
    list_ans.append(get_elem_author(elem))

    title = elem.get("title", None)
    date = elem.get("date", None)
    url = elem.get("URL", None)
    if title:
        list_ans.append(f"\\newblock {title}.")
    if date:
        list_ans.append(f"\\newblock {date}.")
    if url:
        list_ans.append(f"\\newblock URL \\url{{{url}}}.")

    lines = [x for x in list_ans if x is not None]
    return "\n".join(lines)


def bbl_code(aux_file, json_bib, bbl_template):
    """Return the code of the bbl file."""
    template = bbl_template.read_text()
    labels = get_labels(aux_file)
    bbl_list = []
    for label in labels:
        elem = get_json(json_bib, label)
        block = json_to_bbl_elem(elem)
        bbl_list.append(block)

    main_code = "\n".join(bbl_list)
    return template.replace("**BBL_CODE**", main_code)


aux_file = Path("Inter_frido-mazhe_pytex.aux")
json_bib = read_json_file("mazhe.json")
bbl_template = Path("bbl_template.tex")
print(bbl_code(aux_file, json_bib, bbl_template))
