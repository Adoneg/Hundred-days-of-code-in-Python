from turtle import Turtle, Screen

timmy = Turtle()

timmy.color("blue")
timmy.shape("turtle")
#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
for _ in range(7):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
    timmy.forward(1)
    timmy.penup()
    timmy.forward(1)

screen = Screen()
screen.exitonclick()
