- Préciser que la licence est GNU-fdl
- Il faudrait préciser que le PDF de Giulietta est la compilation de 4 parties :
    Le frido (FR)
    Giulietta (EN)
    Des corrigés Matlab (FR)
    Des exercices et corrigés (FR)
- Dire que la liste des développements est à nouveau là.
- Suppression de la géométrie différentielle

- Écriture épicène. Je fais du pseudo-aléatoire.

Pour les amateurs de LaTeX, le compteur `numtho` est le numéro courant de théorème, lemme, remarque, etc.

Je définis la macro suivante :
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

- Règlement de l'agrégation.
    Maintenant que l'équité entre les candidats est au centre du règlement, nous pouvons nous amuser avec des paradoxes. Est-ce que les livres qui ne sont plus vendus sont interdits ?

- Il est dans la bibliothèque de l'agreg interne:  https://interne.agreg.org/index.php?id=oraux

- Idées de développements. Il me faut des idées de développement avec:
    * énoncé
    * démonstration
    * un mot expliquant pourquoi ce développement rentre dans la leçon

- permalien avec showkeys
