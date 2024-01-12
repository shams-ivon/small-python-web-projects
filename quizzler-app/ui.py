from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
LABEL_FONT = ("Courier", 15)

class QuizInterface:

    def __init__(self, quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Qizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=LABEL_FONT, bg=THEME_COLOR)
        self.score_label.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150, 
            125, 
            width=270,
            text="question goes here", 
            font=QUESTION_FONT, 
            fill=THEME_COLOR
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=3, column=2)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.current_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=self.current_question)
        
        else:
            result = f"YOUR FINAL SCORE IS {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question, text=result)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)

        
    
