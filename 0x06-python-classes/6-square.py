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
    def __init__(self, size=0, position=(0, 0)):
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

        try:
            if position[0] < 0 or position[1] < 0:
                raise TypeError
            else:
                self.__position = position
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if type(value) is tuple and isinstance(value, int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError
            else:
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")
