import os 
from dotenv import load_dotenv
import json
from typing import Dict, Any
import aiohttp
from fastapi import FastAPI, Request, Response

load_dotenv()
WEATHER_API = os.getenv('WEATHER_API') # importing from .env file
WEATHER_API_URL = os.getenv('WEATHER_API_URL') # importing from .env file

app = FastAPI()

async def fetch_weather(location:str) ->Dict[str,Any]:
    params = {"q":location,"key":WEATHER_API,"units":"metric"}
    async with aiohttp.ClientSession() as session:
        async with session.get(WEATHER_API_URL,params=params) as response:
            try:
                response.raise_for_status()
                data = await response.json()
                return {
                    "temperature" : data["current"]["temp_c"],
                    "conditions" : data["current"]["condition"]["text"],
                    "humidity" : data["current"]["humidity"],
                    "wind_speed" : data["current"]["wind_kph"]
                }
            except aiohttp.ClientResponseError as e:
                return {"error": f"Error fetching weather data: {e.status}, {e.message}"}
            except json.JSONDecodeError as e:
                return {"error": f"Error decoding JSON response: {e}"}
            except Exception as e:
                return {"error": f"An unexpected error occurred: {e}"}
        

@app.post("/")
async def handle_mcp_request(request:Request):
    try:
        body = await request.json()
        method = body.get("method")
        params = body.get("params",{})

        if method == "get_weather":
            location = params.get("location")
            if location:
                weather_data = await fetch_weather(location)
                return {"result" : weather_data}
            else:
                return {"error": "Missing 'location' parameter for 'get_weather"}
        
        else:
            return {"error": f"Unknown Method: {method}"}
        
    except json.JSONDecodeError:
        return {"error":"Invalid JSON Payload"}
    except aiohttp.ClientError as e:
        return {"error":f"Error Fetching weather data  : {e}"}
    except Exception as e:
        return {"error":f"An unexpected error occured : {e}"}
    
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port=8000)
    
