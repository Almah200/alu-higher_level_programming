#!/usr/bin/python3
'''created a class.'''


class BaseGeometry:
    ''' public method.'''
    def area(self):
        raise Exception('area() is not implemented')
    '''public instance method.'''
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')

