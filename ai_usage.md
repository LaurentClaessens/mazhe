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

## Attention l'IA fait de erreurs

La plupart des démonstrations fournies par chatGPT (version gratuite) sont correctes. Mais parfois elles sont fausses, et les erreurs sont presque toujours subtiles.
Je ne conseillerais à aucun étudiant d'utiliser une IA pour créer des démonstrations. Il faut vraiment avoir le niveau pour parfaitement comprendre une démonstration.

## Attention l'IA ne sait que ce qu'il y a sur internet

Voici une question que je pose à l'IA:

```
Je suis étudiant en mathématique à l'université de Grenobles (France).
Je ne suis pas certain de bien comprendre le concept de limite de fonction. 
Prenons un exemple : la fonction f(x)=0 si x différent de 0 et f(0)=1. 
Quelle est sa limite en 0 ? Pourquoi ?
```

Réponse chatGPT : 

```
Pour étudier la limite quand x→0, on regarde ce que deviennent les valeurs de la fonction 
quand x s’approche de 0, mais sans être égal à 0.

[blablabla]

lim f(x)=0
x→0
```

Réponse Mistral :

```
[blablabla]

0<| x-a |< delta

[blablabla]

La limite d'une fonction en un point ne dépend pas de la valeur de la fonction en ce point.

[blablabla]
```

Si vous ne voyez pas le problème, voici du contexte.
La définition de limite utilisée partout dans le monde est avec  `0<| x-a |<delta`. C'est ce qu'on nomme (très) rarement la limite ÉPOITÉE.
Dans l'enseignement en France[1], la définition de limite est avec `| x-a |<delta`. C'est ce qu'on nomme la limité POINTÉE.

Même en m'étant fait passer pour un  étudiant en France, il me balance toute une explication sur la limite ÉPOINTÉE.
Il se fait que la limite POINTÉE est tellement insignifiante sur internet qu'elle est passée complètement sous le radar de l'entrainement de chatGPT et de Mistral.

Tout ça pour dire que si vous êtes étudiant en France, chatGPT peut vous induire en erreur[2] si vous lui posez des questions sur la limite.

[1] Et, scandaleusement, sur Wikipédia. Wikipédia fr est le seul Wikipédia au monde à prendre la défintion POINTÉE.
[2] En réalité c'est plutôt votre prof de math qui vous a induit en erreur en vous donnant, sans vous avertir du danger, une définition pas du tout standard de la limite.

## Première conclusion

N'utilisez une IA que si vous avez vraiment le niveau. Vous devez être capable de comprendre la démonstration et détecter des erreurs très fines, parfois dues à des conventions un peu différentes.

## Exemples de contributions IA

### Souvent : formule

Souvent la contribution de l'IA se limite à me rappeler un théorème qui m'avait échappé.
Par exemple en combinatoire, j'ignore énormément de formules de récurrence sur les coefficients binomiaux.


### Vainqueur : humains

Voici un exemple dans lequel les humains ont fait un bien meilleur travail que l'IA. Pour cette question :

https://math.stackexchange.com/questions/5128234/if-fa-subset-a-then-f-bar-a-bar-a

Tant chatGPT que Mistral m'ont donné une démonstration de ce que je voulais. Mais comme je ne parvenais pas à bien comprendre certains passages, j'ai demandé sur stackexchange.

Les humains n'ont pas été longs à me faire remarquer que l'énoncé était faux. Ça explique pourquoi je ne comprenais pas les démonstrations de l'IA.

### Vainqueur : IA

Pour autant que le sache, [2] est le seul texte sur internet donnant la définition d'une application analytique en-dehors du cadre des fonctions de R dans R.
L'essentiel de l'énorme pile de résultats menant à la démonstration de Cauchy-Lipschitz analytique a donc été produit avec de l'IA.

Je lui ai donné l'énoncé à prouver avec la définition d'une application analytique. Puis j'ai ouvert une nouvelle discussion pour pratiquement chaque phrase en essayant de formuler de lemmes (pas mal de combinatoire entre autres).

Au final l'IA a fait le boulot, mais il a fallu lui demander des détails point par point.

Les humains n'ont par contre pas été d'une grande aide : 

https://math.stackexchange.com/questions/5113042/analytic-picard-lindel%c3%b6f-theorem


-------

[1] Dans ce texte, comme dans tout le Frido, le choix entre lecteur et lectrice est aléatoire. Le Frido est donc neutre en moyenne.

[2] https://www.ams.org/journals/proc/1965-016-05/S0002-9939-1965-0184092-2/S0002-9939-1965-0184092-2.pdf
