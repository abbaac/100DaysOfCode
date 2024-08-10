import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
map = turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.pu()
writer.pencolor("black")

states_data = pd.read_csv("50_states.csv")
states_dict = states_data.to_dict()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(f"{len(guessed_states)}/{len(states_data)} States Correct", "What's another state name?").title()
    if answer_state == "Exit":
        break
    if answer_state in guessed_states:
        continue
    else:
        for i in states_dict["state"]:
            if answer_state in states_dict["state"][i]:
                guessed_states.append(answer_state)
                x_cor = states_dict["x"][i]
                y_cor = states_dict["y"][i]
                writer.goto(x_cor, y_cor)
                writer.write(f"{answer_state}", False, "center", ("Courier", 13, "bold"))


unguessed_states = []
states = states_data.state.to_list()
for state in states:
    if state not in unguessed_states:
        unguessed_states.append(state)

pd.DataFrame(unguessed_states).to_csv("states_to_learn.csv")