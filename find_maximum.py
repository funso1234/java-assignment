def find_maximum(numbers):
    
    maximum = numbers[0]
    
    for num in numbers:
    
        if num > maximum:

            maximum = num
    
    return maximum

numbers = [8, 4, 9, 2, 5, 7, 3]

print(find_maximum(numbers))