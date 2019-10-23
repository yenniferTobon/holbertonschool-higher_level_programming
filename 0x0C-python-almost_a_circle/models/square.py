#!/usr/bin/python3
"""Module to inherit from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of the Square class
            Args:
                size (int): square size
                x (int): space left
                y (int): space above
                id (int): unique id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter to size"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>
        """
        return '[{}] ({}) {}/{} - {}'.format(
                self.__class__.__name__, self.id, self.x, self.y, self.width)

    def update(self, *argv, **kwargs):
        """Assigns attributes -task 8
            Args:
                *args: pointer to a argument list
                **kwargs: double pointer to a dictionary: key/value
        """
        attrib = ['id', 'size', 'x', 'y']
        for i in range(len(argv)):
            setattr(self, attrib[i], argv[i])

        if kwargs is not None:
            for i in range(len(attrib)):
                if attrib[i] in kwargs:
                    setattr(self, attrib[i], kwargs.get(attrib[i]))

    def to_dictionary(self):
        """Returns the dictionary representation of a Square
        """
        dict = {}
        for key, value in vars(self).items():
            if key is "_Rectangle__width":
                key = key.replace("width", "size")
            elif key is "_Rectangle__height":
                key = key.replace("height", "size")
            dict[key.replace("_Rectangle__", "")] = value
        return dict
