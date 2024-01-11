from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.pu()
        self.setpos(pos)
        self.setpos(pos)


        
    def go_up(self):
        current_y = self.ycor()
        if current_y < 250:
            self.sety(current_y+20)

    def go_down(self):
        current_y = self.ycor()
        if current_y > -240:
            self.sety(current_y-20)




