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

    def display(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
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




    



