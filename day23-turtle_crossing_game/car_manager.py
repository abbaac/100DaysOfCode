from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_cars(self):
        frequency = random.randint(1, 6)
        if frequency == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            car.color(f"{random.choice(COLORS)}")
            y = random.randint(-260, 260)
            car.setpos((300, y))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def next_level(self):
        self.car_speed += MOVE_INCREMENT



    
