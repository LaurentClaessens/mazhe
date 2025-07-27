# Erratum du Frido

Ce fichier contient les fautes découvertes dans les versions imprimées du Frido. Elles sont en principe corrigées au fur et à mesure dans la [version courante](https://laurent.claessens-donadello.eu/pdf/lefrido.pdf).

## Frido 2024

- Volume 2. Proposition 12.125 (PROPooHXJAooGaDtme). Dans la partie 'juste un bloc', la justification du fait que '| lambda | ≤ 1' est fausse et s'appuie sur le lemme LEMooGCJEooOAynZW qui est également faux. J'ai également des doutes sur la véracité de LEMooKPWKooOacXju.
- Volume 2. Lemme 15.18 (LemmbWnFI). Critère d'Abel. Il faut d'abord choisir \( r\), et ensuite dire «la suite a_nz^n est bornée». 
- volume 1. Exemple 1.294 (ExVYZPzub). Il manque la classe des éléments du type (a,b)(c)(d).
- volume 1. Lemme 8.94 (LEMooEYPSooLCoPlY). L'ensemble des endomorphismes n'est pas un corps parce qu'il y a plein de non-inversibles. 
- volume 1. Proposition 7.242 (PROPooGXGQooLRTwvH). Conséquence de l'erreur précédente, la partie «somme» n'a aucun sens. Il faut juste utiliser la topologie produit et c'est tout.
- volume 1. Proposition 7.341 (PROPooGXGQooLRTwvH). Je n'ai pas de contre-exemple sous la main, mais à mon avis c'est faux. 
- volume 2. Lemme 15.158 (LEMooRVSIooKcpWoK). La fonction proposée dans le preuve ne marche pas parce que la fonction \varphi tend vers 1 lorsque x->infini. Sa primitive ne peut pas être constante. (trouvée par Quentin Guyot)
- Volume 1. Définition 7.68 (DefIRKNooJJlmiD). La définition de la connexité n'est pas bonne. La définition donnée est celle d'un ESPACE connexe. La définition d'une PARTIE connexe est qu'il doit être connexe pour la topologie induite. Du coup 7.69 (LEMooKXHQooAyVQsT) n'a aucun sens.
- Volume 1. Définition 1.475. La valeur absolue doit prendre ses valeurs dans K et non dans R parce qu'à ce moment R n'est pas défini.
- Volume 2. Proposition-Definition 10.51. Le point (2) est faux : la norme opérateur n'est une norme que sur la partie des applications linéaires bornées.

## Frido 2023 (5 fautes)

- Volume 1. Proposition-Définition 1.380. La définition d'ordre sur Q est complètement fausse. Cela se voit directement en considérant le cas où `b<0` alors que tous les autres sont positifs.
- Volume 3. Proposition 20.154. La factorielle devant le reste devrait être m! et non (m-1)!. Ça change quelques coefficients dans le lemme de Morse 20.201. De toutes façons pour la version 2024, la proposition 20.154 va être changée en faveur de THOooFKZZooAgecfp.
- Volume 3. Proposition 18.63. Il est faux parce que la réciproque n'est pas continue en 1. De plus la notion de différentielle n'est pas définie quand une application n'est pas définie sur un ouvert d'un espace vectoriel. Pour S^1 c'est donc compliqué. Par Quentin Guyot.
- Volume 1. Lemme 1.115. Dans le point (ii si omega est dans B), la définition de varphi demande implicitement que sigma(omega) != omega. Il faut justifier que c'est le cas. Trouvée et corrigée par Patrice Goyer.
- Volume 4. Définition 30.14. La topologie choisie sur les fonctions C^infini à support dans un compact n'est pas la bonne. Par danarmk.

## Frido 2022 (34 fautes)

- Volume 1. Proposition 9.228. Même erreur. Les manipulations de colonnes font intervenir des multiplications à droite. La proposition 9.229 doit donc être également adaptée.
- Volume 1. Théorème 3.28 (de Cauchy). Le groupe doit être cyclique, sinon le théorème est faux. En effet si G est un groupe non cyclique d'ordre n, il ne contient aucun élément d'ordre n.
- Volume 1. Proposition 3.19. Complètement faux. Par exemple q=9 divise 3^4, mais 9 ne divise pas 3. Là où la proposition 3.19 est utilisée, il faut utiliser le lemme 3.20 qui dit que q divise a si et seulement si il divise a^n.
- Volume 4. Les équations (30.29) et (30.30) ne sont pas correctes. En réalité f_i(phi_i)>alpha et f_i=0 sur D(L_i). Pour cela il faut un petit corolaire du théorème de Hahn-Banach.
- Volume 3. Équation (27.664). Rien ne garantit que Z est non vide. Il est possible que ||h||=1 alors que `| h(x) |<1` pour tout x. En fait le but de cette partie de la preuve n'est pas de trouver une extension qui vérifie `|| h ||<1`, mais seulement de trouver une extension qui vérifie `| h |<1`.
- Volume 3. Corolaire 27.142. L'équation (27.576) est dans le mauvais sens, et ça ruine la démonstration. Je ne suis même pas sûr que le résultat soit vrai. Quentin Guyot.
- Volume 3. Proposition 27.143. L'équation (27.579) est dans le mauvais sens, et ça ruine la démonstration. Le résultat est cependant correct. Quentin Guyot.
- Volume 3. Lemme 27.83. La seconde partie n'est pas correcte. Quentin Guyot.
- Volume 3. Les équations (27.303) sont un peu confuses et il manque une inégalité. Quentin Guyot.
- Volume 2. Proposition 27.38. La partie «égalité» est fausse. La condition f+g=0 n'est pas suffisante pour avoir l'égalité de Minkowsky. Quentin Guyot
- Volume 3. Proposition 27.29. La partie «Injective» prouve en réalité que psi est bien définie. Il n'y a donc pas de preuve de l'injectivité. Quentin Guyot.
- Volume 3. Proposition 22.11. Il y a une confusion de signe autour de l'équation (22.27). Le cercle est centré en -omega/s et non en omega/s. Tel que les choses sont écrites, il faut des + et non des - dans les parenthèses.
- Volume 3. Lemme 18.81(3). Il s'agit du produit de 'n' réflexions et non 'n+1' (l'énoncé n'est donc formellement pas faux). Cela est parce que si f est une isométrie, f-id peut n'avoir pas de points fixes, et donc le rang(f-id) vaut au maximum 'n'.
- Volume 3. Lemme 17.82. Il faut considérer un intervalle fermé I=[a,b], sinon il n'y a pas de garanties que f soit définie en a et b. Heureusement tout point d'un ouvert de R possède un voisinage fermé contenu dans l'ouvert.
- Volume 3. Juste en-dessous de (17.162). L'application Phi n'est pas supposée contractante. Il n'est donc pas spécialement vrai que `k<1`. Il n'en reste pas moins que la factorielle va plus vite que les puissances; donc k^pT^p/p! -> 0. Notez que la justification "c'est le terme général de l'exponentielle" n'est pas excellente parce que pour justifier que la série exponentielle converge, il faut justement étudier n^p/p!. Trouvée par Quentin Guyot.
- Volume 3. Proposition 17.40. Cette proposition est probablement fausse. En effet si x_{n+1}=f(x_n) et que x est une limite de (x_n), alors x est un point fixe de f. Ça c'est vrai. Mais si on considère une sous-suite, disons \( y_n\), elle ne vérifie pas y_{n+1}=f(y_n). Et on ne peut même pas dire qu'il existe un p tel que y_{n+1} = f^p(y_n). Quentin Guyot.
- Volume 3. Définition 17.32 et lemme 17.33. Une condition locale sur f'(a) ne peut évidemment pas donner d'informations sur la divergence de la suite. La définition de point répulsif ne dit rien sur ce qu'il se passe lorsque la suite est convergente vers autre chose que a. Bref, la seconde partie de la définition n'est pas correcte et donc la seconde partie du lemme ne va pas. Vous pouvez utiliser le lemme comme définition; c'est ce que presque tout le monde fait. Quentin Guyot.
- Volume 2. Proposition 12.425. Équations (12.1211). Il manque des supremum sur x dans K un peu partout. En particulier, la première inégalité est fausse. Elle devient une égalité si on ajoute un sup. Quentin Guyot.
- Volume 2. Proposition 12.411. La conclusion du point (iii) est un peu rapide. D'abord elle mélange deux epsilon différents, et ensuite elle ne traite que les x+epsilon, et non les x-epsilon. Trouvé par Quentin Guyot.
- Volume 2. Proposition 12.407. La fonction x |-> x^a n'est pas croissante sur les négatifs quand a>0. Prenez par exemple a=3. La deuxième partie de l'énoncé est donc faux. Quentin Guyot.
- Volume 2. Proposition 12.397. La preuve ne fonctionne qu'avec x_k>0. Il faut faire un cas séparé pour `x_k<0` en utilisant a^(-x_k)=1/a^(x_k), et ensuite un cas général. Merci Quentin Guyot.
- Volume 2. Proposition 12.186. Une fonction peut être strictement croissante avec une dérivée qui s'annule en un point. Par exemple x^3 est strictement croissante alors que sa dérivée s'annulle en zéro. Quentin Guyot.
- Volume 2. Équation (12.216). Cela prouve la linéaire indépendance, pas le fait que les polynômes soient premiers entre eux. Vue par Quentin Guyot.
- Volume 2. Proposition 12.61. Équation (12.112). Suppose l'uniforme continuité alors qu'on ne l'a pas. C'est le même type que l'erreur du lemme 14.61 en 2018. Heureusement cette fois l'énoncé est correct. C'est Quentin Guyot qui a trouvé cette faute.
- Volume 2. Proposition 11.208. Les | x | au dénominateur devraient être au numérateur.
- volume 2. Lemme 11.207. La norme de x doit venir au numérateur.
- Volume 2. Proposition 10.7. Les parties O_i ne recouvrent pas K parce que les x_i eux-même ne sont pas dedans.
- Volume 4. Théorème 36.109. La formule (36.358) donnée pour `P(X<=x)` est complètement fausse.
- Volume 1. Théorème 9.253. La preuve de f injective => f_L injective est circulaire à cause du moment où on dit que g_L est injective. Encore une découverte par Quentin Guyot.
- Volume 1. Théorème 6.29. La dernière ligne de la démonstration est fausse. Si kp+lq=0 avec p et q premiers entre eux, nous ne pouvons pas déduire que k=l=0. Prenez par exemple p=3, q=5 et cherchez l,k tels que 3k+5l=0. Facile: k=5, l=-3. Trouvée par Quentin Guyot.
- Volume 1. Proposition-définition 4.134. Une structure réelle n'est pas une involution. La condition (1) est sigma^2=id et non sigma^2=sigma. Trouvée par Quentin Guyot.
- Volume 1. Définition 4.119. Le dual algébrique n'est pas GL(E,K), mais L(E,K). Pour rappel, GL contient les applications linéaires inversibles (le G est pour «groupe»), alors que L contient toutes les applications linéaires.
- Volume 1. Proposition-Définition 1.201. « alors toute décomposition en permutations sera ... » -> « alors toute décomposition en TRANSPOSITIONS sera en quantité paire. ». Trouvée par Quentin Guyot.
- Volume 1. Proposition 3.118 (triplet pythagoriciens). L'équation (3.141) est fausse d'un facteur 4. Il faut séparer en deux cas suivant que z+y ou z-y est divisible en 4. Ensuite on peut continuer en adaptant un peu. Trouvée par Quentin Guyot.

## Frido 2021 (7 faute)

- Volume 2. Proposition 14.237. Si la série n'est pas absolument convergente, la proposition est fausse. En effet, l'intégrale ne dépend pas de l'ordre d'intégration (c'est un des points forts de l'intégrale de Lebesgue), alors que la série dépend de l'ordre des termes.
- Volume 3. Lemme 27.130. L'utilisation de Hölder pour obtenir (27.485b) est incorrecte parce qu'elle demande `0<p<q` alors qu'ici, avec l'hypothèse `1<p<2`, nous avons `q>2`. Merci [Oliver Díaz](https://math.stackexchange.com/questions/3208736/clarkson-inequality-for-complex-numbers/4457490#4457490). Ça ne ruine peut-être pas toute la preuve, [voir ici](https://math.stackexchange.com/questions/1607683/how-to-prove-clarksons-inequality).
- Volume 1. Lemme 10.42. Ce lemme est juste faux : la suite 1/n est un contre-exemple.
- Volume 2. Théorème 14.33. Il faut ajouter l'hypothèse que mu(E_n) et nu(E_n) sont finis. Manque découvert par Alain Vigne.
- Volume 1. Remarque 9.159. L'équation (9.321) est fausse. La réalité est que (f - a 1)^2e_2=0 et non que (f - alpha 1)^2e_2=0. Heureusement, la conclusion ne change pas.
- Volume 3. Lemme 27.114. On invoque à tort le théorème 27.3. Le problème est que 27.3 concerne S^1 alors qu'ici on travaille sur [0,2pi[. Pour adapter, il faudrait composer avec un isomorphisme.
- Volume 1. Équation 6.66. L'inclusion est en réalité dans l'autre sens. Merci à Alain Vigne pour l'avoir trouvée.

## Frido 2020 (12 fautes)

- Volume 3. Proposition 26.105. Il me semble que les fonctions proposées ne séparent pas les points. Par exemple e_k(0)=e_k(T) pour tout k. Il y a peut-être une faute dans la définition des fonctions de base.
- Volume 1. Proposition 1.115. Le epsilon est un élément de K, pas de Q. Donc après avoir fait la majoration qui arrive à 2epsilon, il faut encore prouver qu'il existe un élément de K dont le double est plus petit que epsilon. Autrement dit, il faut trouver epsilon' tel que `2epsilon' < epsilon`.
    D'habitude, en analyse, on ne justifie pas plus loin parce que epsilon est un élément de R et on n'a qu'à prendre epsilon'=epsilon/2. Ici ce n'est pas aussi simple. Il faut trouver un morphisme de Q vers K qui respecte l'ordre.
    Merci à Patrice Goyer pour avoir découvert ce petit bijou.
- Volume 1. Proposition 1.108. Il faut démontrer que S est un corps, et prouver que phi est un morphisme. De plus il manque l'expression d'un isomorphisme sigma entre A et A'. Une bonne partie des 'a' et 'b' sont en réalité des 'sigma(a)' et 'sigma(b)'. La proposition 1.104 fait une partie de ce travail.
- Volume 1. Proposition 1.28. Dans la partie «L'autre sens», rien ne va. Les A et B sont mélangés et phi n'est pas injective (mais de toutes façons elle devait aller dans l'autre sens).
- Volume 1. Lemme 9.85. Dans l'équation (9.161), le premier terme doit être (lambda1-lambda1)v_1, et donc être nul. Ensuite, il faut continuer à appliquer les (A-lambda_i) avec `i < p` pour finir avec v_p=0. Et continuer avec p-1. Merci à Patrice Goyer pour l'avoir trouvée.
- Volume 3. Proposition 26.37. Inégalité de Minkwowski. La partie (2) sur le cas d'égalité est fausse.
- Volume 2. Théorème 11.32. La convergence de f_k vers f est seulement uniforme sur tout compacts.
- Volume 1. Définition 1.97. Les mots «corps» et «anneaux» sont inversés. Un corps est un anneau dans lequel les non nuls sont inversibles.
- Volume 2. Théorème 11.311. La passage de (11.813) à (11.814) limite la validité de l'inéquation à des valeurs de i assez grandes. Or ce "assez grand" dépend à priori des valeurs de n,y et x (qui sont cachées dans alpha_n). Il n'est pas clair que nous puissions prendre la limite n->infini si facilement parce que rien ne garantit que le domaine de validité (par rapport à i) de l'inéquation reste non vide. Cela est particulièrement délicat au moment de prendre le supremum sur y un peu plus bas, parce qu'encore le domaine de validité en i dépend de y. La solution est de remarquer que l'on travaille sur un compact, de telle sorte que `| y-x | < M`. Nous faisons alors une étape supplémentaire de majoration | y-x | < M à l'intérieur de alpha_n. 
- Volume 1. Lemme 7.286. Il s'agit d'une inclusion et non d'une égalité.
- Volume 1. Théorème 7.288. Il manque le traitement de pas mal de subtilités topologiques. En particulier la preuve de d(x,y)=0 => x=y n'est pas écrite, et elle est moins simple que vous pouvez le croire. La définition dans l'équation (7.335) manque d'une sérieuse preuve de l'injectivité de la fonction qui à un r donné fait correspondre le n et la suite des coefficients.
- Volume 3. Définition 19.20 d'une partition de l'unité. Cette définition me semble très bizarre : si l'ouvert est composé de deux ouverts non connexes, je ne vois pas comment c'est possible. Décuplez votre vigilance, et dites-moi si vous connaissez un énoncé exact.

## Frido 2019 (7 fautes)

- Volume 1. Définition 1.45 d'anneau commutatif. C'est la multiplication qui doit être commutative. La somme est toujours commutative; c'est dans la définition d'un anneau.
- Volume 2. Proposition 15.193. La démonstration ne traite pas le cas d'une union dénombrable. Il faut utiliser le théorème de la convergence monotone pour passer à la limite. C'est-à-dire suivre les lignes de la proposition 15.187.
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
  Mais elle n'est pas continue en chacun de ses points parce que nous n'avons pas défini la notion de limite sur un point qui n'est pas un point d'accumulation. Bien entendu, A ne possède aucun point d'accumulation.

## Frido 2017 (9 fautes)

- Volume 1. La définition de forme bilinéaire n'est pas correcte. Elle mélange bilinéarité et symétrie. Être bilinéaire signifie être linéaire en chacune des deux composantes séparément.
- Volume 1. Toute suite dans un compact de R admet une sous-suite convergente (théorème 6.93). La démonstration est fausse, en particulier le cas où nous n'avons qu'un nombre fini de points maximaux. Exemple : x0=5, et ensuite alterner une suite partant de zéro et croissante vers 1 avec une suite partant de zéro et décroissante vers -1. Dans ce cas, x0 est l'unique élément maximal de cette suite.

    Merci à bibi6 pour avoir trouvé cette faute.
- Volume 2. La définition de mesure positive sur un espace mesurable est incorrecte (définition 13.23). La première condition doit être remplacée par 
        mu(vide)=0.
    Sinon, il est possible d'avoir une mesure pour laquelle tous les éléments de la tribu ont une mesure infinie (y compris le vide). Dans
    ce cas, la remarque qui suit la définition de la mesure ne s'applique pas (remarque 13.24), et il n'est en réalité pas garanti d'avoir mu(vide)=0.
- Volumes 1 et 2. Définition de la limite. Induit en erreur à moitié par mon manque d'attention et à moitié par Wikipédia, la définition de la limite d'une fonction était incorrecte, et surtout incohérente avec les théorèmes démontrés plus bas.

    La définition correcte de la limite se fait *en excluant* le point vers lesquels on fait tendre x.
- Volume 1. Définition 4.8. La définition du pgcd dans un anneau n'est pas correcte. 'd' est un pgcd de 'a' et 'b' si tout diviseur commun de 'a' et 'b' divise 'd' ET SI 'd' divise 'a' et 'b'.
- Volume 3. Définition 24.63. La définition d'espace réflexif n'est pas correcte; il faut parler de bidual. Du coup l'énoncé du théorème 24.64 (qui est probablement bien vrai quand même) est à prendre avec des précautions.
- Volume 1. Proposition 4.70. Je suis presque certain qu'il faut ajouter l'hypothèse que I est un idéal propre, c'est-à-dire que l'inclusion de I dans A est stricte.
- Volume 1. L'exemple 4.73 prétend que les anneaux Z/nZ sont principaux. Cela n'est pas vrai en général parce que lorsque `n` n'est pas premier, Z/nZ n'est pas intègre. Il est tout de même vrai que ses idéaux sont principaux.
- Volume 1. L'exemple 4.85 prétend que Z n'est ni principal ni euclidien. En réalité, Z est euclidien (et donc principal) parce que la valeur absolue donne un stathme. [merci cdr](https://github.com/LaurentClaessens/mazhe/issues/58).

