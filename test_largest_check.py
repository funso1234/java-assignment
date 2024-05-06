from largest_checker import largest, smallest


def test_largest_number():

	assert largest(4, 6, 9) == 9
	
	assert largest(7, 10, 90) == 90

	assert largest(41, 16, 19) == 41



def test_smallest_number():

	assert smallest(4, 6, 9) == 4

	assert smallest(7, 10, 90) == 7

	assert smallest(41, 16, 19) == 16

