import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_data = {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        }
        return weather_data
    else:
        return None

def main():
    api_key = "a9fa9fe4c6d42b07bbc0b19937672170"
    location = input("Enter a city or ZIP code: ")
    weather = get_weather(api_key, location)

    if weather:
        print(f"Weather in {location}:")
        for key, value in weather.items():
            print(f"{key}: {value}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    main()