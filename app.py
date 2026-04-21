from fastapi import FastAPI
from pydantic import BaseModel
from simulator import readGen
from storage import openReadings, saveReadings, getTankReading, getAlertReadings, getTankAlert

app = FastAPI()

class UsrReading(BaseModel):
    tankId = str
    temperature = float
    ph = float
    waterLevel = float
