#!/usr/bin/python3
"""12-pascal_triangle.py: Pascal's Triangle
"""


def pascal_triangle(n):
    """ Defines Pascal's Triangle of sizs n
    Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1]
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)
    return triangle
