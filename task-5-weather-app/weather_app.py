
import json
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError


def get_coordinates(city):
    params = urlencode({
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    })

    url = f"https://geocoding-api.open-meteo.com/v1/search?{params}"

    with urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    results = data.get("results", [])

    if not results:
        return None

    place = results[0]
    return (
        place["latitude"],
        place["longitude"],
        place["name"],
        place.get("country", "")
    )


def get_weather(latitude, longitude):
    params = urlencode({
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m"
    })

    url = f"https://api.open-meteo.com/v1/forecast?{params}"

    with urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def describe_weather(code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    return descriptions.get(code, "Weather condition unavailable")


def main():
    print("=== Weather App ===")
    city = input("Enter a city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    try:
        location = get_coordinates(city)

        if location is None:
            print("City not found. Please check the spelling.")
            return

        latitude, longitude, city_name, country = location
        data = get_weather(latitude, longitude)
        current = data["current"]

        print(f"\nWeather for {city_name}, {country}")
        print("-" * 30)
        print(f"Temperature: {current['temperature_2m']} °C")
        print(f"Feels like: {current['apparent_temperature']} °C")
        print(f"Humidity: {current['relative_humidity_2m']}%")
        print(f"Wind speed: {current['wind_speed_10m']} km/h")
        print(
            "Condition:",
            describe_weather(current["weather_code"])
        )

    except (HTTPError, URLError, TimeoutError) as error:
        print("Unable to retrieve weather data:", error)
    except (KeyError, ValueError, json.JSONDecodeError):
        print("Unable to process the weather response.")


if __name__ == "__main__":
    main()
