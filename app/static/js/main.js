const API_BASE = '';

function showLoading() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('error').style.display = 'none';
    document.getElementById('weatherInfo').classList.remove('active');
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function showError(message) {
    const errorEl = document.getElementById('error');
    errorEl.textContent = message;
    errorEl.style.display = 'block';
    hideLoading();
}

function displayWeather(data) {
    document.getElementById('cityName').textContent = data.city;
    document.getElementById('country').textContent = data.country;
    document.getElementById('weatherIcon').textContent = data.emoji;
    document.getElementById('temperature').textContent = `${data.temperature}°C`;
    document.getElementById('description').textContent = data.description;
    document.getElementById('feelsLike').textContent = `${data.feels_like}°C`;
    document.getElementById('humidity').textContent = `${data.humidity}%`;
    document.getElementById('windSpeed').textContent = `${data.wind_speed} m/s`;
    document.getElementById('windDirection').textContent = data.wind_direction;
    document.getElementById('visibility').textContent = `${data.visibility} km`;
    document.getElementById('pressure').textContent = `${data.pressure} hPa`;

    document.getElementById('weatherInfo').classList.add('active');
    hideLoading();
}

async function autoDetectLocation() {
    showLoading();
    try {
        const response = await fetch(`${API_BASE}/api/location`);
        const result = await response.json();

        if (result.success) {
            fetchWeatherByCoordinates(result.lat, result.lon);
        } else {
            showError(result.error || 'Could not detect your location. Please enter your city manually.');
        }
    } catch (error) {
        showError('Network error. Please check your connection and try again.');
    }
}

async function fetchWeatherByCoordinates(lat, lon) {
    try {
        const response = await fetch(`${API_BASE}/api/weather?lat=${lat}&lon=${lon}`);
        const result = await response.json();

        if (result.success) {
            displayWeather(result.data);
        } else {
            showError(result.error || 'Failed to fetch weather data.');
        }
    } catch (error) {
        showError('Network error. Please check your connection and try again.');
    }
}

async function searchByCity() {
    const city = document.getElementById('cityInput').value.trim();
    if (!city) {
        showError('Please enter a city name.');
        return;
    }

    showLoading();
    try {
        const response = await fetch(`${API_BASE}/api/weather?city=${encodeURIComponent(city)}`);
        const result = await response.json();

        if (result.success) {
            displayWeather(result.data);
        } else {
            showError(result.error || 'City not found. Please try again.');
        }
    } catch (error) {
        showError('Network error. Please check your connection and try again.');
    }
}

// Event listeners
document.getElementById('autoDetectBtn').addEventListener('click', autoDetectLocation);
document.getElementById('searchBtn').addEventListener('click', searchByCity);
document.getElementById('cityInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        searchByCity();
    }
});

// Auto-detect location on page load
window.addEventListener('load', autoDetectLocation);