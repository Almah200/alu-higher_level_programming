#!/usr/bin/python3
"""
define a square by:
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be int, raise TypeError exception(message size must be an integer)
if size is < 0, raise ValueError exception(message size must be >= 0)
Public instance method: def area(self): returns the current square area
You are not allowed to import any module
"""
''' defined a class.'''
class Square:
    '''Represent a square.'''
    def__init__(self, size=0):
        '''Raising and mananging errors.'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.size = size
        '''created area function.'''
    def area(self):
        '''Return the current area of the square.'''
        return (self.__size * self.__size)
