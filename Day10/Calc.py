
#Add
def add(n1, n2):
    """Takes two numbers and add(+) them"""
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """Takes two numbers and subtract(-) them"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """Takes two numbers and multiply(*) them"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """Takes two numbers and divide(/) them"""
    return n1/n2

math_operation = {
    "-" : subtract,
    "+" : add,
    "*" : multiply,
    "/" : divide

}

num1 = int(input("enter the first number:\n"))
num2 = int(input("enter the second number:\n"))

for operation in math_operation:
    print(operation)

operator = input("choose an operator:\n")

function = math_operation[operator]

result = function(num1, num2)

print(f"{num1} {operator} {num2} = {result}")