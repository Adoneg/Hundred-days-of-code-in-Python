# # Ex1: Facebook Likes
# facebook_post = [   # list of dictionaries
#     {'Likes': 21, 'Comments': 2},
#     {"Likes": 13, "Comments": 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Likes': 19, "Comments": 3}
# ]
# total_likes = 0
#
# for post in facebook_post:
#     try:
#         total_likes = total_likes + post["Likes"]
#     except KeyError:
#         total_likes = total_likes
# print(f"total_likes:{total_likes}")
#

# Ex2: Nato phonetics
# TODO 1. Create a dictionary in this format:

import pandas

# reading csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# creating dataframe
df = pandas.DataFrame(data)
# creating a dictionary from dataframe
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# the nato phonetic list

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
not_error = True
while not_error:
    try:
        user_words = input("Enter a phrase:\n").upper()
        phonetic_list = [phonetic_dict[letters] for letters in user_words]
    except KeyError as error:
        print(f"the key {error} is not allow, please enter text:\n")
    else:
        print(phonetic_list)
        not_error = False
