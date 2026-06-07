# Mon usage de l'IA dans le Frido


## Mon flux de travail

1. J'ai une démonstration sur l'écran de mon ordinateur, sans me préoccuper de la source : cours universitaire, wikipédia, mail envoyé par une lectrice, ia, ...
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

## Le cas des résultats intermédiaires

Je dois faire la démonstration de A.

Si je lis un humain, dans la démonstration de A écrire « en vertu de la proposition B, blabla », souvent je me permets de copier l'énoncé de B dans le Frido et de continuer (j'écris alors B dans ma liste de chose à faire).

Si une IA écrit « en vertu de la proposition B », alors soit je retrouve un énoncé de B par un humain sur internet, soit je demande à l'IA de démontrer B avant de continuer.

Bref, il n'y a pas de résultats dans démonstration dans le Frido dont l'énoncé viendrait seulement d'une IA.



## Trouver les parties assistées par IA

Les démonstrations qui ont bénéficié d'une aide IA sont marquées de ces labels dans la biblio : 

1. BIBooMistral
2. BIBChatGPT
3. BIBChatGPTDifficile

Je répète : il n'y a aucun copié-collé de la sortie d'un LLM vers le Frido. Si une théorème a une de ces sources, ça veut dire que j'ai posé des questions à une IA pour la démonstration, et que certaines de ses suggestions ont été suivies.


## Attention l'IA fait de erreurs

La plupart des démonstrations fournies par chatGPT (version gratuite) sont correctes. Mais parfois elles sont fausses, et les erreurs sont presque toujours subtiles.
Je ne conseillerais à aucun étudiant d'utiliser une IA pour créer des démonstrations. Il faut vraiment avoir le niveau pour parfaitement comprendre une démonstration.

# Pour les contributrices

Je n'ai rien contre une contribution qui aurait été faire par de l'IA. Mais j'ai quelque chose contre un copié-collé d'une sortie de l'IA.

1. Rédigez la preuve vous même
2. Ayez le niveau. Si vous ne pensez pas avoir le niveau pour comprendre la preuve, ne me l'envoyez pas.


# Autres réflexions et exemples d'utilisation de l'IA pour la mathématique


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
La définition de limite utilisée partout dans le monde est avec  `0<| x-a |<delta`. C'est ce qu'on nomme (très) rarement la limite ÉPOINTÉE.
Dans l'enseignement en France[1], la définition de limite est avec `| x-a |<delta`. C'est ce qu'on nomme la limité POINTÉE.

Même en m'étant fait passer pour un  étudiant en France, il me balance toute une explication sur la limite ÉPOINTÉE.
Il se fait que la limite POINTÉE est tellement insignifiante sur internet qu'elle est passée complètement sous le radar de l'entrainement de chatGPT et de Mistral.

Tout ça pour dire que si vous êtes étudiant en France, chatGPT peut vous induire en erreur[2] si vous lui posez des questions sur la limite.

[1] Et, scandaleusement, sur Wikipédia. Wikipédia fr est le seul Wikipédia au monde à prendre la définition POINTÉE.
[2] En réalité c'est plutôt votre prof de math qui vous a induit en erreur en vous donnant, sans vous avertir du danger, une définition pas du tout standard de la limite.

## Première conclusion

N'utilisez une IA que si vous avez vraiment le niveau. Vous devez être capable de comprendre la démonstration et détecter des erreurs très fines, parfois dues à des conventions un peu différentes.

## Un exemples où les humains ont été plus forts (février 2026)

Voici un exemple dans lequel les humains ont fait un bien meilleur travail que l'IA. Pour cette question :

https://math.stackexchange.com/questions/5128234/if-fa-subset-a-then-f-bar-a-bar-a

Tant chatGPT que Mistral m'ont donné une démonstration de ce que je voulais. Mais comme je ne parvenais pas à bien comprendre certains passages, j'ai demandé sur stackexchange.

Les humains n'ont pas été longs à me faire remarquer que l'énoncé était faux. Ça explique pourquoi je ne comprenais pas les démonstrations de l'IA.


## Un cas où l'IA a été plus forte (2025)

Pour autant que le sache, [2] est le seul texte sur internet donnant la définition d'une application analytique en-dehors du cadre des fonctions de R dans R.
L'essentiel de l'énorme pile de résultats menant à la démonstration de Cauchy-Lipschitz analytique a donc été produit avec de l'IA.

Je lui ai donné l'énoncé à prouver avec la définition d'une application analytique. Puis j'ai ouvert une nouvelle discussion pour pratiquement chaque phrase en essayant de formuler de lemmes (pas mal de combinatoire entre autres).

Au final l'IA a fait le boulot, mais il a fallu lui demander des détails point par point.

Les humains n'ont par contre pas été d'une grande aide : 

https://math.stackexchange.com/questions/5113042/analytic-picard-lindel%c3%b6f-theorem


[2] https://www.ams.org/journals/proc/1965-016-05/S0002-9939-1965-0184092-2/S0002-9939-1965-0184092-2.pdf


## L'IA fait encore des erreurs incroyablement basiques (mai 2026)

Oui, l'IA m'a fait une preuve de Cauchy-Lipchitz analytique. Impressionnant.

Mais en lui demandant de relire ma preuve du lemme LEMooUXWKooKEjyrb, Mistral est parvenu à me dire que \( S\) n'était pas spécialement ouvert en donnant un contre-exemple. Je passe les détails, mais Mistral m'a dit (avec exactement ces mots) :

> Alors S=]−1,0[ ∪ ]0,1[, qui n'est pas ouvert (car 0∉S mais 0 est adhérent à S).

Il s'agit d'une faute incroyablement basique sur de la topologie réelle. On n'accepterait pas qu'un étudiant de première année écrive ça sur sa feuille !

Cela dit, j'ai quand même gagné un peu en discutant avec l'AI.

1. Mistral m'a montré que je devais supposer que \( I_1\) et \( I_2\) sont ouverts.
2. chatGPT m'a signalé que j'avais écrit à certains endroits \( A\cap B\) au lieu de \( A_1\cap A_2\).


-------


