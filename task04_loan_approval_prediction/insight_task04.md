# Insight — Task 4 : Prédiction d'approbation de prêt

## Ce qu'on a cherché à savoir
Peut-on prédire si une demande de prêt sera acceptée ou refusée, à partir du profil du demandeur (revenus, actifs, historique de crédit...) ?

## Ce qu'on a trouvé
**Oui, et très bien même** — jusqu'à **97 % de bonnes réponses** avec un arbre de décision, largement au-dessus de la régression logistique de base (92 %).

| Approche | Fiabilité sur "Refusé" | Fiabilité sur "Accepté" |
|---|---|---|
| Régression logistique (base) | 90 % | 93 % |
| **Arbre de décision** ✅ | **96 %** | **98 %** |
| Régression logistique + SMOTE | 91 % | 94 % |

## Le facteur qui explique presque tout : le score de crédit (CIBIL)

**Le `cibil_score` (l'équivalent d'un score de crédit) représente à lui seul 86 % du poids de la décision** dans le modèle. Aucun autre facteur n'arrive à la même hauteur — ni le revenu, ni les actifs possédés (immobilier, biens de luxe, actifs bancaires), ni même la durée du prêt.

Concrètement : **le passif financier du demandeur pèse infiniment plus que sa situation actuelle** (combien il gagne, ce qu'il possède). Un bon revenu ne compense presque pas un mauvais score de crédit dans ce dataset.

## Est-ce que rééquilibrer les classes (SMOTE) a aidé ?
Un peu, mais pas de façon spectaculaire — la régression logistique passe de 90 % à 91 % sur la classe minoritaire ("Rejected"). **L'arbre de décision, sans aucun rééquilibrage, fait déjà bien mieux que la régression + SMOTE.** Ici, le choix du modèle a eu plus d'impact que la technique de rééquilibrage.

## À retenir
1. **Le score de crédit est le vrai décideur** — presque tout le reste (revenu, actifs, ancienneté) ne change presque rien à la décision finale.
2. **L'arbre de décision surpasse nettement la régression logistique** sur ce cas — les règles de décision bancaires semblent suivre une logique de seuils (ex: "si score < X, refus"), ce qui colle bien à la façon dont un arbre raisonne, contrairement à une régression linéaire.
