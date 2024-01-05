from turtle import Turtle

STARTING_POSITION = 0
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake():
    def __init__(self):
        self.segments= []
        self.new_game()
        self.head = self.segments[0]



    def new_game(self):
        x = 0
        for i in range(3):
            new_segments = Turtle(shape="square")
            new_segments.color("white")
            new_segments.pu()
            new_segments.setx(x)       
            self.segments.append(new_segments)
            x -=20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


        

