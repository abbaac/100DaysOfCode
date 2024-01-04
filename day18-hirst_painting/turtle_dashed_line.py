from turtle import Turtle, Screen

tim = Turtle()

for i in range(10):
    tim.forward(15)
    tim.pu()
    tim.forward(15)
    tim.pd()


screen = Screen()
screen.exitonclick()