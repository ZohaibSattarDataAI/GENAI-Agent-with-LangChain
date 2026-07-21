import requests

city = input("Enter city: ")

# Step 1: Get Latitude & Longitude
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url).json()

if "results" not in geo_response:
    print("City not found!")
    exit()

latitude = geo_response["results"][0]["latitude"]
longitude = geo_response["results"][0]["longitude"]

# Step 2: Get Weather
weather_url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

weather = requests.get(weather_url).json()

current = weather["current"]

print("\nCurrent Weather")
print("----------------------")
print("Temperature :", current["temperature_2m"], "°C")
print("Humidity    :", current["relative_humidity_2m"], "%")
print("Wind Speed  :", current["wind_speed_10m"], "km/h")