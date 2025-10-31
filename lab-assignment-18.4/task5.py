import requests
import json
import os

def get_and_store_weather_for_city(city_name):
    """
    Get weather details for a given city, display formatted output, and save each result to results.json (appending).
    """
    API_KEY = "1e3dfe7516f966b2254a4def25c8150f"  # Replace this with your actual API key
    try:
        # Step 1: Get city latitude & longitude
        geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geo_url, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        if not geo_data or not isinstance(geo_data, list):
            print("Error: City not found. Please enter a valid city.")
            return

        lat = geo_data[0].get('lat')
        lon = geo_data[0].get('lon')
        if lat is None or lon is None:
            print("Error: City not found. Please enter a valid city.")
            return

        # Step 2: Get weather details for the coordinates
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        # Step 3: Extract desired fields
        temperature = weather_data.get("main", {}).get("temp")
        humidity = weather_data.get("main", {}).get("humidity")
        weather_list = weather_data.get("weather")
        description = None
        if isinstance(weather_list, list) and weather_list:
            description = weather_list[0].get("description")

        # Step 4: Print results (console output)
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
            print(f"Weather: {description.capitalize()}")
        else:
            print("Weather: Not available")

        # Step 5: Append to results.json in current directory
        result = {
            "city": city_name,
            "temp": round(temperature) if temperature is not None else None,
            "humidity": humidity,
            "weather": description.capitalize() if description else None
        }
        results_file = "results.json"
        try:
            if os.path.exists(results_file):
                with open(results_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if not isinstance(data, list):
                    data = []
            else:
                data = []
        except Exception:
            data = []
        data.append(result)
        with open(results_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Please check your network or API key.")
    except Exception:
        print("Error: City not found. Please enter a valid city.")


if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_and_store_weather_for_city(city)
