import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_cars() 
    car_manager.move()

    screen.onkey(player.move_up, "Up")

    if player.is_at_finish_line():
        player.reset()
        scoreboard.update_level()
        car_manager.next_level()    

    if any(car.distance(player) < 20 for car in car_manager.all_cars):
        game_is_on = False
        scoreboard.game_over()

    screen.listen()

screen.exitonclick()