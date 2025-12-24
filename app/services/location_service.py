import requests
from config import Config

class LocationService:
    @staticmethod
    def get_location_by_ip(ip_address=None):
        """Get user location based on IP address
        
        Args:
            ip_address: Optional IP address. If None, ip-api will detect the public IP automatically
        """
        try:
            # If IP is provided, use it; otherwise, ip-api will use the server's public IP
            url = Config.IPAPI_BASE_URL
            if ip_address:
                url = f"{Config.IPAPI_BASE_URL}/{ip_address}"
            
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            # Check if the response is successful
            if data.get('status') == 'success':
                return {
                    'success': True,
                    'city': data.get('city'),
                    'country': data.get('country'),
                    'lat': data.get('lat'),
                    'lon': data.get('lon')
                }
            elif data.get('status') == 'fail':
                # IP-API returns 'fail' status for private/reserved IPs
                error_msg = data.get('message', 'Cannot detect location from private IP')
                return {
                    'success': False, 
                    'error': f'{error_msg}. Please enter your city manually.'
                }
            else:
                return {'success': False, 'error': 'Could not detect location'}
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Network error: {str(e)}'}
        except Exception as e:
            return {'success': False, 'error': f'Unexpected error: {str(e)}'}
    
    @staticmethod
    def get_coordinates_by_city(city_name):
        """Get coordinates for a given city name"""
        try:
            url = f"{Config.OPENWEATHER_BASE_URL}/weather"
            params = {
                'q': city_name,
                'appid': Config.OPENWEATHER_API_KEY
            }
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            return {
                'success': True,
                'city': data.get('name'),
                'country': data['sys'].get('country'),
                'lat': data['coord'].get('lat'),
                'lon': data['coord'].get('lon')
            }
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return {'success': False, 'error': 'City not found'}
            return {'success': False, 'error': 'Failed to fetch city data'}
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Network error: {str(e)}'}