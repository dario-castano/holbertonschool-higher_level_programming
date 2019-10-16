#!/usr/bin/python3


def add_attribute(obj, attr_name, attr_val):
    """Try to add attributes to a class"""
    if obj.__class__.__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    elif hasattr(obj, '__slots__'):
        if attr_name in obj.__slots__:
            setattr(obj, attr_name, attr_val)
        else:
            raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_val)
