#!/usr/bin/python3
""" models base """
import json
import csv
import turtle


class Base:
    """ Defines a Model Base Clads"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string rep of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_list = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 2)
            if cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                obj_list = cls.from_json_string(json_string)
                return [cls.create(**d) for d in obj_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialization - csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as myfile:
            if list_objs is None or len(list_objs) == 0:
                myfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributename = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    attributename = ["id", "size", "x", "y"]
                writer = csv.DictWriter(myfile, fieldnames=attributename)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserialiation - csv file"""
        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    attributename = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    attributename = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=attributename)
                for item in reader:
                    item = {k: int(v) for k, v in item.items()}
                    list_objs.append(cls.create(**item))
                return list_objs
        except Exception:
            return list_objs

    @staticmethod
def draw(list_rectangles, list_squares):
    """Draw Rectangles and Squares using the turtle module.
    Args:
        list_rectangles (list): A list of Rectangle objects to draw.
        list_squares (list): A list of Square objects to draw.
    """
    turt = turtle.Turtle()
    turt.screen.bgcolor("#dcdcdc")
    turt.pensize(2)
    turt.shape("turtle")

    for rect in list_rectangles:
        turt.color("#ff6347")
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

    for sq in list_squares:
        turt.color("#4169e1")
        turt.showturtle()
        turt.up()
        turt.goto(sq.x, sq.y)
        turt.down()
        for i in range(4):
            turt.forward(sq.width)
            turt.left(90)
        turt.hideturtle()

    turtle.exitonclick()
