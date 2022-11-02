from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("blue")
        self.goto(STARTING_POSITION)

    def move_up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(0, new_y)
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)


    def move_down(self):
        if self.ycor() >= STARTING_POSITION[1]:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(0, new_y)

    #detect when it touche the top screen