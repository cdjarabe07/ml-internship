# Insight — Task 1 : Prédiction du score d'examen

## Ce qu'on a cherché à savoir
Est-ce que le nombre d'heures d'étude permet de prédire le score final d'un étudiant à l'examen ?

## Ce qu'on a trouvé

**Oui, mais seulement en partie.** Il y a bien un lien entre les deux (corrélation de 0.44 sur 1), mais les heures d'étude à elles seules n'expliquent qu'environ **23 % de la variation des scores** (R² = 0.23). Concrètement : à chaque heure d'étude en plus, le score augmente en moyenne de **+0.29 point**.

Autrement dit, étudier aide clairement, mais **ce n'est pas le facteur qui fait toute la différence.**

## Ce qui compte le plus, en réalité

En ajoutant d'autres informations disponibles dans les données (sommeil, tutorat, activité physique, score précédent), le modèle s'améliore un peu (R² = 0.27). Et surprise : ce n'est pas le score précédent qui pèse le plus, mais **le nombre de séances de tutorat** — c'est le facteur avec le plus gros impact positif sur le score final, plus important même que les heures d'étude.

Le sommeil, lui, a un effet légèrement négatif — mais l'effet est faible, pas de conclusion hâtive à en tirer.

## Marge d'erreur du modèle
Le modèle se trompe en moyenne de **±2.3 à 2.4 points** sur le score prédit. Pour un score qui tourne autour de 67/100 en moyenne, c'est une erreur raisonnable mais pas négligeable.

## À retenir
Les heures d'étude sont un bon point de départ, mais un modèle plus complet (avec tutorat, sommeil, etc.) donne une prédiction plus fiable. Le vrai levier à creuser : **le tutorat**, dont l'effet dépasse celui du simple temps d'étude.
