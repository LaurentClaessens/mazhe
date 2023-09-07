"""
Requires the python module pdfrw (apt install python3-pdfrw)

The purpose of this module is two-fold
- Adding (Vol k) to the chapter names in the table of contents.
  The division is automatic from the given number of volumes.
  This is called from 'lst_frido.py' via the plugin 'split_toc'.
- Actually recompose the 'n' pdf for the decomposition in 'n' parts.
  This functionality is called from the script "split_book.py".
"""


class UnicodeCouple(object):
    def __init__(self, iec, utf):
        self.iec = "\IeC {{{}}}".format(iec)
        self.utf = utf


def IeC_remove(s):
    IeC_couples = []
    IeC_couples.append(UnicodeCouple("\\^\\i ", "î"))
    IeC_couples.append(UnicodeCouple("\\'e", "é"))
    IeC_couples.append(UnicodeCouple("\\^e ", "ê"))
    IeC_couples.append(UnicodeCouple("\\^o ", "ô"))
    IeC_couples.append(UnicodeCouple("\\\"o ", "ö"))
    IeC_couples.append(UnicodeCouple("\\\"u ", "ü"))
    IeC_couples.append(UnicodeCouple("\\`e", "è"))
    IeC_couples.append(UnicodeCouple("\\`A ", "Á"))
    IeC_couples.append(UnicodeCouple("\\`u ", "ù"))
    IeC_couples.append(UnicodeCouple("\\`a", "à"))
    IeC_couples.append(UnicodeCouple("\\'E", "É"))

    for c in IeC_couples:
        s = s.replace(c.iec, c.utf)
    return s


def is_chapter_line(line):
    """
    Return 'true' is 'line' is a line defining a chapter
    in the toc file.
    """
    starting_string = """\contentsline {chapter}{\\numberline {"""
    return line.startswith(starting_string)
