import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = "sfdfgm"
MY_PASSWORD = "ftybq" # Use App Password generator to get this password

# --------------------- MAKE A LETTER ------------------ #

def make_letter(name):
    
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
        text_list = letter.readlines()

    text_list[0] = text_list[0].replace("[NAME]", name)
    return "".join(text_list)

# ------------------------ SEND EMAIL ------------------ #

def send_email(email, text):
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Provides Transport Layer Security
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=email, 
            msg=f"Subject:Birthday Wish\n\n{text}"
        )

# ---------------------- FIND TODAYS DATE ------------------ #

now = dt.datetime.now()

today_month = now.month
today_day = now.day

# ----------------- MAKE A LIST OF BIRTHDAY PEOPLE FROM CSV FILE -------------------- #

datas = pandas.read_csv("birthdays.csv")
birthday_today = datas[(datas["month"] == 1) & (datas["day"] == 9)]

# ----------------------- SEND THEM BIRTHDAY MAIL ---------------------- #

letters_to_send = len(birthday_today)

if letters_to_send > 0:
    birthday_today_name_list = birthday_today["name"].tolist()
    birthday_today_email_list = birthday_today["email"].tolist()

    for index in range(letters_to_send):
        send_email(
            birthday_today_email_list[index], 
            make_letter(birthday_today_name_list[index])
        )
