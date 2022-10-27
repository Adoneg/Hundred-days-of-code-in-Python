from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
tim = Turtle()
tim.speed("normal")
# tim.color(random.choice(colours))
def random_colour():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b

def draw_circle(space):
    for _ in range(round(360/space)):
        tim.color((random_colour()))
        tim.circle(30)
        current_heading = tim.heading()
        tim.setheading(current_heading + space)

draw_circle(15)










screen = Screen()
screen.exitonclick()