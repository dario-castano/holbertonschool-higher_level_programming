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
    msg = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: Size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not Square.__isa_pos2tuple(position):
            raise TypeError(self.msg)
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size != 0:
            print('\n' * self.position[1], end="")
            for i in range(self.size):
                print(' ' * self.position[0], end="")
                print('#' * self.size)
        else:
            print('')

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
        if Square.__isa_pos2tuple(value):
            self.__position = value
        else:
            raise TypeError(self.msg)

    @staticmethod
    def __isa_pos2tuple(tup):
        if (type(tup) is tuple and len(tup) == 2 and
                (tup[0] >= 0 and tup[1] >= 0)):
            return True
        else:
            return False
