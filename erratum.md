# Erratum du Frido

Ce fichier contient les fautes découvertes dans les versions imprimées du Frido. Elles sont en principe corrigées au fur et à mesure dans la [version courante](http://laurent.claessens-donadello.eu/pdf/lefrido.pdf).

## Frido 2020 (8 fautes)

- Volume 1. Lemme 9.85. Dans l'équation (9.161), le premier terme doit être (lambda1-lambda1)v_1, et donc être nul. Ensuite, il faut continuer à appliquer les (A-lambda_i) avec i < p pour finir avec v_p=0. Et continuer avec p-1. Merci à Patrice Goyer pour l'avoir trouvée.
- Volume 3. Proposition 26.37. Inégalité de Minkwowski. La partie (2) sur le cas d'égalité est fausse.
- Volume 2. Théorème 11.32. La convergence de f_k vers f est seulement uniforme sur tout compacts.
- Volume 1. Définition 1.97. Les mots «corps» et «anneaux» sont inversés. Un corps est un anneau dans lequel les non nuls sont inversibles.
- Volume 2. Théorème 11.311. La passage de (11.813) à (11.814) limite la validité de l'inéquation à des valeurs de i assez grandes. Or ce "assez grand" dépend à priori des valeurs de n,y et x (qui sont cachées dans alpha_n). Il n'est pas clair que nous puissions prendre la limite n->infini si facilement parce que rien ne garantit que le domaine de validité (par rapport à i) de l'inéquation reste non vide. Cela est particulièrement délicat au moment de prendre le supremum sur y un peu plus bas, parce qu'encore le domaine de validité en i dépend de y. La solution est de remarquer que l'on travaille sur un compact, de telle sorte que | y-x | < M. Nous faisons alors une étape supplémentaire de majoration | y-x | < M à l'intérieur de alpha_n. 
- Volume 1. Lemme 7.286. Il s'agit d'une inclusion et non d'une égalité.
- Volume 1. Théorème 7.288. Il manque le traitement de pas mal de subtilités topologiques. En particulier la preuve de d(x,y)=0 => x=y n'est pas écrite, et elles est moins simple que vous pouvez le croire. La définition dans l'équation (7.335) manque d'une sérieuse preuve de l'injectivité de la fonction qui à un r donné fait correspondre le n et la suite des coefficients.
- Volume 3. Définition 19.20 d'une partition de l'unité. Cette définition me semble très bizarre : si l'ouvert est composé de deux ouverts non connexes, je ne vois pas comment c'est possible. Décuplez votre vigilance, et dites-moi si vous connaissez un énoncé exact.

## Frido 2019 (7 fautes)

- Volume 1. Définition 1.45 d'anneau commutatif. C'est la multiplication qui doit être commutative. La somme est toujours commutative; c'est dans la définition d'un anneau.
- Volume 2. Proposition 15.193. La démonstration ne traite pas le cas d'une union dénombrable. Il faut utiliser le théorème de la convergence monotone pour passer à la limite. C'est à dire suivre les lignes de la proposition 15.187.
- Volume 1. Proposition 3.24. Les epsilon et epsilon' n'ont rien à faire là et rendent l'énoncé faux. Si e=e'=8, ça multiplie par 8 le PGCD.
- Volume 2. Proposition 13.276. Une fonction est de classe C^k si et seulement si ses dérivées partielles sont de classe C^(k-1) et non C^k.
- Volume 1. Théorème 12.80 sur les séries alternées. La suite (a_n) doit être à termes positifs et non seulement "réels". Sinon il n'y a au final aucune garantie que la série soit alternée.
- Volume 1. Lemme 2.7. Tout sous-groupe de G contenant A contient gr(A) et non "est contenu dans".
- Volume 1. Sous la définition 2.21. La justification du fait que D(G) est non vide est fausse : le fait que G fasse partie des ensembles de l'intersection ne signifie pas que l'intersection est non vide. Par contre l'élément neutre est nécessairement présent. (découverte par Colin Pitrat)

## Frido 2018 (16 fautes)


- Volume 2. Prolongement de fonctions, lemme 14.61. Ce lemme est faux.
            Un contre-exemple est donné par la fonction caractéristique des rationnels plus grands que sqrt(2). C'est une fonction continue sur Q qui n'est pas prolongeable en une fonction continue sur R.
            Merci à Provatiscus pour avoir débusqué ce gros lapin.
        https://github.com/LaurentClaessens/mazhe/issues/124
        https://fr.wikipedia.org/wiki/Fonction_Cauchy-continue
- Volume 3. Groupe diédral. La proposition 20.113 n'est pas tout à fait exacte, parce que certains éléments du groupe diédral s'écrivent sans conjugaison complexe.
- Volume 3. Groupe diédral. Juste au-dessus de la proposition 20.112, il est dit que la conjugaison complexe n'est pas dans le groupe diédral pour n=3. C'est faux : la conjugaison complexe est dans tous les groupes diédraux (n>=3). C'est le point A_3 qui est faux te qui devrait être (-1/2, -sqrt(3)/2).
- Volume 2. Lemme 13.47. La démonstration du fait qu'une application affine préservant les points d'une base affine est l'identité ne fonctionne pas bien. D'abord ça n'a aucun sens de multiplier un point d'un espace affine par un nombre; ensuite la décomposition en composée de translation et d'application linéaire n'est pas vraie. Toute cette preuve fonctionne seulement dans le cas très particulier de R^n.
- Volume 3. Lemme 20.5. Une isométrie est bijective. La démonstration de ce lemme s'appuie sur le théorème 20.4 pour déduire que l'application est bijective, alors que la bijectivité est une hypothèse de 20.4, et non une conclusion.
- Volume 2. Fonctions convexes. La définition 19.85 est trop évasive concernant les fonctions strictement convexes. Pour une fonction strictement convexe, l'inégalité est stricte lorsque lambda est dans ]0,1[ et x1 != x2.
- Volume 1. Somme infinie. Le corolaire 11.197 me semble faux; il manque sans doute l'hypothèse de sommabilité de f(a_i). Voir la proposition 11.199 qui dit la même chose avec plus d'hypothèses.
- Volume 3. Principe des zéros isolés. La valeur des coefficients d_k est erronée. Il faut d_k = c__{m+k}/c_m.
- Volume 3. Dans le gros théorème 28.73 à propos de dualité « théorème de représentation de Riesz », il y a un cas "p=1". La preuve donnée dans cette partie ne traite que le cas où la mesure est finie et non sigma-finie comme annoncée. Il y a donc un trou dans la preuve.
- Volume 2, ellipsoïde de John-Loewner 19.113. L'énoncé manque de préciser que l'ellipsoïde est centrée en l'origine. Il faut lire :
  «Il existe un unique ellipsoïde centré en l'origine etc.». Si nous cherchons des ellipsoïdes en acceptant de ne pas centré en l'origine, il y a moyen à priori d'en trouver de plus petites que celle donnée par le théorème tel que prouvé (pour l'unicité par contre c'est moins clair).
- Volume 1, corolaire 5.36. Il n'est pas vrai en général que, pour une application linéaire, il y a équivalence entre "injectif", "surjectif" et "bijectif". Cela n'est vrai que si les espaces de départ et d'arrivée ont la même dimension.
  La preuve se trompe en mélangeant les dim(E) de l'espace de départ avec les rang(f) qui sont dans l'espace d'arrivée.
- Volume 1, proposition 11.68. Il n'est pas vrai que le groupe O(n) est le groupe des isométries de R^n : parmi les isométries de R^n, il y a aussi
  les translations, comme prouvé ailleurs.
  Ce qui est vrai et démontré dans 11.68 est que, parmi les applications *linéaires*, les isométries sont les éléments de O(n).
- Volume 1. Déterminant de la matrice transposée, lemme 5.63. L'utilisation de la proposition 2.49 n'est pas correcte parce que 2.49 permet de faire un «décalage constant» dans la somme alors qu'ici nous introduisons sigma^2 qui n'est pas constant dans la somme.
    La solution est d'utiliser une proposition similaire pour le produit et d'utiliser, pour chaque élément de la somme, la commutativité du produit; cela revient à ré-indexer le produit par sigma. Ensuite, il faut ré-indexer la somme sur sigma^{-1} au lieu de sigma.
    Voir https://ljk.imag.fr/membres/Bernard.Ycart/mel/de/de.pdf
- Produit sur L^2. Volume 3, lemme 28.58. Il ne faut pas la racine carrée au-dessus de l'intégrale. C'est la norme de 'f' qui demande de prendre une racine carrée.
- Coefficients de Fourier. Dans les équations (31.34) du volume 4, c'est la grande foire aux coefficients manquants. Le fait est que vous aurez remarqué que la section 28.5.4 (volume 3) n'est pas écrite. Les conventions pour les choses attenantes à Fourier sur [-T,T] ne sont pas fixées.
- Il me semble qu'il y ait quelques incohérences entre limite et continuité. Prenons une fonction définie sur un singleton. Soit a ce point et A={a}, l'ensemble.
  Pour sa propre topologie, A est un ouvert. La fonction est continue sur A parce que l'image inverse de tout ouvert est ouvert.
  Mais elle n'est pas continue en chacun de ses points parce que nous n'avons pas définit la notion de limite sur un point qui n'est pas un point d'accumulation. Bien entendu, A ne possède aucun point d'accumulation.

## Frido 2017 (9 fautes)

- Volume 1. La définition de forme bilinéaire n'est pas correcte. Elle mélange bilinéarité et symétrie. Être bilinéaire signifie être linéaire en chacune des deux composantes séparément.
- Volume 1. Toute suite dans un compact de R admet une sous-suite convergente (théorème 6.93). La démonstration est fausse, en particulier le cas où nous n'avons qu'un nombre fini de points maximaux. Exemple : x0=5, et ensuite alterner une suite partant de zéro et croissante vers 1 avec une suite partant de zéro et décroissante vers -1. Dans ce cas, x0 est l'unique élément maximal de cette suite.

    Merci à bibi6 pour avoir trouvé cette faute.
- Volume 2. La définition de mesure positive sur un espace mesurable est incorrecte (définition 13.23). La première condition doit être remplacée par 
        mu(vide)=0.
    Sinon, il est possible d'avoir une mesure pour laquelle tous les éléments de la tribu ont une mesure infinie (y compris le vide). Dans
    ce cas, la remarque qui suit la définition de la mesure ne s'applique pas (remarque 13.24), et il n'est en réalité pas garanti d'avoir mu(vide)=0.
- Volumes 1 et 2. Définition de la limite. Induit en erreur à moitié par mon manque d'attention et à moitié par Wikipédia, la définition de la limite d'une fonction était incorrecte, et surtout incohérente avec les théorèmes démontrés plus bas.

    La définition correcte de la limite se fait *en excluant* le point vers lesquel on fait tendre x.
- Volume 1. Définition 4.8. La définition du pgcd dans un anneau n'est pas correcte. 'd' est un pgcd de 'a' et 'b' si tout diviseur commun de 'a' et 'b' divise 'd' ET SI 'd' divise 'a' et 'b'.
- Volume 3. Définition 24.63. La définition d'espace réflexif n'est pas correcte; il faut parler de bidual. Du coup l'énoncé du théorème 24.64 (qui est probablement bien vrai quand même) est à prendre avec des précautions.
- Volume 1. Proposition 4.70. Je suis presque certain qu'il faut ajouter l'hypothèse que I est un idéal propre, c'est-à-dire que l'inclusion de I dans A est stricte.
- Volume 1. L'exemple 4.73 prétend que les anneaux Z/nZ sont principaux. Cela n'est pas vrai en général parce que lorsque `n` n'est pas premier, Z/nZ n'est pas intègre. Il est tout de même vrai que ses idéaux sont principaux.
- Volume 1. L'exemple 4.85 prétend que Z n'est ni principal ni euclidien. En réalité, Z est euclidien (et donc principal) parce que la valeur absolue donne un stathme. [merci cdr](https://github.com/LaurentClaessens/mazhe/issues/58).

