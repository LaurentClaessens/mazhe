#! /usr/bin/env python3
# -*- coding: utf8 -*-

import os

def isbn(title,n):
    if title=="Le Frido":
        if n==1:
            return "978-2-9540936-5-9"
        if n==2:
            return "978-2-9540936-6-6"
        if n==3:
            return "978-2-9540936-7-3"       
    raise ValueError("No ISBN attributed for the title "+title)

def latex_code(title,n):
    """
    Return the latex code to be compiled for volume 'n'
    """

    sn=str(n)
    text=r"""
\input{e_couverture} 

\begin{document} 

\pagestyle{empty}

\begin{center}
    {\Large """+title+r""", volume """+sn+r"""}\\
    Laurent Claessens
\end{center}

\vspace{3cm}

\begin{center}
    \includegraphics[width=17cm]{vol"""+sn+r""".png}
\end{center}

\newpage

\noindent
\Large
"""+title+r""", volume """+sn+r"""\\
\noindent
\large
Laurent Claessens

\normalsize

\vspace{4cm}

\noindent
Ce livre est destiné aux candidats à l'agrégation de mathématique. Très complet, il couvre la quasi totalité du programme de façon claire et détaillée (rien n'est supposé évident). Publié sous une licence libre (FDL), vous pouvez télécharger une version PDF sur le site de l'auteur :\\
http://laurent.claessens-donadello.eu/pdf/lefrido-vol"""+sn+r""".pdf 

\noindent
Ceci est une œuvre qui se veut collaborative, ainsi n'hésitez pas à écrire à l'auteur pour faire valoir toutes vos remarques et suggestions en vue d'une nouvelle édition plus belle, plus correcte et plus utile.

\noindent
Retrouvez des informations complémentaires sur la page dédié :\\
http://laurent.claessens-donadello.eu/frido.html

\vfill

LOGO

"""+isbn(title,n)+r"""

\end{document}
    """
    return text


title="Le Frido"

for i in [1,2,3]:
    code=latex_code(title,i)
    filename="couverture"+str(i)+".tex"
    with open(filename,'w') as f:
        f.write(code)

    os.system("pdflatex "+filename)
