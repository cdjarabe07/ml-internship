# Insight — Task 6 : Classification de genre musical

## Ce qu'on a cherché à savoir
Peut-on deviner le genre d'un morceau (blues, jazz, metal, pop...) juste en analysant ses caractéristiques sonores, sans l'écouter soi-même ?

## Ce qu'on a trouvé
**Oui, avec une bonne fiabilité : 87 % de bonnes réponses** avec Random Forest — un peu mieux qu'un SVM (85 %) sur les mêmes données.

| Modèle | Bonnes réponses | Fiabilité moyenne par genre |
|---|---|---|
| **Random Forest** ✅ | 87 % | 87 % |
| SVM | 85 % | 84 % |

## Contrairement aux autres tâches : aucun facteur ne domine

Sur les tâches précédentes (prêt bancaire, type de forêt), un seul facteur écrasait tous les autres (86 % du poids de la décision). **Ici, c'est tout l'inverse** : la feature la plus importante (la variance de la clarté tonale, `perceptr_var`) ne pèse que 5 % — et une quinzaine d'autres facteurs se suivent de très près juste derrière (chroma, rythme, timbre/MFCC, largeur spectrale...).

**Ce que ça veut dire concrètement** : reconnaître un genre musical, ce n'est pas repérer UN indice décisif, c'est **combiner beaucoup de petits indices sonores en même temps** — un peu comme reconnaître un accent : pas un seul mot qui trahit tout, mais un ensemble de petites nuances.

## Où le modèle se trompe le plus

- **Le classique et le metal sont les mieux reconnus** (93-97 % de rappel) — logique, ce sont des genres avec une "signature sonore" très marquée et peu ambiguë
- **Le rock est le plus difficile** (76 % de rappel seulement) — probablement parce que le rock partage des caractéristiques sonores avec plusieurs autres genres (country, disco, metal), ce qui crée de la confusion
- **Le country est aussi source d'hésitation**, sans doute pour la même raison de proximité sonore avec d'autres genres

## À retenir
1. **Classer un genre musical demande de combiner de nombreux indices**, pas un seul critère décisif — contrairement aux tâches précédentes de ce stage.
2. **Les genres "flous" à la frontière d'autres styles** (rock, country) sont plus difficiles à classer que les genres très typés (classique, metal) — un vrai reflet de la réalité musicale, pas juste une faiblesse du modèle.
