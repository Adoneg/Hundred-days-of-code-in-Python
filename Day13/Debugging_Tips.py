# def my_function():
#     for i in range(1,20 + 1):
#         if i == 20:
#             print(f"{i} You go it")
    
# my_function()

# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(6,9)
# print(dice_imgs[dice_num])

#play computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("Your are a millenial.")
# elif year >=1994:
#     print("You are a Gen Z.")

# age = int(input("How old are you?"))
# if age > 18:
#  print(f"You can drive at age {age}")

#Print is your friend
# from textwrap import wrap


# pages = 0
# word_per_page = 0
# pages = int(input("number of pages: "))
# word_per_page = int(input("Number of words per page: "))

# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#use a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,4,8,12])
#run your code many times as u progress
#''''
# Take a rest
# Ask a colleague or friend
# Use stackOverflow'''