from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEPS = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles_list = []
        self.create_snake()
        self.head = self.turtles_list[0]

    def create_snake(self):
        for turtle_index in STARTING_COORDINATES:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(turtle_index)
            self.turtles_list.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.turtles_list) - 1, 0, -1):
            new_xcor = self.turtles_list[seg_num - 1].xcor()
            new_ycor = self.turtles_list[seg_num - 1].ycor()
            self.turtles_list[seg_num].goto(new_xcor, new_ycor)
        self.turtles_list[0].forward(MOVE_STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # the method heading returns the turtles current setheading (angle).
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




