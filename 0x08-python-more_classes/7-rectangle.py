#!/usr/bin/python3


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            word = []
            for i in range(self.height):
                if i == self.height - 1:
                    word.append(str(self.print_symbol) * self.width)
                else:
                    word.append(str(self.print_symbol) * self.width + '\n')
            return "".join(word)

    @property
    def width(self):
        """WIDTH GETTER"""
        return self.__width

    @width.setter
    def width(self, value):
        """WIDTH SETTER"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """HEIGHT GETTER"""
        return self.__height

    @height.setter
    def height(self, value):
        """WIDTH SETTER"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
