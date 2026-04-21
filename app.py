from fastapi import FastAPI
from simulator import readGen
from storage import openReadings, saveReadings, getTankReading, getAlertReadings, getTankAlert

app = FastAPI()
