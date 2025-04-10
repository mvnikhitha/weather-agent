def suggest_activity(weather_desc: str, memory_text: str) -> str:
    if "rain" in weather_desc:
        return "How about reading a book or watching a movie indoors?"
    elif "clear" in weather_desc or "sunny" in weather_desc:
        return "Great day for a walk or a picnic!"
    elif "cloud" in weather_desc:
        return "Maybe visit a museum or try a new café nearby?"
    else:
        return "Try something relaxing like journaling or sketching!"
