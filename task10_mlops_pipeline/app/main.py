"""
API de prédiction de panne machine (Task 9 -> Task 10 MLOps).
Wrap le Random Forest entraîné sur AI4I 2020 dans un service FastAPI.
"""
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
import joblib
import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(
    title="Predictive Maintenance API",
    description="Prédit le risque de panne d'une machine industrielle à partir de ses capteurs.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
type_encoder = joblib.load(os.path.join(BASE_DIR, "type_encoder.pkl"))


# --- Schéma d'entrée : Pydantic rejette automatiquement tout type invalide (texte dans un champ numérique, etc.) ---
class MachineType(str, Enum):
    L = "L"
    M = "M"
    H = "H"


class SensorReading(BaseModel):
    type: MachineType = Field(..., description="Type de produit/machine (L, M ou H)")
    air_temperature: float = Field(..., ge=250, le=350, description="Température de l'air en Kelvin")
    process_temperature: float = Field(..., ge=250, le=350, description="Température du process en Kelvin")
    rotational_speed: float = Field(..., gt=0, description="Vitesse de rotation en rpm")
    torque: float = Field(..., ge=0, description="Couple en Nm")
    tool_wear: float = Field(..., ge=0, description="Usure de l'outil en minutes")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "type": "M",
            "air_temperature": 298.1,
            "process_temperature": 308.6,
            "rotational_speed": 1551,
            "torque": 42.8,
            "tool_wear": 0,
        }
    })


class PredictionResponse(BaseModel):
    failure_predicted: bool
    failure_probability: float
    risk_level: str


@app.get("/")
def root():
    return FileResponse(os.path.join(BASE_DIR, "static", "index.html"))


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(reading: SensorReading):
    try:
        type_encoded = type_encoder.transform([reading.type.value])[0]
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Type inconnu : {reading.type}")

    X = pd.DataFrame([{
        "Type": type_encoded,
        "Air temperature": reading.air_temperature,
        "Process temperature": reading.process_temperature,
        "Rotational speed": reading.rotational_speed,
        "Torque": reading.torque,
        "Tool wear": reading.tool_wear,
    }])

    proba = model.predict_proba(X)[0, 1]
    prediction = bool(proba >= 0.5)

    if proba < 0.2:
        risk = "faible"
    elif proba < 0.5:
        risk = "modéré"
    elif proba < 0.8:
        risk = "élevé"
    else:
        risk = "critique"

    return PredictionResponse(
        failure_predicted=prediction,
        failure_probability=round(float(proba), 4),
        risk_level=risk,
    )
