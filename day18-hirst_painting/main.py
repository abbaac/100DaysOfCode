import colorgram
from turtle import Turtle, Screen, colormode
import random

extract = colorgram.extract('.\day18-hirst_painting\painting.jpg', 20)

rgb_colors = [] 

for colors in extract:
    r = colors.rgb.r
    g = colors.rgb.g
    b = colors.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# for i in range(len(extract)):
#     rgb_colors.append(tuple(extract[i].rgb))
    
tim = Turtle()
tim.speed(1)
colormode(255)

start = -200

def color_pattern(rows, columns):
    for i in range(1, rows+1):
        for _ in range(1, columns+1):
            color = random.choice(rgb_colors)
            tim.dot(20, color)
            tim.forward(1)
            tim.pu()
            tim.forward(50)
        tim.setposition(start, tim.position()[1]+50)

tim.hideturtle()
tim.pu()
tim.setposition(start, start)
color_pattern(10,10)

screen = Screen()
screen.exitonclick()



