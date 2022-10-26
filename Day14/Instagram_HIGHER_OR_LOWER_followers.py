from sympy import dsolve
from dataset import data
from random import choice
from replit import  clear
from art import vss
from art import logo


def account_1_printer(name, description, country):
    return f"{name}, {description} from {country}"


def account_2_printer(name, description, country):
    return f"{name}, {description} from {country}"

def compare(follow_count1, follower_count2):
    if follow_count1 > follower_count2:
        return 'a'
    else:
        return "b"

def higher_lower_game():
    
    #create a boolean to hold game state
    is_game_over = False
    # repeat again else print user score 
    current_score = 0
    print(logo)
    while not is_game_over:
        #read randomly from a list two indices to get two dictionaries
        account_1 = choice(data)
        account_2 = choice(data)

    #read the name, country and description and print
        name_1 = account_1['name']
        name_2 = account_2['name']
    #description
        description_1 = account_1['description']
        description_2 = account_2['description']
    #country
        country_1 = account_1['country']
        country_2 = account_2['country']

    #Read follower_counts
        follower_count_1 = account_1['follower_count']
        follower_count_2 = account_2['follower_count']

        print(f"Compare A:{name_1}, {description_1}, from {country_1}")
        print(vss)
        print(f"Compare B:{name_2}, {description_2}, from {country_2}")

        user_ans = input("Who has more followers? type 'A' or 'B':\n").lower()
        if user_ans == compare(follower_count_1, follower_count_2):
            clear()
            current_score += 1
            print(f"You are right! your current score is:{current_score}")
        else:
            is_game_over = True
            print(f"Your final score is:{current_score}")

higher_lower_game()

# ask user if want to play again

play_again = input("Try again? 'y' or 'n': ").lower()

if play_again == 'y':
    clear()
    higher_lower_game()

            

