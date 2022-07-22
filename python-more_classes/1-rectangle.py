#!/usr/bin/python3
'''
Define a rectanle:
set a private instance attribute lenght and width
set property setter and getter for width and lenght
'''
class Rectangle:
    '''.instantiation  a class.'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        ''' set width getter function.'''
        @Property
    def width(self):
        return self.__width
    '''set width setter function.'''
    @width.settter
    def width(self, width):
        self.__width = width
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        '''set height getter function.'''
         @Property
    def lenght(self):
        return self.__height
    '''set height setter function.'''
    @height.settter
    def width(self, value):
        self.height = height
        if not isinstance(width, int):
            raise TypeError('height must be an integer')
        elif width < 0:
            raise ValueError('height must be >= 0')
