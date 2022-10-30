from turtle import Screen
from create_paddle import Paddle
from ball import Ball
import time
from score_dash_board import Score

my_screen = Screen()
my_screen.tracer(0)  # inorder to manually update the screen
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("The Pong Game")
# paddle objects
left_paddle = Paddle((-350, 0))

right_paddle = Paddle((350, 0))
# score object
score = Score()

my_screen.listen()
my_screen.onkey(fun=left_paddle.go_up, key="w")  # when passing a fun as a para don't use ()
my_screen.onkey(fun=left_paddle.go_down, key="s")

my_screen.onkey(fun=right_paddle.go_up, key="Up")  # when passing a fun as a para don't use ()
my_screen.onkey(fun=right_paddle.go_down, key="Down")

#   ball object
ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(ball.time_sp)
    my_screen.update()
    ball.move_right()

    # detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collisionn with the paddle
    if ball.distance(left_paddle) < 100 and ball.xcor() < -310 \
            or ball.distance(right_paddle) < 100 and ball.xcor() > 310:

        ball.bounce_x()

    # detecting miss with left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        score.right_score()

    # detecting miss with right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        score.left_score()

my_screen.exitonclick()
