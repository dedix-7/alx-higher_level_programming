#!/usr/bin/python3
""" A base class from where all the others will inherit from
"""

import json
import csv


class Base:
    """ The base class for the almost a circle project
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """ The constructor for the class and assigns an id to itself
        """

        if (type(id) is not None):
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json representation of list_dictionaries
        """

        if (list_dictionaries is None):
            return ([])
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ write a jsonm string rep to a file
        """

        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as fildes:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = [obj.to_dictionary() for onj in list_objs]
                f.write(Base.to_json_string(json_string))
    @staticmethod
    def from_json_string(json_string):
        """ Returns the liost of json representation from json string
        """

        if json_string is None:
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returnd an instance with set attributes
        """

        if dictionary and (dictionary != {}):
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances
        """

        filename = f"{cls.__name__}.csv"
        lists_dict = []
        try:
            with open(filename, 'r', newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ['id', 'width', 'height', 'x', 'y']
                else:
                    field_names = ["id", "size", "height","x","y"]
                csv_read = csv.DictReader(csv_file, fieldnames=field_names)
                for name in csv_read:
                    row_dicts = {key, int(val) for key, val in name.items()}
                    lists_dicts.append(row_dicts)
                return [cls.create(**d) for d in lists_dicts]
        except IOError:
            return []
        
