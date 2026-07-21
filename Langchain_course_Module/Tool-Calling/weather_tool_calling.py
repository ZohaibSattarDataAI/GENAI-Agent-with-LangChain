import requests

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_ollama import ChatOllama


# ==========================================================
# Weather Code Mapping
# ==========================================================
WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Heavy Drizzle",
    61: "Light Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Light Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    81: "Moderate Rain Showers",
    82: "Heavy Rain Showers",
    95: "Thunderstorm",
}


# ==========================================================
# Weather Tool
# ==========================================================
@tool
def get_weather(city: str) -> str:
    """
    Fetch current weather information for a city
    using the Open-Meteo API.
    """

    try:

        # -----------------------------
        # Get Latitude & Longitude
        # -----------------------------
        geo_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1"
        )

        geo_response = requests.get(geo_url, timeout=10)
        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if "results" not in geo_data:
            return f"City '{city}' not found."

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        city_name = location["name"]
        country = location["country"]

        # -----------------------------
        # Current Weather
        # -----------------------------
        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            "&current="
            "temperature_2m,"
            "apparent_temperature,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "weather_code"
        )

        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()

        weather_data = weather_response.json()["current"]

        condition = WEATHER_CODES.get(
            weather_data["weather_code"],
            "Unknown"
        )

        return f"""
City: {city_name}, {country}
Temperature: {weather_data['temperature_2m']}°C
Feels Like: {weather_data['apparent_temperature']}°C
Condition: {condition}
Humidity: {weather_data['relative_humidity_2m']}%
Wind Speed: {weather_data['wind_speed_10m']} km/h
""".strip()

    except requests.exceptions.RequestException as e:
        return f"Weather API Error: {e}"

    except Exception as e:
        return f"Unexpected Error: {e}"


# ==========================================================
# Load Ollama
# ==========================================================
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

llm_with_tools = llm.bind_tools([get_weather])


# ==========================================================
# Chat Loop
# ==========================================================
print("=" * 60)
print("Weather Assistant (Type 'exit' to quit)")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages = [HumanMessage(content=question)]

    response = llm_with_tools.invoke(messages)

    messages.append(response)

    if response.tool_calls:

        for tool_call in response.tool_calls:

            if tool_call["name"] == "get_weather":

                tool_result = get_weather.invoke(tool_call["args"])

                messages.append(
                    ToolMessage(
                        content=tool_result,
                        tool_call_id=tool_call["id"]
                    )
                )

        final_response = llm_with_tools.invoke(messages)

        print("\nAssistant:\n")
        print(final_response.content)

    else:
        print("\nAssistant:\n")
        print(response.content)