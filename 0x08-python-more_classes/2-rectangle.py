#!/usr/bin/python3

"""atih kasi"""


class Rectangle:
    """taywarih"""
    def __init__(self, width=0, height=0):
        """mo zawi"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """kodo osossi"""
        return self.__width

    @width.setter
    def width(self, value):
        """ma nit"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """mcha lih"""
        return self.__height

    @height.setter
    def height(self, value):
        """litabo"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ada fih"""
        return self.__width * self.__height

    def perimeter(self):
        """fih walo"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
