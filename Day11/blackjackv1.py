
from random import randint


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def assign_card1():
    card1 = randint(2,11)
    return card1

def assign_card2():
    card2 = randint(2,11)
    return card2


def assign_card3():
    card3 = randint(2,11)
    return card3


def assign_card4():
    card4 = randint(2,11)
    return card4


user_card1 = assign_card1()
user_card2 = assign_card2()
user_card3 = assign_card3()
user_card4 = assign_card4()

user_card_list = [user_card1, user_card2]

user_card_sum = user_card_list[0] + user_card_list[1]
print(f"Your card: {user_card_list}, your current score: {user_card_sum}")
comp_random1 = randint(0,11)
comp_card1 = cards[comp_random1]
comp_random2 = randint(0,11)
comp_card2 = cards[comp_random2]
comp_card_list = [comp_card1]
comp_card_sum = comp_card_list[0]
print(f" computer's first hand: {comp_card_list}")

wants_more_card = input("Type 'y' to get another card, type 'n' to pass:\n").lower()

if wants_more_card == 'y':
    user_card_list.append(user_card3)
    user_card_sum = user_card_list[0] + user_card_list[1] + user_card_list[2]
    print(f"Your card: {user_card_list}, your current score: {user_card_sum}")
    wants_more_card = input("Type 'y' to get another card, type 'n' to pass:\n").lower()

    if wants_more_card == 'y':
         user_card_list.append(user_card4)
         user_card_sum = user_card_list[0] + user_card_list[1] + user_card_list[2] + user_card_list[3]
         print(f"Your card: {user_card_list}, your current score: {user_card_sum}")
         if user_card_sum > 21:
                print(f"    computer's first hand: {comp_card_list}")
                print(f"    Your final hand is: {user_card_list}, your final score is: {user_card_sum}")
                comp_card_list.append(comp_card2)
                comp_card_sum = comp_card_list[0] + comp_card_list[1]   
                print(f"Computer final hand is: {comp_card_list}, final score: {comp_card_sum}")
                if comp_card_sum <= 21:
                 print("You went over, you lose!")
                else:
                    print("Its a draw!")
         else:
            comp_card_list.append(comp_card2)
            comp_card_sum = comp_card_list[0] + comp_card_list[1]   
            print(f"Computer second hand is: {comp_card_list}, wiht a score of: {comp_card_sum}")
            if comp_card_sum <= 21 and comp_card_sum > user_card_sum:
                print("You loose!")
            elif comp_card_sum == user_card_sum:
                print("It is a draw")
            else:
                print("You win")

    elif wants_more_card == 'n':
        print(f"Your final hand is: {user_card_list}, your final score is: {user_card_sum}")
        comp_card_list.append(comp_card2)
        comp_card_sum = comp_card_list[0] + comp_card_list[1]   
        print(f"Computer final hand is: {comp_card_list}, final score: {comp_card_sum}")
        if comp_card_sum <= 21 and comp_card_sum > user_card_sum:
            print("You loose!")
        else:
            print("You win!")
elif wants_more_card == 'n':
        print(f"Your final hand is: {user_card_list}, your final score is: {user_card_sum}")
        comp_card_sum = comp_card_list[0]
        if comp_card_sum < 17:
            comp_card_list.append(comp_card2)
            comp_card_sum = comp_card_list[0] + comp_card_list[1]   
            print(f"Computer final hand is: {comp_card_list}, final score: {comp_card_sum}")
            if comp_card_sum <= 21 and comp_card_sum > user_card_sum:
                print("You loose!")
            elif comp_card_sum == user_card_sum:
                print("It is a draw")
            else:
                print("You win!")
        else:
            print(f"Computer final hand is: {comp_card_list}, final score: {comp_card_sum}")
            if comp_card_sum <= 21 and comp_card_sum > user_card_sum:
                print("You loose!")
            elif comp_card_sum == user_card_sum:
                print("It is a draw")
            else:
                print("You win!")
    

               

