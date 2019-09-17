#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    else:
        return [print("{:d}".format(x)) for x in reversed(my_list)]
