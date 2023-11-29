#!/usr/bin/python3
def print_last_digit(number):
    L_d = abs(number) % 10
    print("{}".format(L_d), end="")
    return (L_d)
