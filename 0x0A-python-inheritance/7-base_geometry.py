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
