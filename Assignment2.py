number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

sum = number1 + number2 + number3

product = number1 * number2 * number3

average = number1 + number2 + number3 / 3

smallest = number1

if number2 < smallest:

	smallest = number2

if number3 < smallest:

	smallest = number3

print('smallest value is', smallest)

largest = number1

if number2 > largest:

	largest = number2

if number3 > largest:

	largest = number3

print('sum is', sum)

print('product is', product)

print('average is', average)

print('largest value is', largest)

