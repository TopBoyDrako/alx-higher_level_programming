#!/usr/bin/python3

"""
This module defines a class with a private and public attribute each
@private attribute = __nb_objects
@public attribute = id

"""


from json import dumps, loads
import csv
import turtle


class Base:
    """
    This class defines a function which manages a public attribute "id"
    in all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the public attribute "id" """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string reprsentation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
                list_of_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_of_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        with open(
                    filename, mode="w", newline="", encoding="utf-8"
                    ) as csv_file:
            csv_writer = csv.writer(csv_file)
            for obj in list_objs:
                csv_writer.writerow([getattr(obj, attr)
                                    for attr in cls.attributes()])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                return [cls.create(**dict(zip(cls.attributes(),
                        map(int, row)))) for row in csv_reader]
        except FileNotFoundError:
            return []

    @classmethod
    def attributes(cls):
        """Returns a list of attribute names for CSV serialization."""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            return ["id", "size", "x", "y"]
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
