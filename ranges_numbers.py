def ranges(number):
	minimum_num = number[0]
	for numb in number:
		if numb < minimum_num:
			minimum_num = numb
	maximum_num = number[0]
	for numb in number:
		if numb > maximum_num:
	 		maximum_num = numb
	return maximum_num - minimum_num