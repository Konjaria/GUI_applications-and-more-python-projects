from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        # Window Creation
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # ScoreBoard
        self.ScoreBoard = Label(text=f"Score: {self.quiz.score}", font=("Arial", 10, "italic"), bg=THEME_COLOR,
                                fg="white")
        self.ScoreBoard.grid(row=0, column=1)
        # Canvas Properties
        self.canvas = Canvas(width=300, height=250, bg="white")
        # The Question
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        # Check mark for The correct answer
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Invoking Next Question
        self.get_Question()
        # True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  command=self.userSaidCorrect)
        self.true_button.grid(row=2, column=0)

        # False Button
        false_button = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button, highlightthickness=0,
                                   command=self.userSaidWrong)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_Question(self) -> None:
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def userSaidCorrect(self) -> None:
        self.give_feedback(self.quiz.check_answer("True"))

    def userSaidWrong(self) -> None:
        self.give_feedback(self.quiz.check_answer("False"))

    def answerIsCorrect(self):
        self.ScoreBoard.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="#7DCE13")

    def answerIsWrong(self):
        self.canvas.config(bg="#D2001A")

    def give_feedback(self, condition: bool):
        if condition:
            self.answerIsCorrect()
            self.window.after(1000, func=self.get_Question)
        else:
            self.answerIsWrong()
            self.window.after(1000, func=self.get_Question)
