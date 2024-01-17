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
        
        # if respone_text["isSuccess"] == "true":
        #     print("Account Created Successfully")
        
        # else:
        #     print(respone_text["message"])


    elif input_data == "2":
        
        respone_text = create_graph(
            username=input("Your username: "),
            token_key=input("Your password: "),
            graph_id=input("Set a graph id (A string): "),
            pixela_create_account_endpoint="https://pixe.la/v1/users"
        )

        # if respone_text["isSuccess"] == "true":
        #     print("Graph created successfully")

        # else:
        #     print(respone_text["message"])

    elif input_data == "3":
        
        respone_text = post_a_pixel(
            username=input("Your username: "),
            token_key=input("Your password: "),
            graph_id=input("Id of the graph you want to create record today: "),
            date=today.strftime("%Y%m%d"),
            quantity=input("Quantity: ")
        )

        # if respone_text["isSuccess"] == "true":
        #     print("Graph created successfully")

        # else:
        #     print(respone_text["message"])

    elif input_data == "4":

        respone_text = put_a_pixel(
            username=input("Your username: "),
            token_key=input("Your password: "),
            graph_id=input("Id of the graph you want to create record today: "),
            date=input("Date of the record you want to update: "),
            quantity=input("Quantity: ")
        )
        
        # if respone_text["isSuccess"] == "true":
        #     print("Graph created successfully")

        # else:
        #     print(respone_text["message"])

    elif input_data == "5":

        respone_text = delete_a_pixel(
            username=input("Your username: "),
            token_key=input("Your password: "),
            graph_id=input("Id of the graph you want to create record today: "),
            date=input("Date of the record you want to update: ")
        )
        
        # if respone_text["isSuccess"] == "true":
        #     print("Graph created successfully")

        # else:
        #     print(respone_text["message"])

    elif input_data == "0":
        break

    else:
        print("Please Enter a valid input")

