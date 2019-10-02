#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (type(position) != tuple or
                len(position) != 2 or
                type(position[0]) != int or
                type(position[1]) != int or
                position[0] < 0 or
                position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ square area """
        return self.__size * self.__size

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for l in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
