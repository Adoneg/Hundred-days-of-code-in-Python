
def prime_number_evaluator(number):
    is_a_prime_num = True
    for i in range(2,number): 
        if number%i == 0:
            is_a_prime_num = False
    if is_a_prime_num:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
        
number = int(input("Enter any number:\n"))

prime_number_evaluator(number)