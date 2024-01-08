#!/usr/bin/python3
"""A class that inherits from int"""
class MyInt(int):
    """class that inherits from int"""
    def __eq__(self, other):
        """method is overridden to invert the behavior of the '==' operator"""
        return not super().__eq__(other)
    def __ne__(self, other):
        """methd is overridden to invert the behavior of the '!=' operator"""
        return not super().__ne__(other)
