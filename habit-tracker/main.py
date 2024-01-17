from http_requests.post_a_pixel import post_a_pixel
from http_requests.put_a_pixel import put_a_pixel
from http_requests.delete_a_pixel import delete_a_pixel
from create_account import create_account
from create_graph import create_graph
from datetime import datetime

today = datetime.now()
actions = [
    "Create Account", 
    "Create A Record Graph",
    "Create Work Record",
    "Update Work Record",
    "Delete Work Record"
]

while True:
    print("Choose one action:-")

    for index in range(5):
        print(f"{index + 1}) {actions[index]}")

    input_data = input("Your Choice Option Number (Enter 0 to exit): ")
    
    if input_data == "1":

        respone_text = create_account(
            username=input("Set a username: "),
            token_key=input("Set a password: "),
            pixela_create_account_endpoint="https://pixe.la/v1/users"
        )
        
        if respone_text["isSuccess"] == "true":
            print("Account Created Successfully")
        
        else:
            print(respone_text["message"])


    elif input_data == "2":
        
        respone_text = create_graph(
            username=input("Your username: "),
            token_key=input("Your password: "),
            graph_id=input("Set a graph id (A string): "),
            pixela_create_account_endpoint="https://pixe.la/v1/users"
        )

        if respone_text["isSuccess"] == "true":
            print("Graph created successfully")

        else:
            print(respone_text["message"])

    elif input_data == "3":
        print("c")

    elif input_data == "4":
        print("d")

    elif input_data == "5":
        print("e")

    elif input_data == "0":
        break

    else:
        print("Please Enter a valid input")

# post_a_pixel(
#     username=MY_USERNAME,
#     graph_id=GRAPH_ID,
#     token_key=MY_TOKEN,
#     date=today.strftime("%Y%m%d"),
#     quantity="22"
# )

# put_a_pixel(
#     username=MY_USERNAME,
#     graph_id=GRAPH_ID,
#     token_key=MY_TOKEN,
#     date=today.strftime("%Y%m%d"),
#     quantity="30"
# )

# delete_a_pixel(
#     username=MY_USERNAME,
#     graph_id=GRAPH_ID,
#     token_key=MY_TOKEN,
#     date=today.strftime("%Y%m%d")
# )