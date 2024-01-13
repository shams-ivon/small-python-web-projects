import os
import requests
import smtplib
import time
from datetime import datetime

ISS_POSITION_API_URL = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 23.810331
MY_LNG = 90.412521
MY_EMAIL = os.environ.get("SENDER_EMAIL_ENV")
MY_PASSWORD = os.environ.get("SENDER_EMAIL_PASSWORD_ENV")

# -------------------- SEND MAIL -------------------- #

def send_email():

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Provides Transport Layer Security
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:ISS OVERHEAD\n\nMan!!! Just Look up!"
        )

# -------------------- CHECKING IF NIGHT -------------------- #

def is_night():
    parameters = {
        "lat": MY_LAT, 
        "lng": MY_LNG,
        "formatted": 0,
    }

    response_sun = requests.get(url=SUNRISE_SUNSET_API_URL, params=parameters)

    sun_data = response_sun.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    if sunset <= current_hour <= sunrise + 24:
        return True
    
    else:
        return False


# -------------------- CHECKING ISS IS ON TOP -------------------- #

def iss_is_on_top():
    response_iss = requests.get(url=ISS_POSITION_API_URL)
    iss_data = response_iss.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_lat) <= 5 and abs(MY_LNG - iss_lng) <= 5:
        return True

    else:
        return False


while True:
    time.sleep(60)
    
    if is_night and iss_is_on_top():
        send_email()