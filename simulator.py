import random
from datetime import datetime

# Simulate sensor readings and evaluate them against thresholds
def evalReading(tankId, temperature, ph, waterLevel):
    alert = []

    if temperature < 24 or temperature > 27:
        alert.append(f"Temperature out of range: {temperature} C")

    if ph < 6.5 or ph > 7.5:
        alert.append(f"PH out of range: {ph}")

    if waterLevel < 25:
        alert.append(f"Low water level: {waterLevel} cm")

    if alert:
        status = "ALERT"
    else:
        status = "Healthy"
        alert.append("All indicators are normal")

    return {
        "tankId": tankId,
        "timestamp": datetime.now().isoformat(),
        "temperature": temperature,
        "ph": ph,
        "waterLevel": waterLevel,
        "status": status,
        "alerts": alert
    }
# Function to generate random readings for a specific tank
def readGen(tankId):
    
    temperature = round(random.uniform(20.0,30.0), 2)
    ph = round(random.uniform(6.0,8.5), 2)
    waterLevel = round(random.uniform(20.0, 50.0), 2)
    return evalReading(tankId, temperature, ph, waterLevel)