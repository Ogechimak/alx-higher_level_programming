#!/usr/bin/python3

"""Square module: this class <Square> models a Square object"""


class Square:
    """ square class

    this class implemeents square class with setters and getters.

    """
    def __init__(self, size=0):
        """ __init__ method

        this method is a special method that acts as an instance
        constructor after instantiation

        Args:
            size (int): <size> is a private attribute of type integer.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area of the square

        this method compute the area of the Square

        Args:
            No Args.

        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        self.__size = value
