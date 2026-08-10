# Insight — Task 10 : Pipeline MLOps de bout en bout (Industry Level)

## Ce qu'on a cherché à savoir
Un modèle qui fonctionne dans un notebook peut-il devenir un vrai service utilisable par d'autres applications, de façon fiable ?

## Ce qu'on a construit
Le modèle de maintenance prédictive (Task 9) a été transformé en API FastAPI complète : validation stricte des entrées, frontend de démonstration, tests automatisés, et un pipeline CI/CD qui vérifie tout à chaque modification du code.

**8 tests automatisés, tous passés**, couvrant aussi bien les cas valides que les cas volontairement invalides (texte à la place d'un nombre, type de machine inconnu, champ manquant, valeur négative) — tous rejetés proprement par l'API sans jamais atteindre le modèle avec une donnée corrompue.

## Le vrai enseignement de cette tâche : la différence entre "ça marche chez moi" et "c'est déployable"

Un bug concret rencontré en cours de route illustre bien cette différence : le code fonctionnait parfaitement lancé depuis le dossier `app/`, mais **plantait** dès qu'on l'exécutait depuis un autre dossier (ex: `notebooks/`) — parce qu'il cherchait ses fichiers (`static/`, `model.pkl`) par rapport au dossier *depuis lequel on lance la commande*, pas par rapport à l'endroit où se trouve réellement le code.

**C'est exactement le genre de bug invisible en développement local mais qui casse tout en production** (sur un serveur, dans un conteneur Docker, appelé par un autre programme) — corrigé en faisant pointer les chemins vers l'emplacement du fichier lui-même, peu importe d'où l'API est lancée.

## Docker confirmé fonctionnel de bout en bout
Le build (`docker build`) et le lancement du conteneur (`docker run`) ont été testés avec succès en conditions réelles — frontend accessible sur `localhost:8000`, prédiction correcte affichée. Le pipeline complet (entraînement → export → API → validation → conteneur) fonctionne intégralement, pas seulement sur le papier.

## À retenir
1. **La validation des entrées n'est pas une option** — sans elle, une donnée malformée provoquerait un plantage serveur au lieu d'une erreur propre et compréhensible pour qui appelle l'API.
2. **Les chemins de fichiers relatifs sont un piège classique** entre "ça marche sur ma machine" et "ça marche déployé" — un réflexe à vérifier systématiquement avant de considérer un service prêt pour la production.
3. **Le CI/CD automatise la vigilance** : plutôt que de se souvenir de retester manuellement à chaque changement, GitHub Actions le fait à chaque push, sans exception possible par oubli.
