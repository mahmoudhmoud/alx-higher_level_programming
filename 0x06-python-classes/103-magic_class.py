#!/usr/bin/python3

"""tom dartoh"""

import math


class MagicClass:
    """daira"""

    def __init__(self, radius=0):
        """diro tam"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ado lih"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """tim nit"""
        return (2 * math.pi * self.__radius)
