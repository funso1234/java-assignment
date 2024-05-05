def word_checker(String_alphabet):

	vowel = [a, e, i, o, u]

	consonant = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, y, z]


	if vowel in alphabet:

		vowel += 1

	else:
		consonant += 1

	print("vowel", vowel, "consonant", consonant)
