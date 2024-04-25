def add_ing_ly(string):

    if len(string) < 3:

        return string

    elif string[-3:] == 'ing':

        return string + 'ly'

    else:

        return string + 'ing'

sample_strings = ['abc', 'string', 'on']

for string in sample_strings:

    print(f"Sample String: '{string}'")

    print(f"Expected output: '{add_ing_ly(string)}'")