def element_appearance(string_list):
    display_element = {}
    for string in string_list:
        if string in display_element:
            display_element[string] += 1
        else:
            display_element[string] = 1
    return display_element



