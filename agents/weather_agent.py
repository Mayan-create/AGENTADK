
import os
import requests
from dotenv import load_dotenv
load_dotenv()

class WeatherAgent:
    def run(self, input_data):
        # Placeholder: In real case, fetch coordinates from launchpad ID
        # Here we simulate fixed coordinates for demonstration
        lat, lon = 28.5618571, -80.577366  # Kennedy Space Center (example)

        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            return {"error": "Missing OpenWeather API key"}

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "Failed to fetch weather data"}

        weather = response.json()
        return {
            "location": weather.get("name", "Unknown"),
            "temperature": weather["main"].get("temp"),
            "description": weather["weather"][0].get("description", "")
        }