#!/usr/bin/python3

"""nit zat"""


class Rectangle:
    """thne nit"""

    number_of_instances = 0
    """tam fih"""

    print_symbol = '#'
    """mah fih"""

    def __init__(self, width=0, height=0):
        """idan tam lih"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """chof lih"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """cho lih walo"""
        return self.__height
