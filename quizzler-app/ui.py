from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
LABEL_FONT = ("Courier", 15)

class QuizInterface:

    def __init__(self, score):
        self.window = Tk()
        self.window.title("Qizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {score}", font=LABEL_FONT, bg=THEME_COLOR)
        self.score_label.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150, 
            125, 
            text="question goes here", 
            font=QUESTION_FONT, 
            fill=THEME_COLOR
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=3, column=2)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=3, column=1)

        self.window.mainloop()