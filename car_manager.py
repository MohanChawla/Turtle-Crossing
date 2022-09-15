from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "lightgreen", "skyblue", "turquoise"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_num = random.randint(1, 10)
        if random_num == 2 or random_num == 4:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randrange(-250, 250, 22)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() == 300:
                car.backward(22)
            else:
                car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


