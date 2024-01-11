from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(1,1)
        self.color("white")
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def start_game(self):
        self.home()
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def game_over(self):
        self.start_game()
        self.move_speed = 0.05

