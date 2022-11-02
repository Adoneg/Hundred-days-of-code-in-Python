import turtle
from turtle import Screen
import time
from snake import Snake
from food_class import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
score_count = 0
my_screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
# listening to key bindings

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

is_game_on = True

while is_game_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()
    turtle_x_coor = -40
    if snake.head.distance(food) < 10:   # Object detection. make use of the Turtle class method called distance(x, y)
        score_count += 1
        food.refresh()
        snake.extend()

        score_board.increment_score()

    #detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()


    #detecting head on body colision
    for segment in snake.turtles_list[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()


my_screen.exitonclick()
