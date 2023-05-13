from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.green_image = PhotoImage(file="images/right.png")
        self.green_button = Button(image=self.green_image, highlightthickness=0, command=self.true_button)
        self.green_button.grid(row=2, column=0)

        self.red_image = PhotoImage(file="images/wrong.png")
        self.red_button = Button(image=self.red_image, highlightthickness=0, command=self.false_button)
        self.red_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finished the quiz!")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        elif not is_right:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)
