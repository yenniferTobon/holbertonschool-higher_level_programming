#!/usr/bin/python3
class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, heigth=0):
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value
