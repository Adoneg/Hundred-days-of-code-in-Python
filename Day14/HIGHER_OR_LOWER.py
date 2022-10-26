from sympy import re
from art import  logo, vss
from dataset import data
import random
from replit import clear
def format_data(account):
    '''format accunt data ''' 
    account_name = account['name']
    account_descr = account["description"]
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes user guess and follower count and check if the user is correct"""
    if a_followers > b_followers:
        return guess == 'a' #check if guess == a and return True else returns False
    else:
        return guess == 'b'



#display art
print(logo)
score = 0
account_b = random.choice(data)

 #make the game repeatable
game_should_continue = True

while game_should_continue:
    #display randome account
    account_a = account_b  #Making the account at B move to A
    account_b = random.choice(data)
    while  account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vss)
    print(f"Against B: {format_data(account_b)}.")

    #Ask user for a guess
    guess = input("Who has more followere? Type 'A' or 'B'").lower()
    #get th follower count of eah account
    # use if statement to check
    a_follower_account = account_a['follower_count']
    b_follower_account = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_account, b_follower_account)
    #clear screen
    clear()
    print(logo)
    
    #check if user is correct
    if is_correct:
        #keep track of user score
        score += 1
        print(f"Your right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's cowrong. Final score: {score}")

    

 
