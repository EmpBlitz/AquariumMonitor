import json
from pathlib import Path

DataFile = Path("data/readings.json")

if DataFile.exists():
    with open(DataFile, "r") as f:
        json.dump([], f, indent = 4)


def openReadings():
    if not DataFile.exists():
        return []
    with open(DataFile, "r") as f:
        return json.load(f)
    
def saveReadings(readings):
    readings = openReadings()
    readings.append(readings)
    with open(DataFile, "w") as f:
        json.dump(readings, f, indent = 4)