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

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
