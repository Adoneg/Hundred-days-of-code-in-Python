import turtle
import pandas
from turtle import Turtle

FONT = ("Courier", 10, "normal")

#
# x_list = []
# y_list = []
# cor_list = []
#
# def catch_coordinates(x, y):
#     print(x, y)
#
#     coordinate_dict = {
#                 'regions': ["Bamenda", "Buea", "Yaounde", "Douala", "Bafousam", "Ebolowa", "Bertoua", "Ngoundere", "Garoua", "Maroua"],
#                 'x_coor': [x_list],
#                 'y_coor': [y_list]
#             }
#     df = pandas.DataFrame(coordinate_dict)
#     df.to_csv("cam_regional_coor.csv")



screen = turtle.Screen()
image = "cam_map.gif"
screen.addshape(image)
turtle = turtle.Turtle()
turtle.shape(image)
screen.title("Cameroon Region Game")


# obtaining the dataframe
states_df = pandas.read_csv("cam_regional_coor.csv")
 # get the state data series into a list
state_list = states_df.regions.to_list()
entered_states = []

while len(entered_states) < 50:
    players_ans = screen.textinput(title=f"{len(entered_states)}/10 Enter Region",
                                   prompt="Which Region?").capitalize()
    entered_states.append(players_ans)

    if players_ans == "Exit":
        for guess_state in entered_states:
            if guess_state in state_list:
                state_list.remove(guess_state)

        state_to_learn = pandas.DataFrame(state_list)
        state_to_learn.to_csv("region_to_learn.csv")
        break

    # comparing player answer to current state
    if players_ans in state_list and len(entered_states) != 10:
        # accessing the corresponding row
        current_state = states_df[states_df["regions"] == players_ans]
        # picking up the state's x and y coor.
        state_x = current_state.x_coor
        state_y = current_state.y_coor
        # creating turtle to write on precise regional location
        state_location = Turtle()
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


screen.mainloop()