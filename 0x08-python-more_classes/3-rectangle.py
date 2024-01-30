#!/usr/bin/python3

"""cho mah"""


class Rectangle:
    """sawbo tama ma tam"""
    def __init__(self, width=0, height=0):
        """mano mtalat"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """lkah tam"""
        return self.__width

    @width.setter
    def width(self, value):
        """galso tama hdah"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """kodo"""
        return self.__height

    @height.setter
    def height(self, value):
        """nit tam"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """mani lif"""
        return self.__width * self.__height

    def perimeter(self):
        """jao lih"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """mtalat"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
