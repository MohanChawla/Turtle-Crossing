# Breaking down the problem:
# 1. Create a turtle player that starts at the bottom of the screen and listens for the
# "Up" key to move the turtle north
# 2. Create and move cars
# 3. Detect collision with the cars
# 4. Detect when the Turtle reaches the other side
# 5. Create a scoreboard

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.go_up)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
