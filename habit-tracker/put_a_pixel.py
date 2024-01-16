import requests

def put_a_pixel(username, graph_id, token_key, date, quantity):
    endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"
    header_parameters = {
        "X-USER-TOKEN": token_key,
    }
    body_parameters = {
        "quantity": quantity,
    }
    response = requests.put(url=endpoint, headers=header_parameters, json=body_parameters)
    print(response.text)