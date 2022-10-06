import  random
from replit import clear
# from turtle import clear
from art import logo 
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def calculate_score(cards):
    '''takes a list and returns the sum'''
    if len(cards) == 2 and sum(cards) == 21:
        return 0
        print("Blackjack")
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if comp_score == user_score:
        return "It is a draw game!"
    elif comp_score == 0:
        return "You loose, since computer has a blackjack"
    elif  user_score == 0:
        return "You win!, you have the blackjack"
    elif user_score > 21:
        return "You loose!, score above 21"
    elif comp_score > 21:
        return "You win!, computer's scores more than 21"
    else:
        sign = comp_score - user_score
        if sign > 0:
            print("you loose!")
        else:
          print("You win!")

def play_blackjack():
    '''This function implements the blackjack game...enjoy!!!'''
    is_game_over = False
    print(logo)
    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your card: {user_cards} and you score:{ user_score}")
        print(f"computer first card: {comp_cards[0]} ")

        if user_score == 0 and comp_score == 0 or user_score > 21:
                is_game_over = True
        else:
            is_game_over = False
            more_cards = input("Enter 'y' to draw another card or 'n' to end:\n").lower()
            if more_cards == 'y':
                user_cards.append(deal_card())
            elif more_cards == 'n':
                    is_game_over = True

    while comp_score != 0 and  comp_score < 17:
            comp_cards.append(deal_card())
            comp_score = calculate_score(comp_cards)
            print(f"Computer score is: {comp_score}")

    print(f"You final score is: {user_score}")
    print(f"Computer's final score is: {comp_score}")

    final_result = compare(user_score, comp_score)
    print(final_result)



while (input("Do you want to play the blackjack game? type 'y' or 'n':\n").lower()) == 'y':
    clear()
    play_blackjack()
    