#!/usr/bin/python3
'''.defined aclass.'''


class Rectangle(BaseGeometry):
    '''instantiated the class.'''
    def __init__(self, width, height):
        self.__width = isnumeric(width)
        self.__height = isnumeric(height)
