#!/usr/bin/python3
'''.defined aclass rectangle that inherits from basegeometry.'''
BaseGeometry = __import__('7-base-geometry').BaseGeometry


 def __init__(self, width, height):
     """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
