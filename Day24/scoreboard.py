import turtle
# from turtle import Turtle

TEXT_TYPE = "times new roman"
FONT_SIZE = 15
FONT_TYPE = "normal"
ALIGNMENT = "center"


class ScoreBoard:
    def __init__(self):
        self.score_line = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        turtle.color("white")
        turtle.penup()
        turtle.goto(0, 270)
        turtle.hideturtle()
        self.update_score()

    def update_score(self):
        turtle.clear()
        turtle.write(arg=f"score: {self.score_line} high_score: {self.high_score}", move=False, align=ALIGNMENT, font=(TEXT_TYPE, FONT_SIZE, FONT_TYPE))

    def reset(self):
        if self.score_line > self.high_score:
            self.high_score = self.score_line
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score_line = 0
        self.update_score()

    def increment_score(self):
        self.score_line += 1
        turtle.clear()
        self.update_score()
