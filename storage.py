import json
from pathlib import Path

DataFile = Path("data/readings.json")

def openReadings():
    if not DataFile.exists():
        return []
    try:
        with open(DataFile, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def saveReadings(readings):
    readings = openReadings()
    readings.append(readings)

    DataFile.parent.mkdir(exist_ok=True)

    with open(DataFile, "w") as f:
        json.dump(readings, f, indent = 4)

def getTankReading(tankId):
    readings = openReadings()
    tankReadings = []
    for i in readings:
        if i["tankId"] == tankId:
            tankReadings.append(i)
    return tankReadings

def getAlertReadings():
    readings = openReadings()
    alertReadings = []
    for i in readings:
        if i["status"] == "ALERT":
            alertReadings.append(i)
    return alertReadings

def getTankAlert(tankId):
    readings = openReadings()
    tankAlerts = []
    for i in readings:
        if i["tankId"] == tankId and i["status"] == "ALERT":
            tankAlerts.append(i)
    return tankAlerts