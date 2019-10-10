# Branch description

This files provides a small description of the branches.

## ctes

Dans cette branche j'écris les notes du cours d'analyse numérique du CTES de Marseille.

## propsomme

La proposition propnseries_propdeba sur les propriétés des séries est à démontrer et certainement que certains points sont déjà démontrés ailleurs.

## futur

Solve some future references.

## deploy

Take into account the case with a non empty stash list.

# pictures

Recompile the pictures and some tests...

## testing

Rename some testing scripts

## bibi6

- Ajouter dans la liste des contributeurs.
- Mettre ok les références restées vides.
- Include the work of bibi6.


## url

Track death links.

Ne faire les tests de figure que si "--full" est passé en argument de 'testing.sh'

Track death links. 13,15,21
PDFpersoWanadoo
BezoutCos
NjCCfW



## pr

Deal with the pull requests from github


## pr

Lire le diff de  https://github.com/LaurentClaessens/mazhe/pull/36

Modifiés : les fichiers 46_, 47_ et 48_

Lemme 3.22: il faudrait réfléchir à un meilleur placement de ce lemme. Il est général, pourquoi le mettre avec des choses Z-centrées?

Trouver la définition de groupe simple dans mazhe

## rep

2 - oui, E( P(A|X) ) = P(A). Démo, par les propriétés de l'espérance conditionnelle, E( P(A|X) ) = E( E (1_A|X) ) = E (1_A)= P(A), où 1_A est l'indicatrice de l'événement A.
4 - la question n'a pas forcément de sens en toute généralité : la compacité dépend de la topologie, qui n'a pas de raison d'être lié à la mesure. Étant donnée une mesure, il n'y a pas de façon naturelle de lui associer une topologie. En revanche, l'inverse a un sens : la définition des Borelliens n'est pas restreinte à R^n. Étant donné un espace topologique, par définition, la tribu borellienne est la tribu qui est engendrée par les ouverts de la topologie. Ensuite, on peut mettre n'importe quelle mesure sur cette tribu, et il n'y a pas de raison qu'elle soit de masse finie sur des compacts. Par exemple, on peut prendre [0,1] muni de la tribu borellienne et de la mesure dont la densité par rapport à la mesure de Lebesgue est f(x) = 1/x, la masse de [0,1], pourtant compact, est infinie.
7 - c'est faux. Contre-exemple : prenons Z=XY, avec X et Y indépendants égaux à + ou - 1 avec proba 1/2. Alors E(XY|Z) = Z et E(X|Z) = E(Y|Z) = 0.
8 - E(X) = m n'implique absolument pas que P(X=m-a) = P(X=m+a). Contre exemple : X = 1 ou 3 avec proba 1/4 chacun et -2 avec proba 1/2. Alors E(X) = 0 mais P(X=-k) est différent de P(X=k) pour k = 1,2,3. Ensuite, quand on fait le TCL et qu'on regarde X_n = (somme des X_i, i =1..n)/racine de n, première remarque : P(X_n = a) pour tout a tend vers 0 puisque la gaussienne est à densité. Ensuite, P(X_n<-a) converge vers la même quantité que P(X_n >a), puisque la gaussienne est symétrique, mais il n'y a aucune raison qu'il y ait égalité pour un n donné.

## vecto

On croyait rêver : le chapitre sur les espaces vectoriels parle de dérivabilité, Cinfini et tout ça ...

## url
Track death links. 13,15,21
PDFpersoWanadoo
BezoutCos
NjCCfW

# orga

Écrire des points d'organisation dans le Frido.

# finite

Dans cette branche on parle d'éléments finis.

## futur

Régler les réfénreces vers le futur et faire un peu d'index thématique.

## gradient

On rend plus lisible la méthode du gradient à pas optimal et on démontre les choses qu'il faut au niveau des fonctions convexes.

## corr

Tenir compte de ce que m'a envoyé Anthony Olivier

## tetra

Le isométries du tétrahèdre

## tuto

## xspace
What happens when one suppress xspace ?

## part

Try to add "part" in the toc file

# decoupe

Travailler le découpage en volumes.

# fondamental

Il y avait trois fois le théorème fondamental de l'analyse. Fixer ça.


# madore

Traiter l'équation diophantienne proposée dans
http://www.madore.org/~david/weblog/d.2017-08-18.2460.html#d.2017-08-18.2460

# Alembert

Encore déplacer ce théorème

# weiner

Traiter de la constante de Weiner.

# frido2017

Pour la publication de septembre 2017

# hilbert

Prouver que L^2 est le seul L^p qui soit un espace de Hilbert.

# linuxfr

Les patches venant de linuxfr et autres trucs qui m'arrivent par mail.

# renomme

Il y a deux fichiers 185. Corriger ça.

# eric

Prendre les correctifs de https://github.com/LaurentClaessens/mazhe/pull/55

# lax

Tenir compte des remarques de Antoine Bensalah pour le théorème de Lax-Milgram

# cdr

Les remarques de cdrcprds

# holo

Montrer le coup de l'anneau des fonctions holomorphes sur un compact.
(wikipédia -> anneau principal)

# deschamps

Tenir compte des remarques de Guillaume Deschamps

# gb

Tenir compte des remarques de Guillaume Barriere

# racines

La partie sur les racines de l'unité dans les groupes dépend de
- polynômes
- exponentielle complexe (séries entières)

# rsa

Voir si isométries du cube et RSA peuvent être déplacés.

# l2

Quelques réflexions sur la TF sur L2.

# eg

Les remarques de Éric Guirbal

# ordre

Remise en ordre des nombreux points restés en suspend après le passage de Guillaume Barriere.

# overfull

Supprimer quelque "Overfull \hbox".

# exocorr

Supprimer la dépendence en le paquet personnel 'exocorr'.

bibi
frido2018
thisirs

# guilietta

Work on the 'research' part.
frido
