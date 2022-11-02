import turtle
from turtle import Turtle
import random


class Food(Turtle):     # inheriting from the Turtle class
    def __init__(self):
        super(Food, self).__init__()
        turtle.hideturtle()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # reducing the 20 x 20 turtle to 10 x 10
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        x_coor = random.randint(-280, 280)
        y_coor = random.randint(-280, 280)
        self.goto(x=x_coor, y=y_coor)
