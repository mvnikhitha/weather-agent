import requests
import os

def get_aqi(city: str) -> str:
    api_key = os.getenv("AIRVISUAL_API_KEY")
    if not api_key:
        return "AQI API key not found."

    url = f"http://api.airvisual.com/v2/city?city={city}&state=Karnataka&country=India&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "data" in data:
        aqi = data["data"]["current"]["pollution"]["aqius"]
        category = (
            "Good 😊" if aqi <= 50 else
            "Moderate 😐" if aqi <= 100 else
            "Unhealthy for Sensitive Groups 😷" if aqi <= 150 else
            "Unhealthy 😷" if aqi <= 200 else
            "Very Unhealthy ☠️" if aqi <= 300 else
            "Hazardous ⚠️"
        )
        return f"The AQI in {city} is {aqi} ({category})."
    else:
        return "Sorry, I couldn't fetch the AQI data."
