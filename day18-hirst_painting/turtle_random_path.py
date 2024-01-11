import turtle as t
import random

tim = t.Turtle()

tim.pensize(10)
tim.speed(2000)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color



def random_move():
    tim.color(random_color())
    tim.forward(30)
    direction = 90 * random.randint(0,3)
    tim.setheading(direction)
    # random.choice(directions)


for _ in range(10):
    random_move()


screen = t.Screen()
screen.exitonclick()

