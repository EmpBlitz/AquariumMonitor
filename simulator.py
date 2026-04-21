import random
import datetime

def readGen(tankId):
    
    temperature = round(random.uniform(20.0,30.0), 2)
    ph = round(random.uniform(6.0,8.5), 2)
    waterLevel = round(random.uniform(20.0, 50.0), 2)
    alert = []

    if temperature < 24 or temperature > 27:
        alert.append(f("Temperature out of range: {temperature} C"))

    if ph < 6.5 or ph > 7.5:
        alert.append(f("PH out of range: {ph}"))

    if waterLevel < 25:
        alert.append(f("Low water level: {waterLevel} cm"))

    status = "Healthy" if not alert else "ALERT"

    return {
        "tankId": tankId,
        "timestamp": datetime.datetime.now().isoformat(),
        "temperature": temperature,
        "ph": ph,
        "waterLevel": waterLevel,
        "status": status,
        "alerts": alert
    }