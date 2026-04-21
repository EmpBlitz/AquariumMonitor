from fastapi import FastAPI
from pydantic import BaseModel
from simulator import readGen, evalReading
from storage import openReadings, saveReadings, getTankReading, getAlertReadings, getTankAlert

app = FastAPI()

class UsrReading(BaseModel):
    tankId: str
    temperature: float
    ph: float
    waterLevel: float

@app.get("/")
def home():
    return {"message": "Welcome to Aquarium Monitor API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/reading/{tankId}")
def createSimulatedReading(tankId: str):
    reading = readGen(tankId)
    saveReadings(reading)
    return reading


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


@app.get("/readings")
def getAllReadings():
    return openReadings()


@app.get("/readings/{tankId}")
def getReadings(tankId: str):
    return getTankReading(tankId)


@app.get("/alerts")
def getAlerts():
    return getAlertReadings()


@app.get("/alerts/{tankId}")
def getTankAlerts(tankId: str):
    return getTankAlert(tankId)


@app.get("/simulate/{tankId}/{count}")
def simulate(tankId: str, count: int):
    savedR = []

    for i in range(count):
        reading = readGen(tankId)
        saveReadings(reading)
        savedR.append(reading)

    return {
        "message": f"{count} number of readings was generated for tank {tankId}"}
