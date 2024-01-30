#!/usr/bin/python3
"""lawal tar"""


class Rectangle:
    """tay warih"""
    def __init__(self, width=0, height=0):
        """nazlo"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """nit tam"""
        return self.__width

    @width.setter
    def width(self, value):
        """tam nit"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """twil fihom nit"""
        return self.__height

    @height.setter
    def height(self, value):
        """twil fihom mh sat"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """awad sawbo kdah"""
        return self.__width * self.__height

    def perimeter(self):
        """lawala tanya li tam nit"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """fih lih"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """jo tam"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """katbo walo"""
        print("Bye rectangle...")
