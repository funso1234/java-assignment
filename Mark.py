score = int(input('Enter the pass mark'))

passmark = 45

if score > passmark:

	print(f'your score is', score, 'passed')

elif score > 80 and score < 100:

	print(f"if your score is above 80", score, 'Your grade is A')

elif score > 65 and score < 79:
	print(f"if your score is above 65", score, 'Your grade is B')

elif score > 50 and score < 64:
	print(f"if your score is above 50", score, 'Your grade is c')

elif score > 40 and score < 49:
	print(f"if your score is above 40", score, 'Your grade is D')

else:  
	print('your score is below 40', score, 'failed') 