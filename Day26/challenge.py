numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [n**2 for n in numbers]

# print(squared_numbers)

# result = [number for number in numbers if number % 2 == 0]
# print(result)

with open("file1") as file1:
    # file1_list = file1.read().split()
    file1_list = file1.readlines()


with open("file2") as file2:
    # file2_list = file2.read().split()
    file2_list = file2.readlines()

# for n in file1_list:
#     if n in file2_list:
#         common_members.append(int(n))

# list comprehension equivalent

common_members = [int(num) for num in file1_list if num in file2_list]
print(common_members)
