import turtle
from turtle import Turtle, Screen
import random
# changing the color mode to be able to generate random rgb
turtle.colormode(255)

tim = Turtle()
tim.pensize(5)
tim.goto(1, 0)
tim.speed(1)
colours = ["cadetBlue1", "CornflowerBlue", "chartreuse1", "cyan1", "DarkOrange", "blue"]
directions = [0, 90, 180, 360]
#generating random values for r,g,b

for _ in range(100):
    # tim.color(random.choice(colours))
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    tim.color((r,g,b))
    tim.forward(20)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
