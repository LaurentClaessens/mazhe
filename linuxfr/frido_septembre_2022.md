

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

Voilà. Et comme je suis un monomaniaque du règlement de l'agrégation, je dirais que les livres fournis sans les sources provoquent en une rupture d'équité entre le candidats. Ils sont donc interdits à l'agrégation -- au moins dans l'esprit sinon à la lettre.

Ok. Dit comme ça c'est un peu fort, mais si ça peut faire réfléchir les auteurs : publier les sources LaTeX des bouquins aide vraiment certains aveugles.

## Bibliothèque aggregation interne

- Il est dans la bibliothèque de l'agreg interne:  https://interne.agreg.org/index.php?id=oraux


- Idées de développements. Il me faut des idées de développement avec:
    * énoncé
    * démonstration
    * un mot expliquant pourquoi ce développement rentre dans la leçon

