from pathlib import Path
from fastapi.testclient import TestClient
from main import app
import storage

client = TestClient(app)

originalFile = storage.DataFile
testFile = Path("data/test_readings.json")


def setup_function():
    storage.DataFile = testFile
    storage.clearReadings()

def teardown_function():
    if testFile.exists():
        testFile.unlink()
    storage.DataFile = originalFile



def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Aquarium Monitor API"}

def test_create_simulated_reading():
    response = client.get("/reading/TANK1")
    assert response.status_code == 200

    body = response.json()
    assert body["tankId"] == "TANK1"
    assert "temperature" in body
    assert "ph" in body
    assert "waterLevel" in body
    assert "alerts" in body
    assert "status" in body
    saved = storage.openReadings()
    assert len(saved) == 1

def test_create_manual_reading():
    response = client.post(
        "/readings/usr",
        params={
            "tankId": "TANK2",
            "temperature": 29.0,
            "ph": 8.0,
            "waterLevel": 22.0
        }
    )
    assert response.status_code == 200
    assert response.json()["tankId"] == "TANK2"
    assert response.json()["temperature"] == 29.0
    assert response.json()["ph"] == 8.0
    assert response.json()["waterLevel"] == 22.0
    assert response.json()["status"] == "ALERT"
    assert "alerts" in response.json()

def test_get_all_readings():
    client.get("/reading/TANK1")
    client.get("/reading/TANK2")

    response = client.get("/readings")
    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 2

def test_generate_multiple_readings():
    response = client.get("/generate/TANK3/3")
    assert response.status_code == 200

    body = response.json()
    assert "message" in body
    assert "readingsSaved" in body
    assert len(body["readingsSaved"]) == 3

    saved = storage.openReadings()
    assert len(saved) == 3

def test_get_alert_readings():
    client.post(
        "/readings/usr",
        params={
            "tankId": "TANK1",
            "temperature": 29.0,
            "ph": 8.0,
            "waterLevel": 22.0
        }
    )

    client.post(
        "/readings/usr",
        params={
            "tankId": "TANK2",
            "temperature": 25.0,
            "ph": 7.0,
            "waterLevel": 30.0
        }
    )

    response = client.get("/alerts")
    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 1
    assert body[0]["tankId"] == "TANK1"
    assert body[0]["status"] == "ALERT"

def test_get_tank_alerts():
    client.post(
        "/readings/usr",
        params={
            "tankId": "TANK5",
            "temperature": 29.0,
            "ph": 8.0,
            "waterLevel": 22.0
        }
    )

    client.post(
        "/readings/usr",
        params={
            "tankId": "TANK5",
            "temperature": 25.0,
            "ph": 7.0,
            "waterLevel": 30.0
        }
    )

    response = client.get("/alerts/TANK5")
    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 1
    assert body[0]["tankId"] == "TANK5"
    assert body[0]["status"] == "ALERT"

def test_clear_readings():
    client.get("/reading/TANK1")
    client.get("/reading/TANK2")

    response = client.delete("/readings/clear")
    assert response.status_code == 200
    assert response.json() == {"message": "All readings cleared."}

    saved = storage.openReadings()
    assert saved == []


#Invalid test
def test_create_manual_reading_missing_fields():
    response = client.post(
        "/readings/usr",
        params={
            "tankId": "TANK1",
            "temperature": 25.0
        }
    )
    assert response.status_code == 422