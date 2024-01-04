from turtle import *
import random

tim = Turtle()

tim.speed("fastest")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size_of_gap)

spirograph(10)
spirograph(1)

screen = Screen()
screen.exitonclick()