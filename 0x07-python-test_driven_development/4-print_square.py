#!/usr/bin/python3
def print_square(size):
    if not (type(size) is int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print('#' * size)
