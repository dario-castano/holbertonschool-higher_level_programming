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
        """
        Args:
            size: Size of the square
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print('#' * self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            value: Setter of size property
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
