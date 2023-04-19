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
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height value"""
        self.__height = value

    @property
    def x(self):
        """retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x value"""
        self.__x = value

    @property
    def y(self):
        """ retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y value"""
        self.__y = value
