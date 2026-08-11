[🇫🇷 Français](#français) | [🇬🇧 English](#english)

## Français

# Task 10 — End-to-End MLOps Pipeline

**Modèle utilisé :** Random Forest de la [Task 9](../task09_predictive_maintenance) (maintenance prédictive) — ré-entraîné à l'identique et exporté en `.pkl`.

## Structure

```
task10_mlops_pipeline/
├── app/
│   ├── main.py              # API FastAPI
│   ├── model.pkl             # modèle Random Forest exporté (Task 9)
│   ├── type_encoder.pkl      # encodeur de la colonne "Type"
│   ├── static/index.html     # frontend de démo
│   ├── test_api.py           # tests automatisés (8 tests)
│   ├── requirements.txt
│   └── Dockerfile
├── .github/workflows/ci.yml  # CI : tests + build Docker à chaque push
└── train_and_export.py       # script pour régénérer model.pkl si besoin
```

## Lancer en local (sans Docker)

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```
Puis ouvre http://localhost:8000 (frontend de démo) ou http://localhost:8000/docs (doc interactive Swagger).

## Lancer avec Docker

```bash
cd app
docker build -t predictive-maintenance-api .
docker run -p 8000:8000 predictive-maintenance-api
```

✅ Testé et confirmé fonctionnel de bout en bout (build + run + prédiction via le frontend).

## Endpoints

| Méthode | Route | Description |
|---|---|---|
| GET | `/` | Frontend de démo (formulaire) |
| GET | `/health` | Healthcheck |
| POST | `/predict` | Prédiction (voir schéma ci-dessous) |
| GET | `/docs` | Documentation Swagger interactive |

### Schéma d'entrée (`/predict`)
```json
{
  "type": "M",
  "air_temperature": 298.1,
  "process_temperature": 308.6,
  "rotational_speed": 1551,
  "torque": 42.8,
  "tool_wear": 0
}
```
`type` doit être `L`, `M` ou `H` ; les autres champs sont des nombres positifs. Toute donnée invalide (texte dans un champ numérique, type inconnu, champ manquant, valeur négative) est rejetée automatiquement par Pydantic (HTTP 422 — équivalent du 400 Bad Request demandé dans l'énoncé).

## Tests

```bash
cd app
pip install pytest httpx
pytest test_api.py -v
```
8 tests couvrant : réponse valide, cas à risque, et 5 cas de validation (rejets attendus).

## CI/CD
`.github/workflows/ci.yml` lance automatiquement les tests + un build Docker à chaque push touchant ce dossier.

## English

# Task 10 — End-to-End MLOps Pipeline

**Model used:** Random Forest from [Task 9](../task09_predictive_maintenance) (predictive maintenance) — re-trained identically and exported as `.pkl`.

## Structure

```
task10_mlops_pipeline/
├── app/
│   ├── main.py              # API FastAPI
│   ├── model.pkl             # modèle Random Forest exporté (Task 9)
│   ├── type_encoder.pkl      # encodeur de la colonne "Type"
│   ├── static/index.html     # frontend de démo
│   ├── test_api.py           # tests automatisés (8 tests)
│   ├── requirements.txt
│   └── Dockerfile
├── .github/workflows/ci.yml  # CI : tests + build Docker à chaque push
└── train_and_export.py       # script pour régénérer model.pkl si besoin
```

## Run locally (without Docker)

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```
Then open http://localhost:8000 (demo frontend) or http://localhost:8000/docs (interactive Swagger doc).

## Launch with Docker

```bash
cd app
docker build -t predictive-maintenance-api .
docker run -p 8000:8000 predictive-maintenance-api
```

✅ Tested and confirmed functional end-to-end (build + run + prediction via frontend).

## Endpoints

| Method | Road | Description |
|---|---|---|
| GET | `/` | Demo Frontend (Form) |
| GET | `/health` | Healthcheck |
| POST | `/predict` | Prediction (see diagram below) |
| GET | `/docs` | Interactive Swagger Documentation |

### Input schema (`/predict`)
```json
{
  "type": "M",
  "air_temperature": 298.1,
  "process_temperature": 308.6,
  "rotational_speed": 1551,
  "torque": 42.8,
  "tool_wear": 0
}
```
`type` must be `L`, `M` or `H`; the other fields are positive numbers. Any invalid data (text in a numeric field, unknown type, missing field, negative value) is automatically rejected by Pydantic (HTTP 422 — equivalent to the 400 Bad Request requested in the statement).

## Tests

```bash
cd app
pip install pytest httpx
pytest test_api.py -v
```
8 tests covering: valid response, risk cases, and 5 validation cases (expected rejections).

## CI/CD
`.github/workflows/ci.yml` automatically launches tests + a Docker build with each push touching this folder.
