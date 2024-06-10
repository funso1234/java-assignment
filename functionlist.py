

def check_list(sammy):
    even_numbers = []
    for numbers in sammy:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
    return even_numbers

def even_list2(sammy):
    return [number for number in sammy if number % 2 == 0]
#even = [number for number in range(1, 51) if number % 2 == 0]


numbers = list(range(1, 51))
print(numbers)
print(check_list(numbers))
print (even_list2(numbers))


