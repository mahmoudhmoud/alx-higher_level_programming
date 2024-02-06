#!/usr/bin/python3

"""modaj d"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """issam"""
    def __init__(self, size):

        """aykadam"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        """tarik alih"""
        return self.__size ** 2

    def __str__(self):

        """jao ft"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
