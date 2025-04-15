import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

from utils.city_extractor import extract_city
from memory.memory_manager import MemoryManager
from tools.weather_tool import get_weather
from tools.aqi_tool import get_aqi
from tools.activity_tool import suggest_activity

# --- Setup ---
load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Shared memory manager instance
memory = MemoryManager()

# Tool detector
def detect_tools(message: str):
    msg = message.lower()
    tools = []

    if any(kw in msg for kw in ["weather", "temperature"]):
        tools.append("weather")
    if any(kw in msg for kw in ["air quality", "aqi", "pollution"]):
        tools.append("aqi")
    if any(kw in msg for kw in ["what should i do", "activity", "suggest"]):
        tools.append("activity")

    return tools

# --- Core Chat Handler ---
async def handle_chat(user_id: str, message: str) -> str:
    try:
        logger.info(f"[{user_id}] → {message}")

        # Retrieve relevant memory
        relevant_memory = memory.retrieve_memory(user_id, message)
        if relevant_memory:
            logger.debug(f"[{user_id}] Retrieved memory:\n{relevant_memory}")
        else:
            logger.debug(f"[{user_id}] No relevant memory found.")

        # Tool Detection
        tools = detect_tools(message)

        # Extract City
        city = extract_city(message) or "Bangalore"
        logger.debug(f"[{user_id}] City detected: {city}")

        responses = []
        weather_info = aqi_info = None

        if "weather" in tools:
            weather_info = get_weather(city)
            responses.append(weather_info)

        if "aqi" in tools:
            aqi_info = get_aqi(city)
            responses.append(aqi_info)

        if "activity" in tools:
            if not weather_info:
                weather_info = get_weather(city)
                responses.append(weather_info)
            if not aqi_info:
                aqi_info = get_aqi(city)
                responses.append(aqi_info)

            suggestion = suggest_activity(f"{weather_info.lower()} {aqi_info.lower()}", relevant_memory)
            responses.append(f"🌟 Based on current conditions, here's a suggestion: {suggestion}")

        # Fallback: Use Gemini for general queries
        if not tools:
            prompt = f"{relevant_memory}\nUser: {message}" if relevant_memory else f"User: {message}"
            logger.debug(f"[{user_id}] Prompt sent to Gemini:\n{prompt}")

            model = genai.GenerativeModel("models/gemini-1.5-pro")
            response = model.generate_content(prompt)
            reply = response.text.strip() if response.text else "Sorry, I couldn't understand that."
            responses.append(reply)

        # Final response
        final_reply = "\n\n".join(responses)
        memory.store_memory(user_id, message, final_reply)

        logger.info(f"[{user_id}] ← {final_reply}")
        return final_reply

    except Exception as e:
        logger.exception(f"Error in handle_chat: {e}")
        return "⚠️ Oops! Something went wrong while processing your message."
