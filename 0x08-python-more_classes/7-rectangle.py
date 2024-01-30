#!/usr/bin/python3

'''nawao'''


class Rectangle:
    '''hada nit'''

    number_of_instances = 0
    '''man tam'''

    print_symbol = '#'
    '''nawo lih'''

    def __init__(self, width=0, height=0):
        '''mano ltam'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''tama lih'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''milkya mano'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''man hadak'''
        return self.width * self.height

    def perimeter(self):
        '''malo lih'''
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        '''malak lih'''
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        '''dih lih'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        '''ayat lih'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
