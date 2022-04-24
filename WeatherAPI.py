
import requests
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
env_path = "EmailSenderInfo.env"
load_dotenv(dotenv_path=env_path)
api = os.getenv("WeatherAPIKey")

zip = "33543"
weather = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key={api}&q={zip}&days=1&aqi=no&alerts=no').json()

loc = weather['location']['name']
temp = weather['current']['temp_f']
cond = weather['current']['condition']['text']
hum = weather['current']['humidity']
dayforecast = weather['forecast']['forecastday']
day = dayforecast[0]['day']
astro = dayforecast[0]['astro']

#print(f"Last Update: {weather['current']['last_updated']}\n")

min = day['mintemp_f']
max = day['maxtemp_f']
rain = day['daily_chance_of_rain']
uv = day['uv']

#print(f"Location: {loc}")
#print(f"Current Temperature: {temp}°")
#print(f"High/Low Tempature: {max}°\{min}°")
#print(f"Conditions: {cond}")
#print(f"UV Index: {uv}")
#print(f"Humidity: {hum}%")
#print(f"Chance of Rain: {rain}%")




#print(f"\nSunrise: {astro['sunrise']}")
#print(f"Sunset: {astro['sunset']}")
#print(f"Moon Phase: {astro['moon_phase']}")
