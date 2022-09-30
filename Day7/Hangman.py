
from ctypes.wintypes import WORD
from random import random

import random
from hangman_art import  stages, logo
from Hangman_words import word_list

# index = random.randint(0,2)
# chosen_word = ''
# for word in word_list[index]:
#     chosen_word += word 

chosen_word = random.choice(word_list)

lenght_of_chosen_word = len(chosen_word)

dash_list = []


#for _ in chosen_word:
for lenght in range(lenght_of_chosen_word):
    dash_list += "_"


end_game = False
lives = 8
prev_guess = ''
print(logo)
while not end_game:
    guess = (input("Guess a letter:\n")).lower()
    if prev_guess != guess:
        prev_guess = guess
    else:
        print("You already guessed this letter")
    for position in range(lenght_of_chosen_word):
        letter = chosen_word[position]
        if letter == guess:
            dash_list[position] = guess
    
    if guess not in chosen_word:
     print(f" Your guess, {guess} is not in the chosen word, you loose a life!")
     lives -= 1
     #Reversed_stages = stages.reverse()
     print(stages[lives])
     
     if lives == 0:
        end_game = True
        print(f"You loose!")
    
    print(dash_list)

    if "_" not in dash_list:
        end_game = True
        print(f"You Win! hureeeeey!")

