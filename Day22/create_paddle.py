from turtle import Turtle

STEP = 100


class Paddle(Turtle):
    def __init__(self, paddle_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(paddle_cor)

    def go_up(self):
        new_ycor = self.ycor() + STEP
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - STEP
        self.goto(self.xcor(), new_ycor)


