import requests

def create_account(username, token_key, pixela_create_account_endpoint):
    #  = "https://pixe.la/v1/users"
    user_parameters = {
        "token": username,
        "username": token_key,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    # The following post request was only for creating account purpose
    # body must be a json=
    response = requests.post(url=pixela_create_account_endpoint, json=user_parameters)
    print(response.text)