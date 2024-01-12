import requests

URL = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "boolean",
}

response_question_data = requests.get(url=URL, params=parameters).json()["results"]

question_data = []

for data in response_question_data:
    dict = {
        "text": data["question"],
        "answer": data["correct_answer"]
    }
    question_data.append(dict)

