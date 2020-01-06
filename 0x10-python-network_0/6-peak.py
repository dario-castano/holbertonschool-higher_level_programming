#!/usr/bin/python3
"""
Find a peak in a list of ints
"""

def find_peak(list_of_integers):
    if (not list_of_integers) or (list_of_integers is None):
        return None
    else:
        return sorted(list_of_integers).pop()
