#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Check if ihnerits but not the same"""
    if type(obj) is a_class:
        return False
    else:
        if issubclass(type(obj), a_class):
            return True
        else:
            return False
