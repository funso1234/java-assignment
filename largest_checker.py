def largest(number1, number2, number3):
	largest = number1
	if number2 > largest:
		largest = number2
	if number3 > largest:
		largest = number3
	return largest



def smallest(number1, number2, number3):
	smallest = number1
	if number2 < smallest:
		smallest = number2
	if number3 < smallest:
		smallest = number3
	return smallest
