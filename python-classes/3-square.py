#!/usr/bin/python3
''' defined a class.'''
class Square:
    '''Initialized the parameters.'''
    def__init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.size = size
        ''' created a public instance method.'''
    def area(self):
        '''Return the current area of the square.'''
        return (self.__size * self.__size)
