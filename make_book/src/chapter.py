from src.utilities import dprint
from src.splittoc import IeC_remove
_ = dprint


class Chapter(object):
    r"""
    A chapter is defined from its TOC line which looks like

    ```
\contentsline {chapter}{\numberline {36}Cha\IeC {\^\i }nes de Markov \IeC {\`a} temps discret}{1731}{chapter.36}
    ```

    We use some string manipulations in order to extract the informations :
    - chapter title
    - starting page
    - chapter number
    """

    def __init__(self, original):
        self.original = original
        self.noIeC = IeC_remove(original)
        self.first_page = self.get_first_page()
        self.title = self.get_title()

        dprint("un chapitre")
        dprint(f"  title   {self.title}")
        dprint(f"  prem p. {self.first_page}")

    def number(self):
        a = self.noIeC.split("{")
        sn = a[3][0:a[3].find("}")]
        return int(sn)

    def get_title(self) -> str:
        a = self.noIeC.split("{")
        b = a[3].split("}")
        t = b[1]
        if "IeC" in t:
            print(t)
            raise ValueError
        return(t)

    def get_first_page(self):
        a = self.noIeC.split("{")
        b = a[4].split("}")
        return int(b[0])

    def hack(self, i):
        """
        Append "(vol i)" at the end of the chapter's title.
        """
        a = self.original.split("}")
        a[-4] = a[-4]+" (Vol {})".format(i)
        return "}".join(a)
