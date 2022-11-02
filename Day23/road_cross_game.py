import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Road Cross Game")
# objects
player = Player()
car_manager = CarManager()
score_board = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    # move player
    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")

    # # move car
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision of car vs player
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            score_board.game_status()
            game_is_on = False

    #    detecting successful cross
    if player.at_finish_line():
        player.goto_start()
        car_manager.level_up()
        score_board.inc_level()

screen.exitonclick()