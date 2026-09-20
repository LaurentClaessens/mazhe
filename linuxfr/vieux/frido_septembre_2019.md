Ce texte est maintenant en rédaction. Il ne faut plus le modifier ici.
https://linuxfr.org/redaction/news/nouvelle-depeche-39424


# Le Frido 2019, mathématique pour l'agrégation

Ce fichier contient mes notes pour créer l'article d'annonce du Frido 2019 sur linuxfr.

[Le Frido](https://laurent.claessens-donadello.eu/frido.html) est un livre de mathématique en 4 volumes reprenant à peu près tout de la construction des naturels (non inclue) jusqu'à la fin de l'agrégation, tant en algèbre qu'en analyse.

## Originalité

Il se distingue des autres livres de mathématique par :

- Il couvre tous les champs de l'agrégation, donc il est long (2200 pages)
- Il va dans l'ordre logique mathématique, c'est-à-dire que les démonstrations n'utilisent que des théorèmes déjà démontrés. Cela n'est pas (et de loin) l'ordre pédagogique. Ce n'est donc pas dans le Frido qu'il faut commencer à apprendre la mathématique.
- [Les sources](https://github.com/LaurentClaessens/mazhe) LaTeX sont publiées sous licence FDL et n'attendent que vos commentaires et contributions.

## Quoi de neuf depuis l'année passée ?

Le [journal des changements](https://github.com/LaurentClaessens/mazhe/blob/master/changelogFrido.md) détaille les changements.

Voici les principaux :

- Tout sur le cercle S^1 : topologie, boréliens pour sa propre topologie,
  boréliens induits de R^2, produit de convolution, 
  preuve que les coordonnées polaires fournissent un difféomorphisme 
  de classe  $C^{\infty}$.
- Inégalités de Clarkson
- Démonstration du théorème de d'Alembert
- Démonstration de la formule de Stirling
- Démonstration du théorème de Weinersmith
- élément premier, idéal premier et idéal maximum propre. Des précisions
  et des équivalences.

## Quoi de moins faux depuis l'année passée ?

Il n'y a pas que des choses ajoutées, il y a aussi des choses corrigées; de nombreuses fautes débusquées par beaucoup de lecteurs que je remercie. L'[erratum complet](https://github.com/LaurentClaessens/mazhe/blob/master/erratum.md) donne des détails.

Ma préférée est celle-ci : 

> Toute fonction continue $Q\mapsto R$ 
> (pour la topologie induite de R vers Q) peut 
> être prolongée en une fonction continue sur R.

Avouez que c'est le genre d'énoncé qui a l'apparence de la véracité.

# Giulietta

Le Frido n'est que le début. La suite est [Giulietta](https://laurent.claessens-donadello.eu/pdf/giulietta.pdf) qui contient des choses de plus haut niveau.

Mon objectif là-dedans est d'aller vers la théorie quantique des champs de façon compréhensible par un mathématicien, et en suivant la règle «définition, théorème, démonstration».

Bon, d'accord je sais que ça n'existe pas. Il n'existe pas de formulation mathématiquement cohérente de la théorie quantique des champs.

J'ai déjà :

- Théorie des connexions sur les fibrés vectoriels, principaux et associés
- Transformations de jauge du point de vue de la géométrie différentielle.
- Représentations irréductibles de U(1) et SU(2).
- Équations de Maxwell en termes de connexions

Mon plan pour la suite :

- Représentations irréductibles du groupe de Poincaré, lien avec celles 
  de SL(2,C).
- Savoir ce qu'est exactement un état sur une C*-algèbre.
- Comprendre ce que signifie précisément l'expression «smearing vector».

Le tout :

- En utilisant les bons outils de géométrie différentielle
- En écrivant  $ x\cdot y $  ce que les phycien notent  $ x^iy_i $
- En disant «le vecteur $ v$ »  et non «le vecteur $v_{\mu}$ ».
