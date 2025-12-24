# 🌤️ Weather Dashboard Website

A modern, responsive weather dashboard that automatically detects your location and displays real-time weather information. Built with Flask (Python) backend and vanilla JavaScript frontend.

## ✨ Features

- 🌍 **Auto Location Detection** - Automatically detects user location via client IP address
- 🔍 **Manual City Search** - Search weather for any city worldwide
- 🌡️ **Comprehensive Weather Data** - Temperature, humidity, wind speed, visibility, and more
- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- ⚡ **Real-time Data** - Fetches current weather from OpenWeatherMap API
- 🛡️ **Error Handling** - Graceful error messages for network issues and invalid inputs
- 🔒 **Smart IP Detection** - Handles both public and private IP addresses intelligently

## 📋 Requirements

- Python 3.7+
- OpenWeatherMap API Key (free)
- Modern web browser
- Internet connection

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Weather_Dashboard_Website
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get OpenWeatherMap API Key

1. Go to [OpenWeatherMap Sign Up](https://home.openweathermap.org/users/sign_up)
2. Create a free account
3. Verify your email
4. Navigate to [API Keys](https://home.openweathermap.org/api_keys)
5. Copy your API key

### 5. Configure Environment Variables

```bash
# Create .env file from example
cp .env.example .env

# Edit .env file
nano .env
```

Add your credentials:
```env
SECRET_KEY=your_generated_secret_key_here
OPENWEATHER_API_KEY=your_actual_api_key_here
```

**Generate a secure SECRET_KEY:**
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### 6. Run the Application

```bash
python app.py
```

The application will start on:
- **Local access**: `http://localhost:5000` or `http://127.0.0.1:5000`
- **Network access**: `http://192.168.x.x:5000` (your local IP)

Open your browser and navigate to one of the above URLs.

## 📁 Project Structure

```
Weather_Dashboard_Website/
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── routes.py             # API routes and endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── location_service.py   # IP-based location detection
│   │   └── weather_service.py    # Weather data fetching
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py        # Helper functions (IP detection, conversions)
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css     # Styling
│   │   └── js/
│   │       └── main.js       # Frontend logic
│   └── templates/
│       └── index.html        # Main HTML template
├── venv/                     # Virtual environment (not in git)
├── app.py                    # Application entry point
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not in git)
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🔌 API Endpoints

### 1. Get Location by IP
```
GET /api/location
```
**Description**: Automatically detects user location based on their IP address. Handles both public and private IPs.

**Response:**
```json
{
  "success": true,
  "city": "Cairo",
  "country": "Egypt",
  "lat": 30.0507,
  "lon": 31.2489
}
```

### 2. Get Weather by Coordinates
```
GET /api/weather?lat=30.0507&lon=31.2489
```
**Description**: Fetches weather data for specific coordinates.

### 3. Get Weather by City Name
```
GET /api/weather?city=London
```
**Description**: Fetches weather data for a specific city.

**Response:**
```json
{
  "success": true,
  "data": {
    "temperature": 25.5,
    "feels_like": 24.3,
    "humidity": 65,
    "pressure": 1013,
    "wind_speed": 5.2,
    "wind_deg": 180,
    "wind_direction": "S",
    "description": "Clear sky",
    "main": "Clear",
    "icon": "01d",
    "emoji": "☀️",
    "city": "London",
    "country": "GB",
    "visibility": 10.0,
    "clouds": 20
  }
}
```

## 🎯 Usage

### Auto-Detection
1. Open the application in your browser
2. The app automatically detects your location on page load
3. You can also click **"📍 Auto-Detect My Location"** button to refresh
4. Weather data for your location will be displayed

### Manual Search
1. Enter a city name in the search box (e.g., "London", "New York", "Tokyo")
2. Click **"Search"** button or press **Enter**
3. Weather data for the specified city will be displayed instantly

## 🛠️ Technologies Used

### Backend
- **Flask 3.0.0** - Python web framework
- **Flask-CORS 4.0.0** - Cross-Origin Resource Sharing
- **python-dotenv 1.0.0** - Environment variable management
- **Requests 2.31.0** - HTTP library for API calls

### Frontend
- **HTML5** - Semantic structure
- **CSS3** - Modern styling with gradients, animations, and flexbox/grid
- **JavaScript (ES6+)** - Async/await, fetch API, DOM manipulation

### External APIs
- **OpenWeatherMap API** - Real-time weather data
- **IP-API** - IP-based geolocation service

## 🎨 Features Breakdown

### Weather Information Displayed:
- 🌡️ **Temperature** - Current and "feels like" temperature in Celsius
- 💧 **Humidity** - Relative humidity percentage
- 💨 **Wind** - Speed (m/s) and cardinal direction (N, NE, E, SE, etc.)
- 👁️ **Visibility** - Visibility distance in kilometers
- 🔽 **Pressure** - Atmospheric pressure in hPa
- ☁️ **Cloudiness** - Cloud coverage percentage
- 📝 **Description** - Human-readable weather condition description
- 🎭 **Weather Emoji** - Visual representation with emojis

### Technical Features:
- **Smart IP Detection**: Automatically detects client IP from multiple headers (X-Forwarded-For, X-Real-IP, CF-Connecting-IP)
- **Private IP Handling**: Falls back to server's public IP when accessing from local network
- **Wind Direction Conversion**: Converts degrees to cardinal directions (N, NE, E, SE, etc.)
- **Error Recovery**: Comprehensive error handling for API failures and network issues
- **Loading States**: Visual feedback during data fetching
- **Responsive Design**: Mobile-first approach with breakpoints

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Flask secret key for session security | Yes | Generated 64-char hex string |
| `OPENWEATHER_API_KEY` | OpenWeatherMap API key | Yes | Your API key from OpenWeather |

### API Rate Limits

**OpenWeatherMap Free Tier:**
- 1,000 API calls per day
- 60 calls per minute
- No credit card required

## 🐛 Troubleshooting

### Issue: "Could not detect location"
**Possible Causes:**
- Private IP and server has no internet connection
- IP-API service is down
- Network firewall blocking requests

**Solution:** Use manual city search instead.

### Issue: "City not found"
**Possible Causes:**
- Typo in city name
- City not in OpenWeatherMap database

**Solution:** 
- Check spelling
- Try different city name format (e.g., "New York" or "London,UK")
- Try nearby major city

### Issue: "Network error"
**Possible Causes:**
- No internet connection
- API service temporarily unavailable
- Firewall blocking requests

**Solution:** 
- Check internet connection
- Wait a few moments and retry
- Check firewall settings

### Issue: API returns 401 Unauthorized
**Possible Causes:**
- Invalid API key
- API key not activated yet

**Solution:** 
1. Verify API key in `.env` file is correct
2. Wait 10-15 minutes for new API keys to activate
3. Restart Flask application: `python app.py`

### Issue: Static files not loading (CSS/JS)
**Possible Causes:**
- Wrong working directory
- File permissions issue

**Solution:** 
- Ensure you're in the `backend` directory when running `python app.py`
- Check file permissions: `chmod +r app/static/**/*`

### Issue: Private IP showing wrong location
**Expected Behavior:**
- When accessed from local network (192.168.x.x, 10.x.x.x), the app uses the server's public IP
- This shows the location of your internet service provider, not exact location

**Solution:** This is normal behavior. For exact location from external users, they need to access from the internet with their public IP.

## 📝 Notes

- The free OpenWeatherMap API key may take 10-15 minutes to activate after creation
- Location detection uses IP-based geolocation which provides city-level accuracy (not exact GPS coordinates)
- Weather data is updated in real-time from OpenWeatherMap servers
- For localhost/local network access, location is based on server's public IP
- For internet access, location is based on actual client's public IP

## 🔐 Security

- Never commit your `.env` file to version control
- Keep your API keys secret and secure
- The `.gitignore` file is configured to exclude `.env` and `venv/`
- Use strong, randomly generated SECRET_KEY in production
- Consider using environment-specific configurations for production deployment

