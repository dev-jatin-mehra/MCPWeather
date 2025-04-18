# Simple Weather MCP Server

This is a basic implementation of an MCP (Model Context Protocol) server that retrieves current weather information for a specified location using the WeatherAPI.

## Overview

This server listens for POST requests adhering to a simplified MCP structure. When it receives a request with the method `get_weather` and a `location` parameter, it calls the WeatherAPI, fetches the current weather data, and returns it in a JSON format under the `result` key.

## Prerequisites

* Python 3.7+
* `pip` package installer
* A free or paid API key from [WeatherAPI](https://www.weatherapi.com/).
* `dotenv` for managing environment variables.
* `aiohttp` for asynchronous HTTP requests.
* `uvicorn` as an ASGI server.
* `fastapi` for building the API.

## Setup

1.  **Clone the repository (if you have one, otherwise just create the files):**
    ```bash
    # If you have a repo:
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

2.  **Create a `.env` file in the same directory as `weather_MCPSERVER.py`:**
    ```
    WEATHER_API="YOUR_WEATHER_API_KEY"
    WEATHER_API_URL="[http://api.weatherapi.com/v1/current.json](http://api.weatherapi.com/v1/current.json)"
    ```
    Replace `"YOUR_WEATHER_API_KEY"` with your actual WeatherAPI key.

3.  **Install the required Python libraries:**
    ```bash
    pip install python-dotenv aiohttp uvicorn fastapi
    ```

## Running the Server

1.  Navigate to the directory containing `weather_MCPSERVER.py` in your terminal.
2.  Run the server using Uvicorn:
    ```bash
    python weather_MCPSERVER.py
    ```
    The server will start and listen on `http://localhost:8000`.

## Using the Server (MCP Client Interaction)

To interact with this MCP server, an MCP client (like an AI agent or another application) needs to send a POST request to `http://localhost:8000` with a JSON payload in the following format:

```json
{
  "method": "get_weather",
  "params": {
    "location": "City, Country Code (optional)"
  }
}