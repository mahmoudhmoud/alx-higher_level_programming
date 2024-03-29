#!/usr/bin/python3

"""dat tak"""


class Rectangle:
    """wafih"""
    def __init__(self, width=0, height=0):
        """tabto fih"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """lkah tam"""
        return self.__width

    @width.setter
    def width(self, value):
        """galas maah"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """chof tam"""
        return self.__height

    @height.setter
    def height(self, value):
        """nawao"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ado tam"""
        return self.__width * self.__height

    def perimeter(self):
        """awasd talto tam"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ota hana"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """dala wafo"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
