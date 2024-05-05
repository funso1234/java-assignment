
def word_checker(alphabet):

	vowel = 0

	consonant = 0
	
	for i in range(len(alphabet)):

		
		if alphabet[i] == 'a' or alphabet[i] == 'e' or alphabet[i] == 'i' or alphabet[i] == 'o' or alphabet[i] == 'u':

			vowel += 1
		else:
			consonant += 1
	print('vowel', vowel, "consonant", consonant)

print(word_checker('String'))