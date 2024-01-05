from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_list = []

y = -70

for turtles in range(6):
    tim = Turtle(shape="turtle")
    turtle_list.append(tim)
    tim.color(colors[turtles])
    tim.pu()
    tim.goto(x=-230, y=y)
    y+=30



is_game_on = True

while is_game_on:
    for turtles in turtle_list:
        turtles.forward(random.randint(0, 10))
        if turtles.xcor() > 220:
            is_game_on = False
            winner = turtles.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle finished the race first.")
            else:
                print(f"You lost! The {winner} turtle finished the race first.")


screen.exitonclick()