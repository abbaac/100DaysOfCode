from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

colors = ["pale turquoise", "lime green", "dark gray", "navy", "cyan", "khaki", "firebrick", "orange red", "deep pink", "indigo"]


def draw_shape(number_of_sides):
    tim.color(random.choice(colors))
    for line in range(number_of_sides):
        tim.forward(100)
        tim.left(360/number_of_sides)


for i in range(3,10):
    draw_shape(i)



screen = Screen()
screen.exitonclick()