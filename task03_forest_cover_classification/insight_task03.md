# Insight — Task 3 : Prédiction du type de forêt

## Ce qu'on a cherché à savoir
Peut-on deviner quel type de forêt (7 types possibles) pousse sur un terrain, juste à partir de données géographiques (altitude, pente, distance aux routes, etc.), sans y aller sur place ?

## Ce qu'on a trouvé
**Oui, avec une bonne fiabilité : 88 % de bonnes réponses** avec Random Forest (le modèle le plus performant des deux testés). XGBoost fait un peu moins bien ici (85 %).

| Modèle | Bonnes réponses | Fiabilité moyenne par type de forêt |
|---|---|---|
| **Random Forest** ✅ | 88 % | 80 % |
| XGBoost | 85 % | 78 % |

## Le vrai facteur qui explique tout : l'altitude

**L'altitude (`Elevation`) est, de très loin, l'information la plus utile** pour deviner le type de forêt — presque 2.5 fois plus importante que le deuxième facteur (la distance aux routes). Concrètement : dis-moi à quelle altitude tu es, et j'ai déjà une bonne idée du type de forêt, avant même de savoir quoi que ce soit d'autre sur le terrain.

Les autres facteurs qui comptent, mais beaucoup moins : la distance aux routes et aux points d'incendie, puis la distance à l'eau.

## Où le modèle se trompe le plus

Le modèle est excellent sur les types de forêt les plus courants (types 1 et 2, qui représentent 85 % des cas), mais **beaucoup moins fiable sur les types rares** — notamment le **type 5** (seulement 43 % des cas correctement repérés) et le **type 4** (le plus rare de tous, à peine 222 cas sur 50 000).

C'est un piège classique : le modèle a très peu d'exemples pour apprendre ces types rares, donc il les rate plus souvent — même si l'accuracy globale (88 %) paraît très bonne.

## À retenir
1. **L'altitude seule fait presque tout le travail** — un modèle simplifié basé juste sur l'altitude et la distance aux routes capturerait déjà l'essentiel.
2. **88 % de fiabilité globale cache une vraie faiblesse sur les types rares** — si l'objectif final est de bien détecter TOUS les types (pas juste les plus fréquents), il faudra rééquilibrer les données ou pondérer le modèle en faveur des classes minoritaires.
