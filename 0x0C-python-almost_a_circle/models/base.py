#!/usr/bin/python3
""" A base class from where all the others will inherit from
"""

import json
import csv


class Base:
    """ The base class for the almost a circle project
    """

    __nb_objects = 0
    # This will only give the number of objects without ids

    def __init__(self, id=None):
        """ The constructor for the class and assigns an id to itself
        """

        if (id is not None):
            self.id = id
            self.check = True
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
            self.check = False

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json representation of list_dictionaries
        """

        if (list_dictionaries is None):
            return ('[]')
        elif (list_dictionaries is not None):
            for i in list_dictionaries:
                if (type(i) is not dict):
                    return ('[]')
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

    def __del__(self):
        """ Define a deleter method for this object
        """

        if (self.check):
            __nb_objects -= 1

    @classmethod
    def load_from_file_csv(cls):
        """Deserializing in csv"""

        filename = "{}.csv".format(cls.__name__)
        list_dicts = []
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
                for row in csv_reader:
                    row_dicts = {key: int(val) for key, val in row.items()}
                    list_dicts.append(row_dicts)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This method opens a window and draws all the Rectangles and Squares
        """

        turtl = turtle.Turtle()
        turtl.screen.bgcolor("#fff")
        turtl.pensize(2)
        turtl.shape("turtle")
        turtl.color("orange")
        for r in list_rectangles:
            turtl.showturtle()
            turtl.up()
            turtl.goto(r.x, r.y)
            turtl.down()
            for i in range(2):
                turtl.fd(r.width)
                turtl.rt(90)
                turtl.fd(r.height)
                turtl.lt(90)
            turtl.ht()

        turtl.exitonclick
