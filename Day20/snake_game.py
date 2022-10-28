from turtle import Screen
import time
from snake import Snake
# from food_class import Food
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()

# listening to key bindings

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

is_game_on = True

while is_game_on:
    my_screen.update()
    time.sleep(0.3)

    snake.move()


my_screen.exitonclick()
