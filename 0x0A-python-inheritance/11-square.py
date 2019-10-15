#!/usr/bin/python3


class BaseGeometry:
    """Create a BaseGeometry object"""
    def area(self):
        """Area of the BaseGeometry object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if not (type(value) is int):
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
        else:
            return value


class Rectangle(BaseGeometry):
    """A Rectangle That inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Constructor"""
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Calculate the area of the Rectangle"""
        return self.__width * self.__height


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size):
        """Constructor"""
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)
