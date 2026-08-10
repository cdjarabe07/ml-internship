# Insight — Task 5 : Système de recommandation de films

## Ce qu'on a cherché à savoir
Peut-on recommander à un utilisateur des films qu'il n'a pas encore vus, en se basant sur ce qu'ont aimé des utilisateurs qui lui ressemblent ?

## Ce qu'on a trouvé
Oui — sur un échantillon d'utilisateurs testés, le système retrouve en moyenne **35 % des films réellement aimés** parmi son top 10 de recommandations (Precision@10 = 0.35), quand on cache volontairement certains de leurs vrais coups de cœur pour vérifier si le modèle les retrouve tout seul.

## Un piège important qu'on a dû corriger en cours de route

La première version du test donnait **0 % de précision** — pas parce que le modèle était mauvais, mais parce que **le test lui-même était mal posé** : on demandait au système de retrouver, parmi des films non-vus, des films... déjà vus. Par définition, l'intersection entre "films jamais vus" et "films déjà vus" est toujours vide, quel que soit le modèle utilisé derrière.

**Leçon à retenir :** un score d'évaluation à 0 (ou à 100 %) doit toujours faire lever un sourcil — c'est souvent le signe d'une erreur dans la façon de mesurer, pas d'un vrai résultat. La bonne méthode : cacher une partie des vrais coups de cœur d'un utilisateur *avant* de faire tourner le modèle, puis vérifier s'il les retrouve.

## Trois approches comparées
- **Basée sur la similarité entre utilisateurs** : trouve des utilisateurs aux goûts proches, recommande ce qu'ils ont aimé
- **Basée sur la similarité entre films** (bonus) : recommande des films similaires à ceux déjà aimés par la personne
- **Factorisation matricielle / SVD** (bonus) : compresse les habitudes de tous les utilisateurs en 20 "tendances" latentes, puis reconstruit des prédictions à partir de ça — ne capture que **39 % de l'information originale** avec cette compression, donc il reste de la marge pour affiner (plus de dimensions latentes)

Les trois méthodes convergent vers des films globalement acclamés (Terminator 2, Le Parrain, Sixième Sens...) — cohérent, ces films ont une bonne note moyenne toutes catégories d'utilisateurs confondues.

## À retenir
Le système fonctionne, mais avec seulement 610 utilisateurs, les groupes de goûts similaires restent petits — plus de données utilisateurs améliorerait probablement la précision. Le point le plus important de cette tâche n'est pas le score en lui-même, mais **la vigilance nécessaire sur la méthode d'évaluation** avant de conclure quoi que ce soit.
