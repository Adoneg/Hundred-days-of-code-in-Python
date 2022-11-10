
# syntax
try:
    pass
    # testing code
except KeyError: #specify the type of error else it just work for every error
    # if test code generates specified error
    pass
else:
     # if test works
finally:
    pass
    # whether test fails or not
    raise # enter error type (keyError, ValueError etc)

# Example

try:
    file = open("a_file.txt") # generates FileNotFoundError
    dictionary = {"key": "value"} # generates KeyError
    print(dictionary["name"])
except FileNotFoundError:
    print(f"this file is not found")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    file.read()
finally:
    # file.close()
    raise KeyError ("this key does not exist")


# application: calculating BMI
height = float(input("Height:\n"))
weight = input("Weight:\n")
if height > 3:
    raise ValueError("Height cannot be more than 3")

bmi = weight/height**2
print(bmi)
