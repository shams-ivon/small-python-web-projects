import os
import smtplib

MY_EMAIL = os.environ.get("SENDER_EMAIL_ENV")
MY_PASSWORD = os.environ.get("SENDER_EMAIL_PASSWORD_ENV")

def send_email(email, text):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Provides Transport Layer Security
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=email, 
            msg=f"Subject:Birthday Wish\n\n{text}" 
        )