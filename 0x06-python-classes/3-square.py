#!/usr/bin/python3

"""kidayar"""


class Square:
    """kado"""

    def __init__(self, size=0):
        """tam nit"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """fih nit"""
        return self.__size
