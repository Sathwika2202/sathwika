import requests

def display_city_weather(city_name):
    """
    Fetch and display temperature, humidity, and weather description for a given city
    using the OpenWeatherMap API in a user-friendly format.
    """
    API_KEY = "1e3dfe7516f966b2254a4def25c8150f"  # Replace with your own API key

    try:
        # Get city latitude and longitude
        geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geo_url, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        if not geo_data:
            print(f"Error: City '{city_name}' not found. Please check the spelling.")
            return

        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        # Get weather details
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        # Extract required fields
        temperature = weather_data.get('main', {}).get('temp')
        humidity = weather_data.get('main', {}).get('humidity')
        description = None
        if 'weather' in weather_data and isinstance(weather_data['weather'], list) and weather_data['weather']:
            description = weather_data['weather'][0].get('description')

        # Output in a user-friendly format
        print(f"City: {city_name}")
        if temperature is not None:
            print(f"Temperature: {round(temperature)}°C")
        else:
            print("Temperature: Not available")
        if humidity is not None:
            print(f"Humidity: {humidity}%")
        else:
            print("Humidity: Not available")
        if description:
            print(f"      Weather: {description.capitalize()}")
        else:
            print("      Weather: Not available")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")
    except Exception:
        print("Error: An unexpected error occurred.")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    display_city_weather(city)
