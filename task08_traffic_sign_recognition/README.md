# Task 8 — Traffic Sign Recognition (Industry Level)

**Dataset :** GTSDB (Kaggle)
**Contexte :** Détecter de petits panneaux dans un flux vidéo complet, pas des images pré-recadrées.
**Topics :** Détection dobjets | Inférence temps réel | mAP

## Étapes
1. Entraîner un modèle de détection (YOLOv8 ou SSD) sur images complètes
2. Bounding boxes + classification simultanée
3. Évaluer en FPS ET mAP (contrainte industrielle : vitesse dinférence)

## Bonus
- Export ONNX/TFLite + inférence webcam locale
- Filtre par seuil de confiance
