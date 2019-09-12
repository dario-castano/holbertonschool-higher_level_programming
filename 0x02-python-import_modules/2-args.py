#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv)

    if argc == 2:
        print("{:d} argument:".format(argc - 1))
    elif argc == 1:
        print("0 arguments.".format(argc - 1))
    else:
        print("{:d} arguments:".format(argc - 1))

    [print("{:d}: {}".format(i, argv[i])) for i in range(argc) if i > 0]
