from fastapi import FastAPI
from simulator import readGen
from storage import saveReadings, openReadings

app = FastAPI()
