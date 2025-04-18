import requests 
import json 

MCP_SERVER_URL = "https://localhost:8000"

def get_current_location():
    return "Sukha , Uttarakhand"

def ask_for_weather(location:str):
    print("Will Do !")

if __name__=='__main':
    curr_location = get_current_location()
    print(f"My current location is : {curr_location}")
    ask_for_weather()