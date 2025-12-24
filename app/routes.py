from flask import Blueprint, jsonify, request, render_template
from app.services.weather_service import WeatherService
from app.services.location_service import LocationService
from app.utils.helpers import get_wind_direction, get_weather_emoji, get_client_ip, is_private_ip

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@main.route('/api/location', methods=['GET'])
def get_location():
    """Get user location by IP"""
    # Get client IP from request headers
    client_ip = get_client_ip(request)
    
    print(f"[INFO] Client IP detected: {client_ip}")
    
    # Check if it's a private IP
    if is_private_ip(client_ip):
        print("[INFO] Private IP detected, using server's public IP for location")
        # Don't pass the IP, let ip-api detect the server's public IP
        result = LocationService.get_location_by_ip(None)
    else:
        # Use the client's public IP
        print(f"[INFO] Using client's public IP: {client_ip}")
        result = LocationService.get_location_by_ip(client_ip)
    
    if result['success']:
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@main.route('/api/weather', methods=['GET'])
def get_weather():
    """Get weather data by coordinates or city"""
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    city = request.args.get('city')
    
    if lat and lon:
        result = WeatherService.get_weather_by_coordinates(float(lat), float(lon))
    elif city:
        result = WeatherService.get_weather_by_city(city)
    else:
        return jsonify({'success': False, 'error': 'Missing location parameters'}), 400
    
    if result['success']:
        # Add extra info
        result['data']['wind_direction'] = get_wind_direction(result['data']['wind_deg'])
        result['data']['emoji'] = get_weather_emoji(result['data']['main'])
        return jsonify(result), 200
    else:
        return jsonify(result), 400