from summation_check import summation

def test_summation_func():

	assert summation(1, 2, 3, 4, 5) == 15

	assert summation(11, 12, 13, 14, 15) == 65

	assert summation(11, 11, -31,) == -9