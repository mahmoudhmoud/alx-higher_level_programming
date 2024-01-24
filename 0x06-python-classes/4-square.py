#!/usr/bin/python3

"""daknit"""


class Square:
    """lkah"""

    def __init__(self, size=0):
        """lidaro fih"""
        self.size = size

    @property
    def size(self):
        """mcha maah"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """fih nit"""
        return self.__size ** 2
