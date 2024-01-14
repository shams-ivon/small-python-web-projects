import html

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_question_unescaped = html.unescape(self.current_question.question)
        return f"Q.{self.question_number}: {current_question_unescaped}"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False