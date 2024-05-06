def square(number):

	return number ** 2

print(square(8))
print(square(89))
print(square(12))


def menu():
	print("""
	1. phone book
	2. message
	""")

menu()



def add(a, b=7):
	answer = a + b
	return answer

print(add(4, 5))
print(add(7, 8))
print(add(12, 13))
print(add(5))








def summationx(numbers, x):
	"""this function sums a positional lists
	argument and a number
	positional args numbers comes first
	by the number"""
	total = 0
	for i in numbers:
		total += i
	return total + x
print(summationx(x=50, numbers=[10, 20, 25, 15, 30]))