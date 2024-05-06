from palin import palindrome


def test_palindrome_Strings():

	assert palindrome("madam") == True
	assert palindrome("11111") == True
	assert palindrome("sammy") == False
	assert palindrome("12345") == False