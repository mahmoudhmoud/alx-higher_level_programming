#!/usr/bin/python3

'''nawp mano'''


class Rectangle:
    '''had daraja'''

    number_of_instances = 0
    '''mano ltam'''

    print_symbol = '#'
    '''naao'''

    def __init__(self, width=0, height=0):
    '''marka dyalo'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''khat tam'''
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
        '''daw h lih tam'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''malo lih'''
        return self.width * self.height

    def perimeter(self):
        '''sado mno tam lih'''
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        '''nit iktih'''
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        '''tal tam nit'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        '''tam nit lih'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
