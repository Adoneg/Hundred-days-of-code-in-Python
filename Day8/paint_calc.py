import math
def paint_cal(height, width):
     return math.ceil((height*width)/5)

height = int(input("Height:\n"))
width = int(input("Width:\n"))

Number_of_cans = paint_cal(height, width)
print(f"your number of cans is {Number_of_cans}")
