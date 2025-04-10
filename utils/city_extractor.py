def extract_city(message: str) -> str:
    cities = [
        "bangalore", "mumbai", "delhi", "chennai", "kolkata",
        "hyderabad", "pune", "ahmedabad", "jaipur", "kochi", "indore"
    ]
    msg_lower = message.lower()

    for city in cities:
        if city in msg_lower:
            return city.capitalize()

    return "Bangalore"  # Default fallback if no city found
