from turtle import Turtle, Screen

# timy = Turtle()
# print(timy)
# my_screen = Screen()
# timy.shape('turtle')
# timy.color('red')
# timy.forward(10000)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon_names', ['Squirtle', 'Pikachu', 'Charmander'])
table.add_column('Type', ['water', 'electric', 'fire'])
table.align= 'r'
print(table)