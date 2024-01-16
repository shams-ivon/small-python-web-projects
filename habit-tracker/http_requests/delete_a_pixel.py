import requests

def delete_a_pixel(username, graph_id, token_key, date):
    endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"
    header_parameters = {
        "X-USER-TOKEN": token_key,
    }
    response = requests.delete(url=endpoint, headers=header_parameters)
    print(response.text)