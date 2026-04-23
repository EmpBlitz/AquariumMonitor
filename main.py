#!/usr/bin/env python3

from fastapi import FastAPI
from simulator import readGen, evalReading
from storage import openReadings, saveReadings, getTankReading, getAlertReadings, getTankAlert, clearReadings

app = FastAPI()


# Define API endpoints
@app.get("/")
def home():
    return {"message": "Welcome to Aquarium Monitor API"}

# Endpoint to generate a simulated reading for a single specific tank
@app.get("/reading/{tankId}")
def createSimulatedReading(tankId: str):
    reading = readGen(tankId)
    saveReadings(reading)
    return reading

# Endpoint to generate multiple readings for a specific tank
@app.get("/generate/{tankId}/{count}")
def simulate(tankId: str, count: int):
    savedR = []

    for i in range(count):
        reading = readGen(tankId)
        saveReadings(reading)
        savedR.append(reading)

    return {
        "message": f"{count} number of readings was generated for tank {tankId}",
        "readingsSaved": savedR
    }

# Endpoint to create a reading from user input
@app.post("/readings/usr")
def createReading(
    tankId: str,
    temperature: float,
    ph: float,
    waterLevel: float
):
    evalR = evalReading(tankId, temperature, ph, waterLevel)
    saveReadings(evalR)
    return evalR

# Additional endpoints to retrieve readings and alerts
@app.get("/readings")
def getAllReadings():
    return openReadings()

# Endpoint to retrieve readings for a specific tank
@app.get("/readings/{tankId}")
def getReadings(tankId: str):
    return getTankReading(tankId)

# Endpoint to retrieve all alert readings
@app.get("/alerts")
def getAlerts():
    return getAlertReadings()

# Endpoint to retrieve alert readings for a specific tank
@app.get("/alerts/{tankId}")
def getTankAlerts(tankId: str):
    return getTankAlert(tankId)


# Endpoint to clear all readings from the data file
@app.delete("/readings/clear")
def clear_all_readings():
    clearReadings()
    return {"message": "All readings cleared."}