# Erratum du Frido

Ce fichier contient les fautes découvertes dans les versions imprimées du Frido. Elles sont en principe corrigées au fur et à mesure dans la [version courante](http://laurent.claessens-donadello.eu/pdf/lefrido.pdf).

## Frido 2018

Les fautes sont présentées par ordre anti-chronoligique de découvertes.

- Volume 1, corollaire 5.36. Il n'est pas vrai en général que, pour une application linéaire, il y a équivalence entre "injectif", "surjectif" et "bijectif". Cela n'est vrai que si les espaces de départ et d'arrivée ont la même dimension.
  La preuve se trompe en mélangeant les dim(E) de l'espace de départ avec les rang(f) qui sont dans l'espace d'arrivée.

- Volume 1, proposition 11.68. Il n'est pas vrai que le groupe O(n) est le groupe des isométries de R^n : parmi les isométries de R^n, il y a aussi
  les translations, comme prouvé ailleurs.
  Ce qui est vrai et démontré dans 11.68 est que, parmi les applications *linéaires*, les isométries sont les éléments de O(n).

- Déterminant de la matrice transposée. Lemme 5.63 volume 1. L'utilisation de la proposition 2.49 n'est pas correcte parce que 2.49 permet de faire un «décalage constant» dans la somme alors qu'ici nous introduisons sigma^2 qui n'est pas constant dans la somme.
    La solution est d'utiliser une proposition similaire pour le produit et d'utiliser, pour chaque élément de la somme, la commutativité du produit; cela revient à ré-indexer le produit par sigma. Ensuite, il faut ré-indexer la somme sur sigma^{-1} au lieu de sigma.
    Voir https://ljk.imag.fr/membres/Bernard.Ycart/mel/de/de.pdf

- Produit sur L^2. Volume 3, lemme 28.58. Il ne faut pas la racine carré au-dessus de l'intégrale. C'est la norme de 'f' qui demande de prendre une racine carré.

- Coefficients de Fourier. Dans les équations (31.34) du volume 4, c'est la grande foire aux coefficients manquants. Le fait est que vous aurez remarqué que la section 28.5.4 (volume 3) n'est pas écrite. Les conventions pour les choses attenantes à Fourier sur [-T,T] ne sont pas fixées.

- Il me semble qu'il y ait quelque incohérences entre limite et continuité. Prenons une fonction définie sur un singleton. Soit a ce point et A={a}, l'ensemble.
  Pour sa propre topologie, A est un ouvert. La fonction est continue sur A parce que l'image inverse de tout ouvert est ouvert.
  Mais elle n'est pas continue en chacun de ses points parce que nous n'avons pas définit la notion de limite sur un point qui n'est pas un point d'accumulation. Bien entendu, A ne possède aucun point d'accumulation.

## Frido 2017

Les fautes sont présentées par ordre anti-chronoligique de découvertes.

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

- Volume 1. Proposition 4.70. Je suis presque certain qu'il faut ajouter l'hypothèse que I est un idéal propre, c'est à dire que l'inclusion de I dans A est stricte.

- Volume 1. L'exemple 4.73 prétend que les anneaux Z/nZ sont principaux. Cela n'est pas vrai en général parce que lorsque `n` n'est pas premier, Z/nZ n'est pas intègre. Il est tout de même vrai que ses idéaux sont principaux.

- Volume 1. L'exemple 4.85 prétend que Z n'est ni principal ni euclidien. En réalité, Z est euclidien (et donc principal) parce que la valeur absolue donne un stathme. [merci cdr](https://github.com/LaurentClaessens/mazhe/issues/58).

