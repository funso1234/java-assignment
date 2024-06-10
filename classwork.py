def find_length(calculator):
    #if type(calculator) in(str):
       # raise TypeError("calculator must be iterable")

    count = 0
    for i in calculator:
        count += 1
    return count

display = "calculator"
print(find_length(display))

