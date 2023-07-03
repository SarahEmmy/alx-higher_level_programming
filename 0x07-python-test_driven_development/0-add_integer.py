#!/usr/bin/python3
"""
    Modules containing add_integer function.
    This function returns two integers.
    5 line module comment.
"""


def add_integer(x, y=98):
    """ Add two integers and returns the result.
    Args:
        x (int): The first integer.
        y (int): The secodn integer.
    """
    if type(x) is not int:
        if type(x) is float:
            x = int(x)
        else:
            raise TypeError("x must be an integer")
    if type(y) is not int:
        if type(y) is float:
            y = int(y)
        else:
            raise TypeError("y must be an integer")
    return (x + y)
