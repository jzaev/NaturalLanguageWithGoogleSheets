import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")    #"fd82b230"
APP_KEY = os.environ.get("APP_KEY")    #"f62736f9fefedc85c80e549ae23a05a0"
BEARER_KEY = os.environ.get("BEARER_KEY")    #"kawefuglkagfju9999"

POST_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

input_text = input("What you did?")

query_text = {
    "query": input_text,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 172,
    "age": 45
}

respond = requests.post(url=POST_ENDPOINT, headers=HEADERS, json=query_text)
# print(respond.text)
exercise = respond.json()["exercises"][0]

SHEETY_ENDPOINT = "https://api.sheety.co/3d23ea4e18c396d229e076b5fb916d12/myWorkouts/workouts"

sheet_inputs = {
        "workout": {
            "date": datetime.now().strftime("%Y/%m/%d"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_headers = {
    "Authorization": f"Bearer {BEARER_KEY}"
}

respond = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheet_headers)
print(respond.text)
