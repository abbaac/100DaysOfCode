import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()


APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

print(APP_ID)

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY 
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": "80",
    "height_cm": "180",
    "age": 21
}

response = requests.post(url=endpoint, json=params, headers=headers)
response.raise_for_status()

data = response.json()

for exercises in data["exercises"]:
    exercise = exercises["name"].title()
    duration = exercises["duration_min"]
    calories = exercises["nf_calories"]

    sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().time().strftime("%H:%M:%S")


    sheety_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
    } 

    headers = {
        "Authorization": os.getenv("SHEETY_TOKEN")
    }

    response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers)
    response.raise_for_status()

    print(response.status_code)

