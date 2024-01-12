from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for item in question_data:
    question = item["text"]
    answer = item["answer"]
    question_object = Question(question, answer)
    question_bank.append(question_object)

quizes = QuizBrain(question_bank)
quiz_ui = QuizInterface(0)

# while quizes.still_has_questions():
#     quizes.next_question()

# print("You've completed the quiz!!!")
# print(f"Your final score is: {quizes.score}/{len(question_bank)}")

