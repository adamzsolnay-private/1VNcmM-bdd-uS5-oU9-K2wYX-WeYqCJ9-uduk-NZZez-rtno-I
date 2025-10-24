from typing import Callable, Annotated
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, AfterValidator
from datetime import datetime
from pathlib import Path
import db_ops

# Create the sqlite DB if it doesn't exist
if Path("weather.db").exists() == False:
    db_ops.create_db()

app = FastAPI()

# Normalize metrics to 2 decimal points
# Workaround for this issue: https://github.com/pydantic/pydantic/issues/8903
def round_float(round_to: int) -> Callable:
    def inner_round(v: float):
        return round(v, round_to)
    return inner_round

class WeatherMetrics(BaseModel):
    sensor_id: int
    temperature: Annotated[float, AfterValidator(round_float(2))]
    humidity:    Annotated[float, AfterValidator(round_float(2))]
    wind_speed:  Annotated[float, AfterValidator(round_float(2))]

@app.post('/api/weather_metrics', status_code=201)
def record_metrics(metrics: WeatherMetrics):
    res = db_ops.insert_values(
            timestamp=str(datetime.utcnow()),
            sensor_id=metrics.sensor_id,
            temperature=metrics.temperature,
            humidity=metrics.humidity,
            wind_speed=metrics.wind_speed
            )
    if res != "201":
        raise HTTPException(status_code=400, detail="400 Bad Request")
    else:
        return {"detail": "201 Created"}

# TODO - missing
#1 Design, test and implement querying.
### date range filter logic: datetime.utcnow()-timedelta(days=x)

# TODO - enhancement
#2 Implement ORM against SQL Injections
#3 Secure connection betw client-API and API-DB
#3 Implement Authentication for both GETs and POSTs
#4 Implement solution for non-SI units (ex: Fahrenheit)
#5 Document schemas
