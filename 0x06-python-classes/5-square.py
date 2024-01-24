#!/usr/bin/python3

"""chof"""


class Square:
    """lkah"""

    def __init__(self, size=0):
        """eih lih nit"""
        self.size = size

    @property
    def size(self):
        """ah dik ni ochof"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """mintakto nit"""
        return self.__size ** 2

    def my_print(self):
        """katbo"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
