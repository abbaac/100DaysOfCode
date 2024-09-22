import requests
# from twilio.rest import Client
from dotenv import load_dotenv
import os


MY_LAT = 6.450410
MY_LONG = 3.435330
API_KEY = os.getenv("WEATHER_API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon":MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

# [print("Bring an umbrella") for i in weather_data["list"] if i["weather"][0]["id"] <  700]

will_rain = False
for i in weather_data["list"]:
    if i["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     from_='+14158559918',
    #     body="It's going to rain today. Remember to bring an Umbrella ☔.",
    #     to='+2349162104790'
    # )

    # print(message.status)
    print("Bring an Umbrella")
