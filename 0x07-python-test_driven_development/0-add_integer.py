#!/usr/bin/python3
def add_integer(a, b=98):
    """Sums a pair of ints or floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float(9e999) or a != a or a == float(-9e999):
        raise TypeError("a must be an integer")
    if b == float(9e999) or b != b or b == float(-9e999):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
