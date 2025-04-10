import requests
import os

def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather API key not found."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        weather_main = data["weather"][0]["main"].lower()

        # Suggest activities based on weather
        if weather_main in ["clear", "sunny"]:
            suggestion = "It's a great day for outdoor sports like cricket or jogging!"
        elif "rain" in weather_main or "drizzle" in weather_main:
            suggestion = "Might be better to stay indoors—maybe catch up on a book or do some indoor workouts."
        elif "cloud" in weather_main:
            suggestion = "It's cloudy. Light outdoor activities like walking or cycling should be fine."
        elif "snow" in weather_main:
            suggestion = "If it's safe, enjoy snow activities like building a snowman or skiing!"
        elif "storm" in weather_main or "thunderstorm" in weather_main:
            suggestion = "Avoid outdoor plans—it's stormy. Stay safe indoors!"
        else:
            suggestion = "Conditions are a bit mixed. Consider flexible plans."

        return (
            f"The weather in {city} is {desc} with a temperature of {temp}°C. {suggestion}"
        )
    else:
        return "Sorry, I couldn't fetch the weather data."
