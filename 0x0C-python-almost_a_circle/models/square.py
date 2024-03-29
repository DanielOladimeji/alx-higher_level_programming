#!/usr/bin/python3
""" Module containing a Square class that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square object
        Args:
        size - size of the Square
        x - x axis
        y - y axis
        id - identity of the Square
        NB: All arguments are int values
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update the rectangle instance with given arguments"""
        if args is not None and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for argument in kwargs:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
