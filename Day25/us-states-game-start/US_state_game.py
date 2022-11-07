import turtle
import pandas

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()

screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# obtaining the dataframe
states_df = pandas.read_csv("50_states.csv")

 # get the state data series into a list
state_list = states_df.state.to_list()
entered_states = []

while len(entered_states) < 50:
    players_ans = screen.textinput(title=f"{len(entered_states)}/50 Enter state",
                                   prompt="Which state?").capitalize()
    entered_states.append(players_ans)

    if players_ans == "Exit":
        for guess_state in entered_states:
            if guess_state in state_list:
                state_list.remove(guess_state)

        state_to_learn = pandas.DataFrame(state_list)
        state_to_learn.to_csv("states_to_learn.csv")
        break

    # comparing player answer to current state
    if players_ans in state_list:
        # accessing the corresponding row
        current_state = states_df[states_df["state"] == players_ans]
        # picking up the state's x and y coor.
        state_x = current_state.x
        state_y = current_state.y
        state_location = turtle.Turtle()
        state_location.penup()
        state_location.hideturtle()
        state_location.color("black")
        state_location.goto(int(state_x), int(state_y))
        state_location.write(f"{players_ans}", align="center", font=FONT)
        # OR
        # state_location.write(f"{current_state.state.item()}", align="center", font=FONT)
        # item() is pandas method that graps the first element and returns it


# screen.mainloop()
#     screen.exitonclick()






# manual way of getting x, y coor
# def get_cor(x, y):
#     print(x, y)
# cor = screen.onscreenclick(get_cor)
# print(cor)
