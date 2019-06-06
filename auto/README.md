# Le répertoire `auto`

Contient des fichiers générés automatiquement. Ils sont fournis pour vous simplifier la compilation du document, et diminuer le nombre de dependences.

* `pictures_tex` contient les fichiers des figures générées par [phystricks](https://github.com/LaurentClaessens/phystricks). Vous pouvez créer ces fichiers vous-même avec le script `figures_giulietta.py`, mais cela prend du temps, demande plusieurs passes et des dependences.
* `pictures_tikz` contient les fichiers `md5` et `pdf` des figures générés par `pdflatex/tikz` lors de la première compilation. Sans ces fichiers, la première compilation prend un temps énorme (plusieurs heures).
