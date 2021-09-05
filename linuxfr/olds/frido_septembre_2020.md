Fin de la dédaction ici le 11 sept 2020.
Le reste va sur linuxfr.




# Le Frido et Giulietta : la mathématique libre


[Le Frido](https://laurent.claessens-donadello.eu/pdf/lefrido.pdf) est un livre de mathématique qui a pour but est d'aller de la théorie des ensembles (non comprise) jusqu'à finir l'agrégation. [Giulietta](https://laurent.claessens-donadello.eu/pdf/giulietta.pdf) est une extension qui va de l'agrégation jusqu'à tout ce que je sais en mathématique.

- Si vous voulez juste lire ? téléchargez les versions courantes [le frido](https://laurent.claessens-donadello.eu/pdf/lefrido.pdf) ou [Giulietta](https://laurent.claessens-donadello.eu/pdf/giulietta.pdfhttp://laurent.claessens-donadello.eu/pdf/giulietta.pdf) et profitez. Ces pdf sont régulièrement mis à jour.
- Vous voulez passer l'agreg ? Téléchargez les versions "stables" de cette année, et si vous aimez, achetez. (je ne suis pas certain que vous ayez le droit de venir avec le Frido imprimé depuis chez vous).
- Vous voulez contribuer ? On en parle plus bas.

## Principes de base

La base, c'est que c'est libre (oui, c'est un jeu de mot; j'avais juste envie de le placer).

- Le Frido introduit toutes les notions de l'ordre mathématiquement logique. C'est loin d'être l'ordre pédagogiquement optimal.
- Il n'y a pas d'abus de language ou de notations.
- Rien n'est considéré comme évident.

Donc au final c'est un peu long.

## Images de couverture

Les [images de couverture](https://github.com/LaurentClaessens/mazhe/tree/master/python/Pepper_Carrot) proviennent de la BD libre [Pepper et Carrot](https://www.peppercarrot.com/fr/) par David Revoy.

## Changements depuis septembre 2019

Il y a peu de changements cette année pour cause de covid19 (voir plus bas).

- Une application est C^n si et seulement si ses dérivées partielles sont C^{n-1}. Je suis assez fier de ce résultat parce que c'est démontré complètement, en montrant de manière explicite l'isomorphisme qu'il y a entre l'espace des applications n-multilinéaires et les espaces emboîtés L(V,L(V, L(V,W))) dans lesquels vivent les différentielles d'ordre plus élevés.
- Si A est un ensemble infini, alors AxA est équipotent à A. Utilisation massive du lemme de Zorn.
- Preuve que tout corps admet une clôture algébrique.
    
## Orthographe réformée

J'en fais pas spécialement une religion, mais j'ai décidé de m'y mettre. Des fois, ça pique les yeux parce que je suis trop vieux pour m'y faire (des maximums, le mois d'aout sans accent); des fois c'est juste plus simple (à priori, sans italique).

Tant qu'à parler d'orthogaphe, j'adopte une grammaire terriblement arriérée et non inclusive. Je n'hésite pas à écrire «Cette fonction, est un homomorphisme», sur le même modèle que «le père noël est une ordure» ou «cette femme est un ministre».

## Accessibilité

Il n'y a rien de spécifique pour les aveugles, malvoyants, dyslexiques ... et je n'ai aucune idée de ce que je devrais faire pour rendre le Frido plus accessible.

Si vous savez des choses sur le handicap, faite-le moi savoir. Fonte adaptée à la dyslexie ? Taille des caractères ? Inversion blanc/noir plus plus de contraste ?

Je peux produire autant de pdf différents que vous voulez, et appliquer autant de scripts en python ou en bash qu'il le faut pour modifier le code LaTeX à la volée.

## Pour contribuer

### Niveau facile

Lire et m'écrire quand vous voyez des erreurs ou des choses pas claires.

La version en ligne du Frido utilise `showlabels` pour montrer les labels des théorèmes. Si vous voulez me dire « il y a une erreur à la cinquième ligne de la page 563 », mieux vaut me dire « il y a une erreur juste en-dessous de l'équation DEFooMGXSooWioKie ».

### Niveau avancé

Prenez n'importe quel résultat énoncé sans preuve. Envoyez moi une référence en ligne vers une preuve, ou rédigez-en une.

Vous pouvez télécharger [les sources sur github](https://github.com/LaurentClaessens/mazhe) et tout de suite taper vous-même.

## Frido et covid19

### Frein

La pandémie de covid19 a donné un gros coup d'arrêt au Frido. La raison est que, les écoles étant fermées, j'ai dû faire un mi-temps taf le matin plus un mi-temps garde d'enfants l'après-midi et un troisième mi-temps la nuit pour terminer les heures de boulot.

Ça, c'était du temps du confinement. Maintenant les choses ont changé, et certaines habitudes commencent à se prendre.

Grâce au télétravail, je peux me libérer le mercredi après-midi, et récupérer les soirs entre 21h et 22h. Le télétravail me permet donc de convertir du temps de Frido le soir en temps avec les enfants le mercredi.
