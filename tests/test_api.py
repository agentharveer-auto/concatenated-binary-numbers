from fastapi.testclient import TestClient
from concatenated_binary.api import app

client = TestClient(app)


def test_api_basic():
    resp = client.post("/calculate", json={"n": 3})
    assert resp.status_code == 200
    data = resp.json()
    assert data["n"] == 3
    assert data["result"] == 27


def test_api_invalid():
    resp = client.post("/calculate", json={"n": 0})
    assert resp.status_code == 400
