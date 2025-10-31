import requests
import json

def display_weather_details(city_name):
    """
    Display weather details as JSON output for a given city using OpenWeatherMap API.
    Includes error handling for missing or invalid data.
    """
    API_KEY = "1e3dfe7516f966b2254a4def25c8150f"  # Replace this with your actual API key

    # Step 1: Get city latitude & longitude
    geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
    try:
        geo_response = requests.get(geo_url, timeout=10)
        geo_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the geocoding API.\nDetails: {e}")
        return

    geo_data = geo_response.json()
    if not geo_data:
        print(f"Error: City '{city_name}' not found. Please check the spelling.")
        return

    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    # Step 2: Get weather details
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    try:
        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch weather data.\nDetails: {e}")
        return

    weather_data = weather_response.json()
    print(json.dumps(weather_data, indent=4))


if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    display_weather_details(city)
