#!/usr/bin/python3

""" ha chof"""


class Rectangle:
    """katariha"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ bad ls"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """kat mhiha"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ma tam"""
        return self.__width

    @width.setter
    def width(self, value):
        """glas tam foh"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """kbir tam hdad"""
        return self.__height

    @height.setter
    def height(self, value):
        """li tam nit"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """jo hna"""
        return self.__width * self.__height

    def perimeter(self):
        """do lih"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """likay taktab fih tam"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """awd kado"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
