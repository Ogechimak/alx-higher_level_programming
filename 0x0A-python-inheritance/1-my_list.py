#!/usr/bin/python3
"""Class that inherits from list"""
class MyList(list):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
"""print the list in a sorted order"""
def print_sorted(self):
    copy = self.copy()
    copy.sort()
    print(copy)
