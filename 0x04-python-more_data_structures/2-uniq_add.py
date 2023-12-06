#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for item in set(my_list):
        add += int(item)
        return add

