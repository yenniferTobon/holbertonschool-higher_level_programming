#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
     
    @property
    def width(self):
        """getter for width"""
        return self.__width
 
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value    
     
    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer") 
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x  must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Funtion to return area - taks 4"""
        return self.__width * self.__height
  
    def display(self):
        """Funtion that prints un Rectangulo with # - task 5""" 
        for row in range(self.__height):
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Funtion to print info - task 6"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """Funtion that prints un Rectangulo with # and empty- task 7"""
        for row_Empty in range(self.__y):
            print()
        
        for row in range(self.__height):
            for empty in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def update(self, *argv):
        """assigns an argument to each attribute - task 8"""
        attrib = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(argv)):
            setattr(self, attrib[i], argv[i])
