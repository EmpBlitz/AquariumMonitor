import json
from pathlib import Path

DataFile = Path("data/readings.json")

# Functions to handle reading storage and retrieval
def openReadings():
    if not DataFile.exists():
        return []
    try:
        with open(DataFile, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Function to save a new reading to the data file
def saveReadings(newReading):
    allReadings = openReadings()
    allReadings.append(newReading)

    DataFile.parent.mkdir(exist_ok=True)

    with open(DataFile, "w") as f:
        json.dump(allReadings, f, indent = 4)

# Functions to filter readings based on tank ID and alert status
def getTankReading(tankId):
    readings = openReadings()
    tankReadings = []
    for i in readings:
        if i["tankId"] == tankId:
            tankReadings.append(i)
    return tankReadings

# Function to filter readings that have an alert status
def getAlertReadings():
    readings = openReadings()
    alertReadings = []
    for i in readings:
        if i["status"] == "ALERT":
            alertReadings.append(i)
    return alertReadings

# Function to filter alert readings for a specific tank
def getTankAlert(tankId):
    readings = openReadings()
    tankAlerts = []
    for i in readings:
        if i["tankId"] == tankId and i["status"] == "ALERT":
            tankAlerts.append(i)
    return tankAlerts