#!/usr/bin/python3


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """CONSTRUCTOR"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student"""
        if (attrs is None or
                not attrs or
                not type(attrs) is list):
            return self.__dict__
        else:
            isa_str_list = all([type(x) is str for x in attrs])
            if isa_str_list:
                return {key: self.__dict__[key]
                        for key in attrs if key in self.__dict__}
            return self.__dict__
