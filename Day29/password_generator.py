# Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_gen():
    """returns random password"""
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    # OR
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]
    # OR
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    number_list = [random.choice(numbers) for char in range(nr_numbers)]
    # OR
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_list = letter_list + symbols_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list) # separates elements in the iterable by "" or any string
    # password = ""
    # for char in password_list:
    #     password += char

    return password
