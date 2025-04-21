# ☀️ Simple Weather MCP Server

This is a basic implementation of an MCP (Model Context Protocol) server that retrieves current weather information for a specified location using the WeatherAPI and optionally caches results in a SQLite database.

## Overview

This server listens for POST requests adhering to a simplified MCP structure. When it receives a request with the method `get_weather` and a `location` parameter, it calls the WeatherAPI, fetches the current weather data, optionally caches it, and returns it in a JSON format under the `result` key.

## Prerequisites

- Python 3.7+
- `pip` package installer
- A free or paid API key from [WeatherAPI](https://www.weatherapi.com/).
  > **Note:** The API sometimes does not return the correct results. You can try with some other API too.
- `dotenv` for managing environment variables.
- `aiohttp` for asynchronous HTTP requests.
- `uvicorn` as an ASGI server.
- `fastapi` for building the API.
- `langchain` and `langchain-google-genai` for building the weather agent.
- `sqlite3` for caching purposes. 

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/dev-jatin-mehra/MCPWeather.git
    cd MCPWeather
    ```

2.  **Create a `.env` file in the same directory as `root` dir:**

    ```bash
    WEATHER_API="YOUR_WEATHER_API_KEY"
    WEATHER_API_URL="http://api.weatherapi.com/v1/current.json"
    GEMINI_API="YOUR_GEMINI_API_KEY"
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install python-dotenv aiohttp uvicorn fastapi langchain langchain-google-genai requests
    ```

## Running the Server

1.  Navigate to the `server` directory containing `main.py` in your terminal.
2.  Run the server using Uvicorn:
    ```bash
    python main.py
    ```
    The server will start and listen on `http://localhost:8000`.

## Using the Server (MCP Client Interaction)

To interact with this MCP server, an MCP client (like the provided AI agent or another application) needs to send a POST request to `http://localhost:8000` with a JSON payload in the following format:

> Run the `client/weather_mcpClient.py` OR `agent/weather_mcpAgent.py` to interact with the server.

```json
{
    "method": "get_weather",
    "params": {
        "location": "<city name>, <country/state>"
    }
}
```
## Database Integration and Caching Mechanism

The server incorporates a SQLite database (`weather_cache.db`) to provide an optional caching layer for weather data. This mechanism is designed to optimize performance and reduce the load on the external WeatherAPI.

**Benefits of this Approach:**

* **Efficiency:** Reduces the number of external API calls, conserving API usage and potentially lowering costs.
* **Speed:** Serving data from a local database is significantly faster than fetching it from a remote API.

You can examine the `weather_cache.db` file using the `query_db.py` script in the main project directory to observe the cached data.

> **Note** : Create a file named database.db in the db folder