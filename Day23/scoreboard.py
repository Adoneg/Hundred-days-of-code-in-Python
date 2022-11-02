from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.starting_level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-260, 260)
        self.update_level()

    def inc_level(self):
        self.starting_level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.starting_level}", align="left", font=FONT)

    def game_status(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
