MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    '''takes ordered ingredients and returns boolean depending on available resources'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            return False
        else:
            return True


def calc_tot_coins():
    '''returns the total coin'''
    print("Input coins")
    total = 0
    total = int(input("How many quarters?:\n")) * 0.25
    total += int(input("How many dimes?:\n")) * 0.10
    total += int(input("How many nickles?:\n")) * 0.05
    total += int(input("How many pennies?:\n")) * 0.01
    return total


def transaction(input_amount, drink_cost):
    if input_amount >= drink_cost:
        balance = round(input_amount - drink_cost, 2)
        print(f"Your balance is ${balance}")
        print(f"The waiter will give your drink in a jiffy. Thanks")
        global profit
        profit = drink_cost
        return True
    else:
        print("Sorry! the amount you have put is small.")
        return False


def make_coffee(drink_name, ordered_ingredients):
    '''takes in the choice and ordered ingredients. reset the resources by removing the ordered ingredients'''
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"here is your {drink_name}...enjoy")


is_on = True
while is_on:
    choice = input("what would you like?(espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':

        print(f"water:{resources['water']}\n milk:{resources['milk']}\n coffee:{resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            total_coins = calc_tot_coins()
            print(total_coins)
            cost = drink["cost"]
            if transaction(total_coins, cost):
             make_coffee(choice, drink['ingredients'])
        else:
            print("Resources are insufficient")
