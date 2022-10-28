from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    """ moves the turtle forward by 25 """
    tim.forward(50)


def move_backward():
    """Moves the turtle backward"""
    tim.backward(50)


def left():
    """turn left"""
    tim.left(10)


def right():
    """turn left"""
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_clockwise():
    """Moves the turtle clockwise"""
    tim.setheading(0)
    tim.circle(100)


def move_anticlockwise():
    """moves the turtle anticlockwise"""
    tim.setheading(180)
    tim.circle(100)


def clear_drawing():
    """clears drawing"""
    tim.clear()
    tim.setheading(0)


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_clockwise, key="a")
screen.onkey(fun=move_anticlockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")
screen.onkey(fun=left, key="l")
screen.onkey(fun=right, key="r")


screen.exitonclick()
