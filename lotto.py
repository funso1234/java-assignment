print('Welcome to guess game')

LUCKY_NUMBER = 7

for count in range (3):

	number = int(input("Enter the lucky number: "))

	if number == LUCKY_NUMBER:
	
		print("You've won")

		break

	else:

		print("You're a loser")


