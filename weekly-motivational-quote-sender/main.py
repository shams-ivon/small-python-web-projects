import smtplib
import random
import datetime as dt

MY_EMAIL = "fvdb"
MY_PASSWORD = "dcvcvsd" # Use App Password generator to get this password
SEND_TO = "dfvs"

# ------------------ GETTING THE QUOTES LIST ---------------------- #

quotes_list = []

with open("quotes.txt", "r") as quotes_file:
    quotes_list = quotes_file.readlines()

selected_quote = quotes_list[random.randint(0, len(quotes_list) - 1)]

# ---------------------- FINDING WEEKDAY ------------------------- #

now = dt.datetime.now()
day_of_week = now.weekday()

# ---------------------- SENDING EMAIL --------------------------- #

if day_of_week == 1:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Provides Transport Layer Security
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=SEND_TO, 
            msg=f"Subject:Weekly Motivational Quote\n\n{selected_quote}"
        )
