import turtle
from turtle import Turtle

TEXT_TYPE = "times new roman"
FONT_SIZE = 15
FONT_TYPE = "normal"
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_line = 0
        turtle.color("white")
        turtle.penup()
        turtle.goto(0, 270)
        turtle.hideturtle()
        self.update_score()

    def update_score(self):
        turtle.write(arg=f"score: {self.score_line}", move=False, align=ALIGNMENT, font=(TEXT_TYPE, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        turtle.goto(0, 0)
        turtle.write("Game over", align=ALIGNMENT, font=(TEXT_TYPE, FONT_SIZE, FONT_TYPE))

    def increment_score(self):
        self.score_line += 1
        turtle.clear()
        self.update_score()
