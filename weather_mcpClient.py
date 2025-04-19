import requests 

MCP_SERVER_URL = "http://localhost:8000"

def get_current_location():
    return input("Enter Your location :")

def ask_for_weather(location:str):
    payload = {
        "method" : "get_weather",
        "params" : {"location":location},
    }
    headers = {"Content-Type":"application/json"}
    try:
        response = requests.post(MCP_SERVER_URL,headers=headers,json=payload)
        response.raise_for_status()
        data = response.json()
        if "result" in data:
            weather_data = data["result"]
            print(f"Current Weather in the location {location} is :")
            print(f"Temperature : {weather_data.get('temperature')} Celsius")
            print(f"Conditions : {weather_data.get('conditions')}")
            print(f"Humidity : {weather_data.get('humidity')}%")
            print(f"Wind Speed : {weather_data.get('wind_speed')} kph")
        elif "error" in data:
            print(f"Error : {data['error']}")
        else:
            print(f"Unexpected Response : {data}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to MCP Server : {e}")

if __name__=='__main__':
    curr_location = get_current_location()
    print(f"My current location is : {curr_location}")
    ask_for_weather(curr_location)