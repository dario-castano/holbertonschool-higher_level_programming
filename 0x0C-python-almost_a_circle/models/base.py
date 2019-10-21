#!/usr/bin/python3
import json
from models.rectangle import Rectangle
from models.square import Square


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = Square(1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Base":
            dummy = cls()
            return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        list_dicts = []
        with open('{}.json'.format(cls.__name__), mode="w+") as file:
            if not list_objs:
                file.write("[]")
            else:
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                file.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        objs = []
        try:
            f = open('{}.json'.format(cls.__name__), 'r')
            content = f.read()
            items = cls.from_json_string(content)
            for item in items:
                objs.append(cls.create(**item))
            f.close()
            return objs
        except FileNotFoundError:
            return []
