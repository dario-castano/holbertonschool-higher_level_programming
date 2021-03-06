#!/usr/bin/python3
"""
Find a peak in a list of ints
"""


def find_peak(list_of_integers):
    """Find the peak
    """
    if not list_of_integers:
        return None
    return max(list_of_integers)
