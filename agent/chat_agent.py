import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

from utils.city_extractor import extract_city
from memory.memory_manager import MemoryManager
from tools.weather_tool import get_weather
from tools.aqi_tool import get_aqi
from tools.activity_tool import suggest_activity

load_dotenv()
logger = logging.getLogger(__name__)

# Gemini API setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Default chat model
chat_model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = chat_model.start_chat(history=[])

memory = MemoryManager()

def detect_tools(message: str):
    msg = message.lower()
    tools = []

    if "weather" in msg or "temperature" in msg:
        tools.append("weather")
    if "air quality" in msg or "aqi" in msg or "pollution" in msg:
        tools.append("aqi")
    if "what should i do" in msg or "activity" in msg or "suggest" in msg:
        tools.append("activity")

    return tools

async def handle_chat(user_id: str, message: str) -> str:
    try:
        logger.debug(f"Incoming message from '{user_id}': {message}")
        memory_manager = MemoryManager()

        relevant_memory = memory_manager.retrieve_memory(user_id, message)
        logger.debug(f"Retrieved memory:\n{relevant_memory if relevant_memory else 'No relevant memory found.'}")

        tools = detect_tools(message)

        # 🌆 Dynamic City Extraction
        city = extract_city(message)
        if not city:
            city = "Bangalore"  # fallback default
            logger.debug("City not found in message. Using default: Bangalore")
        else:
            logger.debug(f"City extracted: {city}")

        responses = []
        weather_info, aqi_info = None, None

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
            responses.append(f"Based on that, I suggest: {suggestion}")

        # If no tools matched, send to Gemini for general reasoning
        if not tools:
            prompt = f"{relevant_memory}\nUser: {message}" if relevant_memory else f"User: {message}"
            logger.debug(f"Sending prompt to Gemini:\n{prompt}")

            model = genai.GenerativeModel("models/gemini-1.5-pro")
            response = model.generate_content(prompt)
            assistant_reply = response.text.strip() if response.text else "Sorry, I couldn't understand that."
            responses.append(assistant_reply)

        final_reply = "\n\n".join(responses)
        memory_manager.store_memory(user_id, message, final_reply)

        return final_reply

    except Exception as e:
        logger.error(f"handle_chat failed: {e}")
        return "Oops! Something went wrong while processing your request."
