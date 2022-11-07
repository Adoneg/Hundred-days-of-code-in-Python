
list = [1, 2, 3]
new_list = []
for item in list:
    add = + 1
    new_list.append(add)

# List comprehension equivalent syntax
new_list = [new_item for item in list]
# More examples
# 1
numbers = [1, 2, 3]

new_numbers = [item + 1 for item in numbers]
# 2
name = "Angela"
# creating  a list from every letter of the name Angela
new_list = [letter for letter in name]
# 3
# doubling every number in the range(1,5)
new_range = [n + n for n in range(1, 5)]

# 4
# # creating the names list
names = ["miriam", "Ajoh", "Lyoni", "Afeh", "Preciouse"]

# 5
# selecting short names from the names array above
short_names = [name for name in names if len(name)<5]

# 6
# writing the longer name in names as upper case
long_cap_names = [name.upper() for name in names if len(name) > 4]

# Dictionary comprehension
names = ["miriam", "Ajoh", "Lyoni", "Afeh", "Preciouse"]
import random
# looping thru a list
# dict = {item: item_value for item in list}
random_score = {student: random.randint(1, 100) for student in names}
# output
# {'miriam': 42, 'Ajoh': 92, 'Lyoni': 3, 'Afeh': 53, 'Preciouse': 65}

# looping through a dictionary
passed_students = {key: value for (key, value) in random_score.items()}
# Output
# {'miriam': 42, 'Ajoh': 92, 'Lyoni': 3, 'Afeh': 53, 'Preciouse': 65}

# looping thru a dictionary with condition
passed_students = {key: value for (key, value) in random_score.items() if value >= 60}

# Output
{'Ajoh': 92, 'Preciouse': 65}

# Looping thru a Pandas dataframe

student_score = {
    'student': ["miriam", "Ajoh", "Lyoni", "Afeh", "Preciouse"],
    'scores' : [24, 44, 33, 22, 11,]
}

# for(key, value) in student_score.items():
#     print(key)

# creating a dataframe
import pandas
student_score_dataframe = pandas.DataFrame(student_score)
for(index, row) in student_score_dataframe.iterrows():
    if row.student == "miriam":
        print(row.student)

# creating a dict from a dataframe
# new_list = [index.sth: row.sth for(index, row) in dataframe.iterrows()]
