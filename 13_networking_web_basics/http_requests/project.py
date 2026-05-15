"""
PROJECT: The Weather Reporter (Simulator)

Goal: Build a script that fetches live weather data for any city.

Requirements:

1. Setup:
   - Use the free 'Open-Meteo' API (No API Key required!).
   - Base URL: "https://api.open-meteo.com/v1/forecast"

2. Logic:
   - The user inputs latitude and longitude (e.g., London: lat=51.5, lon=-0.12).
   - Construct the URL with parameters:
     params = {
         "latitude": lat,
         "longitude": lon,
         "current_weather": True
     }
   - Make the GET request.

3. Output:
   - Print the current temperature.
   - Print the windspeed.
   - Handle potential connection errors with a friendly message.

Real-World Logic:
- This is how mobile apps and smart mirrors show you the weather. They don't have thermometers inside them; they just make an HTTP request to a weather server every few minutes!
"""

import requests
import json

# TODO: Implement the Weather Reporter

BASE_URL = "https://api.open-meteo.com/v1/forecast"

35
def get_weather_data(lat, lon):
    """
    Fetch current weather data from Open-Meteo API.
    """

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=5
        )

        # Raise error for bad status codes
        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the weather server.")

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Unexpected Error: {e}")

    return None


def display_weather(data):
    """
    Display weather information nicely.
    """

    if not data:
        print("No weather data available.")
        return

    current_weather = data.get("current_weather")

    if not current_weather:
        print("Current weather information not found.")
        return

    temperature = current_weather.get("temperature")
    windspeed = current_weather.get("windspeed")
    weather_code = current_weather.get("weathercode")
    time = current_weather.get("time")

    print("\n===== CURRENT WEATHER =====")
    print(f"Temperature : {temperature}°C")
    print(f"Wind Speed  : {windspeed} km/h")
    print(f"Weather Code: {weather_code}")
    print(f"Time        : {time}")


def main():

    print("=== Weather Reporter ===")

    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))

        data = get_weather_data(lat, lon)

        display_weather(data)

    except ValueError:
        print("Invalid input. Please enter numeric coordinates.")


if __name__ == "__main__":
    main()