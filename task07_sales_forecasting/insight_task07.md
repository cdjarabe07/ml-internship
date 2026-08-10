# Insight — Task 7 : Prévision des ventes

## Ce qu'on a cherché à savoir
Peut-on prédire les ventes hebdomadaires d'un magasin Walmart à l'avance, à partir de son historique récent et de facteurs externes (météo, prix du carburant, économie) ?

## Ce qu'on a trouvé
**Oui, avec une précision remarquable : 98.8 % de la variation des ventes est expliquée** par le meilleur modèle (LightGBM), avec une erreur moyenne d'environ **41 000 $** — sur des ventes hebdomadaires qui tournent souvent autour de 1 à 2 millions de dollars par magasin, c'est une erreur de l'ordre de 2-3 % seulement.

| Modèle | Erreur moyenne (MAE) | Fiabilité (R²) |
|---|---|---|
| **LightGBM** ✅ | 41 195 $ | 98.8 % |
| XGBoost | 46 355 $ | 98.5 % |
| Régression linéaire | 48 935 $ | 98.4 % |
| Random Forest | 50 640 $ | 98.2 % |

## Ce qui pilote vraiment les ventes

**Le calendrier compte plus que tout le reste** : la semaine de l'année (`WeekOfYear`) est le facteur le plus important — logique, les ventes ont un cycle saisonnier fort (fêtes de fin d'année, périodes de rentrée, etc.).

Juste derrière : **ce qui s'est vendu la semaine précédente** (`Sales_Lag1`) et **la moyenne des 4 dernières semaines** — sans surprise, un magasin qui vendait bien continue généralement à bien vendre à court terme.

Fait intéressant : **la température a plus d'impact que le prix du carburant, l'inflation (CPI) ou le chômage** — le climat influence visiblement les habitudes d'achat plus que le contexte économique global, au moins sur cette période.

## Un point de vigilance sur la méthode

Contrairement aux autres tâches du stage, on n'a **pas séparé train/test au hasard** — on a volontairement coupé par date (les dernières semaines dans le test). Prédire le passé en s'entraînant sur le futur aurait donné un score artificiellement gonflé, qui ne veut rien dire une fois en conditions réelles.

## À retenir
1. **La saisonnalité (semaine de l'année) et la dynamique récente (ventes de la semaine dernière) expliquent l'essentiel** — un modèle simple basé juste sur ces deux éléments capturerait déjà la majorité du signal.
2. **Le climat pèse plus que l'économie** dans ce dataset — à garder en tête si on doit un jour simplifier le modèle pour la production.
