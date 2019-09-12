#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from functools import reduce
    argc = len(argv)
    print(reduce(lambda x, y: int(x) + int(y), argv[1:]))\
        if argc > 1 else print(0)
