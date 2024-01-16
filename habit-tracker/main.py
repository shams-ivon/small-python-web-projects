from http_requests.post_a_pixel import post_a_pixel
from http_requests.put_a_pixel import put_a_pixel
from http_requests.delete_a_pixel import delete_a_pixel
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
        print("a")

    elif input_data == "2":
        print("b")

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