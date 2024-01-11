from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pu()
        self.l_paddle = 0
        self.r_paddle = 0
        self.setpos(0, 260)

    def score(self):
        self.clear()
        self.write(f"{self.l_paddle}\t{self.r_paddle}", move=False, align="center", font=("Arial", 30, "bold"))

    def right_point(self):
        self.r_paddle += 1
        self.score()

    def left_point(self):
        self.l_paddle += 1
        self.score()

    def restart(self):
        self.l_paddle = 0
        self.r_paddle = 0