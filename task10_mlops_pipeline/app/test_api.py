"""
Tests de l'API predictive maintenance.
Lancés automatiquement par GitHub Actions à chaque push (voir .github/workflows/ci.yml).
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_serves_frontend():
    r = client.get("/")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"


def test_predict_valid_input():
    r = client.post("/predict", json={
        "type": "M", "air_temperature": 298.1, "process_temperature": 308.6,
        "rotational_speed": 1551, "torque": 42.8, "tool_wear": 0,
    })
    assert r.status_code == 200
    body = r.json()
    assert "failure_predicted" in body
    assert "failure_probability" in body
    assert 0.0 <= body["failure_probability"] <= 1.0


def test_predict_high_risk_case():
    # valeurs extrêmes connues pour pousser la probabilité de panne à la hausse
    r = client.post("/predict", json={
        "type": "L", "air_temperature": 303, "process_temperature": 312,
        "rotational_speed": 1400, "torque": 65, "tool_wear": 220,
    })
    assert r.status_code == 200
    assert r.json()["risk_level"] in ["élevé", "critique"]


def test_predict_rejects_text_in_numeric_field():
    r = client.post("/predict", json={
        "type": "M", "air_temperature": "chaud", "process_temperature": 308.6,
        "rotational_speed": 1551, "torque": 42.8, "tool_wear": 0,
    })
    assert r.status_code == 422  # validation Pydantic = "400 Bad Request" côté client


def test_predict_rejects_invalid_machine_type():
    r = client.post("/predict", json={
        "type": "X", "air_temperature": 298.1, "process_temperature": 308.6,
        "rotational_speed": 1551, "torque": 42.8, "tool_wear": 0,
    })
    assert r.status_code == 422


def test_predict_rejects_missing_field():
    r = client.post("/predict", json={"type": "M", "air_temperature": 298.1})
    assert r.status_code == 422


def test_predict_rejects_negative_torque():
    r = client.post("/predict", json={
        "type": "M", "air_temperature": 298.1, "process_temperature": 308.6,
        "rotational_speed": 1551, "torque": -10, "tool_wear": 0,
    })
    assert r.status_code == 422
