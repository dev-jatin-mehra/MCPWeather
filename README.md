# 🌤️ Simple Weather MCP Server

This is a basic implementation of an MCP (Model Context Protocol) server that retrieves current weather information for a specified location using the WeatherAPI.

## Overview

This server listens for POST requests adhering to a simplified MCP structure. When it receives a request with the method `get_weather` and a `location` parameter, it calls the WeatherAPI, fetches the current weather data, and returns it in a JSON format under the `result` key.

## Prerequisites

- Python 3.7+
- `pip` package installer
- A free or paid API key from [WeatherAPI](https://www.weatherapi.com/).
> **Note:** The api sometimes does not return the correct results. You can try with some other api too.
- `dotenv` for managing environment variables.
- `aiohttp` for asynchronous HTTP requests.
- `uvicorn` as an ASGI server.
- `fastapi` for building the API.
- `langchain` for building weather agent.

## Setup

1.  **Clone the repository :**

    ```bash
    git clone https://github.com/dev-jatin-mehra/MCPWeather.git
    cd MCPWeather
    ```

2.  **Create a `.env` file in the same directory as `weather_mcpServer.py` :**

    ```bash
    WEATHER_API = "YOUR_WEATHER_API_KEY"
    WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
    GEMINI_API = "YOUR_GEMINI_API_KEY"
    ```

3.  **Install the required Python libraries :**
    ```bash
    pip install python-dotenv aiohttp uvicorn fastapi langchain langchain-google-genai
    ```

## Running the Server

1.  Navigate to the directory containing `weather_MCPSERVER.py` in your terminal.
2.  Run the server using Uvicorn:
    ```bash
    python weather_mcpServer.py
    ```
    The server will start and listen on `http://localhost:8000`.

## Using the Server (MCP Client Interaction)

To interact with this MCP server, an MCP client (like an AI agent or another application) needs to send a POST request to `http://localhost:8000` with a JSON payload in the following format:

> Run the *weather_mcpClient.py* OR *weather_mcpAgent.py* .

```json
{
  "method": "get_weather",
  "params": {
    "location": "City, State" or "location": "City,Country"
  }
}
```