#!/usr/bin/python3
"""
This module contains the classes:
-BaseGeometry.
-Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializer for the square class.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Method called when using print()
        """
        return "{} {}/{}".format("[Square]", self.__size, self.__size)
