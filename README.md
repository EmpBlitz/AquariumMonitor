# Aquarium Monitor API

A FastAPI project for simulating aquarium tank readings, storing them in a JSON file, and checking whether a tank is healthy or in alert state.

## Features

- Generate simulated tank readings
- Add your own readings
- Save readings to `data/readings.json`
- View all readings or readings for one tank
- View readings with alerts
- Clear all saved readings

## Project Files

- `main.py` - FastAPI app and API routes
- `simulator.py` - reading generation and health evaluation
- `storage.py` - JSON file storage and filtering
- `data/readings.json` - saved readings

## Requirements

- Python 3
- FastAPI
- Uvicorn

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Run The API

```bash
uvicorn main:app --reload
```

The API will usually run at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Basic

- `GET /` - welcome message

### Readings

- `GET /reading/{tankId}` - create and save one simulated reading
- `GET /generate/{tankId}/{count}` - generate and save multiple simulated readings
- `POST /readings/usr` - create and save a manual reading
- `GET /readings` - get all saved readings
- `GET /readings/{tankId}` - get readings for one tank
- `DELETE /readings/clear` - remove all saved readings

### Alerts

- `GET /alerts` - get all alert readings
- `GET /alerts/{tankId}` - get alert readings for one tank

## Alert Rules

A reading is marked as `ALERT` when tanks:

- temperature is below 24C or above 27C
- pH is below 6.5 or above 7.5
- water level is below 25cm

Otherwise the reading is marked as healthy.

## Data Storage

All readings are stored locally in:

```text
data/readings.json
```
