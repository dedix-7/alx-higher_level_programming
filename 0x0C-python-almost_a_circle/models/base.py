#!/usr/bin/python3
""" A base class from where all the others will inherit from
"""
import pickle
import json
import csv
import turtle

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

        if (list_dictionaries is None or len(list_dictionaries) <= 0):
            return ('[]')
        else:
            for i in list_dictionaries:
                if (type(i) is not dict):
                    return ('[]')
        return (json.dumps(list_dictionaries, sort_keys=False))

    @classmethod
    def save_to_file(cls, list_objs):
        """ write a jsonm string rep to a file
        """

        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as fildes:
            if ((list_objs is None) or (len(list_objs) == 0)):
                fildes.write("[]")
            else:
                json_string = [obj.to_dictionary() for obj in list_objs]
                fildes.write(Base.to_json_string(json_string))

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
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This method opens a window and draws all the Rectangles and Squares
        """

        turtl = turtle.Turtle()
        turtl.screen.bgcolor("#ffc0cb")
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
