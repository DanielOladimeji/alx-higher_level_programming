#!/usr/bin/python3
"""
def matrix_divided(matrix, div):
This function returns a new matrix with each element
divided by the given 'div' parameter.
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.
    Returns a new matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMatrix = []
    length = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        newRow = []
        for el in row:
            if type(el) is not int and type(el) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            newRow.append(round(el/div, 2))
        newMatrix.append(newRow)
    return newMatrix
