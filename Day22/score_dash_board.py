from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Courier", 40, "normal"))

    def right_score(self):
        self.score_r += 1
        self.update_score()

    def left_score(self):
        self.score_l += 1
        self.update_score()
