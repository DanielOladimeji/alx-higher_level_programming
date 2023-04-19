#!/usr/bin/python3
""" A Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """ A Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle
        Args:
        width - width of the Rectangle
        height - height of the Rectangle
        x - x axis
        y - y axis
        NB: All arguments are int values
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__y = value
