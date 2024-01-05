from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)

def turn_anti_clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_clockwise)
screen.onkey(key="d", fun=turn_anti_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()