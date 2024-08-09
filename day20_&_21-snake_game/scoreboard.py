from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0     
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())


    def display(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}, High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.set_new_high_score()
        self.clear()
        self.display()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)

    def start_game(self):
        self.write(f"PRESS SPACE TO PLAY", True, align=ALIGNMENT, font=FONT)
        return True
    
    def play_again(self):
        self.write(f"PRESS SPACE TO PLAY AGAIN", True, align=ALIGNMENT, font=FONT)

    def set_new_high_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")







    



