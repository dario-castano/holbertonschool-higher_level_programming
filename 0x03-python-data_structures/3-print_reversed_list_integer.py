#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    return [print("{:d}".format(x)) for x in reversed(my_list)]