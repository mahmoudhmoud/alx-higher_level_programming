#!/usr/bin/python3

"""iwa lkah """


class Rectangle:
    """man lkah """
    def __init__(self, width=0, height=0):
        """iwa lkah tam"""
    self.height = height
        self.width = width

    @property
    def width(self):
        """ bhal li tam"""
        return self.__width

    @width.setter
    def width(self, value):
        """mantam"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """dih lih"""
        return self.__height

    @height.setter
    def height(self, value):
        """khodo mano"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
