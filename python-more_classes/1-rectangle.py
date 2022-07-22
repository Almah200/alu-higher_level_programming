#!/usr/bin/python3
'''Defined a class Rectangle.'''


class Rectangle:
    '''Represent a class.'''

    def __init__(self, width=0, height=0):
        '''Initialize a rectangle parameters.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        '''
        self.width = width
        self.height = height

    @Property
    def width(self):
        '''Get width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @Property
    def lenght(self):
        '''get the height of the rectangle.'''
        return self.__height

    @height.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.height = value
