from random import randint
print(f"Welcome to the Guessing Game!\n I'm thinking of a number between 1 and 100")


actual_number = randint(1,100)

def easy():
    attempts = 10
    print("You have 10 attempts remaining to guess the number")
    while attempts > 0:
        guess = int(input("Guess a number: "))
        if guess > actual_number:
            attempts -= 1
            print(f"To high.\n you have {attempts} attempts to guess the right number")

        elif guess < actual_number:
            attempts -= 1
            print(f"To low.\n you have {attempts} attempts to guess the right number")

        else:
            print("You win! congratulations")
            break
        if attempts == 0:
         print(f"The actual number is {actual_number}")
         print("You have exhausted all you attempts")
    
def hard():
    attempts = 5
    print("You have 5 attempts remaining to guess the number")
    while attempts > 0:
        guess = int(input("Guess a number: "))
        if guess > actual_number:
            attempts -= 1
            print(f"To high.\n you have {attempts} attempts to guess the right number")

        elif guess < actual_number:
            print(f"To low.\n you have {attempts} attempts to guess the right number")

            attempts -= 1
        else:
            print("You win! congratulations")
            break
        if attempts == 0:
         print(f"The actual number is {actual_number}")
         print("You have exhausted all you attempts")
    
def play_guessing_game():
    difficulty = input("Choose difficulty level: 'easy' or 'hard':\n").lower()

    if difficulty == 'easy':
        easy()
    elif difficulty == 'hard':
        hard()
play_guessing_game()

play_again = input("Do you want to play again? 'y' or 'n': ").lower()

if play_again == 'y':
    play_guessing_game()
