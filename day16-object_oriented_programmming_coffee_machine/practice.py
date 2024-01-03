# from turtle import Turtle, Screen

# timmy = Turtle()

# timmy.shape('turtle')
# timmy.color('DarkOrange')
# timmy.forward(100)
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

# You can use the pypi website to search for different modules that could be helpful when building programs
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"
print(table)