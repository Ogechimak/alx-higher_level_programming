#!/usr/bin/python3

"""Square module: The class 'Square' contains a Square object"""


class Square:
    """ square class

    this is a square class with a private instance attribute 'size'.

    """
    def __init__(self, size):
        """ __init__ method

        this method is a special method that acts as an instance
        constructor after instantiation

        Args:
            size (int): <size> is a private attribute of type integer.

        """
        self.__size = size
