import os
import requests

MY_TOKEN = os.environ.get("MY_PIXELA_TOKEN")

pixela_create_account_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": MY_TOKEN,
    "username": "ivon",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# The following post request was only for creating account purpose

# response = requests.post(url=pixela_create_account_endpoint, json=user_parameters)
# print(response.text)