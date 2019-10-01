#!/usr/bin/python3
class Square:
    """
    Defines a square

    Args:
        size (int): Size of the square

    Attributes:
        __size (int): Size of the square

    Raises:
        ValueError: When size is less than 0
        TypeError: Size must be an int
    """
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
