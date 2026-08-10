# Insight — Task 2 : Segmentation des clients

## Ce qu'on a cherché à savoir
Peut-on regrouper les 200 clients du centre commercial en profils distincts, selon leur revenu et leur comportement d'achat ?

## Ce qu'on a trouvé
Oui, et le modèle (K-Means) a identifié **5 groupes de clients bien distincts** :

| Groupe | Profil | Âge moyen | Revenu moyen | Dépense moyenne | Taille |
|---|---|---|---|---|---|
| 1 | **Clients premium** — revenu élevé et grosse dépense | 33 ans | 86.5 k$ | 82/100 | 39 clients |
| 2 | **Jeunes petits budgets qui dépensent beaucoup** | 25 ans | 25.7 k$ | 79/100 | 22 clients |
| 3 | **Clients moyens, équilibrés** | 43 ans | 55.3 k$ | 50/100 | 81 clients (le plus gros groupe) |
| 4 | **Revenu élevé mais radins** | 41 ans | 88.2 k$ | 17/100 | 35 clients |
| 5 | **Petit budget, petite dépense** | 45 ans | 26.3 k$ | 21/100 | 23 clients |

## Ce que ça veut dire pour le business

- **Le groupe 1 (premium)** est la cible marketing la plus rentable : ils ont l'argent ET l'envie de dépenser.
- **Le groupe 4 est le plus intéressant à travailler** : ils ont largement les moyens (88 k$ de revenu, le plus haut de tous les groupes) mais ne dépensent presque pas (17/100). Comprendre pourquoi (offre pas adaptée ? manque de fidélisation ?) pourrait débloquer un gros potentiel.
- **Le groupe 2** montre que le revenu n'est pas tout : ce sont les plus jeunes et les moins riches, mais ils dépensent presque autant que les clients premium.
- **Le groupe 3** est le socle client "normal" — 40 % de la clientèle, ni excellent ni mauvais, à fidéliser sans effort marketing excessif.

## Un point de vigilance détecté (bonus DBSCAN)
Une deuxième méthode (DBSCAN) a repéré **8 clients "atypiques"** qui ne rentrent dans aucun profil standard — des comportements d'achat hors norme, à regarder individuellement plutôt qu'à mettre dans une case générique.

## À retenir
Le revenu seul ne prédit pas la dépense — l'âge et le comportement comptent tout autant. Le vrai gisement de valeur non exploité, c'est le **groupe 4** (riches mais peu dépensiers).
