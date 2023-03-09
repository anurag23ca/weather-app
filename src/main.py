from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///weather.db', echo=True)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/api/weather/")
def read_weather_records(date: str = Query(None), station_id: str = Query(None),
                         page: int = Query(1), size: int = Query(10)):
    offset = (page - 1) * size
    query = "SELECT * FROM weather_records"
    filters = []
    if date:
        filters.append(f"Date == '{date}'")
    if station_id:
        filters.append(f"Station_ID== '{station_id}'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    query += f" LIMIT {size} OFFSET {offset}"
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        if not rows:
            raise HTTPException(
                status_code=404, detail="No data found for the specified dates")
        weather_data = []
        for row in rows:
            weather_data.append({
                "station_id": row[5],
                "date": row[1],
                "max_temp": row[2],
                "min_temp": row[3],
                "precipitaion": row[4],

            })
        return weather_data


@app.get("/api/weather/stats")
def read_weather_stats(year: str = Query(None), station_id: str = Query(None),
                       page: int = Query(1), size: int = Query(10)):
    offset = (page - 1) * size
    query = "SELECT * FROM weather_stats"
    filters = []
    if year:
        filters.append(f"Date == '{year}'")
    if station_id:
        filters.append(f"Station_ID== '{station_id}'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    query += f" LIMIT {size} OFFSET {offset}"
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        if not rows:
            raise HTTPException(
                status_code=404, detail="No data found for the specified dates")
        weather_data = []
        for row in rows:
            weather_data.append({
                "station_id": row[1],
                "date": row[2],
                "avg_max_temp": row[3],
                "avg_min_temp": row[4],
                "total_acc_precipitation": row[5]
            })
        return weather_data
