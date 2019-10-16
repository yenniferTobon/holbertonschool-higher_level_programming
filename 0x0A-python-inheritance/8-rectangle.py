#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module contains the classes:
-BaseGeometry.
-Rectangle.
"""


class Rectangle(BaseGeometry):
    """
    Class that defines basic geometries.
    """
    def __init__(self, width, height):
        """
        Initializer for the rectangle class.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
