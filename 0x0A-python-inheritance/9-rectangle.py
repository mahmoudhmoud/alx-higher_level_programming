#!/usr/bin/python3

"""namod jal"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """wahad mano"""
    def __init__(self, width, height):

        """bnah"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        """tarika"""
        return self.__width * self.__height

    def __str__(self):

        """ktab to"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
