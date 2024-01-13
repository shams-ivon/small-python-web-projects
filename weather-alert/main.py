import os
import requests
from twilio.rest import Client

TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_REAL_PHONE_NUMBER = os.environ.get("MY_REAL_PHONE_NUMBER")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID_ENV")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN_ENV")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY_ENV")
URL = "https://api.openweathermap.org/data/2.5/weather"
MY_LAT = 23.810331
MY_LON = 90.412521

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": WEATHER_API_KEY,
}

response_temp = requests.get(url=URL, params=parameters).json()["main"]

if response_temp["feels_like"] - 273 <= 20:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="Bring a warm cloth outside",
        from_=TWILIO_PHONE_NUMBER,
        to=MY_REAL_PHONE_NUMBER
    )

    print(message.status)
