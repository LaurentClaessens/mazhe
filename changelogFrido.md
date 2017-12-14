# Changelog du Frido

## corps de rupture, corps de décomposition (novembre, décembre 2017)

Suite à des remarques de cdrcprds, de gros travaux ont été fait du côté des corps de rupture et de décomposition.

- définition, existence de corps de rupture
- définition, existence et unicité du corps de décomposition
- Clarifier la définition d'un polynôme comme suite presque nulle. Entre autres, donner un sens à la formule P(X)=P
- Clarifier ce qu'est A[X], A(X), A(a), A[a]
- Éléments transcendants et algébriques.

https://github.com/LaurentClaessens/mazhe/issues/60
https://github.com/LaurentClaessens/mazhe/issues/62

## Corps des fractions et (novembre 2017)

Nous définissons Q comme corps des fractions sur Z. Cela nous demande de déplacer encore beaucoup de choses sur les anneaux et corps entre la construction de Z et celle de Q. En réalité nous allons mettre tout cela avec groupes/anneaux/corps entre N et Z.

## Matrices et changement de base (novembre 2017)

- Mettre bien à plat les définitions de matrices associées à une application linéaire et à une forme bilinéaire
- Donner les formules de changement de base (corriger quelque erreurs qu'il y avait là)

## Théorie des ensembles (novembre 2017)

Suite à quelque remarques de Guillaume Deschamps, ajout de quelque précisions un peu partout dans la partie «théorie des ensembles».

En particulier, prévenir le lecteur que la constructions des nombres n'est pas le premier chapitre à lire. Être plus clair sur ce que signifie «supposer avoir une théorie des ensembles».

## Anneau intègre (octobre 2017)

Suite à une remarque de cdr[1], correction d'une faute et quelque améliorations :

- Oui, Z est intègre et euclidien, contrairement à ce qui était écrit.
- Non, Z[X] n'est pas intègre.
- Préciser qui de Z, Z[X] et Z/nZ est principal.
- Quelque exemples et contre-exemples d'anneaux principaux, y compris dans les fonctions holomorphes.


[1] https://github.com/LaurentClaessens/mazhe/issues/58

## Complétude des réels (Octobre 2017)

Séparer plus clairement le théorème qui dit que R est complet au sens des corps complets (avec les notions de suites de Cauchy dans un corps) de ce qui qui dit que R est complet en tant qu'espace métrique.

## Produit scalaire, espaces L^p, complexes et réels (24 septembre 2017)

Il y avait eu du flottement au niveau des définitions, mais il faut prendre des décisions. 

* Les espaces L^p sont des (classes de) fonctions à valeurs dans C et non R
* Un produit scalaire sur un espace sur C n'existe pas
* Un espace de Hilbert est muni soit d'une produit scalaire si il est vectoriel sur R soit 
d'un produit Hermitien si il est vectoriel sur C.

## Sous-groupes finis de SO(3) (17 septembre 2017)

Démonstration de la liste des sous-groupes finis de SO(3).

## Dans le groupe symétrique (4 août 2017)

Nous avons ajouté pas mal de choses concernant le groupe symétrique.

- les sous-groupes normaux de S_n
- le seul sous-groupe d'indice n dans S_n

## Isométries du tétraèdre et une représentation de S_4 (23 juillet 2017)

Le groupe Iso(T) est isomorphe à S_4 (T est une tétraèdre régulier). Quand T est centré en 0, cela donne une représentation
de S_4 de dimension 3.

Nous en calculons les caractères.

## Correction (19 juillet 2017)

Si A est un anneau intègre, il n'est pas vrai que A[X] est euclidien et principal.

## Différences finies : différentes discrétisation du laplacien (13 juillet 2027)

* Il y a deux discrétisations du laplacien : une suivant x et y; l'autre en suivant les coordonnées (1,1) et (1,-1).
* On montre un peu comment une bonne combinaison des deux mène à une meilleure convergence (non fini)

## Réorganisation du chapitre d'analyse réelle (12 juillet 2017)

* Mettre ensemble et au début toutes les choses concernant les fonctions sur R, et après celles sur R^n
* Regrouper les choses sur les dérivées directionnelles et les mettre avant la différentielle
* Ré-exprimer la définition de la différentielle en la mettant comme une proposition-définition pour l'unicité.
* Quelque mots à propos des formes différentielles _avant_ la définition de df.

## Réorganisation des questions (4 Juillet 2017)

* Triage des questions et des demandes d'aide en catégories «facile», «moyen», «difficile».
* Suppression des questions type «il faut relire telle preuve» de la liste des questions. Ces questions sont converties en citation de 'MonCerveau' et en commentaires à l'endroit des preuves.
