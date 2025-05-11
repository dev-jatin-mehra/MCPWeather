import sqlite3
import datetime
from config import DATABASE_FILE,CACHE_EXPIRATION_TIME
from typing import Dict,Any,Optional

def initialize_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data(
                   location TEXT PRIMARY KEY,
                   temperature REAL,
                   conditions TEXT,
                   humidity INTEGER,
                   wind_speed REAL,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                   )"""
    )

    conn.commit()
    conn.close()

def get_cached_weather(location:str)->Optional[Dict[str,Any]]:
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT temperature,conditions,humidity,wind_speed from weather_data WHERE location=?",(location,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "temperature" : row[0],
            "conditions" : row[1],
            "humidity" : row[2],
            "windspeed" : row[3],
            "timestamp" : row[4],
        }
    return None


def cache_weather_data(location:str,weather_data:Dict[str,Any]):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT OR REPLACE INTO 
                       weather_data (location,temperature,conditions,humidity,wind_speed)
                       VALUES (?,?,?,?,?)
                       """
                       ,(location,weather_data.get("temperature"),weather_data.get("conditions"),weather_data.get("humidity"),weather_data.get("wind_speed")),
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error while caching : {e}")
    finally:
        conn.close()

def is_cache_valid(timestamp_str:str)->bool:
    timestamp = datetime.datetime.fromisoformat(timestamp_str)
    now = datetime.datetime.now()
    return now - timestamp < CACHE_EXPIRATION_TIME