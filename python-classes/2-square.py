#!/usr/bin/python3
'''created a square class.'''
class Square:
    ''' initiated the class.'''
    def__init__(self,size=0):
        '''Initialized  a new square.
        Args:
        size (int): The size of the new square.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >=0')
        self.__size = size
