import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
    OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5'
    IPAPI_BASE_URL = 'http://ip-api.com/json'