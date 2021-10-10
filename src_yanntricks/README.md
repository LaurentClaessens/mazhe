# Le répertoire `src_phystricks`

Ce répertoire contient les «sources» des figures. C'est le script `figures_giulietta.py` qui se charge de les compiler et de produire le code `tikz`. Le mécanisme fait appel à [physrticks](https://github.com/laurentclaessens/phystricks).

Vous ne devriez pas être intéressé par ce répertoire, à moins que vous ne comptiez modifier une figure; mais attention : il y a de l'apprentissage.

## Pour recréer les figures

### Préparation

Supprimer les fichiers qui vont être recréés. En supposant être dans le répertoire principal (et non ici) :
```
rm auto/pictures_tex/*.pstricks & rm auto/pictures_tikz/*.md5 & rm auto/pictures_tikz/*.pdf
```
(je rappelle que `rm` est un ancien mot sud-africain signifiant «fais tes backup !!»).

### Création des fichiers `pstricks`

Le fichier `Directories.py` contient les chemins relatifs des différents répertoires vers lesquels le script va chercher ses ressources et placer les fichiers créés. Ce fichier devrait être à jour.

Lancer le script `figures_giulietta.py` :
```bash
cd src_phystricks
figures_giulietta.py --all
```

Cette opération devrait prendre pas mal de temps et produire une longue liste de warning à propos de fichiers `aux` manquants. Ensuite vous compilez le document, d'abord pour obtenir toutes les références correctes :
```bash
pytex lst_giulietta.py --no-external
```
Le `--no-external` fait en sorte que `tikz` ne va pas chercher à créer le `pdf` de chaque figure. Le but de cette compilation est de faire en sorte que `pdflatex` crée les fichiers `aux` contenant la taille des boîtes inclues dans les figures.

Retour à la compilation des figures :
```bash
figures_giulietta.py --all
```
Il devrait y avoir beaucoup moins de warning.

Maintenant vous continuez à tourner entre `pytex` et `figures_giulietta.py` jusqu'à disparition des warning. Vous en avez pour des heures.

### Compilation finale

Maintenant que tout est prêt, demandez à `tikz` de créer les fichiers `md5` et `pdf` :
```bash
pytex lst_giulietta.py --no-external
pytex lst_giulietta.py
```
La première est une simple formalité. La seconde va prendre des heures.


### Astuces

Il y a quelques astuces qui permettent de gagner du temps.

* Lorsque vous faites `figures_giulietta.py`, à partir de la seconde fois, vous pouvez le couper pour ne pas recompiler les figures qui n'ont pas de Warning.
* Pour la dernière compilation, celle `pytex lst_giulietta.py` sans `--no-external`, il faut savoir que chaque figure prendra le temps de compilation de l'ensemble du document. Il vous en coûtera donc environ une minute par figure.

   Si par contre vous compilez `pytex lst_frido.py`, il vous en coûtera que 30 secondes par figures (pour celles qui sont dans la partie Frido). Il est donc très efficace de compiler séparément chaque partie.
