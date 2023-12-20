#!/usr/bin/python3

import math

class MagicClass:
    """Magic class.
    
    This class carries out some calculations.
    """

    def __init__(self, radius=0):
        """Initialize instances of a class."""
        self.__radius = 0
        
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Calculate area of a circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference of a circle."""
        return 2 * math.pi * self.__radius
