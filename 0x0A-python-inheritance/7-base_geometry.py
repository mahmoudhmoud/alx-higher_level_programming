#!/usr/bin/python3

"""namjad lih"""


class BaseGeometry:

    """asas dyalo"""
    def area(self):

        """rika mano"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):

        """tarika dyal"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
