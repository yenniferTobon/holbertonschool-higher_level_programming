#!/usr/bin/python3
"""Module to inherit from Base"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of the Rectangle class
            Args:
                width (int): rectangle width
                height (int): rectangle height
                x (int): space left
                y (int): space above
                id (int): unique id
        """
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
        """Width setter
        """
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
        """Width setter
        """
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
        """X setter
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Funtion to return area - taks 4"""
        return self.__width * self.__height

    def __str__(self):
        """Funtion to print info - task 6
           Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

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

    def update(self, *argv, **kwargs):
        """Assigns an argument to each attribute or assigns a key/value
            argument to attributes
            Args:
                *args: pointer to a argument list
                **kwargs: double pointer to a dictionary: key/value
        """
        attrib = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(argv)):
            setattr(self, attrib[i], argv[i])

        if kwargs is not None:
            for i in range(len(attrib)):
                if attrib[i] in kwargs:
                    setattr(self, attrib[i], kwargs.get(attrib[i]))

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        """
        dict = {}
        for key, value in vars(self).items():
            dict[key.replace("_Rectangle__", "")] = value
        return dict
