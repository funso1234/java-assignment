import random

print('Welcome to guess game')

LUCKY_NUMBER = random.randrange(1, 10)

number = int(input("Enter the lucky number"))

 
while number != LUCKY_NUMBER:

	number = int(input("Enter the lucky number: "))

	if number == LUCKY_NUMBER:
	
		print("You've won")

		break

	else:

		print("You're a loser")


