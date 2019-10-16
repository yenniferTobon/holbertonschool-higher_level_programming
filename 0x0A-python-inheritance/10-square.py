#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
This module contains the classes:
-BaseGeometry.
-Rectangle.
"""

class Square(Rectangle):
    ""
    Class that defines basic geometries.
    """
    def __init__(self, size):
        """
        Definition of the area of the rectangle.
        """
        super().__init__(size, size)
        self.__size = size
