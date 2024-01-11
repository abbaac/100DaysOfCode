from turtle import Turtle

RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
STARTING_LENGTH = 3
POSITIONS = [(0, 0), (0, 0), (0,0)]

class Snake():
    def __init__(self):
        self.segments= []
        self.new_game()
        self.head = self.segments[0]

    def new_game(self):
        for position in POSITIONS:
            self.add_segment(position)
    
            
    def add_segment(self, position):
        new_segments = Turtle(shape="square")
        new_segments.color("white")
        new_segments.shapesize(0.9, 0.9)
        new_segments.pu()
        new_segments.goto(position)       
        self.segments.append(new_segments)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.speed(1)
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


        

