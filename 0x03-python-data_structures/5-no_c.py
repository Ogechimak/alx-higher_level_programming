#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for elements in my_string:
        if elements not in 'cC':
            new_string.append(elements)
            return ''.join(new_string)
