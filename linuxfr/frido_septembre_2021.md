
### Changements

Quelques résultats ajoutés depuis septembre passé.

- Théorème pour permuter distribution et intégrale
- Le dual d'un espace vectoriel normé sépare les points
- Le cas d'égalité dans Hölder et Minkowski
- Les naturels : définition, opérations, ordre.
- Un théorème permettant de définir une application par récurrence.

J'ai ajouté une liste de développements leçon par leçon. Cette liste est très incomplète, et je ne sais pas si les choix sont pertinents. Toutes les recommandations sont les bienvenues

### Agrégation interne

Une grande nouvelle de cette année est que le Frido est [sur la clef agreg](https://interne.agreg.org/index.php?id=oraux) de l'agrégation interne.

Pour l'agrégation externe, je ne sais pas.

### Écriture inclusive

Quand je m'adresse à la persone qui lit, je fais du pseudo-aléatoire.

Pour les amateurs de LaTeX, le compteur `numtho` est le numéro courant de théorème, lemme, remarque, etc. Je définis les macros suivante :
```
\newcounter{rndgendercont}
\newcommand{\randomGender}[2]{%
                \setcounter{rndgendercont}{%
                    \numexpr\value{page}+\value{numtho}\relax%
}%
\ifthenelse{\isodd{\value{rndgendercont}}}{#1}{#2}%
}
```
qui s'utilise en disant par exemple
```
Vous devez savoir, \randomGender{chèr lecteur}{chère lectrice} que etc.
```

Ce n'est pas cryptographiquement sûr, entre autres parce que le compteur de page en LaTeX ne se mets pas à jour exactement au saut de page.

Par contre, ça fait le travail d'être apparemment aléatoire du point de vue de la personne qui lit, tout en étant suffisamment déterministe pour que la valeur aléatoire ne change pas à l'intérieur d'un environnement, ce qui est nécessaire si je veux faire un choix cohérent sur plusieurs phrases.

### Règlement de l'agrégation

Le règlement de l'agrégation concernant les livres est à la page 75 [du rapport](https://agreg.org/data/uploads/rapports/rapport2020.pdf). En très résumé, deux points sont saillants :

- Seuls sont autorisés les ouvrages avec un numéro ISBN et jouissant d’un minimum de diffusion commerciale. 
- Cette restriction est motivée par le principe d’égalité des candidats : les ressources documentaires autorisées doivent être facilement accessibles à tout candidat au concours.

Que pouvons-nous en déduire ?

- Les phrases sont écrites au présent. Les livres qui ne sont plus commercialisés sont donc interdits.
- Si nous comptons l'équité financière dans «facilement accessibles», il est fortement discutable qu'un livre de 30 euros rien que pour la topologie soit autorisé.
- Si nous comptons les aveugles dans «tous les candidats», les livres qui ne fournissent pas les sources LaTeX sont interdits.

Nous retombons sur trois points classiques du libre : la pérennité, le [cout](http://www.renouvo.org/liste.php) et le handicap.

## giulietta


[Giulietta](https://laurent.claessens-donadello.eu/pdf/giulietta.pdf) est un document plus informel. Il contient à peu près tout ce que je connais en mathématique. Il se divise en 4 parties :

- Le Frido en français
- De la mathématique plus avancée en anglais: beaucoup de géométrie différentielle
- Des exercices et corrigés de Matlab que j'avais donné il y a longtemps à Louvain-la-Neuve 
- Des exercices et corrigés de mathématique provenant de TP donnés à Bruxelles et Besançon.


## Comment contribuer ?

Pas besoin de savoir LaTeX pour contribuer.

- Écrivez-moi si vous trouvez des erreurs ou des passages pas clairs.
- Faites une capture d'écran et griffonnez sur le jpg. C'est plus pratique que dire «dans le troisième terme de l'équation en-dessous de (23.127), l'indice du A devrait être j».
-  Rédigez une démonstration à la main sur du papier et envoyez-moi une photo. Plusieurs contributeurs l'ont déjà fait, et ça marche bien.
- Pour désigner une proposition ou une équation, utilisez les labels qui sont affichés. Au lieu de dire «la proposition 27.112», dites «la proposition PROPooHNJZooGfRCfU». Une recherche de «HNJZ» dans le pdf donnera toujours le bon résultat alors que le numéro peut changer.
»
- Si possible ajoutez une référence vers la source utilisée.

------------------------------------------------------------



## Règlement de l'agrégation

    Maintenant que l'équité entre les candidats est au centre du règlement, nous pouvons nous amuser avec des paradoxes. Est-ce que les livres qui ne sont plus vendus sont interdits ?

## Accessibilité

    Un lecteur aveugle m'a expliqué qu'il était surtout intéressé par les sources LaTeX (même pas par le pdf). En gros, il transforme au maximum les formules en unicode équivalent. Par exemple 
```
    $\Sigma^* = \Sigma^+ \cup \{ \varepsilon \}$ 
```
va devenir 
```
    Σ^*=Σ^+∪{ϵ}
```

Cela pour dire que nous retombons dans un discours très classique sur linuxfr : fournir les source (et de préférence des sources claires) a également un intérêt du point de vue de l'accessibilité.

Voila. Et comme je suis un monomaniaque du règlement de l'agrégation, je dirais que les livres fournis sans les sources provoquent en une rupture d'équité entre le candidats. Ils sont donc interdits à l'agrégation -- au moins dans l'esprit sinon à la lettre.

Ok. Dit comme ça c'est un peu fort, mais si ça peut faire réfléchir les auteurs : publier les sources LaTeX des bouquins aide vraiment certains aveugles.

## Bibliothèque aggregation interne

- Il est dans la bibliothèque de l'agreg interne:  https://interne.agreg.org/index.php?id=oraux

- Idées de développements. Il me faut des idées de développement avec:
    * énoncé
    * démonstration
    * un mot expliquant pourquoi ce développement rentre dans la leçon

- permalien avec showkeys


