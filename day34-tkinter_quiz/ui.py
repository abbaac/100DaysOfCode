import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.question_canvas = Canvas(background="white", height=250, width=300)
        self.question = self.question_canvas.create_text(150, 125, width=280, text="yp", font=("Arial", 15, "italic"),
                                                         fill=THEME_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.scoreboard = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR, fg="white")
        self.scoreboard.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=true_image, background=THEME_COLOR, highlightthickness=0, command=lambda: self.check_answer("True"))
        self.correct_button.grid(column=0, row=2)
        self.wrong_button = Button(image=false_image, background=THEME_COLOR, highlightthickness=0, command=lambda: self.check_answer("False"))
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.wrong_button.config(state=DISABLED)
            self.correct_button.config(state=DISABLED)
    def check_answer(self, answer):
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(background="green")
        else:
            self.question_canvas.config(background="red")

        self.window.after(1000, self.get_next_question)

