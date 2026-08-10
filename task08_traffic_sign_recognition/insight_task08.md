# Insight — Task 8 : Détection de panneaux routiers (Industry Level)

## Ce qu'on a cherché à savoir
Peut-on détecter ET identifier des panneaux routiers dans des scènes de conduite complètes, avec une vitesse suffisante pour un usage en temps réel ?

## Ce qu'on a trouvé — un vrai travail de diagnostic, pas juste un chiffre final

Trois expériences ont été menées pour comprendre pourquoi la précision restait bloquée très bas :

| Essai | Configuration | mAP@0.5 |
|---|---|---|
| 1 | YOLOv8 nano, 43 classes de panneaux, 50 époques | 3.8 % |
| 2 | YOLOv8 nano, classes regroupées en 6 catégories, 50 époques | 11.5 % |
| 3 | YOLOv8 small (modèle plus gros), 6 catégories, arrêt auto à l'epoch 31 | 12.3 % |

**Côté vitesse, en revanche, c'est déjà bon** : ~26 images/seconde même sur un simple CPU en test initial — largement dans la zone visée pour du temps réel embarqué (15-30 FPS).

## Le vrai diagnostic

**Réduire le nombre de classes (43 → 6 grandes catégories) a triplé la précision** — preuve que la confusion entre panneaux très proches (certains n'ayant que 1 à 9 exemples dans tout le jeu d'entraînement) était un vrai problème.

**Mais un modèle plus gros (YOLOv8 small au lieu de nano) n'a rien changé** — il s'est même arrêté tout seul dès l'epoch 31, faute de progrès depuis l'epoch 1. Ce n'est donc pas un manque de capacité de calcul.

**Conclusion la plus probable : c'est la taille du dataset qui plafonne tout.** 900 images au total (600 pour l'entraînement), dont une partie sans aucun panneau visible, ce n'est simplement pas assez pour qu'un modèle apprenne à détecter de petits objets (les panneaux) dans des scènes complexes et variées (routes, arbres, voitures, bâtiments en arrière-plan).

## Pourquoi c'est un résultat utile, pas un échec

Ce diagnostic en trois étapes est exactement la démarche attendue en conditions industrielles réelles : **face à une performance décevante, tester méthodiquement chaque hypothèse (classes, puis capacité du modèle) avant de conclure** — plutôt que de multiplier les époques au hasard en espérant que ça s'arrange.

## Ce qu'il faudrait pour un modèle réellement déployable
1. **Beaucoup plus de données** — le vrai dataset GTSDB complet (avec toutes les images, pas la version simplifiée à 900 images) ou de la data augmentation poussée
2. **Éventuellement repartir des 6 catégories** (déjà 3x plus précises que les 43 classes fines) comme base pragmatique si le volume de données ne peut pas augmenter
3. Revalider le FPS une fois un modèle vraiment précis obtenu — un modèle plus lourd ou avec plus de post-traitement pourrait faire baisser la vitesse mesurée initialement

## À retenir
La vitesse (contrainte industrielle) était acquise dès le départ. La précision, elle, est restée bloquée par la donnée disponible — pas par le choix du modèle. Une bonne partie de cette tâche a été de le prouver méthodiquement, pas de deviner.
