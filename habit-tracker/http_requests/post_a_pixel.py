import requests

def post_a_pixel(username, graph_id, token_key, date, quantity):
    endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"
    header_parameters = {
        "X-USER-TOKEN": token_key
    }
    body_parameters = {
        "date": date,
        "quantity": quantity,
    }
    respone = requests.post(url=endpoint, headers=header_parameters, json=body_parameters)
    print(respone.text)