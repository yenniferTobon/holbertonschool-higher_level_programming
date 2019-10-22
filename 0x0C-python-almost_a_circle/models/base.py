#!/usr/bin/python2
import json
"""Module Base
"""


class Base():
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class
            Args:
                id (int): unique id of the classes
        """
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
            Args:
                list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
            Args:
                cls: belonging class
                list_objs: list of instances who inherits of Base - example:
                            list of Rectangle or list of Square instances
        """
        new_dict = []
        with open(cls.__name__ + ".json", "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string("[]"))
            else:
                for obj in list_objs:
                    new_dict.append(obj.to_dictionary())
                f.write(Base.to_json_string(new_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
            Args:
                json_string: string representing a list of dictionaries
        """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
            Args:
                cls: belonging class
                **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(8, 8)
        elif cls.__name__ == "Square":
            dummy = cls(8)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
            Args:
                cls: belonging class
        """
        new_list = []
        filename = str(cls.__name__) + ".json"

        with open(filename, "r", encoding="UTF-8") as f:
            for dict in Base.from_json_string(f.read()):
                new_list.append(cls.create(**dict))
            return new_list
