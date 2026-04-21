#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel
from simulator import readGen, evalReading
from storage import openReadings, saveReadings, getTankReading, getAlertReadings, getTankAlert

app = FastAPI()

# Define Pydantic model for user input
class UsrReading(BaseModel):
    tankId: str
    temperature: float
    ph: float
    waterLevel: float

# Define API endpoints
@app.get("/")
def home():
    return {"message": "Welcome to Aquarium Monitor API"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Endpoint to create a simulated reading for a specific tank
@app.get("/reading/{tankId}")
def createSimulatedReading(tankId: str):
    reading = readGen(tankId)
    saveReadings(reading)
    return reading

# Endpoint to create a reading from user input
@app.post("/readings/usr")
def createReading(reading: UsrReading):
    evalR = evalReading(
        reading.tankId,
        reading.temperature,
        reading.ph,
        reading.waterLevel
    )
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

# Endpoint to simulate multiple readings for a specific tank
@app.get("/simulate/{tankId}/{count}")
def simulate(tankId: str, count: int):
    savedR = []

    for i in range(count):
        reading = readGen(tankId)
        saveReadings(reading)
        savedR.append(reading)

    return {
        "message": f"{count} number of readings was generated for tank {tankId}"}
