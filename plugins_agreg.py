import os
import sys
from pathlib import Path

import pygit2

from make_book.src.book import Book


frido_mark_list = []
frido_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
frido_mark_list.append("% SCRIPT MARK -- GARDE MES NOTES")
frido_mark_list.append("% SCRIPT MARK -- TOC")
frido_mark_list.append("% SCRIPT MARK -- FRIDO")
frido_mark_list.append("% SCRIPT MARK -- DÉVELOPPEMENTS POSSIBLES")
frido_mark_list.append("% SCRIPT MARK -- FINAL")

book_mark_list = frido_mark_list

research_mark_list = []
research_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
research_mark_list.append("% SCRIPT MARK -- GARDE MES NOTES")
research_mark_list.append("% SCRIPT MARK -- TOC")
research_mark_list.append("% SCRIPT MARK -- RESEARCH PART")
research_mark_list.append("% SCRIPT MARK -- FINAL")

mazhe_mark_list = []
mazhe_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
mazhe_mark_list.append("% SCRIPT MARK -- GARDE MAZHE")
mazhe_mark_list.append("% SCRIPT MARK -- TOC")
mazhe_mark_list.append("% SCRIPT MARK -- ENGLISH INTRODUCTION")
mazhe_mark_list.append("% SCRIPT MARK -- MOODLE")
mazhe_mark_list.append("% SCRIPT MARK -- INTRO SAGE")
mazhe_mark_list.append("% SCRIPT MARK -- FRIDO")
mazhe_mark_list.append("% SCRIPT MARK -- DÉVELOPPEMENTS POSSIBLES")
mazhe_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUES")
mazhe_mark_list.append("% SCRIPT MARK -- RESEARCH PART")
mazhe_mark_list.append("% SCRIPT MARK -- MATLAB")
mazhe_mark_list.append("% SCRIPT MARK -- EXERCICES")
mazhe_mark_list.append("% SCRIPT MARK -- CdI")
mazhe_mark_list.append("% SCRIPT MARK -- FINAL")


class set_filename(object):
    def __init__(self, new_output_filename):
        self.new_output_filename = new_output_filename

    def __call__(self, medicament):
        raise DeprecationWarning(
            "Use myRequest.new_output_filename='foo.pdf' instead")
        medicament.new_output_filename = self.new_output_filename

# TODO : use a partial object from the module 'functools'
# https://pymotw.com/3/functools/


class set_counter(object):
    def __init__(self, counter_name, init_value, final_value):
        self.counter_name = counter_name
        self.init_value = init_value
        self.final_value = final_value

    def __call__(self, A):
        """
        Changes the line
        \setcounter{<counter_name>}{<init_value>}
        into
        \setcounter{<counter_name>}{<final_value>}
        """
        u = "\setcounter{{{}}}{{{}}}".format(
            self.counter_name, self.init_value)
        S = A.replace(u, u.replace(
            str(self.init_value), str(self.final_value)))
        return S


class set_boolean(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __call__(self, A):
        r"""
        Changes the line
        \boolfalse{<name>}
        into
        \booltrue{<name>}
        or the contrary
        """
        true_line = r"\booltrue{{{}}}".format(self.name)
        false_line = r"\boolfalse{{{}}}".format(self.name)
        if self.value == "true":
            S = A.replace(false_line, true_line)
        elif self.value == "false":
            S = A.replace(true_line, false_line)
        else:
            raise ValueError("You have to choose between 'true' of 'false'")
        return S


class set_pdftitle(object):
    def __init__(self, pdftitle):
        self.pdftitle = pdftitle

    def __call__(self, old_text):
        r"""
        Changes the line
        \newcommand{\pdftitle}{<wathever>}
        into
        \newcommand{\pdftitle}{<pdftitle>}

        @param {str} `old_text`     the tex file which will be compiled
        @return {str}               the tex file (changed) to be compiled
        """
        mark = r"\newcommand{\pdftitle}"
        new_command_line = r"""\newcommand{\pdftitle}{PDFTITLE}""".replace(
            "PDFTITLE", self.pdftitle)
        new_text_list = []
        for line in old_text.split("\n"):
            if line.startswith(mark):
                new_text_list.append(new_command_line)
            else:
                new_text_list.append(line)
        return "\n".join(new_text_list)


set_isFrido = set_boolean("isFrido", "true")


def up_to_text(liste, text):
    for i, l in enumerate(liste):
        if l.startswith(text):
            return i


def is_dirty(repo):
    status = repo.status()
    print("list done")
    for filepath, flags in status.items():
        if flags != pygit2.GIT_STATUS_CURRENT:
            if flags != 16384:
                return True
    return False


def get_hexsha(repo):
    commit = repo.revparse_single('HEAD')
    return commit.id


def set_commit_hexsha(A):
    repo = pygit2.Repository(os.getcwd())
    hexsha = str(get_hexsha(repo))
    if is_dirty(repo):
        hexsha = hexsha+" -- and slightly more"
    u = "\\newcommand{\GitCommitHexsha}{\info{missing information}}"
    print(hexsha)
    A = A.replace(u, u.replace("missing information", hexsha))
    return A


def assert_MonCerveau_first(options):
    """
    Check that the reference "MonCerveau" is the first one.

    Make the check in the bbl file.
    """
    filename = "Inter_frido-mazhe_pytex.bbl"
    bbl_filename = options.bibliographie()
    if not os.path.exists(bbl_filename):
        print(f"Le fichier {bbl_filename} n'existe pas. C'est pas très normal.  Si cela persiste à la prochaine compilation, posez-vous des questions.")
        return None
    bbl_content = open(bbl_filename).read()
    bbl_first = bbl_content.find("bibitem")
    bbl_second = bbl_content.find("bibitem", bbl_first+1)
    text = bbl_content[bbl_first:bbl_second]
    if not "MonCerveau" in text:
        print("""Il semblerait que la référence bibliographique 'MonCerveau' ne soit pas la première. Il faut corriger ça. En effet, le lecteur doit savoir que lorsqu'il voit la référence [1], ça veut dire 'danger'.

        Après modification, le plus simple est de supprimer le fichier {} et de relancer.

                """.format(filename))
        raise ValueError(
            f"The reference 'MonCerveau' is not the first one. The first is one is: {text}")


def split_toc(name, n):
    """
    Rewrites the TOC file with adding "(Vol i)" to the chapter name.
    With i being the number of the volume in which the
    chapter should appears.

    @param n : the number of volumes
    @param name (string) the name of the document we are speaking about
    @return : a function which makes the work

    The parameter 'name' serves to distinguish 'frido' from 'book' when
    creating the pathname of the toc file.
    """

    def _split_doc(options=None):
        cwd = os.getcwd()
        sys.path.append(os.path.join(cwd, "python"))
        toc_filename = f"Inter_{name}-mazhe_pytex.toc"
        pdf_filename = f"Inter_{name}-mazhe_pytex.pdf"
        toc_path = Path('.').resolve() / toc_filename
        pdf_path = Path('.').resolve() / pdf_filename
        book = Book(toc_path, pdf_path)
        book.rewrite_toc(n)
    return _split_doc
