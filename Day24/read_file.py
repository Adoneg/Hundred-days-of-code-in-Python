# Reading to a file

# file = open("my_name")            # with this method u must close the file
# contents = file.read()
# print(contents)
# file.close()
# "../" is used to move one step up in a file system
#  the absolute directory "/home/adoneg/Desktop/my_name" has as relative directory from
# "home/adoneg/Documents/Python Programming/myProjects/AI_Projects/100DaysOfPythonCode/Day24/rea"
# to be "../../../../../../Desktop/my_name"


with open("../../../../../../Desktop/my_name", mode= "r") as file:  # with this method file closes automatically after operation
    contents = file.read()
    print(contents)

# home/adoneg/Documents/Python Programming/myProjects/AI_Projects/100DaysOfPythonCode/Day24/rea
# Writing to a file

# file = open("my_name", mode="w")
# contents = file.write("Hey Ado")
# print(contents)
# file.close()

# with open("my_name", mode="a") as file:
#     contents  = file.write("\nNew chat")
#     print(contents)


# Create new file

# with open("high_score.txt", mode='w') as file:
#     contents = file.write("")
