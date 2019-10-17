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
        if attrs is None or not attrs:
            return self.__dict__
        else:
            isa_str_list = all([type(x) is str for x in attrs])
            if isa_str_list:
                new_dict = dict()
                old_dict = self.__dict__
                for atr in attrs:
                    if atr in old_dict:
                        new_dict.update({atr: old_dict[atr]})
                return new_dict
            return self.__dict__
