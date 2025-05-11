import os
from dotenv import load_dotenv
import datetime
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

WEATHER_API = os.getenv('WEATHER_API') # importing from .env file
WEATHER_API_URL = os.getenv('WEATHER_API_URL') # importing from .env file
DATABASE_FILE = Path(__file__).resolve().parent / 'db' / 'database.db'
CACHE_EXPIRATION_TIME = datetime.timedelta(minutes=5)