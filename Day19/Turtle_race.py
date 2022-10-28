from turtle import Turtle, Screen
import random

screen = Screen()
def turtle_race():
    screen.setup(height=300, width=600)
    user_guest = screen.textinput(title="Make your bet", prompt="Which colour will win?: ")

    turtle_colours = ["red", "orange", "yellow", "black", "green", "blue"]
    is_race_on = False

    all_turtles = []
    y_axis = [-125, -75, -25, 25, 75, 125]

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        colour = turtle_colours[turtle_index]
        new_turtle.color(colour)
        new_turtle.goto(x=-280, y=y_axis[turtle_index])
        all_turtles.append(new_turtle)

    if user_guest:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 280:      # a turtle is 40 x 40
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_guest:
                    print(f"You have won! the winning colour is {winning_color}. Congratulation. ")
                else:
                    print(f"You have lost! the winning colour is {winning_color}.")
            random_dist = random.randint(0, 5)
            turtle.forward(random_dist)


turtle_race()           # calling the race function












screen.exitonclick()