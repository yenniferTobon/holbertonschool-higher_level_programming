#!/usr/bin/python3
"""Module Base """


import json
import os


class Base():
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class
            Args:
                id (int): unique id of the classes
        """

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
        with open(cls.__name__ + ".json", "w", encoding="UTF-8") as f:
            if list_objs == []:
                f.write('[]')
            new_dict = []
            for obj in list_objs:
                new_dict.append(obj.to_dictionary())
            f.write(cls.to_json_string(new_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
            Args:
                json_string: string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
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

        try:
            with open(filename, "r") as f:
                for dict in Base.from_json_string(f.read()):
                    new_list.append(cls.create(**dict))
                return new_list
        except FileNotFoundError:
            return []
