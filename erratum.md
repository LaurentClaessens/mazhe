# Erratum du Frido

Ce fichier contient les fautes découvertes dans les versions imprimées du Frido. Elles sont en principe corrigées au fur et à mesure dans la [version courante](http://laurent.claessens-donadello.eu/pdf/lefrido.pdf).

## Frido 2017

Les fautes sont présentées par ordre anti-chronoligique de découvertes.

- Volume 1. Définition 4.8. La définition du pgcd dans un anneau n'est pas correcte. 'd' est un pgcd de 'a' et 'b' si tout diviseur commun de 'a' et 'b' divise 'd' ET SI 'd' divise 'a' et 'b'.
 
- Volume 3. Définition 24.63. La définition d'espace réflexif n'est pas correcte; il faut parler de bidual. Du coup l'énoncé du théorème 24.64 (qui est probablement bien vrai quand même) est à prendre avec des précautions.
    voir par exemple wikipédia : https://fr.wikipedia.org/wiki/Espace_réflexif

- Volume 1. Proposition 4.70. Je suis presque certain qu'il faut ajouter l'hypothèse que I est un idéal propre, c'est à dire que l'inclusion de I dans A est stricte.

- Volume 1. L'exemple 4.73 prétend que les anneaux Z/nZ sont principaux. Cela n'est pas vrai en général parce que lorsque `n` n'est pas premier, Z/nZ n'est pas intègre. Il est tout de même vrai que ses idéaux sont principaux.

- Volume 1. L'exemple 4.85 prétend que Z n'est ni principal ni euclidien. En réalité, Z est euclidien (et donc principal) parce que la valeur absolue donne un stathme. [merci cdr](https://github.com/LaurentClaessens/mazhe/issues/58).


