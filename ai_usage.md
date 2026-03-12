# Mon usage de l'IA dans le Frido

## Mon flux de travail

1. J'ai une démonstration sur l'écran de mon ordinateur, sans me préoccuper de la source : cours universitaire, wikipédia, mail envoyé par une lectrice[1], ia, ...
2. Je rédige une démonstration à la main, au crayon sur une feuille de papier. C'est l'étape la plus importante
        - Faire les calculs avec toutes les étapes intermédiaires.
        - Ajouter les étapes intermédiaires que ma source aurait négligé.
        - Vérification que tous les résultats intermédiaires sont déjà dans le Frido (sinon ajouter les énoncés utiles).
        - Modifications éventuelle des notations pour me caler sur ce que je veux.
   Il y a peu de phrases. À la fin, je suis persuadé d'avoir compris chaque pas de la démonstration.

3. Copier de ma feuille de brouillon vers LaTeX.
        - Rédaction des phrases
        - de la remise en forme.


Donc tout ce qui est dans le Frido passe par (au moins) deux rédactions : vers ma feuille puis vers LaTeX.

## Deux types de questions

Dans la vie, il existe deux types de questions : celles pour lesquelles il est facile de vérifier si une proposition de réponse est correcte et celles pour lesquelles vérifier une réponse est aussi compliqué que de trouver la réponse.

### Exemple : donne deux plantes à bulbes autres que la tulipe.

Si on propose la réponse « le cactus et le bégonia », il suffit d'ouvrir les pages wikipédia du cactus et du bégonia pour savoir si c'est bon.

### Exemple : quelle est la date de naissance de Martin Luther King ?

Si on propose la data «1926», la vérifier demande de trouver la réponse.

### En mathématique

En mathématique on est presque toujours dans le premier cas. Si on me propose une démonstration, je peux vérifier qu'elle est correcte, et c'est souvent plus facile que de la réinventer.

## Attention l'IA fait de erreurs

La plupart des démonstrations fournies par chatGPT (version gratuite) sont correctes. Mais parfois elles sont fausses, et les erreurs sont presque toujours subtiles.
Je ne conseillerait à aucun étudiant d'utiliser une IA pour créer des démonstrations. Il faut vraiment avoir le niveau pour parfaitement comprendre une démonstration.

## Attention l'IA ne sait que ce qu'il y a sur internet

Voici une question que je pose à l'IA:

```
Je suis étudiant en mathématique à l'université de Grenobles (France).
Je ne suis pas certain de bien comprendre le concept de limite de fonction. 
Prenons un exemple : la fonction f(x)=0 si x différent de 0 et f(0)=1. 
Quelle est sa limite en 0 ? Pourquoi ?
```

Réponse : 

```
Pour étudier la limite quand x→0, on regarde ce que deviennent les valeurs de la fonction 
quand x s’approche de 0, mais sans être égal à 0.

[blablabla]

lim f(x)=0
x→0
```

Même en ayant précisé que je suis étudiant en France, il me balance toute une explication sur la limite ÉPOINTÉE.
Il se fait que la limite POINTÉE est tellement insignifiante sur internet qu'elle est passée complètement sous le radar de l'entrainement de chatGPT.


## Exemples de contributions IA

### Souvent : formule

Souvent la contribution de l'IA se limite à me rappeler un théorème qui m'avait échappé.


### Vainqueur : humains

Voici un exemple dans lequel les humains ont fait un bien meilleur travail que l'IA. Pour cette question :

https://math.stackexchange.com/questions/5128234/if-fa-subset-a-then-f-bar-a-bar-a

Tant chatGPT que Mistral m'ont donné une démonstration de ce que je voulais. Mais comment je ne parvenais pas à bien comprendre certains passages, j'ai demandé sur stackexchange.
Les humains n'ont pas été longs à me faire remarquer que l'énoncé était faux. Ça explique pourquoi je ne comprenais pas les démonstrations de l'IA.

### Vainqueur : IA

Pour autant que le sache, [2] est le seul texte sur internet donnant la définition d'une application analytique en-dehors du cadre des fonctions de R dans R.
L'essentiel de l'énorme pile de résultats menant à la démonstration de Cauchy-Lipschitz analytique a donc été produit avec de l'IA.

Je lui ai donné l'énoncé à prouver avec la définition d'une application analytique. Puis j'ai ouvert une nouvelle discussion pour pratiquement chaque phrase en essayant de formuler de lemmes (pas mal de combinatoire entre autres).

Au final l'IA a fait le boulot, mais il a fallu lui demander des détails point par point.

Les humains n'ont par contre pas été d'une grande aide : 

https://math.stackexchange.com/questions/5113042/analytic-picard-lindel%c3%b6f-theorem


[1] Dans ce texte, comme dans tout le Frido, le choix entre lecteur et lectrice est aléatoire. Le Frido est donc neutre en moyenne.
[2] https://www.ams.org/journals/proc/1965-016-05/S0002-9939-1965-0184092-2/S0002-9939-1965-0184092-2.pdf
