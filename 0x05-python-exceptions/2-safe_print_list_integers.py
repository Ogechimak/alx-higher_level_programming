#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        flag = 0
        while i < x:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                i += 1
            else:
                i += 1
                flag += 1
        print()
        return i - flag
    except IndexError:
        raise
