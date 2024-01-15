import os
# import requests
from post_a_pixel import post_a_pixel

MY_USERNAME = "ivon"
GRAPH_ID = "graph-01"
MY_TOKEN = os.environ.get("MY_PIXELA_TOKEN")

pixela_create_account_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": MY_TOKEN,
    "username": MY_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# The following post request was only for creating account purpose
# body must be a json=

# response = requests.post(url=pixela_create_account_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_create_account_endpoint}/{MY_USERNAME}/graphs"

graph_header = {
    "X-USER-TOKEN": MY_TOKEN,
}

graph_body = {
    "id": GRAPH_ID,
    "name": "Push Up Counter",
    "unit": "reps",
    "type": "int",
    "color": "shibafu",
}

# The following post request was only for creating graph purpose
# body must be a json=

# graph_response = requests.post(url=graph_endpoint, headers=graph_header, json=graph_body)
# print(graph_response.text)

post_a_pixel(
    username=MY_USERNAME,
    graph_id=GRAPH_ID,
    token_key=MY_TOKEN,
    date="20240115",
    quantity="16"
)