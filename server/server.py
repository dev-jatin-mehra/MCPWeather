from fastapi import FastAPI,Request,Response
import json 
from weatherapi import fetch_weather
from model import initialize_db,cache_weather_data,get_cached_weather,is_cache_valid
import aiohttp
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)

app = FastAPI()

@app.on_event("startup")
async def startupEvent():
    initialize_db()

@app.post("/")
async def handle_mcp_request(request:Request):
    try:
        body = await request.json()
        method = body.get("method")
        params = body.get("params",{})

        if method == "get_weather":
            location = params.get("location")
            if location:
                cached_data = get_cached_weather(location)
                if cached_data and is_cache_valid(cached_data['timestamp']):
                    return {
                        "result" : cached_data
                    }
                else:
                    weather_data = await fetch_weather(location=location)
                    cache_weather_data(location,weather_data)
                    return {
                        "result" : weather_data
                    }
            else:
                return {
                    "error" : "Missing 'location' parameter for 'get_weather'"
                }
    except json.JSONDecodeError as e:
        return {
            "error" : f"Error decoding JSON : {e}"
        }
    except aiohttp.ClientError as e:
        return {
            "error" : f"Error fetching weather data : {e}"
            }
    except Exception as e:
        return {
            "error" : f"Unexpected Error Occured : {e}"
        }
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,host='0.0.0.0',port=8000)