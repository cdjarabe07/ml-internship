[🇫🇷 Français](#français) | [🇬🇧 English](#english)

## Français

# ML Internship — 10 Tasks (1 mois)

Environnement de travail pour le stage ML : Level 1 → Industry Level.

## Structure

Chaque tâche a son propre dossier, indépendant :

```
taskXX_nom/
├── data/         # datasets (non versionnés, voir .gitignore)
├── notebooks/     # exploration, prototypage
├── src/           # code réutilisable (.py)
└── outputs/       # modèles sauvegardés, figures, résultats
```

## Roadmap (1 mois, 10 tâches) — ✅ terminé

| Semaine | Tâches | Focus |
|---|---|---|
| 1 | Task 1, 2 | Régression, clustering — bases |
| 2 | Task 3, 4, 5 | Classification multi-classe, données déséquilibrées, reco |
| 3 | Task 6, 7 | Audio/CNN, séries temporelles |
| 4 | Task 8, 9, 10 | Détection d'objets, maintenance prédictive, MLOps |

Les 10 tâches ont été complétées, avec au moins un bonus réalisé sur chacune.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Liste des tâches

| # | Tâche | Niveau | Statut | Résultat clé |
|---|---|---|---|---|
| 1 | [Student Score Prediction](./task01_student_score_prediction) | Level 1 | ✅ | Le tutorat pèse plus que les heures d'étude (R²=0.27) |
| 2 | [Customer Segmentation](./task02_customer_segmentation) | Level 1 | ✅ | 5 segments clients, dont un fort potentiel inexploité |
| 3 | [Forest Cover Classification](./task03_forest_cover_classification) | Level 2 | ✅ | 88% accuracy — l'altitude domine tout |
| 4 | [Loan Approval Prediction](./task04_loan_approval_prediction) | Level 2 | ✅ | 97% accuracy — le score de crédit pèse 86% |
| 5 | [Movie Recommendation System](./task05_movie_recommendation) | Level 2 | ✅ | Precision@10 = 0.35 (après correction d'un piège de méthode) |
| 6 | [Music Genre Classification](./task06_music_genre_classification) | Level 3 | ✅ | 87% accuracy — aucune feature ne domine |
| 7 | [Sales Forecasting](./task07_sales_forecasting) | Level 3 | ✅ | R²=98.8% — la saisonnalité prime sur l'économie |
| 8 | [Traffic Sign Recognition](./task08_traffic_sign_recognition) | Industry | ✅ | FPS ok (26), précision limitée par la taille du dataset |
| 9 | [Predictive Maintenance](./task09_predictive_maintenance) | Industry | ✅ | Compromis FDR/Recall — le couple est le meilleur indicateur |
| 10 | [MLOps Pipeline](./task10_mlops_pipeline) | Industry | ✅ | API + Docker + CI/CD validés de bout en bout |

Chaque dossier contient un `README.md` (contexte technique) et un `INSIGHT.md` (analyse en langage simple, une page).

## English

# ML Internship — 10 Tasks (1 month)

Working environment for the ML internship: Level 1 → Industry Level.

## Structure

Each task has its own, independent folder:

```
taskXX_nom/
├── data/         # datasets (non versionnés, voir .gitignore)
├── notebooks/     # exploration, prototypage
├── src/           # code réutilisable (.py)
└── outputs/       # modèles sauvegardés, figures, résultats
```

## Roadmap (1 month, 10 tasks) — ✅ completed

| Week | Tasks | Focus |
|---|---|---|
| 1 | Task 1, 2 | Regression, clustering — basics |
| 2 | Task 3, 4, 5 | Multi-class classification, imbalanced data, recce |
| 3 | Task 6, 7 | Audio/CNN, time series |
| 4 | Task 8, 9, 10 | Object detection, predictive maintenance, MLOps |

All 10 tasks have been completed, with at least one bonus achieved on each.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Task List

| # | Task | Level | Status | Key result |
|---|---|---|---|---|
| 1 | [Student Score Prediction](./task01_student_score_prediction) | Level 1 | ✅ | Tutoring weighs more than study hours (R²=0.27) |
| 2 | [Customer Segmentation](./task02_customer_segmentation) | Level 1 | ✅ | 5 customer segments, including strong untapped potential |
| 3 | [Forest Cover Classification](./task03_forest_cover_classification) | Level 2 | ✅ | 88% accuracy — altitude dominates everything |
| 4 | [Loan Approval Prediction](./task04_loan_approval_prediction) | Level 2 | ✅ | 97% accuracy — credit score weighs 86% |
| 5 | [Movie Recommendation System](./task05_movie_recommendation) | Level 2 | ✅ | Precision@10 = 0.35 (after fixing a method trap) |
| 6 | [Music Genre Classification](./task06_music_genre_classification) | Level 3 | ✅ | 87% accuracy — no feature dominates |
| 7 | [Sales Forecasting](./task07_sales_forecasting) | Level 3 | ✅ | R²=98.8% — seasonality takes precedence over the economy |
| 8 | [Traffic Sign Recognition](./task08_traffic_sign_recognition) | Industry | ✅ | FPS ok (26), precision limited by the size of the dataset |
| 9 | [Predictive Maintenance](./task09_predictive_maintenance) | Industry | ✅ | FDR/Recall trade-off — torque is the best indicator |
| 10 | [MLOps Pipeline](./task10_mlops_pipeline) | Industry | ✅ | End-to-end validated API + Docker + CI/CD |

Each folder contains a `README.md` (technical background) and an `INSIGHT.md` (plain language analysis, one page).
