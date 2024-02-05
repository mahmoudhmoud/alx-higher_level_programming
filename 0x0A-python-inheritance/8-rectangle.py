#!/usr/bin/python3

"""lih mod"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """hat kisam"""
    def __init__(self, width, height):

        """tika to"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
