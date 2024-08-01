from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.hideturtle()
        self.setpos((-280, 260))
        self.level= 1
        self.display_level()

    def update_level(self):
        self.level +=1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}")

    def game_over(self):
        self.setpos((0,0))
        self.write("GAME OVER", align="center", font=FONT)
