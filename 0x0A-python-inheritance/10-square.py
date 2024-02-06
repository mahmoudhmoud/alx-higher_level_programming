#!/usr/bin/python3

"""nmodaj"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """rakol ti"""
    def __init__(self, size):

        """binae"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        """tarika kado"""
        return self.__size ** 2
