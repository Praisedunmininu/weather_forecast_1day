import requests
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_key")
city = input("Enter a city:")
url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "2af5dbc12ecd2a6ac040d34a668b2981"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    weather_data = response.json()
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["main"]

    print(f"The temperatue in {city} is {temp:.1f} °C")
    print(f"The humidity in {city}   is {humidity:.1f} %")
    if condition == "clear":
        print("The sky is clear!")
    elif condition == "cloudy":
        print("it is cloudy!")
    elif condition == "rain":
        print("it is raining!")
    else:
         print(f"The current condition! is {condition}")

    if temp > 30:
        print("It's too hot!")
    elif temp < 10:
        print("It's very cold!")
    else:
        print("It's warm!")
else:
    print("Invalid city name or Request failed.")