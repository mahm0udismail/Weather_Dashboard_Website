import requests
from config import Config

class WeatherService:
    @staticmethod
    def get_weather_by_coordinates(lat, lon):
        """Fetch weather data using coordinates"""
        try:
            url = f"{Config.OPENWEATHER_BASE_URL}/weather"
            params = {
                'lat': lat,
                'lon': lon,
                'appid': Config.OPENWEATHER_API_KEY,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            return {
                'success': True,
                'data': {
                    'temperature': round(data['main']['temp'], 1),
                    'feels_like': round(data['main']['feels_like'], 1),
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'wind_speed': round(data['wind']['speed'], 1),
                    'wind_deg': data['wind'].get('deg', 0),
                    'description': data['weather'][0]['description'].capitalize(),
                    'main': data['weather'][0]['main'],
                    'icon': data['weather'][0]['icon'],
                    'city': data.get('name'),
                    'country': data['sys'].get('country'),
                    'visibility': data.get('visibility', 0) / 1000,  # Convert to km
                    'clouds': data['clouds']['all']
                }
            }
        except requests.exceptions.HTTPError as e:
            return {'success': False, 'error': 'Failed to fetch weather data'}
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Network error: {str(e)}'}
        except KeyError as e:
            return {'success': False, 'error': 'Invalid response from weather API'}
    
    @staticmethod
    def get_weather_by_city(city_name):
        """Fetch weather data using city name"""
        try:
            url = f"{Config.OPENWEATHER_BASE_URL}/weather"
            params = {
                'q': city_name,
                'appid': Config.OPENWEATHER_API_KEY,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            return WeatherService.get_weather_by_coordinates(
                data['coord']['lat'], 
                data['coord']['lon']
            )
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return {'success': False, 'error': 'City not found'}
            return {'success': False, 'error': 'Failed to fetch weather data'}
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Network error: {str(e)}'}