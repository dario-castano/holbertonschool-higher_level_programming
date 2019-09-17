#!/usr/bin/python3
def no_c(my_string):
    newstr = "".join([x for x in my_string if x is not 'C' and x is not 'c'])
    return newstr
