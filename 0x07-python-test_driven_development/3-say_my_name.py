#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints: My name is <first name> <last name>"""
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    elif not type(last_name) is str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))