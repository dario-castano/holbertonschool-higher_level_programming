#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        out = []
        for i in range(self.y):
            out.append('\n')
        for j in range(self.height):
            out.append(' ' * self.x + '#' * self.width + '\n')
        print(''.join(out), end="")

    def update(self, *args, **kwargs):
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            valid_args = args[:5]
            args_list = ['id', 'width', 'height', 'x', 'y']
            for index in range(len(valid_args)):
                setattr(self, args_list[index], valid_args[index])

    def to_dictionary(self):
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
