# Journal des changements du Frido

## Novembre 2022

- L'index est classé avec les é compté comme un e. Grâce à un script en lua.

## Décembre 2021

- Série de Laurent
- Mise en ordre autour des coefficients de Fourier, et de la différence entre Fejér et Fourier proprement dit.
- Corolaire à Banach Steinhaus avec des seminormes.

## Novembre 2021

- corps topologique
- un ensemble avec ses seminormes est un espace vectoriel topologique

## Septembre-Octobre 2021

Dualité.

- L^p est réflexif
- L^1 s'injecte dans L^infini, mais pas surjectivement

## Septembre 2021

- compilation via un docker par Gjacquenot

## Juillet-aout 2021

- Les entiers et les naturels : définition, opérations, relation d'ordre
- Application définie par récurrence sur N. Existence et unicité.
- Base trigonométrique sur L^2(a,b).

## Juillet 2021
- Théorème de l'application ouverte, théorème d'isomorphisme de Banach

## Juin 2021

- Encore à propos de limite pointée et épointée. Démonstration du théorème complet de composition de limites.
- Énormément de relecture et de précisions à propos de la construction des réels et des suites de Cauchy dans un corps totalement ordonné. En particulier tout corps ordonné contient une copie de Q, et cette copie respecte l'ordre.

## Mai 2021

- Théorème de prolongement de Riemann
- L^1 avec le produit de convolution est une algèbre de Banach.
- cas d'égalité dans Hölder et Minkowski

## Mars-Avril 2021

- Tétraèdre et bijections affines.
- Commencer une section «géométrie dans l'espace» pour y regrouper plans, droites, etc.
- Produit de Cauchy : mise en ordre et un peu de démonstration.
- Il y a deux fois la partition d'un entier en parts égales. J'avais commencé à en faire une troisième. Fusion, prendre le meilleur des trois.
- Mise en ordre; j'ai plus ou moins la progression suivantes :
    * La topologie sur R est celle de la valeur absolue
    * On démontre juste ce qu'il faut pour définir la racine carrée (théorème des valeurs intermédiaires)
    * On peut alors faire différentes normes, R^n, espaces vectoriels normés.

## Février 2021

Théorème de Hahn-Banach. 
- Extension de fonctionnelle linéaire.
- Le dual sépare les points dans un espace vectoriel normé.

## Janvier 2021

- Décision : on vire la géométrie différentielle, et en particulier :
    * orientation
    * intégration sur des variétés
    * espace tangent
    * démonstration de Brower via le théorème de Stokes
  Tout cela nous mène trop loin et sera déplacé progressivement vers [Giulietta](http://laurent.claessens-donadello.eu/pdf/giulietta.pdf)

## Décembre 2020

- Encore des fonctions plateau
- Lemme d'Urysohn en plusieurs dimensions
- Je décide d'écrire «multiindice», sur le modèle de «multinational» et dans l'esprit des règles[1]. Idem pour "seminorme".
- Changer énormément de \href en entrées dans la bibliographie
- espace vectoriel topologique : métrisabilité. Ça fait pas mal de topologie générale sur les espaces vectoriels topologiques. En particulier le fait que de tels espaces séparent les fermés des compacts.

[1] http://www.renouvo.org/regles.php

## Novembre 2020

- Dérivation de fonction composée (oui, c'est fou, mais ça n'y était pas)
- Dérivation partielle de fonction composée 
- Quelque version des accroissements finis avec des dérivées partielles

## Distributions (octobre 2020 - Décembre 2020)

- partition de l'unité
- principe de recollement (pour les distributions)
- permuter distribution et dérivée

## Septembre-octobre 2020

- L'identification matrice-application linéaire est continue.

## Formes quadratiques (mars 2020)

- signature d'une forme quadratique
- réduction de Gauss
- q-orthogonalité, existence de bases q-orthogonales
- théorème de Sylvester

## Trigonométrie (mars 2020)

- Preuve de pas mal de valeurs remarquables pour les fonctions trigonométriques.

## Connexe, mais pas par arcs (mars 2020)

- le graphe de (t,sin(1/t)) avec (0,0) est connexe mais pas connexe par arcs.
- connexité par arcs de la compactification en un point

## Clôture algébrique (février 2020)

- Existence et unicité d'une clôture algébrique

## Cardinalité (janvier-février 2020)

- Prouver que si A est infini, alors AxA est équipotent à A
- Quelques autres résultats de cardinalité comme A-B=A si B est strictement subpotent à A
- Une réunion dénombrables d'ensembles dénombrables est dénombrable.
- Théorème de Cantor, inexistence de l'ensemble des ensembles
- Théorème de Cantor-Bernstein et de la comparabilité cardinale : on a à peu près un ordre 
  sur l'ensemble des ensembles.

## Topologie produit, topologie engendrée (Décembre 2019)

Le but est de prouver que (x,y)->x+y est continue de RxR->R.
Plusieurs mises en ordre

- Définition de la topologie engendrée par un ensemble de parties
- Définition de la topologie produit
- Équivalence de la limite pour la topologie métrique produit ou la topologie produit
- Définition de la topologie sur R^n en tenant compte de tout ça.

## Différentiabilité (novembre 2019 - décembre 2019)

Le but est de prouver qu'une application est C^n si et seulement si ses dérivées partielles d'ordre sont C^(n-1).

- Espaces d'applications multilinéaires.
- Isomorphisme entre les espaces emboîtés et les applications multilinéaires

## Octobre 2019

- Déplacer plusieurs résultats sur les fonctions holomorphes qui sont en réalité des résultats sur les fonctions analytiques.
- Prouver le théorème du prolongement analytique.
- Intégrale de Dirichlet via une dérivation sous l'intégrale et beaucoup de séries alternées
- Énormément de fautes d'orthographe corrigées par vuod et Bruno Turgeon (qui sont peut-être la même personne...)

- Pas directement lié, mais j'ai fait un passage à python3 pour `phystricks`, qui est au passage renommé `yanntricks`.
  Ça utilise maintenant une version de Sage compilée avec python3 (pas encore totalement officielle pour l'instant). Les
  figures du Frido sont recompilées, et j'espère qu'il n'y aura aucune différences visuelles.
  https://github.com/LaurentClaessens/yanntricks

## Septembre 2019

- Discussion plus complète entre limite pointée et épointée
- Quotient d'un anneau par un idéal, placé avant la définition de R (qui est un quotient d'anneau par un idéal)
- Une bonne définition des anneaux de polynômes à partir du A-module libre A^I.

## Aout 2019

- Lemme de Urysohn, version basique dans R
- lim x->oo de int_0^x est égale à int_0^{oo}.

## Formule de Stirling (aout 2019)

- Taylor avec reste intégral.
- Encadrement de ln(2)
- intégrales de Wallis

## Fonction Cauchy-continue (juillet 2019)

Correction d'une faute : il n'est pas vrai qu'une fonction
continue sur Q s'étend en une fonction continue sur R.

- Donner un contre-exemple
- Adapter la preuve du lemme d'extension pour l'hypothèse de Cauchy-continue
- Prouver que q -> a^q est Cauchy-continue.

## Isométries affines (juin 2019 - aout 2019)

- Orientation dans un espace affine ou euclidien.
- un peu de mise au clair à propos de la différence entre des isométries de (R^n,d) et de (R^n, ||.||).
- sous-groupes finis des isométries affines du plan.
- Démonstration que les rotations centrées en (0,0) sont exactement le groupe SO(2).
- pavages du plan.

## Formes bilinéaires (mai 2019)

* Démonstration des transformations de Lorentz
* Mise en ordre et correction d'une faute

## Théorème de la projection normale (avril 2019 - mai 2019)

- Banach uniformément convexe
- Projection normale
- Inégalités de Clarkson
- Inégalités de Hölder

## exponentielle de matrices (mars 2019)

- e^A e^B = e^(A+B) dès que A et B commutent.

## Fonction puissance (mars 2019)

- Introduction de l'exponentielle par l'équation fonctionnelle
- Preuve que a^x est dérivable via l'utilisation de primitive
- Déplacer Stone-Weierstrass beaucoup plus haut pour avoir
  la notion de primitive avant de discuter la fonction puissance
- Complètement séparer le concept de primitive de celui d'intégrale

## Convexité de \| x \|^p (Février-mars 2019)

Stricte convexité de la fonction x->| x |^p lorsque p>1

## Banach-Steinhaus (Févirer 2019)

- Différence entre convergence forte et convergence en norme dans le cas de suite d'opérateurs.
- Preuve plus simple de Banach-Steinhaus

## Réflexivité de L^p (Févirer 2019)

Les espaces L^p sont réflexifs, preuve

## John-Loewner (Janvier 2019)

- préciser qu'on ne parle que d'ellipsoïdes centrés en l'origine
- parler de ce qu'il se passe si on se permet de bouger le centre
- corriger quelques fautes pointées par Benoît Tran.

## hyperplan (Décembre 2018)

- lien entre hyperplan et forme linéaire
- sous-espace vectoriel comme intersection d'hyperplans

## Ordre dans les conventions autour de Fourier (Octobre 2018 - ...)

- Reprise en détail du cas de S^1 : 
    * structure d'espace mesuré
    * convolution
    * approximation de l'unité
    * densité des polynômes trigonométriques
- Définition du système trigonométrique sur [-T,T].
- Fixer les conventions en ce qui concerne le produit scalaire sur L^2.
- Régler des problèmes de coefficients un peu partout.

## Limite et continuité (Octobre 2018)

Il y avait du flottement entre limite et continuité dans le cas d'une
fonction définie sur un point isolé.
- Fixer cela
- Changer la définition de continuité pour utiliser les voisinages plutôt que la limite

## Élément premier (Octobre 2018)

Ayant reçu quelques réponses d'algèbres de Gregory Berhuy, j'ai ajouté les notions d'élément premier et les démonstrations de quelques faits comme l'équivalence entre
- (p) est un idéal premier
- p est un élément premier
- p est un élément irréductible
- (p) est un idéal maximal propre.

Fixer un certain nombre de flottements sur ce qui pouvait être réduit à {0} ou non. Un corps le peu. Cela a des conséquences sur des idéaux qui doivent être propres ou non dans d'autres énoncés.

Je crois qu'il y a une faute dans Wikipédia
https://fr.wikipedia.org/wiki/Discussion:Idéal_premier#Idéaux_premiers_dans_un_anneau_principal

## Théorème de d'Alembert (Septembre 2018)

Démontrer le théorème de d'Alembert, suite à une remarque de kantien sur linuxfr [1].
- Le gros morceau est de prouver que z^n=a+bi a une solution pour tout entier n>1 sans passer par la forme trigonométrique
  des nombres complexes.

[1] https://linuxfr.org/nodes/115201/comments/1748682

## Limite et dérivée (Septembre 2018)

Ajout d'une démonstration du théorème d'inversion de limite et dérivée sans passer par les intégrales par Pierre Lairez.

## Matrices et déterminant : manipulations de lignes et de colonnes (août 2018)

Ceci parle principalement de matrices en tant que tableaux de nombres (dans un corps) sans parler d'applications linéaires.
- La façon dont le déterminant change lorqu'on manipule les lignes et colonnes
- Les matrices qui font ces opérations
- Réduction de Gauss
- preuve de det(AB)=det(A)det(B)

Ceci est nécessaire pour identifier le produit mixte dans l'intégrale sur des variétés de dimension 3.

## Intégration sur les variétés (juillet 2018 - août 2018)

- Définition d'une variété via les cartes. Nous nous limitons au cas de variétés dans R^n dans le but de 
  définir l'intégrale sans passer par l'arbitraire d'une forme volume.
- Définition de l'intégrale sur une variété.
- Cas de dimension 1, 2 et 3. Entrée en jeu du produit vectoriel et du produit mixte.

## Produit tensoriel d'espaces vectoriels (juin 2018)

Parce qu'on en aura besoin pour parler de différentielle d'ordre supérieur de produit.
- produit tensoriel d'espaces topologiques
- Dérivation d'un produit tensoriel de fonctions
- application au fait que les coordonnées polaires sont de classe  C^{\infty}

## Mise en ordre de la topologie (juin 2018)

- Meilleur division en trois chapitres :
    * topologie générale
    * topologie réelle
    * topologie générale (suite)
- Démonstration de quelques résultats laissés en suspend.

## Mise en ordre coordonnées polaires/cylindrique/sphériques (juin 2018)

- Entre autres, la démonstration du théorème qui donne les coordonnées polaires comme difféomorphisme de classe C^{\infty}.

## Polynômes et série de Taylor (mai 2018)

- Une démonstration du théorème de de Taylor avec son reste classique (il existe c dans ]a,b[ tel que \ldots).
- Définition de fonction analytique
- exemple de ln(1+x)

## Suppression de exocorr (mai 2018)

- Le paquet LaTeX personnel `exocorr` n'est plus nécessaire pour compiler le Frido.
- Il est encore nécessaire pour compiler `everything`
- Les exercices ont été converti en exemples

## Coefficients de Fourier (mars 2018)

Les coefficients de Fourier dans L^2(-T/2,T/2) étaient définis avec un coefficients 1/T. Cela étant incohérent avec la définition du
produit scalaire sur L^2, on change la définition pour supprimer les coefficients.

Ça fait un sacré paquet de changements un peu partout.

## Fonction puissance (février-avril 2018)

Définition de la fonction puissance x->a^x.

- définition de a^q pour q rationnel
- prolongation par continuité à R
- déplacement de nombreux exemples utilisant les puissances vers plus bas dans le texte.

## Limite de fonction (janvier 2018)

Des incohérences ont été détectées, essentiellement dues à mon inattention et accessoirement dues au fait que Wikipédia francophone utilise une définition pas du tout standard sans prévenir[1].

Les définitions ont été clarifiées et unifiées. La définition de limite choisie ici est celle que les Français nomme "épointée", et qui est la seule correcte dans l'histoire de l'univers depuis (au moins) l'apparition de eukaryotes, partout sauf en France.

[1] https://fr.wikipedia.org/wiki/Espace_topologique  
    Si vous ne voyez pas le problème avec la définition de la limite, lisez la page de discussion.

## Théorème de Weiner (décembre 2017 - ...)

Le théorème qui dit que L^p est un Hilbert si et seulement si p=2.
Pas encore terminé.

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
- Donner les formules de changement de base (corriger quelques erreurs qu'il y avait là)

## Théorie des ensembles (novembre 2017)

Suite à quelques remarques de Guillaume Deschamps, ajout de quelques précisions un peu partout dans la partie «théorie des ensembles».

En particulier, prévenir le lecteur que la constructions des nombres n'est pas le premier chapitre à lire. Être plus clair sur ce que signifie «supposer avoir une théorie des ensembles».

## Anneau intègre (octobre 2017)

Suite à une remarque de cdr[1], correction d'une faute et quelques améliorations :

- Oui, Z est intègre et euclidien, contrairement à ce qui était écrit.
- Non, Z[X] n'est pas intègre.
- Préciser qui de Z, Z[X] et Z/nZ est principal.
- Quelques exemples et contre-exemples d'anneaux principaux, y compris dans les fonctions holomorphes.


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
* Quelques mots à propos des formes différentielles _avant_ la définition de df.

## Réorganisation des questions (4 Juillet 2017)

* Triage des questions et des demandes d'aide en catégories «facile», «moyen», «difficile».
* Suppression des questions type «il faut relire telle preuve» de la liste des questions. Ces questions sont converties en citation de 'MonCerveau' et en commentaires à l'endroit des preuves.
