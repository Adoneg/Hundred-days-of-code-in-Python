def add(*adds):  # *args or *something it is called unlimited positional argument it
    #  is way to tell a function to accept any amount of arguments
    sum = 0
    for n in adds:
        sum += n
    return sum

print(add(4, 2, 2, 8, 1, 9, 9))

