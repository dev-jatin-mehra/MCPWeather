import os
import warnings
from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
import requests

#Supress Langchain deprecation warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

load_dotenv()
GOOGLE_API = os.getenv('GEMINI_API')
MCP_SEVER_URL = "http://localhost:8000"

def get_weather_from_mcp(location:str):
    payload = {
        "method" : "get_weather",
        "params" : {"location" : location},
    }

    headers = {
        "Content-Type" : "application/json",
    }
    try:
        response = requests.post(MCP_SEVER_URL,headers=headers,json=payload) # Structure of the request
        response.raise_for_status() # Error raise 
        data = response.json()
        if "result" in data:
            weather_data = data['result']
            temperature = weather_data.get('temperature')
            condition = weather_data.get('conditions')
            humidity = weather_data.get('humidity')
            wind_speed = weather_data.get('wind_speed')
            return f"The Weather in {location} is {temperature}\u00B0C with {condition}. Humidity is {humidity}% and Wind Speed is predicted to be {wind_speed} kph."
        elif "error" in data:
            return f"Error fetching weather : {data['error']}."
        else:
            return "Could not retrieve weather info."

    except requests.exceptions.RequestException as e:
        return f"Error Connecting to MCP Server : {e}"
    
weather_tool = Tool(
    name = "get_current_weather",
    func = get_weather_from_mcp,
    description = "Useful for getting the current weather in a specific location. Input should be a city name."
)

tools = [weather_tool]

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite',google_api_key = GOOGLE_API)

memory = ConversationBufferMemory(return_messages=True)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)


if __name__ == '__main__':
    print("Welcome to the Weather Chatbot!")
    while(True):
        user_input = input("You :")
        if user_input.lower()=="exit":
            break
        response = agent.invoke({"input":user_input})
        readable_response = response["output"]
        print(f"Bot: {readable_response}")