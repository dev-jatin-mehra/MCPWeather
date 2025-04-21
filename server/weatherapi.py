import aiohttp
from typing import Dict, Any
from config import WEATHER_API,WEATHER_API_URL
import json

async def fetch_weather(location:str)->Dict[str,Any]:
    params = {"q":location ,"key":WEATHER_API,"units":"metric"}
    async with aiohttp.ClientSession() as session:
        async with session.get(WEATHER_API_URL,params=params) as response:
            try:
                response.raise_for_status()
                data = await response.json()
                print(json.dumps(data, indent=2)) # DEBUG LINE
                return {
                    "temperature" : data["current"]["temp_c"],
                    "conditions" : data["current"]["condition"]["text"],
                    "humidity" : data["current"]["humidity"],
                    "wind_speed" : data["current"]["wind_kph"]
                }
            except aiohttp.ClientResponseError as e:
                return {
                    "error":f"Error fetching weather data : {e}"
                }
            except json.JSONDecodeError as e:
                return {
                    "error":f"Error decoding JSON : {e}"
                }
            except Exception as e:
                return {
                    "error" : f"Unexpected Error Occured : {e}"
                }