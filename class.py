Amount = int(input("Enter the amount: "))

number_of_years = int(input("Enter the number of years: "))

interest_rate = 0.2


for number in range (1, number_of_years):
	first_amount = Amount * interest_rate

	sum += first_amount

	print(sum)	

