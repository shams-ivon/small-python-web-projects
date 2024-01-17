import requests

def create_graph(username, token_key, graph_id, pixela_create_account_endpoint):
    graph_endpoint = f"{pixela_create_account_endpoint}/{username}/graphs"
    graph_header = {
        "X-USER-TOKEN": token_key,
    }
    graph_body = {
        "id": graph_id,
        "name": "Push Up Counter",
        "unit": "reps",
        "type": "int",
        "color": "shibafu",
    }
    # The following post request was only for creating graph purpose
    # body must be a json=
    response = requests.post(url=graph_endpoint, headers=graph_header, json=graph_body)
    print(response.text)