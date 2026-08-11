[🇫🇷 Français](#français) | [🇬🇧 English](#english)

## Français

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

## English

# Task 8 — Traffic Sign Recognition (Industry Level)

**Dataset:** GTSDB (Kaggle)
**Background:** Detect small panels in a full video stream, not pre-cropped frames.
**Topics:** Object detection | Real-time inference | mAP

## Steps
1. Train a detection model (YOLOv8 or SSD) on full images
2. Bounding boxes + simultaneous classification
3. Evaluate in FPS AND mAP (industrial constraint: inference speed)

## Bonuses
- ONNX/TFLite export + local webcam inference
- Filter by confidence threshold
