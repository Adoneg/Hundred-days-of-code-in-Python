import turtle
from turtle import Turtle, Screen
import  random
tim = Turtle()

sides = 1
colours = ["red", "blue", "yellow", "green"]
while sides <= 20:
    tim.color(random.choice(colours))
    for _ in range(sides):
        tim.forward(50)
        angle = 360/sides
        tim.right(angle)
    sides += 1

screen = Screen()
screen.exitonclick()