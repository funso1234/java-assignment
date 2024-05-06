from print import largest_number

def test_largest_number():

	assert largest_number(1, 2, 2, 2, 3) == 3

	assert largest_number(2, 3, 5, 1, 2) == 5