def get_wind_direction(degrees):
    """Convert wind direction from degrees to cardinal direction"""
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                  'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    index = round(degrees / 22.5) % 16
    return directions[index]

def get_weather_emoji(weather_main):
    """Get emoji based on weather condition"""
    weather_emojis = {
        'Clear': '☀️',
        'Clouds': '☁️',
        'Rain': '🌧️',
        'Drizzle': '🌦️',
        'Thunderstorm': '⛈️',
        'Snow': '❄️',
        'Mist': '🌫️',
        'Fog': '🌫️',
        'Haze': '🌫️'
    }
    return weather_emojis.get(weather_main, '🌤️')

def get_client_ip(request):
    """Extract client's real IP address from Flask request object
    
    This function checks multiple headers to find the real client IP,
    especially important when behind proxies, load balancers, or CDNs.
    
    Priority order:
    1. X-Forwarded-For (most common for proxies)
    2. X-Real-IP (nginx)
    3. CF-Connecting-IP (Cloudflare)
    4. True-Client-IP (Akamai, Cloudflare)
    5. request.remote_addr (direct connection)
    """
    # X-Forwarded-For can contain multiple IPs: "client, proxy1, proxy2"
    # We want the first one (the original client)
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
        return ip
    
    # X-Real-IP is commonly set by nginx
    if request.headers.get('X-Real-IP'):
        return request.headers.get('X-Real-IP').strip()
    
    # Cloudflare specific header
    if request.headers.get('CF-Connecting-IP'):
        return request.headers.get('CF-Connecting-IP').strip()
    
    # Akamai and Cloudflare also use this
    if request.headers.get('True-Client-IP'):
        return request.headers.get('True-Client-IP').strip()
    
    # Fallback to remote_addr (direct connection)
    return request.remote_addr

def is_private_ip(ip):
    """Check if an IP address is private/local"""
    if not ip:
        return True
    
    # Check for localhost
    if ip.startswith('127.') or ip == 'localhost':
        return True
    
    # Check for private IP ranges
    private_ranges = [
        '10.',
        '172.16.', '172.17.', '172.18.', '172.19.',
        '172.20.', '172.21.', '172.22.', '172.23.',
        '172.24.', '172.25.', '172.26.', '172.27.',
        '172.28.', '172.29.', '172.30.', '172.31.',
        '192.168.'
    ]
    
    for private_range in private_ranges:
        if ip.startswith(private_range):
            return True
    
    return False